# TLS Termination, Offloading & Mutual TLS (mTLS)

## Executive Summary

Load balancers terminate incoming client SSL/TLS connections, offloading cryptographic handshakes from application compute nodes and enforcing modern cipher suites.

---

## 1. TLS Termination vs End-to-End Encryption

```mermaid
graph TD
    subgraph Option A: Edge TLS Termination [STANDARD WEB]
        Client1[Client] -->|HTTPS: TLS 1.3| LB1[Load Balancer]
        LB1 -->|Unencrypted Plaintext HTTP over Private VPC Subnet| App1[Compute Backend]
    end

    subgraph Option B: Full End-to-End Encryption [REGULATED / PCI-DSS]
        Client2[Client] -->|HTTPS: Public Certificate| LB2[Load Balancer]
        LB2 -->|Re-Encrypted HTTPS: Internal Root CA Certificate| App2[Compute Backend]
    end
```

---

## 2. Mutual TLS (mTLS) at the Gateway

For zero-trust machine-to-machine APIs (e.g., Open Banking partner integrations), configure the load balancer for **mTLS (Mutual TLS)**:
- The load balancer requests and cryptographically verifies the client's X.509 certificate against an enterprise Trust Store (CA bundle) during the initial TLS handshake.
- Unauthenticated requests are dropped at the network boundary before reaching application code.
