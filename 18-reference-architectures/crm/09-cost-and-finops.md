# Cost Estimation & FinOps Model: Enterprise CRM

## 1. Estimated Monthly TCO Model Across Scale Tiers

| Cost Category | 2,500 Agents / 5M Contacts | 25,000 Agents / 50M Contacts | 250,000 Agents / 500M Contacts |
| :--- | :--- | :--- | :--- |
| **Relational Database (Aurora)**| $3,200 (db.r6g.2xlarge) | $14,500 (db.r6g.8xlarge) | $58,000 (Multi-Region Sharded)|
| **Activity Store (DynamoDB)** | $1,800 / month | $8,500 / month | $42,000 / month |
| **Search Cluster (OpenSearch)** | $1,400 / month | $6,200 / month | $24,000 / month |
| **EKS Container Fleet** | $2,500 / month | $11,000 / month | $48,000 / month |
| **Kafka & Integration** | $1,200 / month | $4,800 / month | $18,500 / month |
| **Observability & Logging** | $1,500 / month | $5,500 / month | $22,000 / month |
| **Total Monthly TCO** | **$11,600 / month** | **$50,500 / month** | **$212,500 / month** |
