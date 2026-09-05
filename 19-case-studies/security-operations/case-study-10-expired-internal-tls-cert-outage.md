# Enterprise Case Study: Catastrophic Global Outage Triggered by Expired Internal mTLS Certificate

## 1. Business Context
- **Organization Profile**: Tier-1 Investment Bank
- **Scale & Revenue Impact**: Multi-million dollar operational platform serving global users.

## 2. System Context
- **Architecture**: Distributed cloud-native microservices architecture on Kubernetes.
- **Affected Subsystem**: Trading Execution Platform

## 3. Incident / Risk Description
- Internal mTLS Root CA certificate expired on Sunday at midnight

## 4. Direct Business & Technical Impact
- All inter-service microservice RPCs failed authentication; complete trading platform paralysis for 6 hours.

## 5. Detection & Triage Timeline
- Incident detected via elevated SLO error budget burn rate and customer incident reports.
- War room convened within 15 minutes.

## 6. Root Cause Analysis
- Root CA was manually created 5 years prior with zero automated monitoring or renewal alerts.

## 7. Contributing Systemic Factors
- Missing automated architectural guardrails.
- Inadequate automated verification in CI/CD pipeline.

## 8. Immediate Mitigation
- Emergency re-issuance of CA certificate and manual bounce of 450 microservice deployments.

## 9. Permanent Architectural Fix
- Automated certificate lifecycle via Cert-Manager / HashiCorp Vault; configured multi-window alerts at 60 and 30 days prior to expiration.

## 10. Security Changes
- Hardened IAM boundaries, enforced least privilege, and eliminated static credentials.

## 11. Operational & SRE Changes
- Implemented multi-window burn-rate alerts and verified operational runbooks.

## 12. Lessons Learned
- Never rely on human memory for security or operational maintenance.
- Systems must be engineered to fail gracefully when dependencies degrade.

## 13. Preventive Controls & Guardrails
- Automated CI/CD linting and architectural review gates blocking unapproved changes.
