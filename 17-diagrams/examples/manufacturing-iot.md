# Smart Manufacturing & Industrial IoT (IIoT) Architecture

This reference architecture models an industrial IoT smart factory ecosystem connecting manufacturing floor PLCs, edge MQTT brokers, time-series telemetry pipelines, digital twin simulations, and predictive maintenance ML models.

## 1. Business Context & Architectural Drivers
* **Real-Time Edge Analytics**: Detect machine anomaly vibrations and thermal spikes at the factory edge within 10ms to trigger emergency stops.
* **Protocol Bridging**: Ingest legacy factory protocols (Modbus, OPC-UA, Profinet) and translate them to lightweight MQTT/Protobuf.
* **Scale**: Support 50,000 industrial sensors per plant streaming telemetry at 100Hz into a central cloud time-series lakehouse.

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph FactoryFloor ["Plant Floor"]
        RobotArm["Robotic Welding Arms"]
        CNC["CNC Milling Machines"]
        Sensors["Vibration & Thermal Sensors"]
    end

    subgraph SmartFactoryPlatform ["Industrial IoT Platform"]
        PlatformCore["Smart Factory Engine<br/>- Edge Ingestion & Protocol Translation<br/>- Real-time Anomaly Detection<br/>- Digital Twin & Asset Management<br/>- Predictive Maintenance Models"]
    end

    subgraph PlantStakeholders ["Factory Operations"]
        PlantManager["Plant Operations Manager"]
        MaintTech["Maintenance Technician"]
    end

    subgraph EnterpriseERP ["Enterprise Backbone"]
        SAP["SAP S/4HANA (Plant Maintenance - PM)"]
    end

    RobotArm --> PlatformCore
    CNC --> PlatformCore
    Sensors --> PlatformCore
    PlatformCore -->|"Alerts machine downtime"| PlantManager
    PlatformCore -->|"Dispatches work orders"| MaintTech
    PlatformCore -->|"Generates spare part orders"| SAP
```

## 3. C4 Level 2: Edge-to-Cloud Streaming Pipeline

```mermaid
graph LR
    subgraph FactoryEdgeNetwork ["Factory Edge (On-Premises DMZ)"]
        PLC["Siemens / Rockwell PLCs<br/>(OPC-UA / Modbus)"]
        EdgeGateway["Edge IoT Gateway (K3s / Docker)<br/>- Protocol Converter (OPC-UA to MQTT)<br/>- Local EMQX MQTT Broker<br/>- Edge ML Anomaly Detector (ONNX)"]
        PLC --> EdgeGateway
    end

    subgraph CloudIngress ["Cloud Ingestion Tier (AWS)"]
        IoTCore["AWS IoT Core<br/>(TLS 1.3 / Mutual Auth X.509)"]
        Kafka["Kafka Telemetry Buffer"]
        EdgeGateway -->|"MQTT over TLS"| IoTCore
        IoTCore --> Kafka
    end

    subgraph TimeSeriesCompute ["Stream Analytics & Digital Twin"]
        FlinkJob["Apache Flink Streaming Cluster<br/>- Sliding Window Fast Fourier Transform (FFT)<br/>- Real-time Vibration Spike Detection"]
        TimescaleDB[("TimescaleDB / InfluxDB<br/>(Hot Telemetry - 30 Days)")]
        DigitalTwin["AWS IoT TwinMaker<br/>(3D Virtual Asset Representation)"]

        Kafka --> FlinkJob
        FlinkJob --> TimescaleDB
        TimescaleDB --> DigitalTwin
    end

    subgraph ColdArchive ["Industrial Data Lakehouse"]
        IcebergLake[("Parquet Lakehouse (S3 / Iceberg)<br/>[Historical Analytics - 7 Years]")]
        Kafka --> IcebergLake
    end
```

## 4. Edge Anomaly Detection & Emergency Stop Sequence

```mermaid
sequenceDiagram
    autonumber
    participant Sensor as Vibration Sensor (100Hz)
    participant Edge as Edge Gateway (Local Runtime)
    participant PLC as Machine Safety PLC
    participant Cloud as AWS IoT Core
    participant Maint as Maintenance Tech App

    Sensor->>Edge: Stream Raw Accelerometer Samples
    Edge->>Edge: Execute ONNX Anomaly Detection Model
    
    alt Harmonic Vibration Exceeds Safety Threshold (>8.5g)
        Edge->>PLC: Send Hardware Digital Interrupt (E-STOP)
        PLC->>PLC: Immediate Hydraulic Brake Engaged (<10ms)
        Edge->>Cloud: Emit Critical Alert: PDM_BEARING_FAILURE
        Cloud->>Maint: Push High-Priority Alarm (Work Order #991)
    else Normal Operation
        Edge->>Cloud: Batch Telemetry (5-second aggregates)
    end
```

## 5. Architectural Decisions
* **Local Autonomy at Edge**: Anomaly detection and safety interlocks run locally on ruggedized edge servers with zero dependence on cloud WAN connectivity.
* **Time-Series Columnar Lakehouse**: Telemetry is written directly to Apache Iceberg formatted Parquet files, reducing storage costs by 80% compared to traditional relational stores.
