# Global Logistics & Freight Orchestration Reference Architecture

## 1. Executive Summary & Architectural Vision
The Global Logistics & Freight Orchestration Platform is a high-throughput supply chain system governing Transportation Management (TMS), dynamic Vehicle Routing Problem (VRP) optimization, real-time IoT fleet telematics, offline-first mobile driver delivery execution, and B2B carrier EDI integration.

```
[Driver Mobile App (Offline Sync), Dispatch Portal, Shipper Tracking, Fleet Telematics]
                                  │
             ═════════════════════▼═════════════════════  [IoT / Edge Gateway]
                      Logistics Core Engine
     ┌─────────────────┬──────────────────┬──────────────────┐
     ▼                 ▼                  ▼                  ▼
[TMS Route Optimizer] [Fleet Telematics] [Shipment Tracker] [EDI 204/214 B2B]
(VRP Genetic Solver)  (IoT Sensor Stream)(Milestone FSM)    (AS2 Carrier Rail)
     │                 │                  │                  │
     └─────────────────┼──────────────────┴──────────────────┘
                       ▼
            [High-Throughput Geo-Event Stream (Kafka)]
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
[Geofencing & ETA Engine]   [Cold-Chain Telemetry Vault]
(Real-Time GPS Spatial Index) (FDA FSMA Compliance Storage)
```

## 2. Architectural Package Contents
- [01-business-and-requirements.md](01-business-and-requirements.md): Freight personas, fleet telematics scale, and SLA budgets.
- [02-architecture-and-c4.md](02-architecture-and-c4.md): C4 Context, Container, Component models, and cloud mappings.
- [03-application-architecture.md](03-application-architecture.md): VRP route solver, geofencing, and offline-first mobile sync.
- [04-data-architecture.md](04-data-architecture.md): Spatial indexing (H3/PostGIS), time-series telematics, and shipment ledgers.
- [05-integration-architecture.md](05-integration-architecture.md): Carrier EDI (EDI 204/214), telematics MQTT, and map APIs.
- [06-security-and-compliance.md](06-security-and-compliance.md): Driver Hours of Service (HOS), FDA FSMA cold-chain, and GPS privacy.
- [07-infrastructure-and-devops.md](07-infrastructure-and-devops.md): Edge MQTT brokers, Kubernetes VRP worker pools, and IaC.
- [08-observability-and-reliability.md](08-observability-and-reliability.md): On-Time In-Full (OTIF) metrics, geofence event lag, and DR.
- [09-cost-and-finops.md](09-cost-and-finops.md): Map API cost optimization, IoT cellular data charges, and monthly TCO.
- [10-sequences-and-flows.md](10-sequences-and-flows.md): Delivery dispatch, GPS geofence arrival trigger, and proof of delivery.
- [11-adrs-and-evolution.md](11-adrs-and-evolution.md): Canonical ADRs (Offline SQLite Sync, Uber H3 Spatial Index) and roadmap.
