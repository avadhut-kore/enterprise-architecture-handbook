# Golden Paths and Service Templates

A "Golden Path" is an opinionated, well-supported, and supported path to building and operating software inside an enterprise.

## 1. What a Golden Path Includes

```
Golden Path = Scaffolding Template (Cookiecutter / Backstage)
            + Pinned Modern Tech Stack (.NET 8 / Java 21 / Node 20)
            + Pre-configured CI/CD Pipeline (GitHub Actions)
            + Built-in Security Scans (SAST, SCA, Trivy, Secret detection)
            + Automated Dockerfile & Helm Charts
            + Standardized OpenTelemetry Observability Dashboards
            + Production Readiness Review Baseline
```

## 2. Paved Road, Not Paved Prison
- **Default Autonomy**: 85% of standard enterprise services follow the golden path happily because it eliminates weeks of boilerplate configuration.
- **The Specialized Escape Hatch**: If a specialized team needs to build a custom Rust low-latency matching engine, they are permitted to deviate from the golden path, but they must own their custom pipeline maintenance and prove compliance during security audits.

## Related Resources
- [Platform as a Product](./platform-as-a-product.md)
- [Developer Experience](../developer-experience/README.md)
