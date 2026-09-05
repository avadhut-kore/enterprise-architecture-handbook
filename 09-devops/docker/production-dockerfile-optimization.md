# Production Dockerfile Optimization & Hardening

Writing production Dockerfiles requires optimizing for three competing dimensions: **Security (minimal attack surface)**, **Speed (build cache efficiency)**, and **Image Size (network transfer overhead)**.

## 1. Hardening Golden Rules

1. **Never Run as Root**: Always declare a non-root user (`USER nonroot:nonroot` or `USER 10001:10001`). If a container escapes via a kernel exploit, root inside the container equals root on the host!
2. **Use Multi-Stage Builds**: Separate the heavy compilation environment (SDKs, compilers, git, package managers) from the lean runtime container.
3. **Adopt Distroless Base Images**: Google Distroless or Chainguard images strip out package managers (apt/yum), shells (bash/sh), and standard utilities, eliminating 90%+ of common CVEs.
4. **Order by Change Frequency**: Place static dependency installation (`COPY package.json`) *before* copying application source code (`COPY . .`) to maximize Docker layer cache hits.

## 2. Standard Enterprise Multi-Stage Dockerfile Blueprint
```dockerfile
# Stage 1: Build & Compile
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS builder
WORKDIR /src
COPY *.csproj ./
RUN dotnet restore --locked-mode
COPY . .
RUN dotnet publish -c Release -o /app/publish --no-restore

# Stage 2: Hardened Runtime
FROM mcr.microsoft.com/dotnet/nightly/aspnet:8.0-chiseled
WORKDIR /app
COPY --from=builder --chown=$APP_UID:$APP_UID /app/publish .
USER $APP_UID
EXPOSE 8080
ENV ASPNETCORE_URLS=http://+:8080
ENTRYPOINT ["dotnet", "MyService.dll"]
```

## Related Resources
- [Docker Architecture Internals](./docker-architecture-and-container-internals.md)
- [DevSecOps Architecture](../devsecops/README.md)
