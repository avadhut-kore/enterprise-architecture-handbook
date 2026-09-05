# Business Architecture & Requirements: Logistics Platform

## 1. Operational Realities & Personas
- **Fleet Drivers**: Operate in remote rural areas with spotty cellular coverage; mobile apps must execute deliveries, capture signatures, and record proof-of-delivery 100% offline.
- **Dispatchers**: Require live operational maps tracking thousands of trucks with real-time ETA recalculations taking traffic and weather into account.
- **Shippers & Consignees**: Demand millisecond milestone tracking notifications (Order Picked Up, In Transit, Out for Delivery, Delivered).

---

## 2. Scale Model & Capacity Assumptions

| Scale Dimension | Regional Carrier | Global Freight Network |
| :--- | :--- | :--- |
| **Connected Fleet Vehicles** | 5,000 trucks | 80,000 trucks |
| **Daily Active Shipments** | 50,000 shipments | 1,500,000 shipments |
| **Telematics Ping Frequency** | 10 seconds per truck | 5 seconds per truck |
| **Peak Telematics Ingestion Rate** | 500 GPS events/sec | 16,000 GPS events/sec |
| **Daily Geofence Evaluations** | 5 Million evaluations | 150 Million evaluations |
