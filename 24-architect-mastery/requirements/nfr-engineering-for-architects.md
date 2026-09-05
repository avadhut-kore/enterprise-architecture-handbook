# NFR Engineering for Architects

Vague requirements produce failed architectures. The architect's duty is to translate ambiguous human desires into mathematically testable engineering budgets.

---

## 1. The Vague-to-Measurable Translation Table

| Vague Business Requirement | Measurable Architectural NFR Specification | Verification Mechanism |
| :--- | :--- | :--- |
| *"The system must be fast."* | **Latency Budget**: 95% of read requests must complete within 200 ms; 99% within 500 ms under a peak load of 5,000 requests/sec. | Continuous k6 load testing in staging CI/CD pipeline. |
| *"The system can never go down."* | **Availability Budget**: 99.95% monthly uptime (max 21.9 minutes of unplanned downtime per month), excluding scheduled maintenance. | Datadog Synthetic Monitoring + SLO alert. |
| *"We can't lose any customer data."* | **Durability & Recovery**: RPO = 0 (zero committed transaction loss) across regional datacenter failover; RTO < 15 minutes. | Automated Chaos Engineering failover drills. |
| *"It must be secure."* | **Security Baseline**: 100% of network traffic encrypted via TLS 1.3; sensitive data encrypted at rest via AES-256 GCM; Zero Critical/High CVEs. | Automated SonarQube & Trivy CI gates. |
| *"The system must scale easily."* | **Elastic Scalability**: Auto-scale compute fleet from 10 to 100 pods within 120 seconds in response to a 4x surge in request queue depth. | Horizontal Pod Autoscaler (HPA) stress tests. |
| *"It should be easy to maintain."* | **Operability & Observability**: 100% of microservices emit OpenTelemetry distributed traces; MTTR for Sev-1 incidents < 30 minutes. | Automated runbook audits and Game Day drills. |
| *"Keep costs reasonable."* | **FinOps Unit Economics**: Infrastructure cost must not exceed $0.0045 per settled customer transaction at steady-state load. | Monthly AWS Cost Explorer allocation report. |

---

## 2. NFR Budgeting Principle: The Knapsack Model
NFRs consume resources. You cannot have sub-10ms global latency, multi-region synchronous strong consistency, 99.999% availability, and lowest possible cloud cost simultaneously. An architect must explicitly allocate finite NFR budgets across the system topology.
