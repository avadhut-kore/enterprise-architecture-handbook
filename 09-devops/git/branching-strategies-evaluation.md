# Branching Strategies Evaluation: Trunk-Based vs GitFlow

Branching strategy is not a matter of developer personal preference; it directly dictates release frequency, merge conflict overhead, and CI/CD automation efficiency.

## 1. Comparative Architecture

### Trunk-Based Development (Recommended for Modern Continuous Delivery)
- **Model**: All developers commit directly to a single shared branch (`main` / `trunk`) or merge very short-lived feature branches (< 1-2 days).
- **Enabler**: Requires comprehensive automated testing and Feature Flags for unreleased work.
- **Flow**:
```
main: ──●────●────●────●────●────●────●──► (Continuous Deployment to Staging/Prod)
         \  /      \  /
feat:     ──        ── (Merged within 24 hours)
```

### GitFlow (Legacy Multi-Branch Architecture)
- **Model**: Dual long-lived branches (`master` and `develop`) plus dedicated `feature/*`, `release/*`, and `hotfix/*` branches.
- **Flow**:
```
master:   ●──────────────────────────────●──────────────●──► (Production)
           \                            / \            /
release:    \                  ─────────   \          /
             \                /             \        /
develop:      ●────●────●────●───────────────●──────●──► (Integration)
               \  /
feature:        ── (Lives for weeks/months)
```

## 2. Decision Matrix

| Dimension | Trunk-Based Development | GitFlow |
| :--- | :--- | :--- |
| **Deployment Frequency** | Multiple times per day (Continuous Delivery) | Bi-weekly or monthly scheduled releases |
| **Merge Friction** | Minimal (Continuous micro-merges) | High ("Merge Hell" during release branch consolidation) |
| **Tooling Dependency** | High (Requires Feature Flagging & fast CI) | Low (Relies on Git branches for environment isolation) |
| **Recommended Context** | Web apps, SaaS, Cloud-Native, High-velocity teams | Packaged software with multi-version maintenance (e.g., v1.2, v1.3) |

## Related Resources
- [Merge vs Rebase vs Squash](./merge-vs-rebase-vs-squash.md)
- [Deployment Strategies](../deployment-strategies/README.md)
