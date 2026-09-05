# GitLab Architecture and Runners

GitLab's hierarchical model of Groups, Subgroups, and Projects aligns cleanly with enterprise organizational structures and departmental cost centers.

## 1. GitLab Architecture Topology

```
┌─────────────────────────────────────────────────────────────┐
│                    GITLAB CORE SERVER                       │
│  Gitaly (Git RPC) / PostgreSQL / Redis / Puma / Workhorse   │
├──────────────────────────────┬──────────────────────────────┤
│      SHARED RUNNER FLEET     │      SPECIFIC RUNNER FLEET   │
│  - Kubernetes Autoscaler     │  - Dedicated high-security   │
│  - Multi-tenant workloads    │    isolated bare-metal nodes │
│  - Ephemeral Docker containers│  - Compliance-locked pipelines│
└──────────────────────────────┴──────────────────────────────┘
```

## 2. GitLab CI Runner Executors
- **Kubernetes Executor**: Provisions an ephemeral Pod for each job; ideal for elastic cloud workloads.
- **Docker+Machine Executor**: Provisions ephemeral cloud VMs (e.g., EC2) on-demand; provides complete kernel-level isolation.
- **Shell Executor (Anti-Pattern in Multi-Tenant)**: Runs jobs directly on the runner OS host; presents severe privilege escalation risks.

## Related Resources
- [GitHub vs GitLab Decision Matrix](./github-vs-gitlab-decision-matrix.md)
- [CI/CD Architecture](../ci-cd/README.md)
