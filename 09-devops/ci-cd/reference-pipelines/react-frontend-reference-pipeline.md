# React / Next.js Frontend Reference Pipeline

CI/CD architecture for modern web applications with Server-Side Rendering (SSR) and static generation.

## 1. Pipeline Flow
```
[Commit] ──► [Install & Lint] ──► [Vitest / RTL Unit Tests] ──► [Next.js Build & Bundle Analyze]
                                                                            │
[Purge Global CDN Cache] ◄── [Deploy Edge Containers / S3 Assets] ◄─────────┘
```

## 2. Performance & Cost Checks
- **Bundle Budget Gates**: Fail build if client JavaScript bundle increases by > 10KB without architectural justification.
- **Static Asset Invalidation**: Upload versioned hashed assets (`/_next/static/xyz.js`) with immutable caching headers (`Cache-Control: public, max-age=31536000, immutable`).

## Related Resources
- [Frontend Architecture](../../../04-frontend/README.md)
- [Reference Pipelines Catalog](./README.md)
