# DevSecOps Pipeline Architecture (`devsecops/`)

## Executive Summary

DevSecOps automates security controls within the Continuous Integration and Continuous Deployment (CI/CD) pipelines, converting security policies into non-bypassable code gates.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`devsecops-pipeline-architecture.md`](devsecops-pipeline-architecture.md) | Pipeline Design | End-to-end automated pipeline with layered security stages |
| [`security-gates-and-pr-blocking.md`](security-gates-and-pr-blocking.md) | CI/CD Gating | Automated pull request blocking policies and exception handling |
| [`secret-scanning-in-ci.md`](secret-scanning-in-ci.md) | Secret Prevention | Pre-commit hooks, Gitleaks, push protection |
| [`container-and-iac-scanning-in-ci.md`](container-and-iac-scanning-in-ci.md) | Artifact Scanning | Automated Trivy container scans and Checkov IaC linting |
