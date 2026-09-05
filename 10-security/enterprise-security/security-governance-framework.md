# Enterprise Security Governance Framework

## Executive Summary

Enterprise security governance establishes the organizational structure, authority lines, control objectives, and reporting mechanisms that ensure technical systems align with enterprise risk appetite.

---

## 1. The Three Lines of Defense Model

```mermaid
flowchart TD
    subgraph Line1 ["First Line of Defense (Engineering & Operations)"]
        A["Software Developers"]
        B["Solution Architects"]
        C["Cloud SREs / Ops"]
    end
    subgraph Line2 ["Second Line of Defense (Risk & Compliance)"]
        D["Information Security (CISO)"]
        E["Enterprise Architecture Board"]
        F["Privacy & Compliance Office"]
    end
    subgraph Line3 ["Third Line of Defense (Independent Assurance)"]
        G["Internal Audit"]
        H["External Regulators / Certifiers"]
    end
    Line1 -->|Builds & Operates Controls| Line2
    Line2 -->|Sets Policies & Oversees Compliance| Line1
    Line3 -->|Independently Audits & Validates| Line1
    Line3 -->|Independently Audits & Validates| Line2
```

---

## 2. Key Responsibilities Across the Three Lines

1. **First Line (Engineering & Architecture)**:
   - Owns day-to-day risk management and control implementation.
   - Authors threat models, adheres to secure coding standards, and remediates vulnerabilities within SLA.
2. **Second Line (Security & Governance)**:
   - Establishes enterprise security standards, policies, and control baselines.
   - Operates centralized detection tooling (SIEM), conducts ARB architecture security reviews, and governs risk acceptance.
3. **Third Line (Internal Audit)**:
   - Provides objective, board-level assurance that First and Second Line controls are operating effectively.
