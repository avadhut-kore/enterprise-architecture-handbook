# Security Anti-Pattern: Logging Sensitive PII and Passwords

## 1. Description & Context
Logging Sensitive PII and Passwords introduces severe systemic risk, violating the core tenets of defense-in-depth and least privilege.

## 2. Symptoms & Consequences
- Credentials in log files

## 3. Root Cause
- Architectural shortcuts, unmanaged technical debt, or lack of automated preventative guardrails.

## 4. Architectural Refactoring
- **Remediation**: Automated log forwarder regex scrubbing
