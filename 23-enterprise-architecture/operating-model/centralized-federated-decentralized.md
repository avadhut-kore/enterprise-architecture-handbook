# Centralized vs Federated vs Decentralized Operating Models

A decision framework for allocating architectural decision rights across corporate headquarters, business units, and autonomous engineering squads.

---

## 1. Trade-Off Evaluation Matrix

| Dimension | Centralized Model | Federated Model (Recommended) | Decentralized / Autonomous |
| :--- | :--- | :--- | :--- |
| **Decision Authority** | Central Architecture Committee. | Central Core defines guardrails; Domain SAs decide within boundaries. | Individual teams make all technology choices. |
| **Speed of Local Innovation** | Slow (bottlenecked by central approval). | High (fast local execution within approved paved roads). | Maximum local speed; rapid experimentation. |
| **Enterprise Standard Consistency** | Maximum (monolithic compliance). | High (common platforms, consistent interfaces, shared data models). | Extremely Low (extreme technology sprawl, duplicate spend). |
| **Technical Debt Accumulation** | Low localized debt; high corporate bureaucracy. | Governed debt with systematic tracking and remediation roadmaps. | Severe unmanaged debt; incompatible systems across teams. |
| **Enterprise TCO** | Low software licensing duplication; high coordination overhead. | Optimal TCO (economies of scale on platforms, rapid value delivery). | Catastrophic TCO (duplicate SaaS contracts, incompatible data pipelines). |

---

## 2. Recommended Decision Boundaries
* **Centralized Mandate**: Cloud landing zones, core identity (IAM), enterprise security baselines, master data definitions, enterprise AI gateway.
* **Federated Discretion**: Solution component design, localized database engine selection (within approved radar), framework language choice (within approved standards).
* **Decentralized Discretion**: Code modularity, internal class hierarchies, unit test frameworks, sprint task sequencing.
