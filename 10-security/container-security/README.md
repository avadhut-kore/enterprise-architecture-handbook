# Container Security Architecture (`container-security/`)

## Executive Summary

Containers package application runtimes and OS userland dependencies. Container security requires a defense-in-depth pipeline: minimal hardened base images, automated vulnerability scanning, cryptographic image signing, rootless container execution, and real-time eBPF runtime monitoring.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`container-security-architecture.md`](container-security-architecture.md) | Container Hardening | Distroless images, non-root users, dropping Linux capabilities |
| [`container-vulnerability-scanning.md`](container-vulnerability-scanning.md) | Static Scanning | Trivy / Grype, gating CI/CD builds on CVE thresholds |
| [`container-image-signing-cosign.md`](container-image-signing-cosign.md) | Image Integrity | Sigstore Cosign, keyless OIDC signing, Rekor transparency log |
| [`container-runtime-security.md`](container-runtime-security.md) | Runtime Defense | Falco eBPF kernel syscall monitoring, anomaly detection |
