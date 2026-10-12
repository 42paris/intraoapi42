package intraoapi42

import (
	"bytes"
	"context"
	"io"
	"net/http"
	"sync"
	"time"

	"golang.org/x/oauth2"
	"golang.org/x/oauth2/clientcredentials"
)

type Config struct {
	clientcredentials.Config
	ServerURL string
}

var ProductionConfig = Config{
	Config: clientcredentials.Config{
		TokenURL: "https://api.intra.42.fr/oauth/token",
	},
	ServerURL: "https://api.intra.42.fr/v2",
}

var StagingConfig = Config{
	Config: clientcredentials.Config{
		TokenURL: "https://api.intra-staging.42.fr/oauth/token",
	},
	ServerURL: "https://api.intra-staging.42.fr/v2",
}

func (c Config) WithClientCredentials(clientID, clientSecret string) Config {
	c.ClientID = clientID
	c.ClientSecret = clientSecret
	return c
}

func (c Config) WithScopes(scopes ...string) Config {
	c.Scopes = scopes
	return c
}

func New(config Config) (*ClientWithResponses, error) {
	tokenSource := newRefreshableTokenSource(config)

	oauthTransport := &oauth2.Transport{
		Source: tokenSource,
		Base:   http.DefaultTransport,
	}

	oauthClient := &http.Client{
		Transport: newRetryTransport(oauthTransport, nil, tokenSource),
	}

	client, err := NewClientWithResponses(
		config.ServerURL,
		WithHTTPClient(oauthClient),
	)
	if err != nil {
		return nil, err
	}
	return client, nil
}

const (
	rateLimitRetryDelay   = time.Second
	rateLimitMaxRetries   = 3
	serverErrorRetryDelay = 500 * time.Millisecond
	serverErrorMaxRetries = 5
)

type retryTransport struct {
	base        http.RoundTripper
	sleep       func(time.Duration)
	tokenSource *refreshableTokenSource
}

func newRetryTransport(
	base http.RoundTripper,
	sleepFn func(time.Duration),
	tokenSource *refreshableTokenSource,
) http.RoundTripper {
	if base == nil {
		base = http.DefaultTransport
	}
	if sleepFn == nil {
		sleepFn = time.Sleep
	}
	return &retryTransport{base: base, sleep: sleepFn, tokenSource: tokenSource}
}

// RoundTrip implements the http.RoundTripper interface.
func (t *retryTransport) RoundTrip(req *http.Request) (*http.Response, error) {
	err := ensureReplayableBody(req)
	if err != nil {
		return nil, err
	}

	rateLimitAttempts := 0
	serverErrorAttempts := 0

	for {
		resp, err := t.base.RoundTrip(req)
		if err != nil {
			return nil, err
		}

		if resp.StatusCode == http.StatusTooManyRequests &&
			rateLimitAttempts < rateLimitMaxRetries {
			rateLimitAttempts++
			drainResponse(resp)
			err = resetRequestBody(req)
			if err != nil {
				return nil, err
			}
			t.sleep(rateLimitRetryDelay)
			continue
		}

		if resp.StatusCode == http.StatusInternalServerError &&
			serverErrorAttempts < serverErrorMaxRetries {
			serverErrorAttempts++
			drainResponse(resp)
			err = resetRequestBody(req)
			if err != nil {
				return nil, err
			}
			t.sleep(serverErrorRetryDelay)
			continue
		}

		if resp.StatusCode == http.StatusUnauthorized {
			t.tokenSource.Invalidate()
			drainResponse(resp)
			err = resetRequestBody(req)
			if err != nil {
				return nil, err
			}
			continue
		}

		return resp, nil
	}
}

type refreshableTokenSource struct {
	config Config
	mu     sync.Mutex
	token  *oauth2.Token
}

func newRefreshableTokenSource(config Config) *refreshableTokenSource {
	return &refreshableTokenSource{config: config}
}

func (r *refreshableTokenSource) Token() (*oauth2.Token, error) {
	r.mu.Lock()
	defer r.mu.Unlock()

	if r.token != nil && r.token.Valid() {
		return r.token, nil
	}

	src := r.config.TokenSource(context.Background())
	token, err := src.Token()
	if err != nil {
		return nil, err
	}

	r.token = token
	return token, nil
}

func (r *refreshableTokenSource) Invalidate() {
	r.mu.Lock()
	r.token = nil
	r.mu.Unlock()
}

func ensureReplayableBody(req *http.Request) error {
	if req.Body == nil || req.GetBody != nil {
		return nil
	}
	buf, err := io.ReadAll(req.Body)
	if err != nil {
		return err
	}
	req.Body = io.NopCloser(bytes.NewReader(buf))
	req.GetBody = func() (io.ReadCloser, error) {
		return io.NopCloser(bytes.NewReader(buf)), nil
	}
	return nil
}

func resetRequestBody(req *http.Request) error {
	if req.GetBody == nil {
		return nil
	}
	body, err := req.GetBody()
	if err != nil {
		return err
	}
	req.Body = body
	return nil
}

func drainResponse(resp *http.Response) {
	if resp.Body == nil {
		return
	}
	_, _ = io.Copy(io.Discard, resp.Body)
	_ = resp.Body.Close()
}
