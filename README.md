# Intra 42 API — OpenAPI Rewrite

Community-driven rewrite of the [42 School Intra API](https://api.intra.42.fr/apidoc) as a proper [OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.2.html) specification, with auto-generated, published clients for **Go**, **Python**, and **TypeScript**.

The original Intra API documentation predates OpenAPI tooling and offers no machine-readable contract, no generated clients, and inconsistent or missing details on required roles, scopes, and response shapes. This project rebuilds the spec endpoint by endpoint, verifying each one against real responses, and ships ready-to-use client libraries generated directly from that spec.

## Live documentation

The rendered API reference (built with [Scalar](https://scalar.com)) is published from the [`docs/`](./docs) directory. It includes custom conventions on top of the base spec:

| Marker | Meaning                                                                                       |
| ------ | --------------------------------------------------------------------------------------------- |
| 🔑     | Restricted call — requires an elevated staff role and/or an application scope beyond `public` |
| 👤     | Restricted to the authenticated resource owner                                                |

Progress on rewriting each endpoint is tracked in [`openapi-rewrite-progress.md`](./openapi-rewrite-progress.md).

## Project structure

```
.
├── specs/           # Source of truth: modular OpenAPI fragments (paths, schemas, parameters)
├── openapi/         # Bundled, released OpenAPI contract (generated from specs/)
├── clients/         # Generated API clients, one per language
│   ├── go/
│   ├── python/
│   └── typescript/
├── docs/            # Scalar-based API reference site + custom plugins
├── tool/            # Build tooling (index generation, versioning scripts)
└── .github/         # CI/CD workflows
```

### `specs/`

The hand-maintained source of the API contract. Split into three concerns to keep large resources manageable:

- **`paths/`** — one directory per resource (e.g. `users`, `closes`, `coalitions`), each containing the path definitions and operations for that resource.
- **`schemas/`** — one directory per resource, containing the data models. Shared types (e.g. `error.yaml`) live at the top level.
- **`parameters/`** — reusable parameters (pagination, filtering, sorting) shared across operations.

Each directory contains an auto-generated `_index.yaml` that aggregates its contents. The root `specs/openapi.yaml` holds the top-level OpenAPI metadata — info, servers, security schemes.

### `openapi/`

The bundled, single-file OpenAPI document produced from `specs/`, versioned and released independently via `semantic-release`. This is the artifact consumers and code generators actually depend on.

### `clients/`

Each client is generated from the bundled spec in `openapi/` and released independently:

| Client| Generator | Package |
|-------|-----------|---------|
| Go | [`oapi-codegen`](https://github.com/oapi-codegen/oapi-codegen) | [`github.com/42paris/intraoapi42/clients/go`](https://pkg.go.dev/github.com/42paris/intraoapi42/clients/go) |
| Python | [`openapi-python-client`](https://pypi.org/project/openapi-python-client/) with custom templates | [`intraoapi42`](https://test.pypi.org/project/intraoapi42/) on PyPI |
| TypeScript | [`openapi-typescript`](https://www.npmjs.com/package/openapi-typescript) | [`@cdurdetrouver/intraoapi42`](https://www.npmjs.com/package/@42paris/intraoapi42) on npm |

Each client directory is self-contained (own `Dockerfile`, `config.yaml`, `.releaserc.json`) and can be regenerated and released independently of the others.

### `docs/`

The Scalar-based documentation site (`index.html`) plus a custom Scalar plugin (`scalar-required-roles-plugin.js`) that renders the 🔑/👤 role and scope requirements directly on each operation page, matching Scalar's native styling.

## Getting started

### Prerequisites

All spec bundling, linting, and client generation runs inside Docker containers via the `Makefile` — you don't need Go, Python, or Node installed locally to contribute to the spec itself. The only requirement is:

- [Docker](https://docs.docker.com/get-docker/)

Toolchain versions for local development on the clients themselves (if you need to work inside `clients/go`, `clients/python`, or `clients/typescript` directly) are pinned via [Nix flakes](https://nixos.wiki/wiki/Flakes) (`flake.nix` / `.envrc` with [direnv](https://direnv.net/)), which provisions Node.js, Go, and Python automatically when entering the project directory.

## Contributing

Contributions are welcome!

To contribute, edit the relevant files under [`specs/`](./specs) — this is the source of truth for the API contract (paths, schemas, and parameters).

Once you've made your changes, run:

```bash
make all
```

This regenerates the index files, bundles the spec, and lints the result — confirming that `openapi/openapi.yaml` is valid.

Then, regenerate the clients:

```bash
make generate-clients
```

This updates the Go, Python, and TypeScript clients under [`clients/`](./clients) to match your spec changes. You can also generate a single client individually with `make generate-go`, `make generate-python`, or `make generate-typescript`.

Before opening a pull request:

- Update [`openapi-rewrite-progress.md`](./openapi-rewrite-progress.md) to reflect the status of the endpoint(s) you worked on.
- Run `make ci-check` to confirm your generated files are fully in sync with your spec changes — this is the same check CI runs, so a clean local run means CI won't flag drift.

### Commit messages

Commits must follow the [Angular Commit Message Conventions](https://github.com/angular/angular/blob/main/contributing-docs/commit-message-guidelines.md):

- Use `feat` when adding a **new** path.
- Use `fix` when updating an **existing** path or schema.

Once everything looks good, open a pull request.

## Disclaimer

This is an unofficial, community project and is not affiliated with or endorsed by 42/Le Réseau. It documents the public-facing behavior of the Intra API as observed; some endpoints, fields, or access rules may be incomplete, inferred, or subject to change without notice on 42's side.

## License

See [`LICENSE`](./LICENSE).
