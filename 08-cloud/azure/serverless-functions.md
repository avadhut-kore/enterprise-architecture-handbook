# Azure Serverless Architecture: Azure Functions & Durable Functions

## Executive Summary

Azure Functions provides event-driven serverless compute. For complex multi-step distributed workflows, **Durable Functions** introduces code-centric stateful orchestration without external databases.

---

## 1. Durable Functions State Orchestration Pattern

```mermaid
graph TD
    Client[Client POST /order] --> HttpTrigger[HttpTrigger: Starter Function]
    HttpTrigger --> Orchestrator[Orchestrator Function: 'ProcessOrder']

    Orchestrator -->|Call Activity 1| A1[Activity: Reserve Inventory]
    A1 --> Orchestrator
    Orchestrator -->|Call Activity 2| A2[Activity: Process Payment]
    A2 --> Orchestrator
    Orchestrator -->|Call Activity 3| A3[Activity: Dispatch Notification]

    Orchestrator -.->|Automatic Checkpointing to Azure Storage Table| State[(Durable Storage State)]
```

---

## 2. Hosting Plan Selection

| Dimension | Consumption Plan | Premium Plan (Elastic) | Dedicated (App Service) Plan |
| :--- | :--- | :--- | :--- |
| **Cold Starts** | Substantial (seconds on idle) | Zero cold starts (pre-warmed instances) | Zero cold starts |
| **VNet Integration** | Not supported | Supported (Private VNet connectivity) | Supported |
| **Max Execution Duration**| 5 to 10 Minutes | Guaranteed up to 60 minutes | Unlimited |
| **Billing Model** | Pure pay-per-execution + GB-seconds | Base hourly rate per pre-warmed instance | Predictable monthly VM rate |
| **Enterprise Verdict** | Internal dev/test and low-priority cron jobs | **Standard for enterprise APIs and VNet-connected workers** | Suitable when consolidating with existing App Service fleets |
