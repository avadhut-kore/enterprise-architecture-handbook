# Operational Decision Frameworks (`decision-frameworks/`)

## Executive Summary

This directory provides 8 structured decision frameworks balancing reliability, feature delivery velocity, and operational cost.

---

## Operational Decision Frameworks
1. **SLO Target Selection**: Balancing 99.9% vs 99.95% vs 99.99% against business downtime costs.
2. **On-Call Operating Model**: Embedded SREs within squads vs Centralized NOC/SRE rotation.
3. **Automated vs Manual Failover**: Deciding when to automate disaster recovery failovers vs requiring human sign-off.
4. **Multi-AZ Warm Standby vs Multi-Region Active-Active**: Balancing RTO/RPO requirements against 2.5x cost tax.
5. **Backup Frequency & Retention**: RPO sizing, daily vs hourly snapshots, immutable WORM lock duration.
6. **Progressive Canary vs Blue-Green Deployment**: Choosing rollout strategies based on statefulness and traffic.
7. **Centralized vs Decentralized Operational Governance**: Platform Golden Paths vs team-owned tooling.
8. **Toil Reduction vs Feature Velocity**: Allocating engineering sprint capacity based on Error Budget health.
