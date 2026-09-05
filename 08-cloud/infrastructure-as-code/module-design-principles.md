# Enterprise IaC Module Design Principles

## Executive Summary

Well-architected IaC modules reduce code duplication and enforce security baselines across hundreds of development teams. Poorly architected modules become unmaintainable monolithic monsters.

---

## 1. The Single-Responsibility Module Principle

```mermaid
graph TD
    subgraph ANTI-PATTERN: The 'Mega-Module' [DO NOT DO THIS]
        Mega[module 'everything': VPC + EKS + RDS + S3 + IAM]
        Mega --> Fragile[Change to S3 triggers re-evaluation of VPC! Catastrophic blast radius!]
    end

    subgraph ENTERPRISE STANDARD: Composability
        ModVPC[Module: networking/vpc]
        ModEKS[Module: compute/eks]
        ModRDS[Module: database/rds-postgres]

        ModVPC ==>|Outputs: vpc_id, subnets| ModEKS
        ModVPC ==>|Outputs: db_subnets| ModRDS
    end
```

---

## 2. Semantic Versioning & Immutability
- **Pin Module Versions**: Never reference the `main` branch of an IaC module repository (`source = "git::...ref=main"`). If a platform engineer updates `main`, all downstream pipelines break unexpectedly.
- **Strict Semantic Versioning**: Reference immutable semantic release tags (`ref=v2.4.1`). Upgrades must be deliberate, peer-reviewed pull requests.
