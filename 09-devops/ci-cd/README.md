# CI/CD Architecture & Pipeline Engineering

Continuous Integration and Continuous Delivery (CI/CD) represents the core automated execution engine of modern software engineering.

## Contents

- [CI/CD Core Principles](./fundamentals/ci-cd-core-principles.md) — Fundamental definitions, CI vs CD vs Continuous Deployment, and feedback loops.
- [Pipeline Design and Orchestration](./pipeline-architecture/pipeline-design-and-orchestration.md) — Pipeline stages, DAG dependencies, caching strategies, test parallelization, and build reproducibility.
- [Pipeline Governance and Standards](./pipeline-governance/pipeline-governance-and-standards.md) — Pipeline-as-code, auditability, quality gates, and risk-based security controls.
- [Pipeline Security and Hardening](./pipeline-security/pipeline-security-and-hardening.md) — Runner isolation, secret injection, ephemeral build environments, and poison pipeline protection.
- [Reusable Pipelines Platform](./reusable-pipelines/README.md) — Enterprise pipeline templates, shared workflows, and golden pipelines.
- [Reference Pipelines Catalog](./reference-pipelines/README.md) — Language and platform reference architectures (.NET, Java, Python, Node, React, Angular, Mobile, Monorepo, Polyrepo).

## Architectural Axioms
1. **Build Once**: A binary or container image is compiled once; environment-specific variables are injected at runtime.
2. **Fail Fast**: Syntax, linting, and fast unit tests execute before expensive end-to-end or integration suites.
3. **Reproducibility**: Builds must be strictly deterministic and pinned to exact dependency versions (lockfiles).
