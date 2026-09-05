# Security Anti-Pattern: Long-Lived Static Access Keys

## 1. Description & Context
Long-Lived Static Access Keys is a critical architectural anti-pattern observed across enterprise organizations attempting to accelerate feature delivery at the expense of security guardrails.

## 2. Root Causes
- Pressure to hit release deadlines.
- Lack of automated security tooling in the developer workflow.
- High operational friction in legacy security review processes.

## 3. Symptoms & Real-World Consequences
- Developers create AWS IAM user access keys with infinite lifespans and embed them in Jenkins scripts or local `.aws/credentials` files. Stolen keys result in massive cryptomining hijacking.

## 4. Architectural Refactoring & Remediation
- **Target Architecture**: Completely ban IAM users and static keys. Enforce Workload Identity Federation (EKS Pod Identity / GitHub OIDC) that issues 15-minute temporary STS credentials.
- **Automated Verification**: Implement automated CI/CD policy linting to permanently block recurrence.
