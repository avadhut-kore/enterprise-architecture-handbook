# Python Enterprise Reference Pipeline

CI/CD architecture for high-performance Python services (FastAPI, Django).

## 1. Pipeline Architecture Flow

```
[Commit] ──► [Poetry Install Locked] ──► [Ruff Lint & mypy Type Check] ──► [pytest-xdist Parallel]
                                                                                   │
[Deploy K8s] ◄── [Trivy Vulnerability Scan] ◄── [Multi-Stage Distroless Docker] ◄──┘
```

## 2. Hardening & Best Practices
- **Linting Speed**: Use `Ruff` for linting and formatting (10-100x faster than Flake8/Black).
- **Strict Typing**: Fail pipeline on `mypy` type errors.
- **Wheel Isolation**: Multi-stage build compiles C-extensions in a builder image, copying only `.whl` files into a distroless runtime container.

## Related Resources
- [Python Backend Architecture](../../../03-backend/python/README.md)
- [Reference Pipelines Catalog](./README.md)
