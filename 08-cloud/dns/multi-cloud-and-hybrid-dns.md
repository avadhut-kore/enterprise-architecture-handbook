# Hybrid & Multi-Cloud DNS Resolution Architecture

## Executive Summary

Connecting on-premises Active Directory DNS with cloud-native private DNS zones requires bidirectional forwarding to resolve hostnames seamlessly across hybrid links.

---

## 1. Bidirectional Hybrid DNS Forwarding Architecture

```mermaid
graph LR
    subgraph Corporate Data Center
        OnPremDNS[Active Directory DNS Server: 10.0.1.10]
    end

    subgraph Cloud Network Transit
        DirectConnect[Direct Connect / ExpressRoute Link]
    end

    subgraph AWS VPC / Azure VNet
        InboundResolver[Inbound DNS Endpoint: 10.16.0.50]
        OutboundResolver[Outbound DNS Resolver / Forwarding Rules]
        CloudPrivateZone[Private Zone: *.aws.internal]
    end

    OnPremDNS -->|Forward queries for '*.aws.internal'| InboundResolver
    InboundResolver --> CloudPrivateZone

    OutboundResolver -->|Forward queries for '*.corp.local'| OnPremDNS
```

---

## 2. Resolution Mechanics

- **Inbound Endpoints**: Exposes a static private IP inside the cloud VPC that on-premises DNS servers can target with conditional forwarding rules.
- **Outbound Endpoints & Rules**: Inspects VPC DNS queries; if a query matches `*.corp.local`, it intercepts the query and forwards it across Direct Connect to the on-premises domain controllers.
