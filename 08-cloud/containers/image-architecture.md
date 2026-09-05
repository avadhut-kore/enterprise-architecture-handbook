# Container Image Architecture & Optimization

## Executive Summary

Enterprise container images must be optimized for **minimal surface area**, **fast deployment transfer**, and **high build cache efficiency**.

---

## 1. Multi-Stage Build Architecture

Never ship compilers, build tools, or source code files inside production container images. Use multi-stage Dockerfiles to isolate the build environment from the lean runtime container:

```dockerfile
# Stage 1: Build & Compilation (Discarded)
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o /app/server ./cmd/server

# Stage 2: Production Runtime (Shipped to Production)
FROM gcr.io/distroless/static-debian12:nonroot
WORKDIR /
COPY --from=builder /app/server /server
USER nonroot:nonroot
EXPOSE 8080
ENTRYPOINT ["/server"]
```

---

## 2. Layer Caching & Distroless Hardening

1. **Order of Operations**: Place slow-changing layers (e.g., OS package installs, dependency manifests `package.json`, `pom.xml`) at the top of the Dockerfile. Place fast-changing application source code at the bottom to maximize Docker build cache reuse.
2. **Distroless Base Images**:
   - Standard Ubuntu/Debian base images contain package managers (`apt`), shell interpreters (`bash`, `sh`), and system utilities (`curl`, `nc`). These tools provide an attacker with exploitation capabilities following a Remote Code Execution (RCE) breach.
   - Standardize on **Distroless** images (containing solely the compiled application binary and essential root CA certificates). Zero shell means zero interactive remote code execution.
