# intraoapi42

A Go client library for accessing the Intra 42 API, generated from the OpenAPI
contract with [oapi-codegen](https://github.com/oapi-codegen/oapi-codegen), plus
a set of hand-written helpers for authentication, retries, pagination, and Intra's
date/time formats.

## Usage

### Quick start with `New`

The recommended way to get a working, authenticated client is `New`, which
handles OAuth2 client-credentials authentication, automatic token refresh, and
retries for you:

```go
import intraoapi42 "github.com/42paris/intraoapi42/clients/go"

config := intraoapi42.ProductionConfig.WithClientCredentials("your-client-id", "your-client-secret")

client, err := intraoapi42.New(config)
if err != nil {
    log.Fatal(err)
}
```

A `StagingConfig` is also provided for testing against the 42 staging environment:

```go
config := intraoapi42.StagingConfig.WithClientCredentials("your-client-id", "your-client-secret")

client, err := intraoapi42.New(config)
```

If your application needs specific OAuth2 scopes, chain `WithScopes`:

```go
config := intraoapi42.ProductionConfig.
    WithClientCredentials("your-client-id", "your-client-secret").
    WithScopes("public", "projects")

client, err := intraoapi42.New(config)
```

`New` returns a `*ClientWithResponses` (the oapi-codegen generated client),
so you can call any generated endpoint method on it directly once constructed.

### What `New` gives you

Using `New` instead of constructing an oapi-codegen client manually wires in
three behaviors:

- **Automatic token refresh.** `refreshableTokenSource` fetches an OAuth2
  client-credentials token via `golang.org/x/oauth2/clientcredentials` and
  caches it until it expires (checked via `token.Valid()`), refreshing
  transparently when needed.
- **Automatic re-auth on `401`.** The retry transport invalidates the cached
  token and retries the request whenever the API responds with
  `401 Unauthorized`, so an expired or revoked token self-heals on the next call.
- **Automatic retries.** Requests that receive `429 Too Many Requests` are
  retried up to 3 times, 1 second apart; requests that receive
  `500 Internal Server Error` are retried up to 5 times, 500ms apart. Request
  bodies are buffered and replayed safely across retries.

### Calling endpoints

Once you have a client (via `New` or a manually constructed `ClientWithResponses`),
call any generated endpoint the way oapi-codegen normally works:

```go
resp, err := client.GetMyDataModelWithResponse(ctx, &params)
if err != nil {
    log.Fatal(err)
}

if resp.JSON200 != nil {
    // use resp.JSON200
}
```

## Pagination helpers

Intra 42's API paginates list endpoints via `page`/`per_page` query params and
returns the total item count in an `X-Total` response header. This library
provides two generic helpers, in `pages.go`, that drive pagination for you so
you don't have to write the page-walking loop by hand for every list endpoint.

### `FetchAll`

Fetches every page of a list endpoint sequentially and returns the full,
concatenated slice of results.

```go
users, err := intraoapi42.FetchAll(
    ctx,
    client.GetUsersWithResponse,
    &intraoapi42.GetUsersParams{},
)
```

An optional page size can be passed as a final argument (defaults to `100`):

```go
users, err := intraoapi42.FetchAll(
    ctx,
    client.GetUsersWithResponse,
    &intraoapi42.GetUsersParams{},
    50,
)
```

`FetchAll` keeps requesting pages until a page comes back with fewer items
than the page size, which it treats as the last page.

### `FetchAllConcurrent`

Same result as `FetchAll`, but fetches pages 2..N concurrently after
determining the total page count from the first page's `X-Total` header.
Useful for large collections where sequential paging is too slow.

```go
users, err := intraoapi42.FetchAllConcurrent(
    ctx,
    client.GetUsersWithResponse,
    &intraoapi42.GetUsersParams{},
    5, // concurrency
)
```

An optional page size can be passed as a final argument, same as `FetchAll`:

```go
users, err := intraoapi42.FetchAllConcurrent(
    ctx,
    client.GetUsersWithResponse,
    &intraoapi42.GetUsersParams{},
    5,
    50,
)
```

If `concurrency` is `0` or negative, it defaults to `5`. If the total number
of remaining pages is smaller than the requested concurrency, the number of
workers is capped to the remaining page count. If any page fails, all other
in-flight requests are cancelled via context and the first error encountered
is returned.

### Requirements for using the pagination helpers

Both helpers use reflection internally, so your generated params and response
types need to satisfy a couple of conventions already produced by oapi-codegen
for paginated Intra endpoints:

- The params struct (`P`) must have `Page *Page` and `PerPage *PerPage` fields
  — these are set automatically by the helpers via `setPage`/`setPerPage`.
- The response type (`R`) must implement `HasJSON200Slice[T]`, i.e. expose
  `GetJSON200() *[]T` and `GetBody() []byte` — this is what lets the helpers
  read parsed results or fall back to the raw body on a malformed response.
- For `FetchAllConcurrent` specifically, the response type must also expose a
  `Headers200` field containing an `XTotal *int` (or similar integer pointer)
  field, since that's how the total item count is read to compute `totalPages`.

If a param or response type doesn't match these shapes, `setPage`/`setPerPage`
silently no-op (no page/per_page will be set) and `getResponseXTotal` returns
an error, so `FetchAllConcurrent` will fail loudly while `FetchAll` will just
loop based on item count instead of total pages.

## Intra date/time handling

Intra's API returns dates and timestamps in several different formats
depending on the endpoint (date-only, RFC3339, or space-separated formats with
explicit UTC offsets). The generated models use `IntraTime`, a wrapper around
`time.Time` defined in `time.go`, to normalize this.

```go
var event MyEventModel
if err := json.Unmarshal(data, &event); err != nil {
    log.Fatal(err)
}

t := event.CreatedAt.Time() // returns a plain time.Time
```

`IntraTime` implements `UnmarshalJSON` by trying each of the following layouts
in order until one parses successfully:

- `time.RFC3339Nano`
- `2006-01-02` (date-only)
- `2006-01-02T15:04:05`
- `2006-01-02T15:04:05Z07:00`
- `2006-01-02 15:04:05 -07:00`
- `2006-01-02 15:04:05.000 -07:00`
- `2006-01-02 15:04:05.000000 -07:00`

An empty string unmarshals to the zero `time.Time` without error, which
matches how Intra represents optional/unset date fields. When marshaling back
to JSON, `IntraTime` always writes `RFC3339Nano`, regardless of which format
it was originally parsed from.

## Advanced customizations

### Custom `Config`

`Config` embeds `clientcredentials.Config` from `golang.org/x/oauth2`, plus a
`ServerURL` field for the API base URL. Since `WithClientCredentials` and
`WithScopes` return a new `Config` value rather than mutating in place, it's
safe to derive variants from a shared base:

```go
customConfig := intraoapi42.Config{
    Config: clientcredentials.Config{
        TokenURL: "https://my-proxy.internal/oauth/token",
    },
    ServerURL: "https://my-proxy.internal/v2",
}.WithClientCredentials("id", "secret")
```

### Retry and token-refresh internals

The building blocks used internally by `New` are not exported, but the retry
and re-auth logic in `client.go` follows this flow if you need to understand
or replicate it:

- `refreshableTokenSource.Token()` returns the cached token if it's still
  valid (`token.Valid()`), otherwise fetches a fresh one via
  `clientcredentials.Config.TokenSource` and caches it, guarded by a mutex for
  concurrent-safe access.
- `refreshableTokenSource.Invalidate()` clears the cached token, forcing the
  next `Token()` call to fetch a new one — this is called automatically by
  the retry transport on a `401` response.
- `retryTransport.RoundTrip` buffers the request body up front
  (`ensureReplayableBody`) so it can be safely replayed on retry, drains and
  closes intermediate responses (`drainResponse`) to avoid leaking
  connections, and resets the body (`resetRequestBody`) before each retry
  attempt.

If you need custom retry/backoff behavior instead of the built-in delays, you
would need to fork or wrap `retryTransport`, since its retry delays and
attempt counts are currently fixed constants (`rateLimitRetryDelay`,
`rateLimitMaxRetries`, `serverErrorRetryDelay`, `serverErrorMaxRetries`)
rather than configurable fields.

## Building / regenerating this package

This client's HTTP layer (`ClientWithResponses`, request/response types, and
models) is generated from the Intra 42 OpenAPI contract via oapi-codegen.
`client.go`, `pages.go`, and `time.go` are hand-written and are not
regenerated — do not overwrite them when re-running codegen.

To regenerate the generated portion of the client after an OpenAPI contract
update, run your project's codegen step (e.g. `go generate ./...` or your
`Makefile`'s codegen target, depending on how oapi-codegen is wired into this
repo) and verify the hand-written files still compile against the newly
generated types, since field names and interfaces referenced by
`pages.go` (`GetJSON200`, `Headers200`, `XTotal`, `Page`, `PerPage`) depend on
the shape of the generated params/response structs.
