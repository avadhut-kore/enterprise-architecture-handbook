# Security Anti-Pattern: Security as an Afterthought

## 1. Description & Context
Security as an Afterthought is a critical architectural anti-pattern observed across enterprise organizations attempting to accelerate feature delivery at the expense of security guardrails.

## 2. Root Causes
- Pressure to hit release deadlines.
- Lack of automated security tooling in the developer workflow.
- High operational friction in legacy security review processes.

## 3. Symptoms & Real-World Consequences
- Engineering builds the application and requests a security review 3 days before production launch. Security identifies architectural flaws, delaying the release by 3 months.

## 4. Architectural Refactoring & Remediation
- **Target Architecture**: Mandate Security Inception Gate: No architecture proposal receives funding or engineering allocation without an approved STRIDE threat model.
- **Automated Verification**: Implement automated CI/CD policy linting to permanently block recurrence.
