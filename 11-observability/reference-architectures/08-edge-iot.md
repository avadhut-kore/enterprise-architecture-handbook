# Reference Architecture 08: Industrial Edge & IoT Observability

## 1. System Context & Overview
Industrial Internet of Things (IIoT), smart manufacturing, and fleet telemetry operate on resource-constrained microcontrollers, smart gateways, and remote edge sites connected over high-latency, intermittent cellular or satellite links.

This architecture solves the challenge of **intermittent connectivity and severe bandwidth limitations**.

---

## 2. Architecture Diagram

```mermaid
flowchart LR
    subgraph Remote_Edge_Site ["Remote Edge Site (Factory Floor / Offshore Rig)"]
        Sensors["PLC & Industrial Sensors (Modbus / OPC-UA)"]
        Edge_GW["Edge Gateway (K3s / Linux Yocto)"]
        
        subgraph Store_Forward ["Store-and-Forward Telemetry Engine"]
            SQLite["Local SQLite / Embedded TSDB Buffer\n(Stores up to 14 days of offline data)"]
            Compress["Zstandard Compactor\n(10:1 Compression Ratio)"]
        end
        
        Sensors --> Edge_GW
        Edge_GW --> SQLite --> Compress
    end

    subgraph WAN_Link ["Intermittent WAN / Satellite Link"]
        Compress -->|Sync on Connection Available| Central_Gateway
    end

    subgraph Cloud_Platform ["Central Enterprise Cloud"]
        Central_Gateway["IoT Telemetry Ingestion Hub (MQTT / Kafka)"]
        TSDB["Enterprise TSDB & Digital Twin Platform"]
        Central_Gateway --> TSDB
    end
```

---

## 3. Key Architectural Decisions
1. **Store-and-Forward Architecture**: When remote cellular or satellite links fail, telemetry is appended to local persistent storage (embedded SQLite or LevelDB). Upon reconnection, telemetry is streamed with timestamp backfilling.
2. **Dynamic Adaptive Downsampling**: When network bandwidth is constrained ($< 50\text{ kbps}$), the edge agent drops high-frequency raw vibration samples and transmits only rolling statistical aggregates (Min, Max, Mean, Variance).
3. **Binary Protocol Telemetry**: Telemetry is encoded in **Protocol Buffers or CBOR** rather than verbose JSON, reducing network payload size by $85\%$.
