# ADR-0046: Hub-and-Spoke Networking via AWS Transit Gateway

## Metadata
```yaml
id: ADR-0046
title: Hub-and-Spoke Networking via AWS Transit Gateway
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Full-mesh VPC peering across 40+ accounts created an unmanageable network routing matrix (N*(N-1)/2 connections) that lacked centralized traffic inspection.

---

## 2. Decision
We adopt a Hub-and-Spoke transit network architecture powered by AWS Transit Gateway (TGW) and a Centralized Inspection VPC housing Next-Generation Firewalls.

---

## 3. Positive Consequences
- Single point of security inspection and egress filtering for all outbound internet traffic.
- Simplifies routing down to spoke-to-hub attachments.
- Supports transitive routing across hybrid Direct Connect links.

---

## 4. Negative Consequences & Trade-offs
- Incurs Transit Gateway attachment hourly fees and $0.02/GB data processing charges.

---

## 5. Alternatives Considered & Rejected
- **Full Mesh VPC Peering**: Rejected due to peering connection limits and lack of transitive routing.
