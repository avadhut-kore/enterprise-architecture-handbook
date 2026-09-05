# Case Study: Uber Real-Time Dispatch & Marketplace

## 1. Company & Business Context

Uber operates a global real-time mobility and delivery marketplace connecting tens of millions of active riders and eaters with millions of independent driver-partners across 70+ countries and 10,000+ cities. The platform handles dynamic supply-and-demand matchmaking, continuous GPS tracking, real-time routing, dynamic pricing (surge), and automated dispatching.

The primary architectural requirement is extreme real-time responsiveness: driver location updates must be ingested every 4 seconds, location queries must execute in under 20 milliseconds, and dispatch matchmaking algorithms must converge globally within seconds while preventing double-dispatching the same driver.

---

## 2. Scale & Workload Profile

```
+------------------------------------+---------------------------------------+
| Metric                             | Production Volume                     |
+------------------------------------+---------------------------------------+
| Monthly Active Platform Consumers | 140M+ Active Users                    |
| Active Drivers Online Concurrently | > 5 Million Drivers Globally          |
| Driver Telemetry Updates           | > 1.25 Million GPS Ingests / Second   |
| Trip Dispatch Executions           | > 30 Million Trips / Day              |
| Geospatial Query P99 Latency       | < 15 Milliseconds                     |
| Cross-Region Replication Latency   | < 500 Milliseconds                    |
+------------------------------------+---------------------------------------+
```

---

## 3. Original Architecture (The Python & Postgres Monolith)

Uber's early architecture consisted of a monolithic Python web application (`dispatch-daemon`) running on top of a single centralized PostgreSQL database:
- **Single Node Bottleneck**: All driver updates and dispatch queries hit a single Postgres database with PostGIS extensions.
- **Lock Contention**: Frequent row-level write locks on active driver tables during rapid GPS updates caused cascading connection pool exhaustion.
- **Geographic Coupling**: A rider in London was routed through the same central database infrastructure as a rider in San Francisco.

---

## 4. Modern Target Architecture: Geospatial Microservices & H3

Uber decomposed the monolith into a microservices architecture powered by:
1. **H3 Spatial Indexing System**: A hexagonal hierarchical spatial index partitioning the surface of the Earth into regular hexagonal cells across 16 resolution levels.
2. **Ringpop & Consistent Hash Ring**: A decentralized, cooperative node cluster protocol implementing consistent hashing and SWIM gossip membership for stateful in-memory location tracking.
3. **Schemaless & Docstore**: A distributed, sharded datastore built on top of MySQL engines providing append-only immutability.

```mermaid
flowchart TB
    subgraph DriversLayer [Driver Fleet Telemetry]
        DriverApp1[Driver Device App]
        DriverApp2[Driver Device App]
    end

    subgraph IngestionEdge [Edge & Ingest Tier]
        LB[Global L4 Load Balancer]
        PushGateway[Netty TCP / gRPC Edge Gateway]
        KafkaIngest[Apache Kafka Telemetry Topic]
    end

    subgraph GeospatialCluster [DISPATCH & LOCATION MESH]
        LocationRing[Ringpop Location In-Memory Node Ring]
        H3Engine[H3 Geospatial Index Service]
        SupplyService[Supply State Service]
        DemandService[Demand & Search Service]
    end

    subgraph MatchmakingCore [Marketplace Optimization]
        DISPATCH[Marketplace Dispatch Engine (OR-Tools)]
        DynamicPricing[Dynamic Pricing Engine (Surge)]
    end

    subgraph Persistence [Storage Tier]
        DocStore[(Docstore Sharded MySQL Engine)]
        RedisCache[(Redis Geospatial Cache)]
    end

    DriverApp1 -->|GPS ping every 4s| LB
    DriverApp2 -->|GPS ping every 4s| LB
    LB --> PushGateway
    PushGateway --> KafkaIngest
    KafkaIngest --> LocationRing
    LocationRing --> H3Engine
    H3Engine --> SupplyService

    SupplyService --> RedisCache
    SupplyService --> DocStore

    DISPATCH -->|Query supply within H3 Hex K-Ring| H3Engine
    DISPATCH --> DynamicPricing
    DISPATCH -->|Assign match with lease lock| SupplyService
```

---

## 5. Core Architectural Inventions

### A. H3 Hexagonal Spatial Index
Unlike square or geohash-based bounding boxes, hexagons have the mathematical property that all neighboring cells have identical center-to-center distances.
- **Neighbor Smoothness**: Any H3 hexagon has exactly 6 neighbors at equal distance $d$. This eliminates dimensional distortion when calculating distance radii ($K\text{-rings}$) for searching nearby drivers.
- **Hexagon Hierarchies**: Resolution 8 (average area $\approx 0.737 \text{ km}^2$) serves as the primary aggregation unit for dynamic pricing and supply density.

### B. Consistent Hashing & Ringpop
To avoid querying central databases for rapid 4-second telemetry pings:
- Ringpop hashes driver IDs across a cluster of in-memory worker processes.
- Nodes maintain a gossip protocol (SWIM) to detect node join/leave/failure events without central coordinators.
- A rider looking for drivers in a specific area queries the location service, which translates the geo-coordinates to an H3 index and queries the worker nodes hosting those H3 cells.

### C. Two-Phase Locking & Optimistic Concurrency in Dispatch
To prevent the "double-dispatch" anomaly where two nearby riders are simultaneously assigned the same driver:
- The dispatch engine evaluates batch assignments across a geographical bucket every 3 seconds (batch optimization rather than first-come-first-served greedy matching).
- When a driver is selected, an atomic conditional write with a short lease TTL (e.g., 5 seconds) is executed against the Driver State Machine. If the lease fails, the optimizer selects the next candidate.

---

## 6. Distributed Trade-Offs & Decisions

```
+-----------------------------------+----------------------------------------+
| Dimension                         | Uber Architectural Choice              |
+-----------------------------------+----------------------------------------+
| Matching Algorithm                | Batch Assignment vs Greedy Match       |
| Geospatial Projection             | H3 Hexagons vs Geohash / PostGIS       |
| Ingest Protocol                   | Persistent gRPC / HTTP/2 vs HTTP Polling|
| Storage Model                     | Append-Only Event Log vs In-Place Update|
+-----------------------------------+----------------------------------------+
```

---

## 7. Engineering Lessons & Enterprise Takeaways

1. **Partition by Domain Mathematics**: Choosing the right geometric primitive (H3 hexagons over square geohashes) reduced geospatial neighborhood search query complexity from $O(N)$ polygon intersections to $O(1)$ constant-time coordinate lookups.
2. **Shift High-Frequency Ephemeral Writes to In-Memory Rings**: Driver GPS updates every 4 seconds do not require immediate disk-persisted relational transactions; holding current state in memory rings with Kafka event streaming guarantees durability without storage exhaustion.
3. **Batch Optimization Trumps Greedy Matching**: In two-sided marketplaces, batching match requests over a 2–5 second sliding window yields superior global system efficiency and lower rider wait times compared to instant greedy allocation.
