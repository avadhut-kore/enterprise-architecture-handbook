# Cloud Architecture Decision Frameworks

## Executive Summary

Architecture decision frameworks provide measurable, objective scoring rubrics for evaluating high-stakes infrastructure choices, eliminating emotional or vendor-driven decisions.

---

## The Decision Framework Matrix

| Framework Document | Architectural Decision Evaluated | Key Evaluation Dimensions |
| :--- | :--- | :--- |
| **[Cloud vs On-Premises](cloud-vs-on-prem.md)** | Infrastructure placement | TCO, operational maturity, capital vs operational expenditure, elasticity |
| **[Single vs Multi-Cloud](single-vs-multi-cloud.md)** | Provider concentration risk | Regulatory mandates, best-of-breed ROI, egress fees, operational complexity |
| **[Single vs Multi-Region](single-vs-multi-region.md)** | Regional redundancy | Availability SLA (99.99% vs 99.999%), RTO/RPO, WAN latency, cost multiplier |
| **[VM vs Container vs Serverless](vm-vs-container-vs-serverless.md)**| Compute runtime selection | Startup latency, runtime control, scaling dynamics, cost at hyper-scale |
| **[Managed vs Self-Managed DB](managed-vs-self-managed-db.md)**| Database hosting model | SRE headcount labor vs provider markups, automated HA failover |
| **[Rehost vs Replatform vs Refactor](rehost-vs-replatform-vs-refactor.md)**| Modernization pathway | Technical debt carryover, migration timeline, cloud agility ROI |
| **[Centralized vs Decentralized Platform](centralized-vs-decentralized-platform.md)**| Team operating model | Developer autonomy vs enterprise security guardrails and compliance |
