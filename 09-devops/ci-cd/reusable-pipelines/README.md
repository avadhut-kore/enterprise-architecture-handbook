# Reusable Pipelines Platform Architecture

Building enterprise "Golden Pipelines" that enforce corporate standards while maximizing developer self-service.

## 1. The Reusable Pipeline Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│              CENTRAL PLATFORM REPOSITORY                    │
│  `enterprise-ci-templates/` (Semantic Versioned: v2.1.0)    │
│  - reusable-dotnet.yml                                      │
│  - reusable-java.yml                                        │
│  - reusable-node.yml                                        │
│  - reusable-docker-build.yml                                │
├──────────────────────────────┬──────────────────────────────┤
│      APP REPO A (Billing)    │      APP REPO B (Search)     │
│  uses: templates/dotnet@v2   │  uses: templates/node@v2     │
│  with: coverage_target: 85%  │  with: coverage_target: 80%  │
└──────────────────────────────┴──────────────────────────────┘
```

## 2. Governance Principles for Reusable Workflows
- **Semantic Versioning**: Tag template releases (`@v1`, `@v2`). Never push breaking changes to existing major tags.
- **Opinionated Defaults with Parameterized Overrides**: Provide standard build/test/scan commands, but allow application teams to specify custom test arguments or JVM flags.
- **Backward Compatibility**: Maintain previous major versions for at least 6 months before deprecation.

## Related Resources
- [Pipeline Architecture](../pipeline-architecture/pipeline-design-and-orchestration.md)
- [Platform Engineering](../../platform-engineering/README.md)
