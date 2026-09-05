# Node.js / TypeScript Enterprise Reference Pipeline

Architecture for scalable TypeScript microservices and API gateways.

## 1. Pipeline Architecture Flow

```
[Commit] ──► [pnpm Install Frozen Lockfile] ──► [TypeScript tsc & ESLint] ──► [Vitest Tests]
                                                                                     │
[Deploy Serverless/K8s] ◄── [Sign Image] ◄── [Distroless Node.js Image] ◄────────────┘
```

## 2. Best Practices
- **Package Manager**: Enforce `pnpm` for deterministic symlinked dependency isolation, preventing phantom dependencies.
- **Vitest**: 4x faster than Jest due to native ESM and worker thread pooling.
- **Production Pruning**: Run `pnpm prune --prod` before packaging to eliminate devDependencies.

## Related Resources
- [Node.js Backend Architecture](../../../03-backend/nodejs/README.md)
- [Reference Pipelines Catalog](./README.md)
