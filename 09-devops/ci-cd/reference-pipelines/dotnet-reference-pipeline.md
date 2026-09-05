# .NET 8/9 Enterprise Reference Pipeline

A production-grade CI/CD pipeline architecture for modern enterprise .NET microservices.

## 1. Pipeline Architecture Flow

```
[Commit] ──► [Restore NuGet with Lockfile] ──► [Build Release] ──► [Unit & Contract Tests]
                                                                        │
[Deploy to Dev/Staging] ◄── [Scan Trivy] ◄── [Package Chiseled OCI] ◄───┘
```

## 2. Hardening & Container Best Practices
- **Base Image**: Use `mcr.microsoft.com/dotnet/nightly/aspnet:8.0-chiseled` (non-root, minimal attack surface, zero package manager).
- **AOT / ReadyToRun**: Compile with `PublishReadyToRun=true` to minimize container cold-start latency.
- **Lockfile Enforcement**: Build with `--locked-mode` to prevent unreviewed package dependencies.

## Related Resources
- [.NET Backend Architecture](../../../03-backend/dotnet/README.md)
- [Reference Pipelines Catalog](./README.md)
