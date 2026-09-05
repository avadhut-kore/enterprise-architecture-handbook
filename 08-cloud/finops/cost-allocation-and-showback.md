# Cloud Cost Allocation, Showback & Chargeback

## Executive Summary

Without precise cost allocation, cloud bills become an unallocated corporate overhead expense ("black box IT").

---

## 1. Showback vs Chargeback

```mermaid
graph TD
    subgraph Stage 1: Cost Visibility (Showback)
        Bill1[Monthly AWS/Azure Bill] --> Report[Generate Cost Dashboards per Engineering Team]
        Report --> Awareness[Builds Financial Awareness Without Moving Money]
    end

    subgraph Stage 2: Financial Accountability (Chargeback)
        Bill2[Monthly Cloud Bill] --> Ledger[Corporate ERP / SAP Financial Journal]
        Ledger --> Debit[Directly Debits Business Unit P&L Budget!]
    end
```

---

## 2. Allocating Shared Infrastructure Costs
- **The Shared Cost Dilemma**: Shared services (Transit Gateways, central logging accounts, Kubernetes shared clusters) cannot be tagged to a single product team.
- **Proportional Allocation Model**: Distribute shared infrastructure costs proportionally based on each team's percentage of direct application compute spend.
