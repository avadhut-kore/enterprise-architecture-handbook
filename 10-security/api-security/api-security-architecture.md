# API Security Architecture: Edge to Core

## Executive Summary

Securing enterprise APIs requires a multi-tier defense where responsibilities are cleanly divided between Edge Gateways, Central API Gateways, and Internal Microservices.

---

## 1. Multi-Tier API Defense Architecture

```mermaid
flowchart TD
    Client["Client (Mobile / Web / Partner)"] --> Edge["1. Edge WAF / CDN<br/>- Volumetric DDoS Mitigation<br/>- TLS 1.3 Termination<br/>- IP Reputation & Bot Filtering"]
    Edge --> APIGW["2. Enterprise API Gateway<br/>- Distributed Rate Limiting (Redis)<br/>- OIDC / OAuth JWT Verification<br/>- Token Exchange (Opaque -> Internal JWT)<br/>- Strict JSON Schema Validation"]
    APIGW --> ServiceMesh["3. Internal Service Mesh<br/>- Mutual TLS (mTLS) Encryption<br/>- Fine-Grained Authorization (OPA)<br/>- Service-to-Service RBAC"]
    ServiceMesh --> Microservice["4. Backend Microservice<br/>- Object-Level Authorization (BOLA Check)<br/>- Business Logic Constraints<br/>- Parameterized Database Queries"]
```
