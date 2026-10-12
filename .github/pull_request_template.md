<!--
Thanks for contributing! Please fill out this template before submitting your pull request.
See CONTRIBUTING guidelines in the README for full details.
-->

## Description

<!-- What does this PR change? Which endpoint(s)/resource(s) does it add or update? -->

## Type of change

<!-- Mark the one that applies with an "x" -->

- [ ] `feat` — Adds a new path
- [ ] `fix` — Updates an existing path or schema

## Checklist

- [ ] Changes were made under [`specs/`](../specs) (paths, schemas, and/or parameters).
- [ ] I ran `make all` and confirmed the bundled `openapi/openapi.yaml` is valid (bundle + lint pass).
- [ ] I ran `make generate-clients` (or the relevant `make generate-go` / `make generate-python` / `make generate-typescript`) and committed the updated client output.
- [ ] I updated [`openapi-rewrite-progress.md`](../openapi-rewrite-progress.md) to reflect the new status of the endpoint(s) touched in this PR.
- [ ] Commit messages follow the [Angular Commit Message Conventions](https://github.com/angular/angular/blob/main/contributing-docs/commit-message-guidelines.md) (`feat` for new paths, `fix` for updates to existing paths/schemas).

## Additional notes

<!-- Anything reviewers should know: fields verified against a live response, access roles/scopes confirmed, known limitations, etc. -->
