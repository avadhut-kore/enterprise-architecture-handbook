# Static Application Security Testing (SAST)

## Executive Summary

SAST analyzes source code without executing it, identifying vulnerabilities (SQL injection, XSS, insecure cryptography) early in the developer workflow.

---

## 1. Enterprise SAST Standard
- Standardize on fast, semantic, rules-based engines (**Semgrep** / **SonarQube**).
- Gating rule: PR builds fail if a rule tagged `security/critical` is triggered.
- Keep scan times $< 3\text{ minutes}$ on pull requests to avoid disrupting developer velocity.
