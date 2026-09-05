# Security Architecture Decision Frameworks (`decision-frameworks/`)

## Executive Summary

This directory contains 16 formal architectural decision scorecards evaluating complex security trade-offs across identity, authorization, cryptography, and network perimeters.

---

## Decision Framework Index

| Framework | Core Trade-Off | Primary Recommendation |
| :--- | :--- | :--- |
| [`rbac-vs-abac-vs-rebac.md`](rbac-vs-abac-vs-rebac.md) | Authorization Model | RBAC for coarse roles; ABAC/PBAC for fine-grained contextual rules |
| [`oauth2-vs-api-keys.md`](oauth2-vs-api-keys.md) | API Authentication | OAuth 2.0 with PKCE for user apps; mTLS/private keys for M2M |
| [`jwt-vs-opaque-tokens.md`](jwt-vs-opaque-tokens.md) | Session Representation | JWT for internal microservices; Opaque tokens for public web sessions |
| [`saml-vs-oidc.md`](saml-vs-oidc.md) | Federation Protocol | OIDC for cloud, mobile, and APIs; SAML 2.0 for legacy enterprise apps |
| [`centralized-vs-decentralized-authorization.md`](centralized-vs-decentralized-authorization.md) | Policy Topology | Centralized policy authoring with decentralized sidecar evaluation (OPA) |
| [`mtls-vs-token-authentication.md`](mtls-vs-token-authentication.md) | Service-to-Service | Layered defense: mTLS for transport + JWT for application user context |
| [`waf-vs-application-validation.md`](waf-vs-application-validation.md) | Edge vs Code | Defense-in-depth: WAF blocks broad scanning; code validates business rules |
| [`tokenization-vs-column-encryption.md`](tokenization-vs-column-encryption.md) | Data Protection | Tokenization for PCI compliance; column encryption for internal queries |
| [`kms-vs-cloud-hsm.md`](kms-vs-cloud-hsm.md) | Key Custody | Multi-tenant KMS for 99% of workloads; Cloud HSM for banking/PKI roots |
| [`centralized-vault-vs-cloud-secrets.md`](centralized-vault-vs-cloud-secrets.md) | Secret Storage | Vault for multi-cloud & dynamic credentials; native cloud secrets for simple apps |
| [`automated-gates-vs-advisory-ci.md`](automated-gates-vs-advisory-ci.md) | DevSecOps Gating | Strict blocking gates on Critical CVEs; advisory on Low/Medium |
| [`sast-vs-dast-vs-sca-investment.md`](sast-vs-dast-vs-sca-investment.md) | Tooling Budget | Balanced allocation: 40% SCA, 35% SAST, 25% DAST/PenTesting |
| [`managed-cspm-vs-open-source.md`](managed-cspm-vs-open-source.md) | Posture Defense | Managed CSPM for enterprise compliance; open source (Prowler) for audits |
| [`zero-trust-mesh-vs-ingress-only.md`](zero-trust-mesh-vs-ingress-only.md) | Zero Trust Scope | Full service mesh (Istio) for microservices; ZTNA proxy for user access |
| [`subnet-isolation-vs-ebpf-microsegmentation.md`](subnet-isolation-vs-ebpf-microsegmentation.md) | Microsegmentation | Subnet tiering for coarse blast radius; eBPF (Cilium) for pod-to-pod |
| [`cryptographic-tenancy-vs-database-per-tenant.md`](cryptographic-tenancy-vs-database-per-tenant.md) | SaaS Data Model | Cryptographic per-tenant KMS keys in shared DB for cost-effective scale |
