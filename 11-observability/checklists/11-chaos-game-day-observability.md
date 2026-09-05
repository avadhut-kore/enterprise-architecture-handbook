# Checklist 11: Chaos Engineering & Game Day Observability Audit

## 1. Overview
Used during Chaos Game Days to evaluate whether the observability platform accurately reflects synthetic failure injections (packet loss, pod crashes, CPU starvation, dependency delays).

---

## 2. Verification Rubric

| Injected Failure Scenario | Expected Observability Behavior | Validated? |
| :--- | :--- | :--- |
| **Pod Kill / CrashLoop** | Kubernetes dashboard reflects pod restart; Alertmanager fires `KubePodCrashLooping` within 2m. | [ ] |
| **Network Latency (+500ms)**| Distributed traces immediately show elongated downstream child spans; Latency SLO burns. | [ ] |
| **Database Pool Exhaustion**| Application exposes `db.pool.active == db.pool.max`; Off-CPU profiling highlights thread waiting. | [ ] |
| **Upstream 500 Errors** | Distributed traces flag spans with `otel.status_code=ERROR`; Availability SLO multi-burn fires. | [ ] |
| **Kafka Broker Partition** | Consumer lag metric spikes; alerting notifies on-call before topic buffer saturates. | [ ] |
| **Runbook Verification** | On-call responders successfully mitigate the failure using the alert's runbook within MTTR target. | [ ] |
