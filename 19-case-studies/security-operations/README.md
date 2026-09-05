# Security & Operations Enterprise Case Studies (`19-case-studies/security-operations/`)

## Executive Summary

This directory documents 20 detailed enterprise case studies based on real-world production outages, cybersecurity incidents, and major architectural transformations.

Every case study strictly follows the standard 15-section architectural post-mortem specification:
$$\text{Business Context} \rightarrow \text{System Context} \rightarrow \text{Incident} \rightarrow \text{Impact} \rightarrow \text{Detection} \rightarrow \text{Root Cause} \rightarrow \text{Contributing Factors} \rightarrow \text{Mitigation} \rightarrow \text{Permanent Fix} \rightarrow \text{Architecture Changes} \rightarrow \text{Security Changes} \rightarrow \text{Ops Changes} \rightarrow \text{Lessons Learned} \rightarrow \text{Preventive Controls}$$

---

## Case Study Index

| Case Study File | Domain Focus | Incident / Transformation |
| :--- | :--- | :--- |
| [`case-study-01-data-breach-sql-injection.md`](case-study-01-data-breach-sql-injection.md) | AppSec | Blind SQL injection leading to customer database exfiltration |
| [`case-study-02-cloud-root-credential-leak.md`](case-study-02-cloud-root-credential-leak.md) | Cloud IAM | Leaked AWS root access key and \$450,000 cryptomining hijack |
| [`case-study-03-api-credential-stuffing.md`](case-study-03-api-credential-stuffing.md) | API Security | Distributed bot credential stuffing causing account takeovers |
| [`case-study-04-secrets-in-public-git.md`](case-study-04-secrets-in-public-git.md) | Secrets Ops | Production database credentials committed to public GitHub repo |
| [`case-study-05-kubernetes-hostpath-privilege-escalation.md`](case-study-05-kubernetes-hostpath-privilege-escalation.md) | K8s Security | Pod escape and cluster compromise via hostPath volume mount |
| [`case-study-06-ransomware-outbreak-worm-recovery.md`](case-study-06-ransomware-outbreak-worm-recovery.md) | Ransomware | Enterprise ransomware attack and recovery from S3 WORM backups |
| [`case-study-07-cascading-microservice-failure.md`](case-study-07-cascading-microservice-failure.md) | SRE/Resilience | Missing circuit breakers causing global payment cluster outage |
| [`case-study-08-database-failover-flapping-outage.md`](case-study-08-database-failover-flapping-outage.md) | Database Ops | Unstable health checks causing continuous primary failover flapping |
| [`case-study-09-regional-datacenter-dr-execution.md`](case-study-09-regional-datacenter-dr-execution.md) | Disaster Recovery | Executing unannounced multi-region disaster recovery in 14 minutes |
| [`case-study-10-expired-internal-tls-cert-outage.md`](case-study-10-expired-internal-tls-cert-outage.md) | PKI / Certs | Expired internal mTLS root CA halting all microservice RPCs |
| [`case-study-11-secret-rotation-database-outage.md`](case-study-11-secret-rotation-database-outage.md) | Secrets Ops | Uncoordinated database password rotation crashing connection pools |
| [`case-study-12-canary-bypass-configuration-drift.md`](case-study-12-canary-bypass-configuration-drift.md) | Release Ops | Manual ClickOps change bypassing canary and taking down checkout |
| [`case-study-13-online-schema-migration-table-lock.md`](case-study-13-online-schema-migration-table-lock.md) | Database Ops | ALTER TABLE locking 50M-row table and exhausting connection pool |
| [`case-study-14-kafka-consumer-lag-explosion.md`](case-study-14-kafka-consumer-lag-explosion.md) | Streaming Ops | Poison pill message causing consumer CrashLoop and 2M event backlog |
| [`case-study-15-idp-token-signing-key-outage.md`](case-study-15-idp-token-signing-key-outage.md) | Identity / OIDC | Unannounced IdP JWKS key rotation causing global 401 Unauthorized |
| [`case-study-16-layer-7-ddos-checkout-saturation.md`](case-study-16-layer-7-ddos-checkout-saturation.md) | Edge Defenses | 500,000 req/sec HTTP flood saturating application thread pools |
| [`case-study-17-compromised-npm-supply-chain-package.md`](case-study-17-compromised-npm-supply-chain-package.md) | Supply Chain | Malicious dependency exfiltrating environment variables |
| [`case-study-18-pci-dss-4-0-tokenization-modernization.md`](case-study-18-pci-dss-4-0-tokenization-modernization.md) | Compliance | Modernizing payment architecture to achieve 90% CDE scope reduction |
| [`case-study-19-healthcare-monolith-hipaa-zero-trust.md`](case-study-19-healthcare-monolith-hipaa-zero-trust.md) | Healthcare | Refactoring legacy monolithic healthcare EHR for HIPAA & Zero Trust |
| [`case-study-20-enterprise-two-year-zero-trust-journey.md`](case-study-20-enterprise-two-year-zero-trust-journey.md) | Transformation | 2-Year enterprise migration from VPN perimeter to full Zero Trust |
