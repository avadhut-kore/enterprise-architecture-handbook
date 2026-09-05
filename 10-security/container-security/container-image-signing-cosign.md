# Container Image Signing & Verification (Sigstore Cosign)

## Executive Summary

Image signing guarantees that a container image running in production was produced by an authorized enterprise CI/CD pipeline and has not been tampered with in the registry.

---

## 1. Keyless Signing Architecture

```mermaid
sequenceDiagram
    autonumber
    participant CI as GitHub Actions CI Pipeline
    participant Fulcio as Sigstore Fulcio (CA)
    participant OIDC as GitHub OIDC Issuer
    participant Registry as Container Registry (ECR / ACR)
    participant Rekor as Rekor Transparency Log
    participant K8s as Kubernetes Cluster (Kyverno)

    CI->>OIDC: Requests short-lived OIDC Identity Token
    OIDC-->>CI: Returns signed OIDC token
    CI->>Fulcio: Presents OIDC token; requests short-lived X.509 cert
    Fulcio-->>CI: Issues 10-minute signing certificate
    CI->>Registry: Signs image hash via Cosign
    CI->>Rekor: Writes cryptographic signature entry to public immutable log
    
    Note over K8s: Production Admission Control
    K8s->>Registry: Image deployment requested
    K8s->>Rekor: Verifies signature, Fulcio cert, and GitHub workflow identity
    K8s-->>K8s: Image verified; pod allowed to start!
```
