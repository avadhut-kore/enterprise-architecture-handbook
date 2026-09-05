# DEP-K8S-001: Multi-Region Active-Active Kubernetes Deployment

---
**Metadata**:
* **Document ID**: DEP-K8S-001
* **Platform**: AWS EKS across us-east-1 and eu-west-1
* **Status**: Approved
---

## 1. Runtime Topology
Deploys core banking transaction microservices across two active AWS regions. Traffic is distributed via Route 53 Latency-based routing. Database persistence is powered by CockroachDB across both regions to provide continuous availability with zero data loss during a full regional outage.
