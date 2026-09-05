# Security Anti-Pattern: Fragile Certificate Pinning

## 1. Description & Context
Fragile Certificate Pinning introduces severe systemic risk, violating the core tenets of defense-in-depth and least privilege.

## 2. Symptoms & Consequences
- App bricking on cert renewal

## 3. Root Cause
- Architectural shortcuts, unmanaged technical debt, or lack of automated preventative guardrails.

## 4. Architectural Refactoring
- **Remediation**: Public key pinning (SPKI) with backup pins
