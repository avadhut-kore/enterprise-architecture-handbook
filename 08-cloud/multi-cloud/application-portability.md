# Application Code Portability & Hexagonal Isolation

## Executive Summary

Application portability ensures that software source code can be compiled, containerized, and executed across multiple cloud providers or on-premises environments without rewriting core business logic.

---

## 1. Hexagonal Architecture for Cloud Portability

```mermaid
graph TD
    subgraph Core Domain [100% VENDOR NEUTRAL]
        Logic[Core Business Entities & Domain Logic]
        Ports[Outbound Ports / Interfaces: 'MessagePublisher', 'BlobStorage']
    end

    subgraph Cloud Adapters [SWAPPABLE INFRASTRUCTURE]
        AWSAdapter[AWS SQS / S3 Adapter]
        AzureAdapter[Azure Service Bus / Blob Storage Adapter]
        GCPAdapter[GCP PubSub / Cloud Storage Adapter]
    end

    Logic --> Ports
    Ports -.-> AWSAdapter
    Ports -.-> AzureAdapter
    Ports -.-> GCPAdapter
```

---

## 2. Portability Rules for Application Engineers

1. **Zero Cloud SDK Imports in Domain Code**:
   - Under no circumstances may application code import `com.amazonaws.*`, `com.azure.*`, or `com.google.cloud.*` in domain models, controllers, or business services.
   - All cloud SDK calls must reside entirely inside infrastructure adapter modules implementing clean domain interfaces.
2. **Twelve-Factor Configuration**:
   - Inject all configuration, connection strings, and feature toggles exclusively via environment variables or standardized configuration endpoints, never via proprietary cloud runtime metadata services.
3. **Standardized Open Telemetry Instrumentation**:
   - Instrument applications using vendor-neutral **OpenTelemetry SDKs**. Export telemetry over standard OTLP/gRPC to collectors, allowing telemetry backends to be swapped without modifying application code.
