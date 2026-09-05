# Security Anti-Pattern: Missing Audit Logs on Critical Paths

## 1. Description & Context
Missing Audit Logs on Critical Paths introduces severe systemic risk, violating the core tenets of defense-in-depth and least privilege.

## 2. Symptoms & Consequences
- Zero forensic trail

## 3. Root Cause
- Architectural shortcuts, unmanaged technical debt, or lack of automated preventative guardrails.

## 4. Architectural Refactoring
- **Remediation**: Immutable S3 Object Lock WORM logging
