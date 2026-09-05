# GCP Networking Architecture: Global VPC & Private Service Connect

## Executive Summary

Unlike AWS and Azure where virtual networks are regional constructs, **GCP VPCs are natively global**. A single GCP VPC spans every physical region worldwide without complex multi-region peering meshes.

---

## 1. Shared VPC Architecture

```mermaid
graph TD
    subgraph Host Project [Central Network Team]
        HostVPC[Global Shared VPC: 10.128.0.0/9]
        SubnetUS[Subnet: us-central1 - 10.128.0.0/20]
        SubnetEU[Subnet: europe-west1 - 10.128.16.0/20]
        CloudRouter[Cloud Router: Dedicated Interconnect]
    end

    subgraph Service Project A [Payments Team]
        GKEPoolA[GKE Node Pool in us-central1]
    end

    subgraph Service Project B [Analytics Team]
        GKEPoolB[GKE Node Pool in europe-west1]
    end

    GKEPoolA --> SubnetUS
    GKEPoolB --> SubnetEU
```

---

## 2. Private Service Connect (PSC)

GCP **Private Service Connect** allows consumers to privately access managed GCP services (BigQuery, Cloud Storage) or third-party SaaS services inside their VPC using internal IP addresses, completely bypassing the public internet and eliminating public NAT gateway egress.
