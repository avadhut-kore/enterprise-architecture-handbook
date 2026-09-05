# Deployment Architecture Review Checklist

- [ ] Are all target cloud regions and availability zones clearly indicated?
- [ ] Is compute capacity distribution (auto-scaling rules, minimum/maximum pod replicas) documented?
- [ ] Are single points of failure (SPOFs) eliminated with multi-AZ redundancy?
- [ ] Are network subnets explicitly differentiated (public vs private app vs isolated data)?
- [ ] Are database replication modes (synchronous vs asynchronous) clearly labeled?
- [ ] Is disaster recovery RTO and RPO explicitly achievable given the documented topology?
