# Circular Dependencies: Detection and Refactoring

## 1. Root Causes of Circular Coupling
Circular dependencies occur when developers take shortcuts:
- Module A (`Billing`) needs customer details from Module B (`Customer`).
- Later, Module B (`Customer`) needs invoice summaries from Module A (`Billing`).

---

## 2. Refactoring Strategies

```mermaid
flowchart TB
    subgraph Cycle [Before: Circular Dependency]
        A[Module A: Billing] <--> B[Module B: Customer]
    end

    subgraph Solution1 [Solution: Extract Shared Interface]
        A2[Module A: Billing] --> IB[Interface: ICustomerSummary]
        B2[Module B: Customer] ..|> IB
    end

    subgraph Solution2 [Solution: Extract Third Module]
        A3[Module A: Billing] --> Shared[Module C: CustomerInvoicing]
        B3[Module B: Customer] --> Shared
    end
```
