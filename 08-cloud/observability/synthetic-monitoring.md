# Synthetic Monitoring & Active Canary Probing

## Executive Summary

Passive telemetry alerts only after real end users experience an outage. **Synthetic Monitoring** simulates critical user journeys continuously from global edge locations to detect failures before customers do.

---

## 1. Synthetic Canary Architecture

```mermaid
graph LR
    ProbeUS[Synthetic Edge Probe: North America] -->|Automated Headless Browser: Playwright| App[Production Web / API Platform]
    ProbeEU[Synthetic Edge Probe: Europe] --> App
    ProbeAPAC[Synthetic Edge Probe: Asia] --> App

    ProbeUS --> Script[Executes Journey: Login -> Search -> Add to Cart -> Verify Checkout API]
    Script -->|Step Fails or Takes > 3s| Page[PAGES ON-CALL SRE BEFORE USERS COMPLAIN!]
```
