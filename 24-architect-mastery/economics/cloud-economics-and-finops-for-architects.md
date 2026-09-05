# Cloud Economics and FinOps for Architects

Cloud expenditure is an architectural metric. Every architectural decision is an economic decision.

## 1. The Hidden Architectural Cost Traps

```
┌─────────────────────────────────────────────────────────────┐
│ 1. CROSS-AZ & CROSS-REGION DATA EGRESS                      │
│ Transferring data between availability zones costs $0.01/GB;│
│ multi-region egress costs $0.02-$0.09/GB. Heavy inter-pod   │
│ traffic across AZs can easily exceed compute costs!         │
├─────────────────────────────────────────────────────────────┤
│ 2. UNINDEXED DATABASE READ CAPACITY / IOPS                  │
│ In DynamoDB / CosmosDB / Aurora, unindexed queries consume  │
│ astronomical read capacity units or IOPS provisioning.      │
├─────────────────────────────────────────────────────────────┤
│ 3. OVER-PROVISIONED CONTAINER MEMORY RESERVATIONS           │
│ Pods requesting 4GB RAM while using 300MB waste thousands   │
│ per node by preventing pod bin-packing on EC2/VMs.          │
├─────────────────────────────────────────────────────────────┤
│ 4. LOG & TRACE INGESTION VOLUMES                            │
│ Ingesting 5TB of debug logs daily into Datadog or CloudWatch│
│ frequently costs more than the compute running the app!     │
└─────────────────────────────────────────────────────────────┘
```

## 2. FinOps Principles for Solution Architects

1. **Tagging and Attribution**: Every Kubernetes namespace, cloud resource, and storage bucket must carry standardized tags: `CostCenter`, `Environment`, `OwnerTeam`, `Service`.
2. **Right-Sizing Heuristic**: Compute requests should target 70% average utilization under normal peak.
3. **Storage Tiering**: Automatically transition S3 objects from Standard to Glacier Instant Retrieval after 30 days.

## Related Modules
- [Unit Economics and Cost Modeling](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/economics/unit-economics-and-cost-modeling.md)
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/trade-offs/master-trade-offs-library.md)
