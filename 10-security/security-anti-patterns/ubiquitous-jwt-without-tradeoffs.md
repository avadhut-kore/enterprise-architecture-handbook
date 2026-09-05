# Security Anti-Pattern: Ubiquitous JWT Without Trade-Off Analysis

## 1. Description & Context
Ubiquitous JWT Without Trade-Off Analysis introduces severe systemic risk, violating the core tenets of defense-in-depth and least privilege.

## 2. Symptoms & Consequences
- Unrevocable user sessions

## 3. Root Cause
- Architectural shortcuts, unmanaged technical debt, or lack of automated preventative guardrails.

## 4. Architectural Refactoring
- **Remediation**: Opaque reference tokens in Redis for browser sessions
