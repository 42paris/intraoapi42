OPENAPI_SPEC ?= openapi/openapi.yaml
USER_ID := $(shell id -u)
GROUP_ID := $(shell id -g)

all: indexes bundle lint

indexes:
	docker run --rm --user $(USER_ID):$(GROUP_ID) \
		-e HOME=/tmp \
		-w / \
		-v ./specs:/specs \
		-v ./tool:/tool \
		python:3.11-slim \
		bash -c "pip install --no-cache-dir --user -r /tool/requirements.txt && PATH=/tmp/.local/bin:\$$PATH python /tool/generate_indexes.py"

bundle:
	docker run --rm --user $(USER_ID):$(GROUP_ID) \
		-v ./specs:/spec \
		-v ./$(OPENAPI_SPEC):/gen/openapi.yaml \
		-v ./redocly.yaml:/redocly.yaml:ro \
		redocly/cli:2.40.0 \
		bundle openapi.yaml --config /redocly.yaml --force --ext yaml -o /gen/openapi.yaml 2> /dev/null

lint:
	docker run --rm --user $(USER_ID):$(GROUP_ID) \
		-v ./$(OPENAPI_SPEC):/spec/openapi.yaml \
		-v ./redocly.yaml:/redocly.yaml:ro \
		redocly/cli:2.40.0 \
		lint --config /redocly.yaml --lint-config error openapi.yaml

generate-python:
	docker build -f clients/python/Dockerfile -t oapi-gen-py .
	rm -rf clients/python/intraoapi42
	docker run --rm --user $(USER_ID):$(GROUP_ID) -v ./clients/python:/out oapi-gen-py \
		sh -c "cp -r /src/intraoapi42 /out/ && cp /src/custom-templates/custom_client.py.txt /out/intraoapi42/custom_client.py"

generate-go:
	docker build -f clients/go/Dockerfile -t oapi-gen-go .
	docker run --rm --user $(USER_ID):$(GROUP_ID) -v ./clients/go:/out oapi-gen-go \
		sh -c "cp /src/openapi.gen.go /out/openapi.gen.go"

generate-typescript:
	docker build -f clients/typescript/Dockerfile -t oapi-gen-ts .
	docker run --rm --user $(USER_ID):$(GROUP_ID) -v ./clients/typescript:/out oapi-gen-ts \
		sh -c "cp /src/src/types.ts /out/src/types.ts"

generate-clients: generate-go generate-python generate-typescript

ci-check:
	$(MAKE) all
	$(MAKE) generate-clients
	@status=$$(git status --porcelain); \
	if [ -n "$$status" ]; then \
		echo "ERROR: generated files are out of date."; \
		echo "$$status"; \
		echo ""; \
		echo "Run 'make all generate-clients' locally and commit the changes."; \
		exit 1; \
	fi