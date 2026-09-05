# Security Incident Severity Classification Matrix

## Executive Summary

| Severity | Definition | Target MTTA | Target MTTC | Escalation & Communications |
|:---|:---|:---:|:---:|:---|
| **SEV-1 (Critical)** | Active data exfiltration, active ransomware, cloud root account compromised | **$< 15\text{ mins}$** | **$< 2\text{ hours}$** | Pages CISO, CEO, Legal, PR immediately. Continuous war room. |
| **SEV-2 (Major)** | Compromised employee credential, severe DoS on non-critical service, high-severity CVE active | **$< 30\text{ mins}$** | **$< 6\text{ hours}$** | Notifies Security Director and VP of Engineering. |
| **SEV-3 (Moderate)**| Internal malware blocked by EDR, brute force scanning detected, unpatched high CVE | **$< 2\text{ hours}$** | **$< 24\text{ hours}$**| Handled during standard SOC business hours. |
| **SEV-4 (Minor)** | Informational scan, isolated phishing report without credential submission | **$< 8\text{ hours}$** | **$< 5\text{ days}$** | Handled asynchronously via Jira ticket. |
