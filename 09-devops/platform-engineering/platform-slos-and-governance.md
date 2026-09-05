# Platform SLOs and Governance

Internal developer platforms must be held to strict operational Service Level Objectives (SLOs) just like external customer-facing services.

## 1. Core Platform SLO Metrics
- **Portal Availability**: Backstage developer portal available >= 99.9% of business hours.
- **CI Runner Queue Wait Time**: 95% of CI jobs start executing within < 30 seconds of push.
- **Environment Provisioning Latency**: Ephemeral preview environments ready within < 10 minutes.
- **Platform Support SLA**: P1 blocker issues acknowledged by platform engineers within < 15 minutes.

## Related Resources
- [DORA Metrics](../devops-metrics/dora-metrics-deep-dive.md)
- [SRE Architecture](../../11-observability/README.md)
