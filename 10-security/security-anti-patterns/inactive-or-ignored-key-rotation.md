# Security Anti-Pattern: Inactive or Ignored Key Rotation

## 1. Description & Context
Inactive or Ignored Key Rotation introduces severe systemic risk, violating the core tenets of defense-in-depth and least privilege.

## 2. Symptoms & Consequences
- Keys unrotated for years

## 3. Root Cause
- Architectural shortcuts, unmanaged technical debt, or lack of automated preventative guardrails.

## 4. Architectural Refactoring
- **Remediation**: Automated 365-day KMS key rotation
