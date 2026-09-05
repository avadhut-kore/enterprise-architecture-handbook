# Enterprise Case Study: Cloud Root Account Credential Leakage & Cryptomining Hijack

## 1. Business Context
- **Organization Profile**: Global SaaS Platform
- **Scale & Revenue Impact**: Multi-million dollar operational platform serving global users.

## 2. System Context
- **Architecture**: Distributed cloud-native microservices architecture on Kubernetes.
- **Affected Subsystem**: AWS Infrastructure

## 3. Incident / Risk Description
- Root account access key embedded in public GitHub repository

## 4. Direct Business & Technical Impact
- Adversary provisioned 400 GPU instances within 20 minutes; incurred $450,000 in unauthorized compute fees.

## 5. Detection & Triage Timeline
- Incident detected via elevated SLO error budget burn rate and customer incident reports.
- War room convened within 15 minutes.

## 6. Root Cause Analysis
- Developer stored root access keys in personal dotfiles pushed to a public GitHub repo.

## 7. Contributing Systemic Factors
- Missing automated architectural guardrails.
- Inadequate automated verification in CI/CD pipeline.

## 8. Immediate Mitigation
- Applied DenyAll inline policy; terminated all rogue GPU instances; engaged AWS security for fee mitigation.

## 9. Permanent Architectural Fix
- Permanently deleted root access keys; enforced SCP blocking root API keys; mandated Workload Identity Federation.

## 10. Security Changes
- Hardened IAM boundaries, enforced least privilege, and eliminated static credentials.

## 11. Operational & SRE Changes
- Implemented multi-window burn-rate alerts and verified operational runbooks.

## 12. Lessons Learned
- Never rely on human memory for security or operational maintenance.
- Systems must be engineered to fail gracefully when dependencies degrade.

## 13. Preventive Controls & Guardrails
- Automated CI/CD linting and architectural review gates blocking unapproved changes.
