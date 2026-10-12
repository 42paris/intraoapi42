FROM node:20.15.1 AS generator
WORKDIR /src
COPY clients/typescript/package.json clients/typescript/package-lock.json ./
RUN npm ci
COPY clients/typescript/. .
COPY openapi/openapi.yaml ./openapi.yaml
RUN npm run generate:api