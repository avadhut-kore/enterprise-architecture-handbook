# Cloud Reference Architectures

## Executive Summary

This section provides 10 production-grade cloud reference architecture blueprints. Each blueprint details the multi-tier topological layout, traffic flow, data persistence, security controls, and disaster recovery design required for enterprise scale.

---

## Catalog of Cloud Reference Architectures

| Blueprint | Architectural Role | Core Cloud Technologies |
| :--- | :--- | :--- |
| **[Enterprise Web Application](enterprise-web-application.md)** | Modern 3-tier web platform | CDN, WAF, ALB, Containerized Frontend/API, Redis, Aurora |
| **[Enterprise SaaS Platform](enterprise-saas-platform.md)** | Multi-tenant B2B SaaS | Tenant isolation, dynamic schema routing, tiered metering |
| **[E-Commerce Platform](ecommerce-platform.md)** | High-throughput retail engine | Catalog search, Cart in Redis, EventBridge, Aurora Multi-AZ |
| **[Financial Transaction Platform](financial-transaction-platform.md)**| High-resiliency payments | Strict idempotency, Kafka clearing, Ledger DB, Active-Passive DR |
| **[Enterprise API Platform](enterprise-api-platform.md)** | API Gateway & Portal | API Gateway / APIM, OAuth2 / OIDC, WAF, Rate Limiting |
| **[Event-Driven Platform](event-driven-platform.md)** | Asynchronous stream backbone | Managed Kafka (MSK), Schema Registry, SQS DLQs, Flink |
| **[Multi-Region Platform](multi-region-platform.md)** | Global Anycast platform | Google Global LB / Route 53 ARC, Cloud Spanner / Aurora Global |
| **[Hybrid Enterprise Platform](hybrid-enterprise-platform.md)** | Data Center + Cloud | Direct Connect / ExpressRoute, Identity Federation, Legacy ESB |
| **[Kubernetes Platform](kubernetes-platform.md)** | Enterprise container cluster | EKS/AKS/GKE, Karpenter, Cilium eBPF, ArgoCD GitOps, OTel |
| **[Serverless Platform](serverless-platform.md)** | Event-driven serverless stack | API Gateway, Lambda / Cloud Run, DynamoDB Single-Table |
