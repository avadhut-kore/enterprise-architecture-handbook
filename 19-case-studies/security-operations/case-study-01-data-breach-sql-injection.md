# Enterprise Case Study: Major Data Breach via Blind SQL Injection & Lateral Movement

## 1. Business Context
- **Organization Profile**: Fortune 500 Retailer
- **Scale & Revenue Impact**: Multi-million dollar operational platform serving global users.

## 2. System Context
- **Architecture**: Distributed cloud-native microservices architecture on Kubernetes.
- **Affected Subsystem**: Public Product Review API

## 3. Incident / Risk Description
- Blind SQL injection via unescaped search parameter

## 4. Direct Business & Technical Impact
- Attacker dumped 1.4M customer records; moved laterally via shared database credentials to payment database.

## 5. Detection & Triage Timeline
- Incident detected via elevated SLO error budget burn rate and customer incident reports.
- War room convened within 15 minutes.

## 6. Root Cause Analysis
- Developer concatenated raw search query string; database user had over-permissioned SELECT on all schemas.

## 7. Contributing Systemic Factors
- Missing automated architectural guardrails.
- Inadequate automated verification in CI/CD pipeline.

## 8. Immediate Mitigation
- Refactored code to compile-time parameterized query; isolated payment database into dedicated private subnet with separate credentials.

## 9. Permanent Architectural Fix
- Mandate compile-time type-safe ORM; enforce Database Row-Level Security and strict schema isolation.

## 10. Security Changes
- Hardened IAM boundaries, enforced least privilege, and eliminated static credentials.

## 11. Operational & SRE Changes
- Implemented multi-window burn-rate alerts and verified operational runbooks.

## 12. Lessons Learned
- Never rely on human memory for security or operational maintenance.
- Systems must be engineered to fail gracefully when dependencies degrade.

## 13. Preventive Controls & Guardrails
- Automated CI/CD linting and architectural review gates blocking unapproved changes.
