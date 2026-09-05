# Business Capability Architecture

Business Capability Architecture is the cornerstone of Enterprise Architecture. It establishes what an organization does to deliver value, providing a stable, technology-agnostic foundation for IT investment, application rationalization, and digital transformation.

---

## 1. The Capability Hierarchy

Capabilities are organized into a strict, mutually exclusive, collectively exhaustive (MECE) 3-tier hierarchy:

```text
Level 1: Domain Capability (Macro Category)
  └── Level 2: Core Capability (Operational Competency)
        └── Level 3: Specific Capability (Discrete Functional Ability)
```

```mermaid
graph TD
    L1["Level 1: Customer Relationship Management"]
    L1 --> L2A["Level 2: Customer Acquisition"]
    L1 --> L2B["Level 2: Customer Service"]
    L1 --> L2C["Level 2: Customer Identity & KYC"]
    L2A --> L3A["Level 3: Lead Scoring"]
    L2A --> L3B["Level 3: Campaign Personalization"]
    L2C --> L3C["Level 3: Document Biometric Verification"]
    L2C --> L3D["Level 3: Watchlist Sanctions Screening"]
```

---

## 2. Directory Contents

* **[capability-modeling-principles.md](capability-modeling-principles.md)**: Rules for identifying, scoping, and naming capabilities.
* **[capability-decomposition.md](capability-decomposition.md)**: Deep decomposition playbooks and MECE boundaries.
* **[capability-ownership-and-maturity.md](capability-ownership-and-maturity.md)**: Ownership models, RACI, and capability maturity scoring.
* **[capability-heatmaps.md](capability-heatmaps.md)**: Strategic, operational health, and investment heatmaps.
* **[capability-duplication-and-rationalization.md](capability-duplication-and-rationalization.md)**: Identifying redundant systems and consolidating platforms.
* **[capability-mapping-templates.md](capability-mapping-templates.md)**: Standard templates linking Capability $	o$ Process $	o$ Application $	o$ Data $	o$ Infrastructure.
