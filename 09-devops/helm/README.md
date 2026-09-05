# Helm Architecture & Chart Governance

Helm serves as the de-facto package manager for Kubernetes workloads across the enterprise. This domain establishes architecture, chart modularity standards, values hierarchy, testing paradigms, and organizational chart governance.

## Core Architectural Responsibilities

1. **Workload Packaging & Versioning**: Packaging complex multi-tier microservices into immutable SemVer-tagged chart archives stored in enterprise OCI registries.
2. **Configuration Separation**: Strict separation between static template logic (	emplates/) and environment-specific values (alues-dev.yaml, alues-prod.yaml).
3. **Chart Governance & Linters**: Mandatory automated linting (helm lint), static security scanning (Trivy, Checkov), and unit testing (helm-unittest) within continuous integration pipelines.
4. **Helm vs Kustomize Synthesis**: Defining when to use pure Helm templates versus combining Helm chart rendering with Kustomize post-render overlays for cluster-specific patches.

## Contents

- [Helm Architecture and Chart Governance](./helm-architecture-and-chart-governance.md) - Production chart structure, values hierarchy, OCI chart distribution, automated unit testing, and enterprise governance frameworks.
- [Cross-Reference: Kubernetes Architecture](../kubernetes/README.md) - Production Kubernetes workload abstractions, control plane architectures, and operational guardrails.
