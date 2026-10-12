FROM python:3.11-slim AS generator
RUN pip install --no-cache-dir "openapi-python-client==0.29.0"
WORKDIR /src
COPY clients/python/. .
COPY openapi/openapi.yaml ./openapi.yaml
RUN openapi-python-client generate \
    --path openapi.yaml --config config.yaml \
    --output-path . --custom-template-path custom-templates --overwrite