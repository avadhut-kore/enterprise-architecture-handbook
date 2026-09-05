# Enterprise Case Study: Cascading Microservice Outage Caused by Missing Circuit Breakers

## 1. Business Context
- **Organization Profile**: High-Growth FinTech
- **Scale & Revenue Impact**: Multi-million dollar operational platform serving global users.

## 2. System Context
- **Architecture**: Distributed cloud-native microservices architecture on Kubernetes.
- **Affected Subsystem**: Payment Processing Cluster

## 3. Incident / Risk Description
- Third-party fraud scoring API latency spike from 40ms to 8000ms

## 4. Direct Business & Technical Impact
- Upstream thread pools exhausted waiting on timeouts; cascading failure collapsed checkout for 3 hours.

## 5. Detection & Triage Timeline
- Incident detected via elevated SLO error budget burn rate and customer incident reports.
- War room convened within 15 minutes.

## 6. Root Cause Analysis
- No circuit breakers or bulkheads; synchronous blocking calls with 30-second default timeouts.

## 7. Contributing Systemic Factors
- Missing automated architectural guardrails.
- Inadequate automated verification in CI/CD pipeline.

## 8. Immediate Mitigation
- Manually disabled fraud scoring feature flag; scaled backend instances to clear queued connection backlog.

## 9. Permanent Architectural Fix
- Implemented Resilience4j circuit breakers (tripping at 50% error/timeout); configured 300ms timeout with local cache fallback.

## 10. Security Changes
- Hardened IAM boundaries, enforced least privilege, and eliminated static credentials.

## 11. Operational & SRE Changes
- Implemented multi-window burn-rate alerts and verified operational runbooks.

## 12. Lessons Learned
- Never rely on human memory for security or operational maintenance.
- Systems must be engineered to fail gracefully when dependencies degrade.

## 13. Preventive Controls & Guardrails
- Automated CI/CD linting and architectural review gates blocking unapproved changes.
