# Security & Operations Reference Architectures (`18-reference-architectures/security-operations/`)

## Executive Summary

This directory provides 6 end-to-end production architectural blueprints demonstrating how security guardrails, zero trust controls, automated SRE reliability patterns, and continuous operations integrate across high-scale enterprise systems.

---

## Reference Blueprint Index

| Blueprint File | Architecture Pattern | Key Invariants |
| :--- | :--- | :--- |
| [`secure-enterprise-web-application.md`](secure-enterprise-web-application.md) | Multi-Tier Web Security | WAF, Edge CDN, BFF OIDC auth, encrypted private Aurora DB, SIEM logging |
| [`zero-trust-enterprise-architecture.md`](zero-trust-enterprise-architecture.md) | Universal Zero Trust | Identity-as-perimeter, device posture check, mTLS mesh, microsegmentation |
| [`secure-kubernetes-platform-architecture.md`](secure-kubernetes-platform-architecture.md) | Hardened Container Platform | OPA/Kyverno admission, Cilium eBPF, Distroless images, read-only root FS |
| [`secure-cicd-supply-chain-platform.md`](secure-cicd-supply-chain-platform.md) | Supply Chain & DevSecOps | Hermetic builds, CycloneDX SBOM, Cosign keyless signing, SLSA Level 3 |
| [`security-operations-siem-platform.md`](security-operations-siem-platform.md) | Detection & Response | Streaming telemetry (Kafka/Kinesis), OpenSearch/Sentinel, SOAR playbooks |
| [`highly-reliable-enterprise-platform.md`](highly-reliable-enterprise-platform.md) | SRE Resiliency Blueprint | Multi-AZ quorums, circuit breakers, canaries, multi-window burn alerting |
