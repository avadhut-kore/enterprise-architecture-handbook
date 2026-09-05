# Checklist 08: Incident Response & On-Call Readiness Audit

## 1. Overview
Ensures engineering teams, tooling, and operational runbooks are prepared to handle high-severity production outages (SEV-1 / SEV-2) effectively.

---

## 2. Verification Rubric

| Readiness Area | Operational Requirement | Pass/Fail |
| :--- | :--- | :--- |
| **On-Call Rota** | Primary and secondary on-call rotations configured in PagerDuty/Opsgenie with clear schedules. | [ ] |
| **Escalation Policy** | Automatic escalation to Engineering Manager / SRE Lead if unacknowledged after 10 minutes. | [ ] |
| **Runbook Quality** | Runbooks include: 1. Architecture diagram, 2. Triage commands, 3. Rollback instructions. | [ ] |
| **Tooling Access** | All on-call engineers possess verified access to Grafana, Kubernetes clusters, and cloud consoles. | [ ] |
| **Incident War Room** | Automated Slack channel and video bridge generation triggered upon SEV-1 incident declaration. | [ ] |
| **Blameless Post-Mortem**| Retrospective template available; all SEV-1 incidents require review within 72 hours. | [ ] |
| **Action Item Tracking**| Post-mortem action items logged in Jira with designated owners and 30-day completion SLAs. | [ ] |
