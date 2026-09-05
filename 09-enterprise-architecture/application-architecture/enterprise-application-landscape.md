# Enterprise Application Landscape

How to categorize and structure hundreds or thousands of software applications across a global organization.

---

## 1. The 3-Tier Enterprise Application Hierarchy (Pace-Layered)

```mermaid
graph TD
    subgraph Systems of Innovation (Rapid Change: Weeks/Months)
        I1["Mobile Apps & Portals"]
        I2["Generative AI Copilots"]
        I3["Marketing Campaign Micro-sites"]
    end
    subgraph Systems of Differentiation (Medium Change: Months/Year)
        D1["Custom Pricing & Underwriting Engine"]
        D2["Proprietary Recommendation Model"]
        D3["B2B Partner API Gateway"]
    end
    subgraph Systems of Record (Slow Change: Years/Decades)
        R1["SAP S/4HANA ERP Core"]
        R2["Mainframe Ledger"]
        R3["Customer Master Data Management (MDM)"]
    end
    I1 --> D1
    I2 --> D2
    D1 --> R1
    D2 --> R3
```

* **Systems of Record**: The transactional bedrock (ERP, core banking, billing). Architectural rule: prioritize stability, strict ACID transactions, and compliance.
* **Systems of Differentiation**: Proprietary capabilities that provide competitive advantage. Architectural rule: prioritize modularity, agility, and domain-driven design.
* **Systems of Innovation**: Short-lived experiments and emerging customer touchpoints. Architectural rule: prioritize rapid iteration, serverless runtimes, and low blast radius.
