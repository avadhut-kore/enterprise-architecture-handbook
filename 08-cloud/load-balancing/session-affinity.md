# Session Affinity (Sticky Sessions) & Scalability Impacts

## Executive Summary

Session affinity binds a client's requests to a specific physical backend instance for the duration of their session. While simple to enable, **session affinity is an architectural anti-pattern for horizontally scalable systems**.

---

## 1. How Sticky Sessions Break Horizontal Scaling

```mermaid
graph TD
    LB[Load Balancer with Sticky Cookie Affinity]
    ClientA[Heavy Power User / API Client] --> LB
    ClientB[Standard User] --> LB

    LB ==>|10,000 requests/min locked to Instance 1| Target1[Instance 1: 99% CPU OVERLOADED!]
    LB -->|10 requests/min| Target2[Instance 2: 2% CPU IDLE]
```

---

## 2. The Architectural Alternative: Externalized Stateless Sessions

1. **The Flaws of Stickiness**:
   - If Target 1 crashes or scales down, all sessions bound to it are dropped, corrupting shopping carts or user state.
   - Autoscaling fails because traffic cannot be redistributed away from overloaded nodes.
2. **The Modern Standard**:
   - Applications must remain **100% stateless**. Store user sessions in an external distributed cache (Redis / DynamoDB) indexed by a secure session token passed in the HTTP `Authorization` header. Any backend instance can serve any user request interchangeably.
