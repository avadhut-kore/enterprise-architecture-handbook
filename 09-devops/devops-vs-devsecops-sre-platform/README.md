# DevOps vs DevSecOps vs SRE vs Platform Engineering

In enterprise technology, job titles and buzzwords often overlap, creating confusion. An architect must evaluate these disciplines as **distinct, complementary capabilities** rather than competing organizational factions.

## 1. Capability Taxonomy & Venn Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                           DEVOPS                            │
│  (The Cultural Philosophy & Continuous Delivery Foundation) │
├──────────────────────────────┬──────────────────────────────┤
│          DEVSECOPS           │             SRE              │
│  - Shift-Left Security       │  - Site Reliability Eng      │
│  - SAST / DAST / SCA         │  - SLO / SLA / Error Budgets │
│  - Secret Management         │  - Incident Response & On-call│
│  - Software Supply Chain     │  - Capacity & Chaos Eng      │
├──────────────────────────────┴──────────────────────────────┤
│                    PLATFORM ENGINEERING                     │
│  - Internal Developer Platform (IDP)                        │
│  - Golden Paths & Self-Service Infrastructure APIs          │
│  - Developer Experience (DevEx) & Scaffolding Tooling       │
└─────────────────────────────────────────────────────────────┘
```

## 2. Detailed Capability Breakdown

| Capability Dimension | DevOps | DevSecOps | Site Reliability Engineering (SRE) | Platform Engineering |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Mission** | Accelerate safe delivery of customer value. | Embed security and compliance into every stage of delivery. | Ensure production reliability, availability, and performance. | Reduce developer cognitive load via self-service platforms. |
| **Core Metric** | Lead Time for Changes, Deployment Frequency. | Mean Time to Remediate (MTTR) CVEs, Zero criticals in prod. | SLO Attainment, Error Budget Burn Rate, MTTR. | Developer Onboarding Time, Golden Path Adoption Rate. |
| **Primary Customer** | The Business & End Users. | Enterprise Risk & Compliance Officers. | End Users & Production Stakeholders. | Internal Software Developers. |
| **Key Artifacts** | CI/CD Pipelines, Build manifests, Dockerfiles. | Security gates, SBOMs, Vault policies, Trivy scans. | Monitoring dashboards, Alert rules, Runbooks, Post-mortems. | Developer Portals (Backstage), Platform APIs, Helm templates. |

## 3. Organizational Interlocking & Collaboration
- **Platform Engineering** builds the self-service Kubernetes cluster and CI/CD golden path.
- **DevSecOps** embeds automated vulnerability scanners and OPA policies into the platform's golden path.
- **DevOps/Product Teams** use the golden path to build and deploy microservices autonomously.
- **SRE** establishes SLOs, error budgets, and on-call response standards for the deployed microservices.

## Related Resources
- [DevOps Maturity Model](../devops-maturity/README.md)
- [SRE & Observability](../../11-observability/README.md)
- [Security Architecture](../../10-security/README.md)
