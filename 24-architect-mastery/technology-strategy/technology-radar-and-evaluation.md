# Technology Radar and Evaluation Framework

An enterprise Technology Radar (inspired by ThoughtWorks) aligns technical direction across distributed engineering teams, preventing tech stack sprawl while enabling controlled innovation.

## 1. The Four Rings of Adoption

```
                       ┌─────────────────────────┐
                       │          HOLD           │
                       │   ┌─────────────────┐   │
                       │   │     ASSESS      │   │
                       │   │   ┌─────────┐   │   │
                       │   │   │  TRIAL  │   │   │
                       │   │   │  ┌───┐  │   │   │
                       │   │   │  │ A │  │   │   │
                       │   │   │  └───┘  │   │   │
                       │   │   │  ADOPT  │   │   │
                       │   │   └─────────┘   │   │
                       │   └─────────────────┘   │
                       └─────────────────────────┘
```

1. **ADOPT**: Default industry-standard choice. High confidence, mature ecosystem, internal production experience. Used for all standard projects without special approvals.
2. **TRIAL**: Successfully proven in limited production pilots. Ready for wider adoption by teams willing to accept minor rough edges.
3. **ASSESS**: Promising technology under active evaluation. Teams may build proofs of concept (PoC), but cannot deploy to mission-critical production.
4. **HOLD**: Do not use for new projects. Technologies being actively sunsetted or deprecated due to security, cost, or obsolescence.

## 2. Evaluation Criteria for New Technology Proposals

Before moving any technology from `ASSESS` to `TRIAL`, evaluate:
- **Community Health**: Github commit frequency, release cadence, corporate backing, active maintainers.
- **Security & Vulnerability History**: Time-to-patch CVEs, SBOM transparency.
- **Operational Fit**: Does our observability stack support it? How does it handle failover and backups?
- **Hiring & Talent Pool**: Can we hire engineers skilled in this technology within 60 days?

## Related Modules
- [Platform Strategy](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/platform-strategy/README.md)
- [Technology Portfolio Management](../../22-reference/README.md)
