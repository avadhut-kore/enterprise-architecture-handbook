# Retail Omnichannel & Edge POS Architecture

This reference architecture models a resilient, omnichannel retail platform uniting physical Point-of-Sale (POS) terminals, e-commerce web storefronts, real-time inventory availability, and unified loyalty programs across thousands of retail stores.

## 1. Business Context & Architectural Drivers
* **Offline-First Store Resilience**: Physical retail stores must process sales, scan barcodes, print receipts, and accept offline credit card swipes during internet WAN outages.
* **Unified Inventory Visibility**: Real-time Buy Online, Pick Up in Store (BOPIS) visibility across 2,500 retail stores and 10 regional distribution centers.
* **Sub-Second Synchronization**: Store sales sync to the central cloud platform within 2 seconds of internet reconnection.

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph Shoppers ["Retail Customers"]
        StoreShopper["In-Store Shopper"]
        OnlineShopper["E-Commerce Shopper"]
    end

    subgraph OmnichannelPlatform ["Omnichannel Retail Platform"]
        StorePOS["Physical Store Edge POS<br/>[System: In-Store Edge Server & Registers]"]
        CloudCommerce["Central Cloud Commerce Platform<br/>- Unified Inventory Availability<br/>- Cross-Channel Loyalty Engine<br/>- Order Orchestration"]
    end

    subgraph ExternalServices ["External Services"]
        PaymentProcessor["Merchant Card Acquirer"]
        WarehouseWMS["Warehouse Management System"]
    end

    StoreShopper -->|"Purchases at register"| StorePOS
    OnlineShopper -->|"Places BOPIS order"| CloudCommerce
    StorePOS <-->|"Bi-directional Sync"| CloudCommerce
    StorePOS -->|"Authorizes in-store payments"| PaymentProcessor
    CloudCommerce <-->|"Inventory updates"| WarehouseWMS
```

## 3. C4 Level 2: Edge-to-Cloud Synchronization Topology

```mermaid
graph TB
    subgraph PhysicalRetailStore ["Local Retail Store (Edge Environment)"]
        Register1["POS Terminal 1 (Electron/Touch)"]
        Register2["POS Terminal 2 (Mobile POS Tablet)"]
        
        LocalEdgeServer["In-Store Edge Server (NUC / K3s)<br/>- Local SQLite / PostgreSQL DB<br/>- Store-and-Forward Queue<br/>- Local Barcode Lookup Cache"]

        Register1 --> LocalEdgeServer
        Register2 --> LocalEdgeServer
    end

    subgraph CloudRetailBackbone ["Central Cloud Platform (AWS)"]
        EdgeSyncGW["Edge Sync Gateway<br/>[Container: Go / Websockets]<br/>Handles 2,500 persistent store connections"]
        
        InventoryService["Global Inventory Service<br/>[Container: Java Spring Boot]"]
        LoyaltyService["Customer Loyalty Service<br/>[Container: Node.js]"]
        
        GlobalKafka["Kafka Event Stream<br/>(Topic: store.transactions.v1)"]
        GlobalInventoryDB[("Global Inventory Store<br/>[CockroachDB Multi-Region]")]
    end

    LocalEdgeServer <-->|"Store-and-Forward (MQTT / HTTPS Sync)"| EdgeSyncGW
    EdgeSyncGW --> GlobalKafka
    GlobalKafka --> InventoryService
    GlobalKafka --> LoyaltyService
    InventoryService --> GlobalInventoryDB
```

## 4. Offline POS Transaction & Eventual Sync Sequence

```mermaid
sequenceDiagram
    autonumber
    actor Customer as Shopper
    participant POS as In-Store POS Register
    participant LocalEdge as In-Store Edge DB
    participant SyncAgent as Store Sync Worker
    participant Cloud as Central Cloud Gateway
    participant GlobalDB as Central Inventory Store

    Customer->>POS: Scan Items & Swipe Card
    Note over POS,LocalEdge: WAN Internet Outage Active
    POS->>LocalEdge: Lookup SKU & Price from Local Cache
    POS->>LocalEdge: Insert Transaction Record (Status: PENDING_SYNC)
    POS-->>Customer: Print Offline Store Receipt
    
    Note over SyncAgent,Cloud: Internet Connection Restored
    SyncAgent->>LocalEdge: Read Unsynced Offline Transactions
    SyncAgent->>Cloud: POST /sync/batch (15 Offline Sales Records)
    Cloud->>GlobalDB: Decrement Store Inventory Balance
    Cloud-->>SyncAgent: 200 OK (Batch Acknowledged)
    SyncAgent->>LocalEdge: Update Status: SYNCED
```

## 5. Architectural Decisions
* **Store-and-Forward Pattern**: Sales transactions are written to local disk before network transmission; POS operations are completely immune to cloud network disruptions.
* **Optimistic Offline Card Auth**: Stores accept offline credit transactions up to $100 per swipe during outages, balancing fraud risk against lost sales volume.
