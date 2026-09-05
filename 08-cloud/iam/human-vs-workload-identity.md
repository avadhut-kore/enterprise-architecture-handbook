# Human vs Workload Identity Architecture

## Executive Summary

Enterprise IAM must maintain a strict architectural separation between **Human Identities** (interactive users) and **Workload Identities** (non-human automated processes).

---

## 1. Identity Characteristics Comparison

| Dimension | Human Identities | Workload / Machine Identities |
| :--- | :--- | :--- |
| **Authentication Flow** | Interactive login, Username/Password, MFA (FIDO2) | Automated cryptographic token exchange (OIDC / mTLS) |
| **Session Lifetime** | 1 to 8 hours (interactive work shift) | 15 minutes to 1 hour (ephemeral runtime execution) |
| **Credential Storage** | Corporate Identity Provider (Entra ID, Okta) | Ephemeral in-memory tokens via instance metadata |
| **Privilege Lifecycle** | **Zero Standing Privilege**; JIT elevation via PIM | Static least-privilege role bound to service execution |
| **Security Risk** | Phishing, session hijacking, weak passwords | Secret leakage in source code, SSRF token theft |

---

## 2. The Golden Rule of Cloud IAM
> **Human engineers never have persistent credentials (access keys or passwords) inside cloud accounts. Workloads never use human user accounts.**
