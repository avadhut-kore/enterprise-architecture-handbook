# Architecture Decision Records & Evolution Roadmap: Logistics

## 1. Canonical Architecture Decision Records

### ADR-001: Adoption of Uber H3 Hexagonal Spatial Index for Geofencing
- **Status**: Accepted
- **Context**: Evaluating 16,000 GPS pings/second against 100,000 polygon geofences using standard PostGIS `ST_Contains` saturated database CPU at 100%.
- **Decision**: Index all geofences and vehicle positions as Uber H3 hexagonal grid cells, reducing geometric intersections to integer lookup sets.
- **Consequences**: Reduces geofence computation time by 95%; adds minor approximation error ($< 50\text{m}$).

---

## 2. Evolution Roadmap (1x to 100x Scale)
- **Stage 1 (1x)**: Monolithic TMS with relational PostGIS queries.
- **Stage 2 (10x)**: Kafka event stream; Flink geofence evaluator; offline mobile sync.
- **Stage 3 (100x)**: AI-driven dynamic predictive ETA engine factoring global weather, driver rest patterns, and border wait times.
