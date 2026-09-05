# Security Anti-Pattern: Publicly Accessible Databases

## 1. Description & Context
Publicly Accessible Databases introduces severe systemic risk, violating the core tenets of defense-in-depth and least privilege.

## 2. Symptoms & Consequences
- Database assigned public IP

## 3. Root Cause
- Architectural shortcuts, unmanaged technical debt, or lack of automated preventative guardrails.

## 4. Architectural Refactoring
- **Remediation**: Private isolated subnets with PrivateLink
