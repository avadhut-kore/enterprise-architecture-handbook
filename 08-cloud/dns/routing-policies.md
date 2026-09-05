# Advanced DNS Routing Policies

## Executive Summary

Modern cloud authoritative DNS engines provide advanced routing policies to optimize user experience and regulatory compliance.

---

## 1. Routing Policy Comparison

```mermaid
graph TD
    Policy[DNS Routing Policies]
    Policy --> Latency[Latency-Based: Directs users to lowest round-trip cloud region]
    Policy --> Geo[Geolocation: Directs users based on client geographic IP]
    Policy --> Weighted[Weighted: Splits traffic by percentage: 80/20 Blue-Green]
    Policy --> Geoprox[Geoproximity: Uses GPS coordinates and regional bias]
    Policy --> Failover[Failover: Active-Passive DR with automated health checks]
```

---

## 2. Latency vs Geolocation Routing

- **Latency-Based Routing**: The cloud DNS provider maintains real-time latency maps between worldwide network networks and cloud data centers. A user in London is routed to `eu-west-1` (Dublin) if Frankfurt has network congestion, ensuring the lowest latency.
- **Geolocation Routing**: Routes strictly by physical geography (e.g., all European visitors routed to Frankfurt). **Mandatory for regulatory compliance (GDPR)** to ensure European citizen traffic is processed exclusively on European soil.
