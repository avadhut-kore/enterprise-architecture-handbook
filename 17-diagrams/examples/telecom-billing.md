# Telecom Call Detail Record (CDR) & Real-Time Billing Architecture

This reference architecture models a telecom mediation and convergent billing engine processing 500,000 call detail records (CDRs) and data usage packets per second with real-time rating, quota enforcement, and automated invoicing.

## 1. Business Context & Architectural Drivers
* **Throughput Capacity**: Sustained ingest of 500,000 CDRs/sec with burst tolerance up to 1,200,000 events/sec.
* **Rating Latency**: Real-time prepaid balance decrement and quota enforcement under 50ms.
* **Durability Guarantee**: Exactly-once processing; zero lost billable usage records.

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph NetworkElements ["Cellular Network Elements"]
        SGW["Serving Gateway / PGW (LTE/5G)"]
        MSC["Mobile Switching Center (Voice/SMS)"]
    end

    subgraph TelecomPlatform ["Convergent Mediation & Billing Platform"]
        Platform["Telecom Billing Platform<br/>- CDR Streaming Ingestion<br/>- Real-time Rating Engine<br/>- Account Balance & Quota Management<br/>- Monthly Invoicing Engine"]
    end

    subgraph DownstreamSystems ["Business Support Systems (BSS)"]
        CRM["Customer Care CRM (Salesforce Telecom)"]
        PaymentGW["Direct Debit Payment Gateway"]
    end

    SGW -->|"GTP-C / Diameter Traffic"| Platform
    MSC -->|"ASN.1 Binary CDR Records"| Platform
    Platform -->|"Updates customer usage & throttling"| SGW
    Platform -->|"Syncs billing profile"| CRM
    Platform -->|"Collects monthly bills"| PaymentGW
```

## 3. C4 Level 2: Stream Processing & Ingestion Pipeline

```mermaid
graph LR
    subgraph NetworkIngest ["5G Network Core"]
        PGW["5G UPF / PGW Nodes"]
    end

    subgraph StreamingPipeline ["Real-Time Mediation & Rating (Kafka + Flink)"]
        KafkaBuffer["Kafka Partitioned CDR Stream<br/>(128 Partitions, Snappy Compression)"]
        
        FlinkRating["Apache Flink Rating Cluster<br/>- Stateful Event Stream Processing<br/>- Rating Matrix Evaluation<br/>- 5-minute Tumbling Window Aggregations"]
        
        RocksState[("Flink State Backend<br/>[Embedded RocksDB]")]

        PGW -->|"High-throughput Syslog / Sockets"| KafkaBuffer
        KafkaBuffer --> FlinkRating
        FlinkRating <--> RocksState
    end

    subgraph FastBalanceTier ["Low-Latency In-Memory Balance Tier"]
        Aerospike[("Aerospike In-Memory Cluster<br/>- Sub-5ms Balance Deductions<br/>- Active Prepaid Subscriber Records")]
        FlinkRating -->|"Real-Time Balance Check"| Aerospike
    end

    subgraph LakehouseBilling ["Analytical Lakehouse & Billing Store"]
        IcebergBills[("Billed Usage Iceberg Tables<br/>(Partitioned by Year/Month/MSISDN)")]
        BillingBatch["Monthly Invoicing Batch (Spark)"]
        
        FlinkRating -->|"Micro-Batch Sinks"| IcebergBills
        IcebergBills --> BillingBatch
    end
```

## 4. Real-Time Data Usage Rating Sequence

```mermaid
sequenceDiagram
    autonumber
    participant UPF as 5G User Plane Function (UPF)
    participant Kafka as Kafka CDR Topic
    participant Flink as Flink Rating Worker
    participant Aero as Aerospike Balance Store
    participant Policy as 5G Policy Server (PCF)

    UPF->>Kafka: Emit Usage Record: MSISDN=555123, Bytes=50MB
    Kafka->>Flink: Ingest Event Stream
    Flink->>Aero: Read & Decrement Prepaid Balance
    
    alt Balance Remaining > 0
        Aero-->>Flink: Balance OK (Remaining: 240MB)
        Flink->>Flink: Append to Billed Usage Output Buffer
    else Balance Exhausted (0 MB)
        Aero-->>Flink: Insufficient Balance Alert
        Flink->>Policy: Diameter / HTTP/2 Request: Throttle Subscriber Speed to 64kbps
        Policy->>UPF: Apply Bandwidth Cap Immediately
        Flink->>Flink: Emit Low-Balance SMS Notification Event
    end
```

## 5. Architectural Decisions
* **Aerospike for Subscriber Balance**: Sub-millisecond reads/writes at scale without JVM garbage collection pauses.
* **Apache Iceberg for Long-Term CDR History**: Enables Petabyte-scale CDR archival with time-travel queries for regulatory customer dispute audits.
