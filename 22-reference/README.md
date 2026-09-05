# Architecture Reference (`22-reference/`)

## Executive Summary

The `22-reference/` directory contains curated dictionaries, acronym definitions, technology comparison matrices, and architectural trade-off evaluations across enterprise computing disciplines.

---

## 1. Glossaries & Terminology
* [`glossaries/architecture-glossary.md`](glossaries/architecture-glossary.md) - Terminology definitions for enterprise, system, and cloud architecture.
* [`acronyms/architecture-acronyms.md`](acronyms/architecture-acronyms.md) - Standard industry acronym definitions (ADR, CCOE, CSPM, FIDO2, mTLS, OIDC, PKCE, RTO, RPO, SLI, SLO, WORM).

---

## 2. Technology & Architectural Trade-off Matrices (`technology-comparison/`)

### Security Comparisons (`technology-comparison/security/`)
* Matrices evaluating JWT vs Opaque tokens, RBAC vs ABAC vs ReBAC, OAuth vs API keys, OIDC vs SAML, mTLS vs Token auth, KMS vs Cloud HSM, and SAST vs DAST vs SCA.

### Operational & SRE Comparisons (`technology-comparison/operations/`)
* Matrices evaluating Active-Active vs Active-Passive DR, Canary vs Blue-Green rollouts, Centralized vs Team-owned ops, and Multi-window burn alerting vs static thresholds.

### Cloud & Infrastructure Comparisons (`technology-comparison/cloud/`)
* Matrices evaluating Cloud Providers (AWS vs Azure vs GCP), Cloud Strategies, Compute Platforms, Database Hosting, and Storage Paradigms.

### Data & Integration Comparisons (`technology-comparison/data-integration/`)
* Comparative matrices for Database Engines, Messaging/Streaming, API Protocols, and Reconciliation Approaches.

### Application Architecture Comparisons (`technology-comparison/application-architecture/`)
* Comparative matrices for Backend Frameworks, Frontend Frameworks, Mobile Frameworks, and State Management.
