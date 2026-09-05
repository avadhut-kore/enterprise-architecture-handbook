# Security Decision Framework: VPC Subnet Tiering vs eBPF Microsegmentation

## Executive Summary
This framework provides the formal evaluation criteria used by the Architecture Review Board.

---

## Evaluation Criteria
- **Security Impact**: Threat reduction, blast radius isolation, compliance alignment.
- **Operational Complexity**: Day-2 maintenance, tooling overhead, engineer cognitive load.
- **Performance & Cost**: Latency impact, compute/network costs, licensing fees.

## Recommendation Matrix
1. **Tier-1 Mission Critical**: Implement hardened, automated, zero-trust controls regardless of nominal complexity.
2. **Tier-2 / Tier-3 Workloads**: Standardize on cloud-native managed capabilities to minimize operational toil.
