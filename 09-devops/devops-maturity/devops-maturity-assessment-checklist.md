# DevOps Maturity Assessment Checklist & Scoring

Score your engineering organization or portfolio across 13 core dimensions on a scale from 1 (Manual) to 5 (Advanced Platform).

## 1. The 13 Dimensions of Evaluation

### A. Source Control & Branching
- [ ] Level 1: Centralized VCS (SVN/TFVC) or unversioned code; long-lived branches (> 6 months).
- [ ] Level 3: Git with GitFlow; feature branches merged weekly with PR reviews.
- [ ] Level 5: Trunk-based development; daily main merges; feature flags for dark launches.

### B. Continuous Integration (CI)
- [ ] Level 1: Builds run on local developer laptops; manual compilation.
- [ ] Level 3: CI server builds on every commit; unit tests pass before merge; build time < 15 mins.
- [ ] Level 5: Distributed build caching (Nx/Bazel); parallelized matrix tests; build time < 5 mins.

### C. Testing Automation
- [ ] Level 1: 100% manual QA testing team; regression testing takes 2 weeks.
- [ ] Level 3: Unit and integration tests automated in CI; code coverage >= 70%; smoke tests.
- [ ] Level 5: Testcontainers, consumer-driven contract tests (Pact), mutation testing, and automated performance gates.

### D. Security & Compliance (DevSecOps)
- [ ] Level 1: Security audits performed once a year before release; credentials hardcoded in Git.
- [ ] Level 3: Secret scanning in pre-commit; SAST/SCA scanners run in CI; manual approval for CVEs.
- [ ] Level 5: SLSA Level 3/4 provenance, automated SBOM generation, image signing (Cosign), zero-trust OIDC runners.

### E. Deployment Automation
- [ ] Level 1: Manual copy via SSH/FTP; multi-hour downtime maintenance windows.
- [ ] Level 3: Automated blue/green or rolling deployment via CI/CD; zero downtime for standard releases.
- [ ] Level 5: GitOps (ArgoCD) pull-based reconciliation, canary analysis with automated rollback based on SLO metrics.

### F. Infrastructure Automation (IaC)
- [ ] Level 1: Cloud/VM resources clicked manually in web consoles; snowflake servers.
- [ ] Level 3: Terraform/Ansible used to provision environments; state files stored remotely.
- [ ] Level 5: Crossplane/Terraform modules in self-service IDP; Policy-as-Code (OPA/Kyverno) enforcing compliance.

### G. Observability & Feedback
- [ ] Level 1: Logging to text files on disk; users report outages before engineering knows.
- [ ] Level 3: Centralized logging (ELK/Datadog); infrastructure metrics; basic PagerDuty alerts.
- [ ] Level 5: OpenTelemetry distributed tracing; SLO-based error budget alerting; canary metrics validation.

## 2. Scoring & Roadmap Formulation
- **0 - 20 Points**: Stage 1 (High Risk — Immediate automation of source control, CI, and secrets required).
- **21 - 40 Points**: Stage 2-3 (Emerging — Focus on pipeline consistency and test automation).
- **41 - 55 Points**: Stage 4 (Modern DevSecOps — Shift-left security and immutable artifacts).
- **56 - 65 Points**: Stage 5 (Elite Platform — Self-service developer platform and golden paths).

## Related Resources
- [DevOps Foundations](../devops-foundations/README.md)
- [DevOps Transformation Roadmap](../devops-transformation/README.md)
