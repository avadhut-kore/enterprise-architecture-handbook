# Security Anti-Pattern: Unrestricted Outbound Egress

## 1. Description & Context
Unrestricted Outbound Egress introduces severe systemic risk, violating the core tenets of defense-in-depth and least privilege.

## 2. Symptoms & Consequences
- Data exfiltration to external C2

## 3. Root Cause
- Architectural shortcuts, unmanaged technical debt, or lack of automated preventative guardrails.

## 4. Architectural Refactoring
- **Remediation**: Egress firewall with TLS SNI domain filtering
