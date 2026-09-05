# Security Decision Framework: JWT vs Opaque Reference Tokens Decision Framework

## Executive Summary
This decision framework establishes objective criteria for evaluating architectural trade-offs.

---

## Architectural Comparison Matrix

| Dimension | Stateless JWT | Stateful Opaque Token |
|:---|:---|:---|
| **Verification Speed** | Sub-millisecond (In-memory) | 5-20ms (Redis lookup) |
| **Revocation Speed** | Delayed (Until `exp` timestamp) | Instantaneous |
| **Payload Overhead** | 500B - 2KB per HTTP request | 32 - 64 bytes |
| **Best For** | Internal high-scale microservices | Public browser sessions & admin portals |

---

## Decision Heuristic
1. Prioritize data security and blast radius containment over raw development convenience.
2. Quantify latency overhead and memory footprint before mandating real-time cryptographic operations on critical paths.
