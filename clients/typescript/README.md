# intraoapi42

Typed TypeScript client for the [42 Intra API](https://api.intra.42.fr/), built on [`openapi-fetch`](https://openapi-ts.dev/packages/openapi-fetch/).

Features:

- Fully typed requests and responses generated from the OpenAPI spec.
- Automatic OAuth2 client credentials flow with token refresh.
- Built‑in retry logic for transient failures.
- Ready‑made configs for production and staging environments.

---

## Installation

```bash
npm install intraoapi42
```

or with a scoped name if you publish as such:

```bash
npm install @your-username/intraoapi42
```

Requires Node.js with ESM support (your `package.json` should have `"type": "module"` or use `.mjs` extensions).

---

## Quick start

```ts
import {
  createApiClient,
  ProductionConfig,
  withClientCredentials,
  withScopes,
} from "intraoapi42";

// Configure OAuth2 client credentials
const config = withClientCredentials(
  ProductionConfig,
  "YOUR_CLIENT_ID",
  "YOUR_CLIENT_SECRET",
);

// Optionally restrict scopes
const scopedConfig = withScopes(
  config,
  "public",
  "projects",
);

// Create the API client
const api = createApiClient(scopedConfig);

// Example: GET /v2/users/:id
const { data, error } = await api.GET("/users/{id}", {
  params: {
    path: { id: 12345 },
  },
});

if (error) {
  throw new Error(`API error: ${error.message}`);
}

console.log(data);
```

Types for paths, parameters, and responses are inferred from the OpenAPI spec, so you get full TypeScript autocomplete and type checking.

---

## Configuration

### Environments

Two built‑in configs are provided:

```ts
import { ProductionConfig, StagingConfig } from "intraoapi42";

ProductionConfig;
// {
//   tokenUrl: "https://api.intra.42.fr/oauth/token",
//   serverUrl: "https://api.intra.42.fr/v2",
// }

StagingConfig;
// {
//   tokenUrl: "https://api.intra-staging.42.fr/oauth/token",
//   serverUrl: "https://api.intra-staging.42.fr/v2",
// }
```

### Adding credentials

Use `withClientCredentials` to attach your OAuth2 client ID and secret:

```ts
import {
  ProductionConfig,
  withClientCredentials,
  createApiClient,
} from "intraoapi42";

const config = withClientCredentials(
  ProductionConfig,
  process.env.INTRA_CLIENT_ID!,
  process.env.INTRA_CLIENT_SECRET!,
);

const api = createApiClient(config);
```

### Adding scopes

Optionally restrict the token’s scopes:

```ts
import { withScopes } from "intraoapi42";

const config = withScopes(
  ProductionConfig,
  "public",
  "projects",
  "activities",
);
```

Scopes are passed to the token endpoint as a space‑separated string.

---

## How authentication works

`createApiClient` sets up:

- A **refreshable token source** that:
  - Requests a new access token using client credentials when needed.
  - Caches the token until close to expiry (with a 60s safety margin).
  - Deduplicates concurrent token requests.
- An **auth middleware** that:
  - Adds `Authorization: Bearer <token>` to every request.
  - On `401 Unauthorized`, invalidates the cached token, fetches a fresh one, and retries the request once.

You don’t need to manage tokens manually; just use the client.

---

## Usage patterns

### List users with pagination

```ts
const { data, error } = await api.GET("/users", {
  params: {
    query: {
      page_size: 50,
      page: 1,
    },
  },
});

if (error) {
  throw new Error(error.message);
}

// data is typed according to the OpenAPI spec
console.log(data);
```

### POST / PATCH / DELETE

```ts
// Example: update a user
const { data, error } = await api.PATCH("/users/{id}", {
  params: {
    path: { id: 12345 },
  },
  body: {
    // typed fields here
    displayname: "New Name",
  },
});
```

All HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, etc.) are available with full typing.

---

## Error handling

Each call returns `{ data, error }`:

- `data` is defined when the request succeeds.
- `error` is defined when the request fails (network error, non‑2xx response, etc.).

```ts
const { data, error } = await api.GET("/users/{id}", {
  params: { path: { id: 12345 } },
});

if (error) {
  // error has shape: { message, body?, response, ... }
  console.error("Status:", error.response.status);
  console.error("Body:", await error.response.clone().text());
  throw new Error("Failed to fetch user");
}

// Use data safely
console.log(data.id, data.login);
```

Refer to `openapi-fetch` docs for the exact error shape and advanced patterns.

---

## TypeScript usage

The package exports types generated from the OpenAPI spec:

```ts
import type { paths } from "intraoapi42";

// paths describes all available endpoints and their shapes
type UsersEndpoint = paths["/users"];
```

Your IDE will infer types automatically from `api.GET`, `api.POST`, etc., so you usually don’t need to import these manually.

---

## Development / Contributing

If you’re working on the client itself:

```bash
cd clients/typescript

# Install dependencies
npm install

# Generate types from OpenAPI spec
npm run generate:api

# Typecheck
npm run typecheck

# Build
npm run build

# Run tests
npm test
```

---

## License

MIT