# Security Anti-Pattern: Secrets Committed to Version Control (Git)

## 1. Description & Context
Secrets Committed to Version Control (Git) is a critical architectural anti-pattern observed across enterprise organizations attempting to accelerate feature delivery at the expense of security guardrails.

## 2. Root Causes
- Pressure to hit release deadlines.
- Lack of automated security tooling in the developer workflow.
- High operational friction in legacy security review processes.

## 3. Symptoms & Real-World Consequences
- Engineers commit database passwords or private certificates to Git repositories. Even if deleted in subsequent commits, the secret remains forever in Git history.

## 4. Architectural Refactoring & Remediation
- **Target Architecture**: Deploy automated pre-commit hooks (Gitleaks) and GitHub Push Protection to block commits containing secrets. Use External Secrets Operator to inject secrets at runtime.
- **Automated Verification**: Implement automated CI/CD policy linting to permanently block recurrence.
