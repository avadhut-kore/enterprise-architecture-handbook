# Security Anti-Pattern: Hardcoded Secrets in Docker Images

## 1. Description & Context
Hardcoded Secrets in Docker Images introduces severe systemic risk, violating the core tenets of defense-in-depth and least privilege.

## 2. Symptoms & Consequences
- Secrets baked into image layers

## 3. Root Cause
- Architectural shortcuts, unmanaged technical debt, or lack of automated preventative guardrails.

## 4. Architectural Refactoring
- **Remediation**: Multi-stage builds and runtime secret mounting
