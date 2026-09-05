# DevOps Production Readiness Review (PRR) Scorecard

No service may be deployed to production without completing the DevOps Production Readiness Review.

## 1. The Multi-Tier PRR Checklist

### A. Application & Build Pipeline
- [ ] Build is fully automated, deterministic, and executes in CI.
- [ ] Dependencies are pinned with strict lockfiles; zero floating versions.
- [ ] Artifacts are immutable, versioned with SemVer, and pushed to enterprise registry.
- [ ] Code coverage meets minimum threshold (>= 75%) with unit and integration tests passing.

### B. Security & Compliance
- [ ] Pre-commit secret scanning enabled (zero credentials in Git).
- [ ] Static Application Security Testing (SAST) passed with zero Critical or High CVEs.
- [ ] Software Composition Analysis (SCA) verified; dependencies free of unpatched critical CVEs.
- [ ] Container images built as non-root; distroless or minimal base image utilized.
- [ ] Image signed cryptographically via Cosign / Sigstore.
- [ ] Secrets retrieved dynamically from HashiCorp Vault or cloud secret manager; zero plaintext secrets.

### C. Infrastructure & Kubernetes
- [ ] All infrastructure provisioned declaratively via Infrastructure as Code (Terraform / GitOps).
- [ ] Kubernetes resource requests and limits explicitly declared; memory request == limit.
- [ ] Pod Disruption Budget (PDB) configured (`minAvailable >= 1` or `maxUnavailable <= 25%`).
- [ ] Liveness (`/health/live`) and Readiness (`/health/ready`) probes configured and decoupled.
- [ ] Horizontal Pod Autoscaling (HPA) configured with realistic min/max thresholds.

### D. Operations & SRE
- [ ] Structured JSON logging emitted to stdout/stderr with correlation/trace IDs propagated.
- [ ] OpenTelemetry distributed tracing enabled.
- [ ] Prometheus metrics exposed for golden signals (Latency, Traffic, Errors, Saturation).
- [ ] PagerDuty alerts configured with actionable runbooks linked in alert payloads.
- [ ] SLOs and error budgets formally agreed with product owners.

### E. Deployment & Recovery
- [ ] Automated canary or blue/green deployment strategy configured.
- [ ] Automated rollback verified in staging (< 60 seconds rollback time).
- [ ] Database migrations backward-compatible (Expand/Contract pattern).
- [ ] Disaster recovery RPO and RTO tested and documented.

## Related Resources
- [Production Readiness Review Mastery](../../24-architect-mastery/operations/production-readiness-review-mastery.md)
- [Checklists Hub](../checklists/README.md)
