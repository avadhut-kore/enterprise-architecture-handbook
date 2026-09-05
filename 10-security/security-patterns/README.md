# Production Security Architecture Patterns (`security-patterns/`)

## Executive Summary

This directory catalogs 17 battle-tested enterprise security architecture patterns. Every pattern strictly adheres to the standard 11-section architectural specification:
$$\text{Problem} \rightarrow \text{Context} \rightarrow \text{Threats} \rightarrow \text{Architecture} \rightarrow \text{Controls} \rightarrow \text{When to Use} \rightarrow \text{When NOT to Use} \rightarrow \text{Trade-offs} \rightarrow \text{Failure Modes} \rightarrow \text{Ops} \rightarrow \text{Evolution}$$

---

## Pattern Index

| Pattern | Focus Domain | Architectural Invariant |
| :--- | :--- | :--- |
| [`zero-trust-identity-perimeter.md`](zero-trust-identity-perimeter.md) | Network/Identity | Verify explicitly; network location provides zero implicit trust |
| [`api-gateway-security-chokepoint.md`](api-gateway-security-chokepoint.md) | Edge & APIs | Non-bypassable ingress gateway enforcing rate limits & auth |
| [`backend-for-frontend-security.md`](backend-for-frontend-security.md) | Frontend/API | BFF terminates public cookies; mints internal microservice JWTs |
| [`service-to-service-mtls.md`](service-to-service-mtls.md) | Microservices | Mutual TLS with short-lived X.509 certs & SPIFFE IDs |
| [`centralized-identity-oidc.md`](centralized-identity-oidc.md) | Enterprise IAM | Single Source of Truth IdP federating via OpenID Connect |
| [`federated-identity-broker.md`](federated-identity-broker.md) | B2B / SaaS | Dynamic Home Realm Discovery federating with partner IdPs |
| [`dynamic-secrets-management.md`](dynamic-secrets-management.md) | Secrets Governance | Ephemeral database credentials generated on-demand via Vault |
| [`envelope-encryption-pattern.md`](envelope-encryption-pattern.md) | Cryptography | Local AES-256 data encryption using KMS-protected DEKs |
| [`secure-file-upload-quarantine.md`](secure-file-upload-quarantine.md) | Application/Storage | Two-bucket asynchronous malware scanning and quarantine |
| [`secure-webhook-hmac.md`](secure-webhook-hmac.md) | Integration | Asymmetric or HMAC-SHA256 request signing with replay nonces |
| [`secure-event-processing-idempotency.md`](secure-event-processing-idempotency.md) | Messaging/Kafka | Distributed idempotency keys preventing double-processing |
| [`cryptographic-tenant-isolation.md`](cryptographic-tenant-isolation.md) | Multi-Tenant SaaS | Dedicated per-tenant KMS keys isolating multi-tenant datastores |
| [`ebpf-network-microsegmentation.md`](ebpf-network-microsegmentation.md) | Infrastructure/K8s | Kernel-level L3/L4/L7 policy enforcement without iptables |
| [`just-in-time-privileged-access.md`](just-in-time-privileged-access.md) | PIM / PAM | Zero standing admin rights; time-bound peer-approved elevation |
| [`secure-cicd-supply-chain.md`](secure-cicd-supply-chain.md) | DevSecOps | Hermetic builds, verified CycloneDX SBOMs, and Cosign signatures |
| [`hardened-kubernetes-pod-standard.md`](hardened-kubernetes-pod-standard.md) | Container/K8s | Distroless base images, read-only root FS, dropped capabilities |
| [`tokenization-privacy-proxy.md`](tokenization-privacy-proxy.md) | Compliance/PCI | Format-preserving tokenization proxy reducing regulatory CDE scope |
