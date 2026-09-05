# Unit Economics and Cost Modeling

Architects must define and monitor unit economics to ensure gross margins improve as business volume scales.

## 1. Defining Architectural Unit Cost

$$\text{Unit Cost} = \frac{\text{Total Fully-Loaded Infrastructure + Licensing Cost}}{\text{Total Business Transactions (e.g., Orders, Rides, Queries)}}$$

If traffic doubles but unit cost remains flat or increases, the architecture has severe scaling anti-patterns (e.g., $O(N^2)$ algorithm or database cross-joins).

## 2. Unit Economic Modeling Table

| Architecture Tier | Monthly Cost ($) | Capacity (Monthly Units) | Unit Cost per Transaction |
| :--- | :--- | :--- | :--- |
| **Option A (Bespoke EC2 + Self-Hosted DB)** | $4,500 | 500,000 orders | $0.0090 / order |
| **Option B (Serverless Lambda + DynamoDB)** | $1,200 | 500,000 orders | $0.0024 / order |
| **Option B at 10M orders Scale** | $18,000 | 10,000,000 orders | $0.0018 / order |

## Related Modules
- [Cloud Economics and FinOps](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/economics/cloud-economics-and-finops-for-architects.md)
- [Executive Communication](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/executive-communication/README.md)
