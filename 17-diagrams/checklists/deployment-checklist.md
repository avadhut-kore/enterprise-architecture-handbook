# Deployment Topology Architecture Checklist

- [ ] Are workloads deployed across at least 3 Availability Zones (AZs) for high availability?
- [ ] Are managed databases decoupled into private, non-routable subnets?
- [ ] Is auto-scaling configured for compute fleets based on CPU/memory and queue depth?
- [ ] Are cross-region disaster recovery replication links and RTO/RPO metrics documented?
- [ ] Are secrets managed via external secret stores rather than embedded in deployment configs?
