# Security Anti-Pattern: Shared Production Credentials

## 1. Description & Context
Shared Production Credentials is a critical architectural anti-pattern observed across enterprise organizations attempting to accelerate feature delivery at the expense of security guardrails.

## 2. Root Causes
- Pressure to hit release deadlines.
- Lack of automated security tooling in the developer workflow.
- High operational friction in legacy security review processes.

## 3. Symptoms & Real-World Consequences
- Engineering teams share a single `admin` username and password for production database access. When an unauthorized change occurs, audit logs show only 'admin', making forensic attribution impossible.

## 4. Architectural Refactoring & Remediation
- **Target Architecture**: Enforce Individual Corporate SSO federated with Just-in-Time (JIT) elevation. Issue short-lived, uniquely attributable database credentials via HashiCorp Vault.
- **Automated Verification**: Implement automated CI/CD policy linting to permanently block recurrence.
