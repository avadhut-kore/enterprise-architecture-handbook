# Architecture Governance Framework

Modern architecture governance enables safe, autonomous engineering velocity through transparent guardrails.

---

## 1. The 3 Lines of Architectural Defense

```mermaid
flowchart TD
    subgraph Line 1: Delivery Squads & Solution Architects
        L1["Self-governance via Paved Roads & Automated CI/CD Fitness Checks"]
    end
    subgraph Line 2: Architecture Review Board (ARB) & Domain Architects
        L2["Peer Review, Standards Enforcement & Exception Adjudication"]
    end
    subgraph Line 3: Internal IT Audit & CISO
        L3["Independent Verification, Compliance Audits & Risk Reporting to Board"]
    end
    L1 -->|Submits Solutions & Exceptions| L2
    L2 -->|Provides Risk Registry Data| L3
```
