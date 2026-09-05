# Supply Chain & Fleet Logistics Architecture

This reference architecture models a real-time global freight logistics platform featuring GPS vehicle telematics, dynamic geofencing, route optimization algorithms, and automated cross-dock warehouse dispatching.

## 1. Business Context & Architectural Drivers
* **Fleet Telemetry Scale**: Track 100,000 active delivery vehicles streaming GPS coordinates and temperature sensors every 10 seconds.
* **Geofence Processing Latency**: Evaluate automated arrival and departure geofencing triggers in $\le 500$ms.
* **Route Optimization**: Real-time vehicle dynamic rerouting based on live traffic congestion and warehouse dock availability.

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph FleetAndFacilities ["Physical Logistics Assets"]
        Truck["Delivery Fleet Vehicles<br/>[GPS & Telematics Transponders]"]
        Warehouse["Distribution Warehouses<br/>[RFID & Dock Scanners]"]
    end

    subgraph LogisticsPlatform ["Global Logistics & Fleet Management System"]
        PlatformCore["Logistics Cloud Platform<br/>- Real-time Fleet Telemetry Engine<br/>- Spatial Geofencing & ETA Predictor<br/>- Dynamic Dispatch & Routing<br/>- Cold-Chain Temperature Monitor"]
    end

    subgraph ExternalServices ["External Providers"]
        MappingAPI["Mapping & Traffic API (Google / HERE)"]
        Shipper["Corporate Shippers & Customers"]
    end

    Truck -->|"Streams GPS Telematics"| PlatformCore
    Warehouse -->|"Scans package handoffs"| PlatformCore
    PlatformCore <-->|"Queries road network conditions"| MappingAPI
    PlatformCore -->|"Sends milestone alerts & live tracking"| Shipper
```

## 3. C4 Level 2: Spatial Telematics & Ingestion Topology

```mermaid
graph LR
    subgraph FleetIngress ["Mobile Fleet Ingestion"]
        FleetOBD["Vehicle Telematics Units (OBD-II / CAN bus)"]
        CellularGW["Cellular Telematics Gateway (MQTT/gRPC)"]
        FleetOBD --> CellularGW
    end

    subgraph SpatialProcessing ["Spatial Telemetry & Geofencing (Kafka + Flink)"]
        KafkaTele["Kafka Telemetry Stream<br/>(Partitioned by VehicleID)"]
        
        SpatialFlink["Apache Flink Spatial Worker<br/>- H3 Spatial Grid Indexing<br/>- Point-in-Polygon Geofence Detection<br/>- Cold-Chain Temperature Anomaly Detection"]

        CellularGW --> KafkaTele
        KafkaTele --> SpatialFlink
    end

    subgraph LiveStateTier ["Real-Time Operational Fleet State"]
        RedisGeo[("Redis Geospatial Cache<br/>- Current Vehicle Lat/Long<br/>- Real-Time Fleet Map Visualizer")]
        SpatialFlink --> RedisGeo
    end

    subgraph DispatchAndStorage ["Dispatch Engine & Persistence"]
        PostGIS[("Spatial Database (PostgreSQL + PostGIS)<br/>- Stored Geofence Polygons<br/>- Route Histories")]
        DispatchSvc["Route Optimization Service (VRP Solver)"]
        
        SpatialFlink --> PostGIS
        PostGIS --> DispatchSvc
    end
```

## 4. Geofence Arrival & Automated Dock Assignment Sequence

```mermaid
sequenceDiagram
    autonumber
    participant Truck as Delivery Truck Transponder
    participant Flink as Flink Spatial Engine
    participant PostGIS as PostGIS Geofence DB
    participant WMS as Warehouse Management System
    participant Driver as Driver Mobile App

    Truck->>Flink: Emit GPS Ping: Lat=40.7128, Long=-74.0060, Speed=35mph
    Flink->>PostGIS: Evaluate Current Coord against Facility Geofence Polygons
    PostGIS-->>Flink: Boundary Crossed: Arrived at Distribution Center #4 (DC-04)
    
    Flink->>WMS: Trigger Event: VehicleArrived (Truck #882, 1,200 Packages)
    WMS->>WMS: Compute Optimal Unloading Bay
    WMS-->>Flink: Assigned Dock Bay #14
    
    Flink->>Driver: Push Notification: "Proceed directly to Dock Bay #14"
```

## 5. Architectural Decisions
* **Uber H3 Spatial Hexagonal Indexing**: Discrete global grid coordinates reduce expensive polygon ray-casting calculations into fast integer hash table lookups.
* **Cold-Chain Safety Sinks**: Continuous temperature violations immediately trigger quarantine events in the logistics warehouse management system before unloading.
