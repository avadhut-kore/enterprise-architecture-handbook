# Organizational Architecture Scenarios: M&A, Consolidation & Compliance

> Handling complex socio-technical crises: post-merger technology consolidation, ambiguous domain ownership, and emergency regulatory compliance mandates.

---

## 1. Scenario: Post-Acquisition (M&A) Platform Consolidation

### The Crisis
Your company (Platform A, built on AWS, Go, PostgreSQL) acquires a direct competitor (Platform B, built on Azure, C# .NET, SQL Server). The executive board mandates that customer accounts and product catalogs must be unified within 6 months to cross-sell products, with a full backend consolidation completed within 18 months.

```mermaid
flowchart LR
    subgraph CompanyA [Platform A (AWS / Go / Postgres)]
        UsersA[Customers A] --> CoreA[Core A]
    end
    
    subgraph CompanyB [Platform B (Azure / .NET / SQL Server)]
        UsersB[Customers B] --> CoreB[Core B]
    end
    
    Federation[Unified API Gateway & Identity Federation: OIDC / Okta]
    Federation --> CoreA
    Federation --> CoreB
```

### Strategic Architectural Roadmap
* **Horizon 1: Unified Identity & Experience (Months 1–3)**:
  * Do not attempt to merge databases immediately.
  * Deploy a unified Identity Provider (IdP) supporting OpenID Connect (OIDC). Federate authentication across Platform A and B so users can log into both portals with a single credential.
  * Place an **Enterprise API Gateway** in front of both platforms to provide a single unified public API contract.
* **Horizon 2: Master Data Management & Cross-Platform Sync (Months 4–9)**:
  * Deploy an event mesh (Kafka) connecting AWS and Azure.
  * Synchronize catalog and inventory events bidirectionally using Change Data Capture.
* **Horizon 3: Systematic Convergence & Decommissioning (Months 10–18)**:
  * Migrate Platform B customer data in waves into Platform A's multi-tenant architecture.
  * Decommission Platform B's legacy Azure infrastructure, realizing $4M in annual licensing and hosting synergies.

---

## 2. Scenario: Ambiguous Domain Ownership & Multi-Team Gridlock

### The Crisis
A major payment processing bug goes unresolved for 2 weeks. The "Checkout Squad" claims the bug belongs to the "Billing Squad"; the "Billing Squad" claims it belongs to the "Platform Payments Squad." No one owns the service, and deploy pipelines are frozen.

### Architectural Governance Resolution
1. **Enforce the Single-Owner Domain Rule**:
   * Every microservice repository and datastore must have an explicit `CODEOWNERS` entry mapping to exactly one stream-aligned team.
2. **Apply Bounded Context Clarification**:
   * Conduct an **Event Storming Workshop** with leads from all three teams. Trace the lifecycle of an order:
     * Checkout Squad owns: Cart, Discount Application, Order Submission.
     * Payments Squad owns: Gateway Integration (Stripe/Adyen), Tokenization, Charge Attempts.
     * Billing Squad owns: Invoicing, Tax Reporting, Subscription Renewals.
3. **Publish Service-Level Agreements (SLAs)**: Define internal OLAs (Operational Level Agreements) for inter-team support tickets.

---

## 3. Cross-References

* **Team Topologies**: [`leadership/team-topology.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/leadership/team-topology.md)
* **Conflict Resolution**: [`leadership/conflict-management.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/leadership/conflict-management.md)
* **Enterprise Architecture Integration**: [`23-enterprise-architecture/handle-ma-technology-integration.md`](file:///d:/company/products/enterprise-architecture-handbook/23-enterprise-architecture/handle-ma-technology-integration.md)
