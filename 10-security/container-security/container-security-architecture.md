# Container Security Architecture & Image Hardening

## Executive Summary

Traditional container images inherit hundreds of unnecessary OS binaries (e.g., `curl`, `bash`, `apt`, `tar`) which drastically expand the container attack surface and provide ready-made exploitation tools to an attacker.

---

## 1. The Hardened Container Specification

```dockerfile
# STEP 1: Multi-stage build in a secure builder environment
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish -c Release -o /app/publish

# STEP 2: Deploy to Google Distroless minimal runtime
# Contains ONLY the runtime and glibc; zero package manager, zero shell!
FROM gcr.io/distroless/dotnet/aspnet:8.0-nonroot
WORKDIR /app
COPY --from=build /app/publish .

# Run as non-root unprivileged user (UID 65532)
USER nonroot:nonroot

# Expose non-privileged port (> 1024)
EXPOSE 8080
ENTRYPOINT ["./PaymentService.dll"]
```

### Security Invariants:
1. **Zero Shell (`/bin/sh`)**: Even if an attacker achieves Remote Code Execution, they cannot spawn an interactive shell or download secondary payloads via `curl`.
2. **Read-Only Root Filesystem**: Mount the container root as read-only; use ephemeral `tmpfs` mounts for temporary scratch files.
3. **Drop Capabilities**: Drop all 38 default Linux capabilities and retain only those explicitly required.
