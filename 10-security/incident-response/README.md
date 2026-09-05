# Security Incident Response Architecture (`incident-response/`)

## Executive Summary

Security Incident Response defines the organizational and technical runbooks required to detect, triage, contain, eradicate, and recover from cybersecurity breaches.

---

## Key Guides in this Directory

| Guide | Scope | Core Focus |
| :--- | :--- | :--- |
| [`security-incident-response-lifecycle.md`](security-incident-response-lifecycle.md) | NIST Lifecycle | 6-Stage incident response framework (NIST SP 800-61) |
| [`incident-severity-classification.md`](incident-severity-classification.md) | Severity Matrix | SEV-1 to SEV-4 classification, MTTR targets, on-call paging |
| [`credential-compromise-runbook.md`](credential-compromise-runbook.md) | IR Runbook | Stolen IAM key / admin token immediate containment runbook |
| [`ransomware-containment-runbook.md`](ransomware-containment-runbook.md) | IR Runbook | Network isolation, golden backup recovery runbook |
| [`data-breach-response-and-forensics.md`](data-breach-response-and-forensics.md) | Forensics | Memory dumps, legal notifications, regulatory reporting |
