# CI/CD Core Principles

Understanding the technical and organizational distinctions between Continuous Integration, Continuous Delivery, and Continuous Deployment.

## 1. The CI/CD Continuum

```
Continuous Integration (CI)
[Commit] ──► [Build] ──► [Unit Test] ──► [Lint & SAST] ──► [Store Artifact]
                                                                  │
Continuous Delivery (CD)                                          ▼
[Deploy to Dev] ──► [Integration Tests] ──► [Deploy to Staging] ──► [1-Click Approval to Prod]
                                                                        │
Continuous Deployment                                                   ▼
[Automated Health Checks & Canary Verification] ────────────────► [Direct to Production]
```

## 2. Core Definitions

### Continuous Integration (CI)
The practice where developers merge code into a shared trunk frequently (at least once per day). Every merge triggers an automated build and test sequence.
- **Success Criteria**: If the build breaks, fixing it is the top organizational priority. The trunk is never left broken.

### Continuous Delivery (CD)
Ensures that code is *always* in a releasable state. Deployments to staging and production are fully automated and push-button simple, but the actual production cutover is a deliberate business decision.

### Continuous Deployment
Every commit that passes the automated pipeline deploys directly to production users with zero human intervention.
- **Requirements**: Requires mature automated canary analysis, feature flagging, and automated rollback capabilities.

## Related Resources
- [Pipeline Design and Orchestration](../pipeline-architecture/pipeline-design-and-orchestration.md)
- [Deployment Strategies](../../deployment-strategies/README.md)
