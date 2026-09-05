# Enterprise Integration: Hybrid & Multi-Cloud Integration Architecture

## 1. Architectural Purpose & Problem Context
Bridging on-premises legacy data centers with multi-cloud workloads: dedicated interconnects (Direct Connect / ExpressRoute), reverse proxies, and mTLS.

---

## 2. API-Led 3-Tier Integration Architecture

```mermaid
flowchart TD
    subgraph Experience Layer
        WebExp[Web Portal Experience API]
        MobileExp[Mobile App Experience API]
        PartnerExp[Partner B2B Experience API]
    end
    subgraph Process Layer
        OrderProcess[Order Fulfillment Process API]
        BillingProcess[Billing & Invoice Process API]
    end
    subgraph System Layer
        SAPSystem[SAP ERP System API]
        SalesforceSystem[Salesforce CRM System API]
        DBSystem[Core Database System API]
    end

    WebExp --> OrderProcess
    MobileExp --> OrderProcess
    PartnerExp --> BillingProcess
    OrderProcess --> SAPSystem
    OrderProcess --> SalesforceSystem
    BillingProcess --> SAPSystem
    BillingProcess --> DBSystem
```

---

## 3. Production Invariants
- Avoid building monolithic centralized ESB bottlenecks where business logic is trapped inside proprietary integration bus scripts.
- Enforce strict layer boundaries: Experience APIs must never bypass the Process layer to directly query backend databases.
