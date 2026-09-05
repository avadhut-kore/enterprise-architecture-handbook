# Enterprise Artifact Management Architecture

Artifact management establishes the single source of truth for compiled binaries, container images, libraries, and Helm charts across the enterprise.

## 1. The Build Once, Promote Everywhere Axiom

```
[Source Commit]
       │
       ▼ (Build Exactly Once)
[Immutable OCI Container Image / Library]
       │
       ▼ (Promote Same Hash)
┌─────────────────────────────────────────────────────────────┐
│                      ARTIFACT REGISTRY                      │
│                  (Artifactory / Harbor / ECR)               │
├──────────────────────────────┬──────────────────────────────┤
│ DEV/TEST REGISTRY            │ PRODUCTION REGISTRY          │
│ - Short retention (14 days)  │ - Immutable retention policy │
│ - Vulnerability scan on push │ - Cryptographically signed   │
│ - Candidate for promotion    │ - Full SLSA provenance & SBOM│
└──────────────────────────────┴──────────────────────────────┘
```

## 2. Core Requirements
- **Immutability**: Never overwrite existing tags (e.g., `v1.2.0`). Tags must point permanently to the exact same SHA-256 digest.
- **Automated Lifecycle Policies**: Automatically purge untagged intermediate PR builds after 14 days to prevent runaway cloud storage bills.
- **Attestation & Signing**: Sign all production artifacts with Cosign/Sigstore; enforce Kubernetes admission controllers (Kyverno) to reject unsigned images.

## Related Resources
- [Software Supply Chain](../software-supply-chain/README.md)
- [DevSecOps Architecture](../devsecops/README.md)
