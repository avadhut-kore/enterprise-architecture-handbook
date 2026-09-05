# GCP Disaster Recovery Reference Patterns

## Executive Summary

Disaster recovery on Google Cloud leverages Google's global Software-Defined Network (Andromeda) and Global External Load Balancers to achieve near-instantaneous traffic failover across continental regions.

---

## 1. Global Anycast Multi-Region Failover Architecture

```mermaid
graph TD
    Client[Worldwide Client Traffic] --> GLB[Global External HTTP(S) Load Balancer: Single Anycast IPv4/IPv6]
    GLB -->|Primary: Lowest Latency| USCentral[Regional Backend: us-central1]
    GLB -.->|Automated Health Check Failover| USEast[Regional Backend: us-east4]

    USCentral --> Spanner[(Cloud Spanner Multi-Region Instance: nam3)]
    USEast --> Spanner
```

---

## 2. Cross-Region Capabilities & SLAs

1. **Global Load Balancer Instantaneous Failover**:
   - Because Google Global Load Balancers utilize a single Anycast IP address announced globally from over 100 edge PoPs, failover does **not rely on DNS record TTL propagation**. 
   - If an entire region fails health checks, edge proxies reroute TCP traffic to healthy alternate regions in **sub-second timeframes**.
2. **Cloud Spanner Multi-Region**:
   - Provides 99.999% availability SLA with zero data loss (RPO = 0) and transparent sub-minute failover across geographic boundaries.
