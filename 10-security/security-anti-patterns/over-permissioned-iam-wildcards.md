# Security Anti-Pattern: Over-Permissioned IAM Wildcards (`*`)

## 1. Description & Context
Over-Permissioned IAM Wildcards (`*`) is a critical architectural anti-pattern observed across enterprise organizations attempting to accelerate feature delivery at the expense of security guardrails.

## 2. Root Causes
- Pressure to hit release deadlines.
- Lack of automated security tooling in the developer workflow.
- High operational friction in legacy security review processes.

## 3. Symptoms & Real-World Consequences
- Frustrated by permission errors during deployment, engineers attach `Action: '*'` and `Resource: '*'` to microservice roles. Compromise of a single pod compromises the entire cloud estate.

## 4. Architectural Refactoring & Remediation
- **Target Architecture**: Enforce Service Control Policies (SCPs) that block wildcard permissions. Use automated IAM Access Analyzers to generate least-privilege policies based on actual runtime API calls.
- **Automated Verification**: Implement automated CI/CD policy linting to permanently block recurrence.
