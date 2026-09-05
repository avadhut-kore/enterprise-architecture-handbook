# Security Anti-Pattern: Unchecked Third-Party Dependencies

## 1. Description & Context
Unchecked Third-Party Dependencies introduces severe systemic risk, violating the core tenets of defense-in-depth and least privilege.

## 2. Symptoms & Consequences
- Malicious package injection

## 3. Root Cause
- Architectural shortcuts, unmanaged technical debt, or lack of automated preventative guardrails.

## 4. Architectural Refactoring
- **Remediation**: Private Artifactory mirror + SCA scanning
