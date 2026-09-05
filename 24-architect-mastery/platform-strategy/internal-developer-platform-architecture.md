# Internal Developer Platform (IDP) Architecture

An Internal Developer Platform treats the developer experience as a product, creating "Golden Paths" that make the right architectural choice the easiest choice.

## 1. Platform Architecture Topology

```
┌─────────────────────────────────────────────────────────────┐
│                      DEVELOPER INTERFACE                    │
│   Backstage Developer Portal / CLI / GitOps PR Templates    │
├─────────────────────────────────────────────────────────────┤
│                      ORCHESTRATION LAYER                    │
│      ArgoCD / Terraform Cloud / Crossplane Operators        │
├─────────────────────────────────────────────────────────────┤
│                      GOLDEN PATH TEMPLATES                  │
│  [Java Microservice]  [Python AI Agent]  [Next.js Frontend] │
│  - CI/CD Pipelines    - Observability     - IAM & Secrets   │
│  - Helm Charts        - OpenTelemetry     - Vault Policies  │
├─────────────────────────────────────────────────────────────┤
│                      CLOUD INFRASTRUCTURE                   │
│         EKS / AKS / Cloud SQL / Kafka / VPC Mesh            │
└─────────────────────────────────────────────────────────────┘
```

## 2. The Golden Path Philosophy
- **Paved Road, Not Paved Prison**: Golden paths provide opinionated, frictionless defaults. Teams can opt out if they have legitimate specialized requirements, but they must own their operational burden and compliance auditing.
- **Self-Service Infrastructure**: Developers provision databases, queues, and DNS via declarative manifests (GitOps) rather than filing Jira support tickets.
- **Cognitive Load Reduction**: Shift-left without burdening developers with Kubernetes networking manifests and IAM policy math.

## Related Modules
- [Organizational Design & Conway's Law](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/organizational-design/README.md)
- [Cloud Architecture Foundation](../../08-cloud/README.md)
