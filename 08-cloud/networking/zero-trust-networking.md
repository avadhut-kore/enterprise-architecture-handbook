# Zero Trust Cloud Networking & Service Mesh

## Executive Summary

In modern enterprise cloud architecture, the network perimeter is assumed to be compromised. **Zero Trust Networking** enforces continuous verification: **Never Trust, Always Verify**.

---

## 1. Zero Trust Architecture Pillars

```mermaid
graph TD
    subgraph Zero Trust Cloud Network
        P1[1. Mutual TLS: mTLS Cryptographic Identity per Pod / Service]
        P2[2. Identity-Aware Proxy: BeyondCorp Model for Internal Web UIs]
        P3[3. Micro-Segmentation: Default-Deny East-West Network Policies]
        P4[4. Ephemeral Credentials: Short-Lived Tokens replacing Static Passwords]
    end
```

---

## 2. Service Mesh Architecture (Istio / Linkerd)

```mermaid
graph LR
    subgraph Pod A
        AppA[Service A Container] --> EnvoyA[Envoy Sidecar Proxy]
    end

    subgraph Pod B
        EnvoyB[Envoy Sidecar Proxy] --> AppB[Service B Container]
    end

    EnvoyA <==>|Mutual TLS: Strict mTLS + SPIFFE Identity Certificates| EnvoyB
```

- **Cryptographic Service Identity (SPIFFE/SPIRE)**: Every microservice is issued an ephemeral X.509 certificate encoding its unique identity (`spiffe://cluster.local/ns/prod/sa/payment-service`).
- **Authorization Policies**: Envoy sidecars enforce L7 authorization rules (e.g., Service B accepts only HTTP `POST /charges` requests from identities matching `payment-service`, rejecting all other callers).
