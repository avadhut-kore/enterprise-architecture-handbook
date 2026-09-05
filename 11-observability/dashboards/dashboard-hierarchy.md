# The Enterprise Dashboard Hierarchy

## 1. Executive Summary
Enterprise architectures require a standardized four-tier dashboard navigation model. Every engineer, executive, and incident responder must know exactly which dashboard to open depending on the operational context.

---

## 2. The 4-Tier Operational Hierarchy

```mermaid
graph TD
    T0["Tier 0: Executive & Business Health\n- Audience: Executives, Product Leads\n- Metrics: Revenue rate, order volume, global active users\n- Update Frequency: 1 - 5 Minutes"]
    
    T1["Tier 1: SRE Service Health (RED Overview)\n- Audience: Incident Commanders, Primary On-Call\n- Metrics: Service RED metrics, SLO burn rate, runbook links\n- Update Frequency: 10 - 30 Seconds"]
    
    T2["Tier 2: Subsystem & Component Drilldown\n- Audience: Squad Engineers, Database Specialists\n- Metrics: SQL query latency, cache hit ratios, queue depth\n- Update Frequency: 10 Seconds"]
    
    T3["Tier 3: Infrastructure & Host Debugging\n- Audience: Platform Engineers, Kernel/Network SREs\n- Metrics: CPU steal, cgroup memory limits, disk IOPS\n- Update Frequency: 5 - 10 Seconds"]
    
    T0 -->|Click Service| T1
    T1 -->|Click Component| T2
    T2 -->|Click Pod / Host| T3
```

---

## 3. Tier Specifications

| Hierarchy Level | Primary Persona | Core Question Answered | Action Taken on Anomaly |
| :--- | :--- | :--- | :--- |
| **Tier 0: Business** | Executive Leadership | *"Is our business making money right now?"* | Executive communication; business disaster declaration. |
| **Tier 1: SRE / Service** | On-Call Engineers | *"Which user journey is broken and why did the page fire?"* | Roll back deployment; toggle feature flag; invoke runbook. |
| **Tier 2: Subsystem** | Software Developers | *"Which internal query, cache, or external API is failing?"* | Restart hung worker; scale connection pool; failover DB. |
| **Tier 3: Infrastructure** | Platform SREs | *"Is the physical or virtual host exhausted?"* | Cordon/drain Kubernetes node; increase pod CPU limits. |
