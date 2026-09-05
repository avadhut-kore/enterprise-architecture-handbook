# Polyrepo Enterprise Shared Pipeline

Managing CI/CD consistency across hundreds of independent microservice repositories.

## 1. Centralized Inheritance Architecture
- Application repositories declare a minimal 10-line pipeline invoking a shared centralized template.
- Enterprise updates (e.g., upgrading security scanner from Trivy to Snyk) take effect instantly across all 500 repositories without editing individual repos.

## Related Resources
- [Reusable Pipelines Platform](../reusable-pipelines/README.md)
- [Reference Pipelines Catalog](./README.md)
