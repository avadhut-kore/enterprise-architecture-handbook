# Monorepo vs Polyrepo Architecture

The debate between hosting multiple projects in a single repository (Monorepo) versus one repository per microservice (Polyrepo) is one of the most critical structural choices in DevOps architecture.

## 1. Multi-Dimensional Trade-Off Matrix

| Evaluation Dimension | Monorepo (Single Repo) | Polyrepo (Multi-Repo) |
| :--- | :--- | :--- |
| **Atomic Cross-Service Changes** | Trivial (Update API & consumer in single commit). | Complex (Requires coordinated multi-repo PRs). |
| **Code Sharing & Refactoring** | Immediate (Direct import of shared libraries). | Slow (Must version, publish, and bump npm/NuGet/PyPI packages). |
| **CI/CD Pipeline Complexity** | High (Requires affected-project graph computation: Nx/Turborepo/Bazel). | Low (Standard pipeline triggered on repo push). |
| **Access Control & Permissions** | Hard (Requires path-based CODEOWNERS and read restrictions). | Simple (Native repo-level IAM and permissions). |
| **Git Clone & Tooling Scale** | Degrades over time without VFS / sparse-checkout. | Lightweight git clones; fast IDE performance. |

## 2. Architectural Heuristic
- Choose **Monorepo** if teams share high-churn domain contracts, operate under a unified tech stack (e.g., full-stack TypeScript), and have platform engineering support to manage specialized tooling (Nx/Bazel).
- Choose **Polyrepo** if microservices are owned by autonomous cross-functional teams with polyglot tech stacks and independent deployment cadences.

## Related Resources
- [CI/CD for Monorepo](../ci-cd/reference-pipelines/monorepo-reference-pipeline.md)
- [CI/CD for Polyrepo](../ci-cd/reference-pipelines/polyrepo-reference-pipeline.md)
