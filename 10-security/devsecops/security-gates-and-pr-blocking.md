# Security Gates & Pull Request Blocking

## Executive Summary

Automated security gates prevent vulnerable code from entering the main codebase.

---

## Non-Bypassable PR Gate Thresholds

| Security Scan | Blocking Criteria | Action on Failure |
| :--- | :--- | :--- |
| **Secret Scanner** | ANY detected API key, private key, or credential | Immediate PR rejection + automatic credential revocation |
| **SAST** | High or Critical severity rule match | PR blocked until fixed or reviewed by Security Champion |
| **SCA** | Critical CVE with available patch | PR blocked; automated Dependabot patch PR suggested |
| **Container Scan** | Critical CVE (CVSS $\ge 9.0$) or High CVE with EPSS $> 0.1$ | Container image push rejected |
| **IaC Scan** | Unencrypted storage or open ingress `0.0.0.0/0` | Terraform plan execution blocked |
