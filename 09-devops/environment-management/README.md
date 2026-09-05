# Environment Management Architecture

Designing clean, reproducible environment topologies and answering the critical enterprise question:
> **"How many environments do we actually need?"**

## 1. The Environment Anti-Pattern: Environment Sprawl
Many legacy enterprises maintain 7+ permanent static environments:
`Dev -> Integration -> System Test -> QA -> UAT -> Pre-Prod -> Staging -> Production`

### Why This Fails:
1. **Massive Cloud Waste**: Idle non-production environments running 24/7 consume up to 60% of cloud spend.
2. **Configuration Drift**: Staging has patches that never existed in Dev; QA database schemas desynchronize from Production.
3. **Queue Bottlenecks**: Testing queues become human bottlenecks where features sit waiting for "UAT sign-off" for weeks.

## 2. The Modern Lean Environment Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ 1. LOCAL / DEVCONTAINER (Ephemeral)                         │
│ - Developer laptop / GitHub Codespaces                      │
│ - Fast unit tests, mocked dependencies                      │
├─────────────────────────────────────────────────────────────┤
│ 2. EPHEMERAL PREVIEW ENVIRONMENTS (PR-Scoped)               │
│ - Spun up automatically on Pull Request creation            │
│ - Tested via synthetic automated E2E tests                  │
│ - Destroyed automatically on PR merge/close                 │
├─────────────────────────────────────────────────────────────┤
│ 3. STAGING (Permanent Production Mirror)                    │
│ - Identical topology, networking, and security as Prod      │
│ - Sanitized production-like data volumes                    │
│ - Final canary verification and performance testing         │
├─────────────────────────────────────────────────────────────┤
│ 4. PRODUCTION (The Live Environment)                        │
│ - Multi-zone / Multi-region deployment                      │
│ - Progressive delivery and canary progression               │
└─────────────────────────────────────────────────────────────┘
```

## Related Resources
- [Environment Parity and Drift](./environment-parity-and-drift.md)
- [Configuration Management](../configuration-management/README.md)
