# Hybrid Cloud Architecture

## Executive Summary

Hybrid Cloud is the operational state of integrating private data centers, colocation facilities, and on-premises infrastructure with one or more public cloud environments. In global enterprises, hybrid cloud is rarely a temporary transitional phase—it is a permanent, strategic architectural reality dictated by regulatory compliance, data gravity, hardware investments, and latency constraints.

---

## Architecture Blueprint

```mermaid
graph TD
    subgraph Enterprise On-Premises Data Center
        Mainframe[Core Legacy Systems / Mainframe]
        SanDB[(Sensitive Financial DB / Oracle SAN)]
        AD[Active Directory Domain Services]
        EdgeApp[Private Edge Applications]
    end

    subgraph Dedicated Hybrid Connectivity
        DX[AWS Direct Connect / Azure ExpressRoute]
        IPsec[Redundant IPsec VPN Backup]
    end

    subgraph Public Cloud Platform [AWS / Azure / GCP]
        Transit[Transit Gateway / Virtual WAN]
        PaaSApp[Cloud-Native Microservices / APIs]
        CloudDB[(Cloud Read Replicas / Data Lake)]
        CloudIAM[Entra ID / AWS IAM Identity Center]
    end

    AD <==>|SAML / OIDC Federation| CloudIAM
    SanDB -.->|Asynchronous CDC / Storage Gateway| CloudDB
    Mainframe <==>|Private gRPC / TLS over DX| PaaSApp
    Transit <==> DX
    Transit -.-> IPsec
```

---

## Core Deliverables & Guides

| Document | Focus Area | Architectural Impact |
| :--- | :--- | :--- |
| **[Architecture Reference](architecture.md)** | Hybrid cloud reference topology | Data flow, blast radius, transit hubs, security zones |
| **[Datacenter Integration](datacenter-integration.md)** | Facility and edge physical bridging | Colocation, hardware cross-connects, edge appliances |
| **[Hybrid Networking](hybrid-networking.md)** | Dedicated circuits & routing | Direct Connect, ExpressRoute, BGP routing, MTU, dual-path HA |
| **[Identity Federation](identity-federation.md)** | Unified hybrid identity | AD DS to Entra ID/Cloud IAM, Kerberos translation, SSO |
| **[Data Synchronization](data-synchronization.md)** | Moving data across hybrid links | Storage gateways, CDC replication, Kafka bridges, egress costs |
| **[Hybrid Databases](hybrid-databases.md)** | Distributed data topologies | Cross-WAN read replicas, split writes, CAP theorem constraints |
| **[Hybrid Messaging](hybrid-messaging.md)** | Event and message bridging | IBM MQ / RabbitMQ to SQS / EventBridge / Cloud Pub/Sub |
| **[Cloud Bursting](cloud-bursting.md)** | Dynamic capacity bursting | When bursting works (batch) vs why stateful bursting fails |
| **[Legacy Integration](legacy-integration.md)** | Modernizing without breaking legacy| Anti-corruption layers, mainframe bridges, transaction boundaries |
| **[Hybrid Decision Framework](hybrid-cloud-decision-framework.md)**| Measurable architecture framework | Determining when hybrid is essential vs operational anti-pattern |
