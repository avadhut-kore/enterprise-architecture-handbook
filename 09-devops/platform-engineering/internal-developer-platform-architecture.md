# Internal Developer Platform (IDP) Reference Architecture

An Internal Developer Platform combines self-service developer tooling, infrastructure orchestration, and observability into a cohesive developer experience.

## 1. The 5-Layer IDP Topology

```
┌─────────────────────────────────────────────────────────────┐
│ 1. DEVELOPER CONTROL PLANE (Developer Portal)               │
│ - Backstage / Port / Internal CLI / GitOps Manifests        │
│ - Service Catalog, API Documentation, Scaffolding Wizards   │
├─────────────────────────────────────────────────────────────┤
│ 2. INTEGRATION & PLATFORM API LAYER                         │
│ - REST / GraphQL Platform APIs                              │
│ - Dynamic Environment Provisioning Engine                   │
├─────────────────────────────────────────────────────────────┤
│ 3. ORCHESTRATION & RESOURCE ALLOCATION                      │
│ - Crossplane / Terraform Cloud / ArgoCD                     │
│ - Dynamic dependency binding (Inject DB credentials to Pod) │
├─────────────────────────────────────────────────────────────┤
│ 4. CLOUD INFRASTRUCTURE & CONTAINER FABRIC                  │
│ - EKS / GKE / AKS / VPCs / Cloud SQL / SQS / Kafka          │
├─────────────────────────────────────────────────────────────┤
│ 5. OBSERVABILITY & SECURITY PLATFORMS                       │
│ - Built-in OpenTelemetry, Prometheus, Datadog, Trivy, Vault│
└─────────────────────────────────────────────────────────────┘
```

## 2. Core Self-Service Workflows
- **Create New Service**: Developer clicks "Create Spring Boot Service" in Backstage $	o$ Backstage scaffolds repo with CI/CD, registers DNS, generates Vault secrets, and deploys Hello-World to Dev in < 5 minutes!
- **Request Database**: Application manifest declares `needs: postgresql:v16` $	o$ Crossplane provisions Cloud SQL instance and injects connection string securely.

## Related Resources
- [Golden Paths and Templates](./golden-paths-and-service-templates.md)
- [Platform Economics](../platform-economics/README.md)
