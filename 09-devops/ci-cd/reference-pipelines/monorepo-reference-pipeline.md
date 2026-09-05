# Monorepo Affected-Project Reference Pipeline

Enterprise pipeline architecture for multi-project monorepos (Nx, Turborepo, Bazel).

## 1. The Affected Project Computation

```
[Git Push (Commit SHA)]
          │
          ▼
[Inspect Git Diff vs Origin/Main]
          │
          ▼
[Calculate Dependency Graph (Nx Affected)]
          │
    ┌─────┴─────────────────────┐
    ▼                           ▼
[Project A Changed]     [Project B Unchanged]
    │                           │
    ▼                           ▼
[Run Build & Test]      [Re-use Cached Remote Artifact]
```

## 2. Remote Build Caching
- Distribute build artifacts to an enterprise S3/GCS bucket; if code and dependencies have not changed, tests return instantly with a cache hit.

## Related Resources
- [Monorepo vs Polyrepo Architecture](../../git/monorepo-vs-polyrepo-architecture.md)
- [Reference Pipelines Catalog](./README.md)
