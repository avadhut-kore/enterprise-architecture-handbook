# Security Decision Framework: OAuth 2.0 vs API Keys Decision Framework

## Executive Summary
This decision framework establishes objective criteria for evaluating architectural trade-offs.

---

## Architectural Comparison Matrix

| Dimension | OAuth 2.0 Tokens | Static API Keys |
|:---|:---|:---|
| **Security Posture** | High (Short-lived, scoped, cryptographic) | Poor (Long-lived, vulnerable to leak) |
| **Revocation** | Granular (Tokens expire in 15m) | Difficult (Requires manual re-keying) |
| **Implementation** | Moderate (Requires Auth Server) | Simple (Static string check) |
| **Best For** | User-facing apps, mobile, modern APIs | Public developer portals (read-only) |

---

## Decision Heuristic
1. Prioritize data security and blast radius containment over raw development convenience.
2. Quantify latency overhead and memory footprint before mandating real-time cryptographic operations on critical paths.
