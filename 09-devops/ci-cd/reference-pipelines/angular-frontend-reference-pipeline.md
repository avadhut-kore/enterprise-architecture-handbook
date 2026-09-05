# Enterprise Angular / Nx Reference Pipeline

Architecture for enterprise Angular applications utilizing signals and Nx monorepo tooling.

## 1. Pipeline Flow
```
[Commit] ──► [Nx Affected Analysis] ──► [Parallel Karma/Jest Tests] ──► [Angular AOT Production Build]
                                                                                     │
[Cloudflare CDN Push] ◄── [Lighthouse CI Performance Gate] ◄─────────────────────────┘
```

## 2. Best Practices
- **Nx Computation Caching**: Re-use previously built artifacts across CI runs via Nx Cloud or self-hosted S3 remote cache.
- **Lighthouse CI**: Enforce minimum Core Web Vitals scores (LCP < 2.5s, CLS < 0.1) in staging review apps.

## Related Resources
- [Frontend Architecture](../../../04-frontend/README.md)
- [Reference Pipelines Catalog](./README.md)
