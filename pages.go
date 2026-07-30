package intraoapi42

import (
	"context"
	"errors"
	"fmt"
	"reflect"
	"sync"
)

type HasJSONDefault interface {
	GetJSONDefault() *ErrorResponse
}

// Varies per endpoint — needs a type parameter
type HasJSON200Slice[T any] interface {
	GetJSON200() *[]T
	GetBody() []byte
}

func FetchAll[T any, P any, R HasJSON200Slice[T]](
	ctx context.Context,
	fetch func(context.Context, *P, ...RequestEditorFn) (R, error),
	params *P,
	pageSize ...int,
) ([]T, error) {
	pageSizeValue := 100
	if len(pageSize) > 0 {
		pageSizeValue = pageSize[0]
	}

	var result []T

	for page := 1; ; page++ {
		setPage(params, page)
		setPerPage(params, pageSizeValue)

		resp, err := fetch(ctx, params)
		if err != nil {
			return nil, err
		}

		items := resp.GetJSON200()
		if items == nil {
			return nil, fmt.Errorf("response does not contain JSON 200 slice %s", string(resp.GetBody()))
		}

		result = append(result, *items...)

		if len(*items) < pageSizeValue {
			break
		}
	}

	return result, nil
}

// pageResult carries one worker's outcome back to the collector goroutine.
type pageResult[T any] struct {
	page  int
	items []T
	err   error
}

func cloneParams[P any](params *P) *P {
	v := reflect.ValueOf(params).Elem()
	clone := reflect.New(v.Type())
	clone.Elem().Set(v)
	return clone.Interface().(*P)
}

func FetchAllConcurrent[T any, P any, R HasJSON200Slice[T]](
	ctx context.Context,
	fetch func(context.Context, *P, ...RequestEditorFn) (R, error),
	params *P,
	concurrency int,
	pageSize ...int,
) ([]T, error) {
	pageSizeValue := 100
	if len(pageSize) > 0 {
		pageSizeValue = pageSize[0]
	}
	if concurrency <= 0 {
		concurrency = 5
	}

	// --- fetch page 1 up front: we need it both for data and for XTotal ---
	// (concurrency is capped below, once we know totalPages, so we never
	// spin up more workers than there is work for)
	firstParams := cloneParams(params)
	setPage(firstParams, 1)
	setPerPage(firstParams, pageSizeValue)

	firstResp, err := fetch(ctx, firstParams)
	if err != nil {
		return nil, err
	}

	firstItems := firstResp.GetJSON200()
	if firstItems == nil {
		return nil, fmt.Errorf("response does not contain JSON 200 slice body=%s", string(firstResp.GetBody()))
	}

	totalElems, err := getResponseXTotal(firstResp)
	if err != nil {
		return nil, err
	}
	totalPages := (totalElems + pageSizeValue - 1) / pageSizeValue

	if totalPages <= 1 {
		return *firstItems, nil
	}

	resultsByPage := make([][]T, totalPages+1)
	resultsByPage[1] = *firstItems

	remainingPages := totalPages - 1
	if concurrency > remainingPages {
		concurrency = remainingPages
	}

	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	pagesCh := make(chan int)
	resultsCh := make(chan pageResult[T])

	var wg sync.WaitGroup
	for i := 0; i < concurrency; i++ {
		wg.Go(func() {
			for page := range pagesCh {
				p := cloneParams(params)
				setPage(p, page)
				setPerPage(p, pageSizeValue)

				resp, err := fetch(ctx, p)
				if err != nil {
					resultsCh <- pageResult[T]{page: page, err: err}
					return // stop this worker; no point fetching more after a failure
				}

				items := resp.GetJSON200()
				if items == nil {
					resultsCh <- pageResult[T]{
						page: page,
						err:  fmt.Errorf("response does not contain JSON 200 slice body=%s", string(resp.GetBody())),
					}
					return
				}

				resultsCh <- pageResult[T]{page: page, items: *items}
			}
		})
	}

	// feed pages to the workers
	go func() {
		defer close(pagesCh)
		for page := 2; page <= totalPages; page++ {
			select {
			case pagesCh <- page:
			case <-ctx.Done():
				return
			}
		}
	}()

	go func() {
		wg.Wait()
		close(resultsCh)
	}()

	var firstErr error
	for res := range resultsCh {
		if res.err != nil {
			if firstErr == nil {
				firstErr = res.err
				cancel()
			}
			continue
		}
		resultsByPage[res.page] = res.items
	}

	if firstErr != nil {
		return nil, firstErr
	}

	var result []T
	for page := 1; page <= totalPages; page++ {
		result = append(result, resultsByPage[page]...)
	}

	return result, nil
}

func setPage(params any, page int) {
	v := reflect.ValueOf(params).Elem()

	f := v.FieldByName("Page")
	if f.IsValid() && f.CanSet() {
		p := Page(page)
		f.Set(reflect.ValueOf(&p))
	}
}

func setPerPage(params any, perPage int) {
	v := reflect.ValueOf(params).Elem()

	f := v.FieldByName("PerPage")
	if f.IsValid() && f.CanSet() {
		p := PerPage(perPage)
		f.Set(reflect.ValueOf(&p))
	}
}

func getResponseXTotal(resp any) (int, error) {
	v := reflect.ValueOf(resp).Elem()

	fHeader200 := v.FieldByName("Headers200")
	if !fHeader200.IsValid() {
		return 0, errors.New("response does not contain Headers200 field")
	}

	if fHeader200.Kind() == reflect.Pointer && fHeader200.IsNil() {
		return 0, errors.New("Headers200 field is nil")
	}

	fXTotal := fHeader200.Elem().FieldByName("XTotal")
	if !fXTotal.IsValid() {
		return 0, errors.New("response does not contain XTotal field")
	}

	if fXTotal.IsNil() {
		return 0, errors.New("XTotal field is nil")
	}

	xTotal := fXTotal.Elem().Int()
	return int(xTotal), nil
}
