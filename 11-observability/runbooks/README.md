# Operational Runbooks (`runbooks/`)

## Executive Summary

Operational runbooks provide clear, step-by-step, copy-pasteable diagnostic and mitigation procedures for on-call engineers resolving live production incidents.

---

## Index of Production Operational Runbooks

Every runbook strictly follows the universal 12-section incident resolution schema:
$$\text{Purpose} \rightarrow \text{Symptoms} \rightarrow \text{Impact} \rightarrow \text{Prerequisites} \rightarrow \text{Checks} \rightarrow \text{Diagnosis} \rightarrow \text{Mitigation} \rightarrow \text{Recovery} \rightarrow \text{Validation} \rightarrow \text{Escalation} \rightarrow \text{Communication} \rightarrow \text{PIR Actions}$$

| Runbook File | Incident Scenario | Primary Mitigation |
| :--- | :--- | :--- |
| [`runbook-application-outage.md`](runbook-application-outage.md) | Complete Application Outage (HTTP 500/503) | Fast rollback to previous known-good deployment |
| [`runbook-database-failover.md`](runbook-database-failover.md) | Database Primary Failure / Read-Only Locks | Forced failover to warm Multi-AZ replica |
| [`runbook-certificate-expiration.md`](runbook-certificate-expiration.md) | Internal/External TLS Certificate Expiration | Emergency certificate renewal via ACME / Cert-Manager |
| [`runbook-kafka-consumer-lag.md`](runbook-kafka-consumer-lag.md) | Kafka Consumer Lag Explosion / Poison Pill | Autoscaling consumers and dead-letter queue isolation |
| [`runbook-memory-leak-oom.md`](runbook-memory-leak-oom.md) | Pod CrashLoopBackOff due to Memory OOMKill | Ephemeral memory limit boost and heap dump capture |
| [`runbook-cpu-saturation.md`](runbook-cpu-saturation.md) | Fleet CPU Saturation (95%+) / Thread Starvation | Horizontal pod autoscaling surge + aggressive rate-limiting |
| [`runbook-region-outage-failover.md`](runbook-region-outage-failover.md) | Cloud Regional Datacenter Outage | Global Anycast / Route53 DNS traffic diversion |
| [`runbook-secret-rotation-failure.md`](runbook-secret-rotation-failure.md) | Database Connection Failures post Secret Rotation | Restoring previous secret version in Vault / ESO sync |
