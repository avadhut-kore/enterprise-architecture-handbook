# Security Ownership & Accountability (RACI)

## Executive Summary

Clear ownership prevents security gaps created by organizational ambiguity ("everyone's responsibility is nobody's responsibility").

---

## Enterprise RACI Matrix for Security Lifecycle

| Security Lifecycle Milestone | Software Engineer | Solution Architect | Cloud Platform / SRE | InfoSec / CISO | Product Owner |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Data Classification** | C | A | I | C | R |
| **STRIDE Threat Modeling** | R | A | C | C | I |
| **Secure Code Implementation** | R | A | I | C | I |
| **IaC Security Hardening** | C | A | R | C | I |
| **CVE Vulnerability Remediation**| R | C | R | A | I |
| **Security Incident Triage** | C | C | R | A | I |
| **Production Risk Acceptance** | I | C | I | C | A |

*(R = Responsible, A = Accountable, C = Consulted, I = Informed)*
