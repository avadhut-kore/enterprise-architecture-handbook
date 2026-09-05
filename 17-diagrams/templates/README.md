# Enterprise Diagram Raw Templates Library (.mmd & .puml)

This directory contains standalone, copy-pasteable raw Mermaid (`.mmd`) and PlantUML (`.puml`) template files designed for rapid integration into architectural documentation, wikis, and design repositories.

## Template Index

### Mermaid Templates (.mmd)
- `c4-context.mmd`: C4 Level 1 System Context starter.
- `c4-container.mmd`: C4 Level 2 Container Architecture starter.
- `c4-component.mmd`: C4 Level 3 Component Design starter.
- `sequence-sync.mmd`: Synchronous request-response sequence with retries.
- `sequence-async.mmd`: Asynchronous event choreography with Kafka.
- `deployment-k8s.mmd`: Multi-tier Kubernetes cluster deployment topology.
- `deployment-multiregion.mmd`: Active-Active multi-region cloud deployment.
- `network-hub-spoke.mmd`: Enterprise cloud Hub-and-Spoke network topology.
- `security-zero-trust.mmd`: Zero Trust segmentation with PEP and PDP.
- `data-flow-etl.mmd`: Batch ETL pipeline from ingestion to analytics.
- `data-flow-streaming.mmd`: Real-time streaming pipeline (Kafka + Flink).

### PlantUML Templates (.puml)
- `c4-context.puml`: C4-PlantUML System Context starter.
- `c4-container.puml`: C4-PlantUML Container architecture starter.
- `deployment-aws.puml`: Production AWS multi-tier VPC deployment.
- `sequence-auth.puml`: OAuth2 / OIDC authentication flow.

### Guidelines & Checklists
- [Templates Reference Guide](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/templates/template.md): How to customize and embed raw diagram templates.
- [Template Lint Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/templates/checklists.md): Standards for contributing new templates.
