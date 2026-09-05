# Microsegmentation & Service Mesh Security

## Executive Summary

Microsegmentation isolates workloads from one another, preventing an attacker who compromises one low-priority container from pivoting laterally to core databases or payment services.

---

## 1. Service Mesh Mutual TLS (mTLS)

```mermaid
sequenceDiagram
    autonumber
    participant AppA as Frontend Pod (Proxy Sidecar)
    participant Mesh as Service Mesh Control Plane (Istio / Linkerd)
    participant AppB as Order Pod (Proxy Sidecar)

    Note over AppA,Mesh: Mutual short-lived X.509 certificate issuance (SPIFFE ID)
    AppA->>AppB: TCP SYN (Port 443)
    Note over AppA,AppB: TLS 1.3 Handshake with Mutual Certificate Verification
    AppA-->>AppB: Validates AppB is `spiffe://cluster.local/ns/prod/sa/order-service`
    AppB-->>AppA: Validates AppA is `spiffe://cluster.local/ns/prod/sa/frontend-service`
    Note over AppB: Evaluates AuthorizationPolicy: Is frontend allowed to call order-service?
    AppA->>AppB: Encrypted HTTP/2 Request
    AppB-->>AppA: 200 OK
```
