# System Design Checklist: Scalability & Elasticity

## 1. Compute & Traffic Elasticity
- [ ] Horizontal Pod Autoscaling (HPA) configured based on CPU/Memory and queue depth?
- [ ] Traffic distributed across multiple Availability Zones using L7 Load Balancers?
- [ ] CDN configured for static assets and public cacheable API responses?

## 2. Database Scaling
- [ ] Read-write splitting configured with read replicas for query offload?
- [ ] Read-your-writes consistency window handled during replication lag?
- [ ] Partition rebalancing strategy documented for future shard additions?
