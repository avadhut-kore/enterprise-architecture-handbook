# Trust Boundaries & Data Flow Diagrams (DFD)

## Executive Summary

A **Trust Boundary** exists whenever data or execution transitions from one level of privilege, ownership, or security control to another. Every crossing of a trust boundary is a high-risk attack surface requiring explicit authentication, authorization, and input validation.

---

## 1. Architectural Trust Boundary Diagram

```mermaid
flowchart TD
    subgraph UntrustedZone ["Untrusted Zone (Internet)"]
        User["Mobile / Web Browser Client"]
    end

    subgraph DMZ ["Trust Boundary 1: Edge Perimeter"]
        CDN["Cloudflare CDN / WAF"]
        ALB["Public Application Load Balancer"]
    end

    subgraph AppZone ["Trust Boundary 2: Private Network (VPC)"]
        APIGW["Internal API Gateway (Envoy)"]
        OrderSvc["Order Microservice (Spring Boot)"]
        PaymentSvc["Payment Microservice (.NET Core)"]
    end

    subgraph DataZone ["Trust Boundary 3: Isolated Data Tier"]
        DB[("PostgreSQL Aurora Primary")]
        KMS["KMS Key Custody"]
    end

    User -->|HTTPS / Port 443 [TB 1]| CDN
    CDN --> ALB
    ALB -->|TLS 1.3 [TB 2]| APIGW
    APIGW -->|mTLS + JWT Claims| OrderSvc
    OrderSvc -->|mTLS + Service Identity| PaymentSvc
    PaymentSvc -->|TLS + KMS Authenticated [TB 3]| DB
    PaymentSvc -.->|Envelope Decryption| KMS
```
