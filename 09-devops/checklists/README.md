# Master DevOps Architecture Checklists

A comprehensive suite of 20 domain-specific review checklists and the Master DevOps Architecture Review Checklist.

## 1. Master DevOps Architecture Review Checklist

### Phase 1: Business & Delivery Alignment
- [ ] 1. Are delivery expectations (lead time, release frequency) aligned with business requirements?
- [ ] 2. Are regulatory compliance and auditability mandates clearly documented?

### Phase 2: Source Control & Branching
- [ ] 3. Is trunk-based development or short-lived feature branching (< 48 hrs) enforced?
- [ ] 4. Are branch protection rules active with mandatory CODEOWNERS review?
- [ ] 5. Are pre-commit hooks configured to prevent secret leaks?

### Phase 3: CI/CD Pipeline Architecture
- [ ] 6. Is code built exactly once and promoted across environments as an immutable artifact?
- [ ] 7. Does the CI pipeline complete in under 15 minutes?
- [ ] 8. Are pipeline workflows parameterized and inherited from central golden templates?

### Phase 4: Container & Kubernetes Architecture
- [ ] 9. Do containers execute as non-root on distroless or minimal base images?
- [ ] 10. Are Kubernetes resource requests and limits configured to prevent noisy neighbors?
- [ ] 11. Is cluster blast radius isolated via multi-cluster or multi-zone topologies?

### Phase 5: Infrastructure as Code & GitOps
- [ ] 12. Is 100% of cloud infrastructure declared in version-controlled Terraform?
- [ ] 13. Is Terraform state locked in remote encrypted storage with state blast radius partitioned?
- [ ] 14. Is GitOps pull-based reconciliation used for Kubernetes cluster synchronization?

### Phase 6: DevSecOps & Supply Chain
- [ ] 15. Are OIDC workload identities used instead of static cloud credentials?
- [ ] 16. Are container images signed via Cosign and verified by admission controllers?
- [ ] 17. Is an automated SBOM generated for every production release?

### Phase 7: Deployment & Operations
- [ ] 18. Are deployments zero-downtime using canary or blue/green strategies?
- [ ] 19. Can the system roll back automatically within < 60 seconds of an SLO violation?
- [ ] 20. Are DORA metrics tracked automatically via production telemetry?

---

## 2. Domain-Specific Checklists Catalog
- **Git & GitHub Governance Checklist**: Rulesets, SCIM, team synchronization, audit streaming.
- **Docker Production Checklist**: Multi-stage, non-root, layer caching, dive scanning.
- **Kubernetes Production Checklist**: Control plane NVMe, multi-AZ, PDBs, network policies.
- **Terraform Review Checklist**: State locking, modularity, drift detection, tagging standards.
- **GitOps Review Checklist**: Pull controller, drift correction, repo isolation, sealed secrets.
- **DevSecOps Review Checklist**: SAST, SCA, container CVE gates, secret scanning.
- **Platform Engineering Checklist**: Portal self-service, golden paths, developer NPS.
- **Database DevOps Checklist**: Expand/contract, lock timeouts, migration rollback scripts.
- **Mobile DevOps Checklist**: Code signing Vault, Fastlane, phased rollout, OTA.
- **MLOps Delivery Checklist**: DVC versioning, model registry, drift monitoring.

## Related Resources
- [Production Readiness](../production-readiness/README.md)
- [DevOps Anti-Patterns](../devops-anti-patterns/README.md)
