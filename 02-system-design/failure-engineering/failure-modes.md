# Failure Modes in Distributed Systems

## 1. Executive Summary

Distributed systems fail in fundamentally more complex ways than single-node applications. In a distributed topology, partial failure is the default state: some nodes are dead, some are slow, some network links are dropping packets, and others are experiencing silent corruption.

---

## 2. Taxonomy of Distributed Failures

```
Distributed Failures
├── Crash-Stop: Node abruptly ceases execution and halts permanently.
├── Crash-Recovery: Node crashes, loses ephemeral state, and reboots.
├── Omission Failures: Messages or packets dropped due to buffer saturation.
├── Timing / Performance Failures: Node operates correctly, but responds outside SLA.
└── Byzantine / Arbitrary Failures: Node sends corrupted, conflicting, or malicious data.
```

---

## 3. The Fallacies of Distributed Computing

L. Peter Deutsch outlined the 8 foundational false assumptions made by novice engineers:
1. *The network is reliable.* (Reality: Packets drop, fibers cut, routers crash).
2. *Latency is zero.* (Reality: Cross-rack is ~1ms; cross-region is ~70ms).
3. *Bandwidth is infinite.* (Reality: Top-of-rack switches saturate during backups).
4. *The network is secure.* (Reality: Internal networks can be tapped or breached).
5. *Topology does not change.* (Reality: Cloud nodes autoscale, IP addresses recycle).
6. *There is one administrator.* (Reality: Multiple teams control routing, DNS, and IAM).
7. *Transport cost is zero.* (Reality: Serialization and cloud egress are expensive).
8. *The network is homogeneous.* (Reality: Diverse NICs, MTUs, OS kernels, and middleboxes).

---

## 4. Architectural Defense Invariants

- **Assume Everything Fails**: Never invoke a network call without a timeout, retry budget, and fallback path.
- **Fail-Safe Defaults**: If authorization or rate limiting fails closed, services protect data integrity at the expense of availability.
