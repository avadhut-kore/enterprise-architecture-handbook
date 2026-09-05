# Application Rationalization: The 7R Decision Framework

A systematic strategy for determining the disposition of every legacy application in the enterprise portfolio.

---

## 1. The 7R Rationalization Taxonomy

```mermaid
flowchart TD
    App["Application Evaluation"] --> Decision{"Business Value & Technical Health Assessment"}
    Decision -->|High Value, Modern Architecture| Retain["1. Retain / Invest: Enhance & Expand"]
    Decision -->|Low Value, Obsolete / Duplicate| Retire["2. Retire: Decommission & Archive"]
    Decision -->|Commodity Capability, High Maintenance| Replace["3. Replace / Repurchase: Adopt Standard SaaS"]
    Decision -->|Healthy Software, Legacy Datacenter| Rehost["4. Re-host: Lift & Shift to Cloud IaaS"]
    Decision -->|Requires Cloud Scale, Code Sound| Replatform["5. Re-platform: Migrate to Managed PaaS/Containers"]
    Decision -->|High Strategic Value, High Tech Debt| Rearchitect["6. Re-architect: Decompose into Microservices"]
    Decision -->|Low Value, Stable, Non-Disruptive| Tolerate["7. Tolerate: Freeze features, maintain run"]
```

---

## 2. Cross-Phase Reference
For deep technical strangler-fig migration patterns, database decoupling, and cutover playbooks, see **[15-modernization](../../15-modernization/README.md)**.
