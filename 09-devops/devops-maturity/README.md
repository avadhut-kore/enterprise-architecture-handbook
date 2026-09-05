# Enterprise DevOps Maturity Model

A pragmatic framework for benchmarking an enterprise's DevOps capabilities, identifying bottlenecks, and planning evolutionary milestones.

## 1. The 6-Level Maturity Continuum

```
Level 1: Manual / Ad-Hoc ──► Level 2: Automated ──► Level 3: Continuous Delivery
                                                          │
Level 6: Intelligent Autonomous ◄── Level 5: Platform Eng ◄── Level 4: DevSecOps
```

| Level | Description | Characteristic Behavior |
| :--- | :--- | :--- |
| **Level 1: Manual** | Ad-hoc, heroic efforts | Deployments via SSH/RDP; manual testing; long deployment maintenance windows; spreadsheets for tracking. |
| **Level 2: Automated** | Scripted tasks | Jenkins/GitLab CI runs unit tests; scripts build container images; manual handoff to ops for deployment. |
| **Level 3: Continuous Delivery** | Repeatable pipelines | Automated build, test, and package on every commit; deployment to staging automated; production requires 1-click approval. |
| **Level 4: DevSecOps** | Security integrated | Automated SAST/DAST/SCA gates; secret scanning; image signing; compliance evidence generated automatically. |
| **Level 5: Platform Engineering** | Self-service ecosystem | Internal Developer Platform (IDP); Golden Paths; declarative GitOps; telemetry built-in; zero ticket queues. |
| **Level 6: Intelligent / Autonomous** | Self-healing & adaptive | Progressive delivery with automated canary analysis; predictive autoscaling; automated chaos engineering; AIOps triage. |

## 2. Assessment Matrix
Use the [DevOps Maturity Assessment Checklist](./devops-maturity-assessment-checklist.md) to score teams across 13 core dimensions.
