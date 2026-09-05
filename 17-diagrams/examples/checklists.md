# Industry Vertical Architecture Review Checklist

Use this 30-point evaluation checklist when reviewing domain-specific enterprise solution architectures for production readiness.

## 1. Domain Standards & Regulatory Alignment
- [ ] Are applicable industry standards implemented (e.g., ISO 20022 for Banking, HL7/FHIR for Healthcare, Modbus/OPC-UA for Manufacturing)?
- [ ] Are statutory data privacy and retention laws satisfied (GDPR, HIPAA, PCI-DSS, CCPA)?
- [ ] Is data sovereignty enforced for multi-national deployments?

## 2. Scalability & Workload Characteristics
- [ ] Is the architecture sized to sustain expected peak workloads (e.g., Black Friday flash sales, tax filing deadlines)?
- [ ] Are stateless application services decoupled from durable streaming ingestion buffers?
- [ ] Are database read replicas and caching layers configured to offload primary transactional engines?

## 3. Resilience, Disaster Recovery & High Availability
- [ ] Are workloads deployed across multiple availability zones with automated failover?
- [ ] Are disaster recovery RTO and RPO targets validated against real-world business impact?
- [ ] Are offline-first store-and-forward mechanisms implemented for edge or retail environments?

## 4. Security, Zero Trust & Auditability
- [ ] Are security trust boundaries explicitly indicated in all architectural diagrams?
- [ ] Is end-to-end encryption enforced in transit (TLS 1.3) and at rest (KMS envelope encryption)?
- [ ] Are immutable write-once-read-many (WORM) audit logs captured for all sensitive business transactions?
