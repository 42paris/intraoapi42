FROM golang:1.25.1 AS generator
WORKDIR /src
COPY clients/go/go.mod clients/go/go.sum ./
RUN go mod download
COPY clients/go/. .
COPY openapi/openapi.yaml ./openapi.yaml
RUN go generate ./...