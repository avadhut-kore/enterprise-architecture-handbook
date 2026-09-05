# Release Management and Cadence

Managing enterprise release cadences requires balancing business predictability with developer velocity.

## 1. Release Cadence Archetypes

| Cadence Model | Frequency | Risk Profile | Best Applied When |
| :--- | :--- | :--- | :--- |
| **Continuous / On-Demand** | Multiple times per day | Low (Micro-batch sizes) | Cloud-native microservices, SaaS, mature CI/CD with automated testing. |
| **Release Trains** | Fixed schedule (e.g., Every Tuesday at 10 AM) | Moderate | Cross-team interdependent systems, mobile apps, or enterprise integrations. |
| **Milestone / Big-Bang** | Quarterly or Semi-annually | Extremely High (Massive blast radius) | Legacy packaged software, regulated air-gapped systems (Target for modernization). |

## 2. Semantic Versioning (SemVer 2.0.0)
$$\text{MAJOR}.\text{MINOR}.\text{PATCH}$$
- **MAJOR**: Breaking API contract changes (requires explicit deprecation windows).
- **MINOR**: Backward-compatible new functionality.
- **PATCH**: Backward-compatible bug fixes and security patches.

## Related Resources
- [Deployment Strategies](../deployment-strategies/README.md)
- [Artifact Management](../artifact-management/README.md)
