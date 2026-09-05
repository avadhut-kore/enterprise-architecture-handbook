# ADR-0052: Adoption of Zero Trust Network Architecture and Identity-Aware Proxies

## Metadata
```yaml
id: ADR-0052
title: Adoption of Zero Trust Network Architecture and Identity-Aware Proxies
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Traditional castle-and-moat corporate VPNs granted excessive lateral network access, creating severe security breach risks.

---

## 2. Decision
We adopt a Zero Trust Architecture where identity is the primary perimeter, enforcing mutual TLS (mTLS) for east-west traffic and Identity-Aware Proxies (IAP) for human administrative access.

---

## 3. Positive Consequences
- Eliminates lateral movement following an edge network breach.
- Provides cryptographic verification for every internal microservice call.
- Eliminates corporate VPN maintenance.

---

## 4. Negative Consequences & Trade-offs
- Requires managing PKI certificates (SPIFFE/SPIRE or service mesh).
- Minor latency overhead (< 1ms) for mTLS handshakes.

---

## 5. Alternatives Considered & Rejected
- **Traditional Flat Corporate VPN**: Rejected due to lack of micro-segmentation and high lateral movement risk.
