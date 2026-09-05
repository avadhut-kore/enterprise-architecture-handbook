# Deployment Strategies & Progressive Delivery

Comprehensive architecture guide to the 9 major software deployment strategies.

## 1. The 9 Core Deployment Strategies

```
┌─────────────────────────────────────────────────────────────┐
│ 1. RECREATE: Terminate old instances, then deploy new.      │
│    Pros: Simple, no state overlap. Cons: Full downtime.     │
├─────────────────────────────────────────────────────────────┤
│ 2. ROLLING: Gradually replace pods/VMs one by one.          │
│    Pros: Zero downtime. Cons: Version coexistence (N & N+1).│
├─────────────────────────────────────────────────────────────┤
│ 3. BLUE/GREEN: Deploy new version to parallel environment,   │
│    switch traffic router instantaneously.                   │
│    Pros: Instant rollback. Cons: 2x infrastructure cost.    │
├─────────────────────────────────────────────────────────────┤
│ 4. CANARY: Route small % of real traffic (1% -> 10% -> 100%) │
│    measuring error rates and latency continuously.          │
├─────────────────────────────────────────────────────────────┤
│ 5. PROGRESSIVE DELIVERY: Canary automated via SLO metric     │
│    analysis (Prometheus/Argo Rollouts) + Feature Flags.     │
├─────────────────────────────────────────────────────────────┤
│ 6. A/B TESTING: Route traffic based on user cohorts / cookies│
│    measuring business conversion rather than technical SLOs.│
├─────────────────────────────────────────────────────────────┤
│ 7. FEATURE FLAGS: Code deployed dark; enabled dynamically   │
│    via remote config for specific tenants or users.         │
├─────────────────────────────────────────────────────────────┤
│ 8. SHADOW DEPLOYMENT: Duplicate live production traffic     │
│    to new version without returning responses to users.     │
├─────────────────────────────────────────────────────────────┤
│ 9. RING DEPLOYMENT: Deploy outwards in concentric rings      │
│    (Ring 0: Canary/Internal -> Ring 1: Low-risk -> Public). │
└─────────────────────────────────────────────────────────────┘
```

## 2. Decision Matrix
See [Deployment Strategies Decision Matrix](./deployment-strategies-decision-matrix.md) for full trade-off evaluation.
