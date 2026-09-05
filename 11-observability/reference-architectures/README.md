# Production Observability Reference Architectures

## Executive Summary

Enterprise systems are rarely homogeneous. A global corporation operates Kubernetes microservices alongside legacy COBOL mainframes, serverless event handlers, Kafka streaming backbones, PCI-DSS payment vaults, and emerging Generative AI models.

Applying a one-size-fits-all observability pattern across these disparate environments leads to architectural failure. This directory provides **11 battle-tested, production-grade reference architectures**, each tailored to the unique operational, compliance, and throughput constraints of specific enterprise technology topologies.

---

## Reference Architectures Index

| Reference Architecture | Target Domain & Tech Stack | Core Architectural Characteristics |
| :--- | :--- | :--- |
| **[`01-cloud-native-k8s.md`](01-cloud-native-k8s.md)** | Cloud-Native Kubernetes (K8s, Envoy, OTel, Thanos, Loki, Tempo) | Node DaemonSet collectors, zero-copy eBPF, Prometheus operator, multi-cluster federation. |
| **[`02-serverless-lambda.md`](02-serverless-lambda.md)** | Serverless & FaaS (AWS Lambda, Cloud Run, API Gateway, X-Ray) | Telemetry API extensions, sub-millisecond freeze handling, cold-start telemetry, asynchronous flushing. |
| **[`03-event-driven-streaming.md`](03-event-driven-streaming.md)** | Event-Driven Backbones (Apache Kafka, Pulsar, Flink) | W3C trace context injection into Kafka record headers, consumer lag tracking, dead-letter telemetry. |
| **[`04-hybrid-cloud.md`](04-hybrid-cloud.md)** | Hybrid Multi-Cloud (AWS + Azure + Bare Metal Datacenter) | Unified correlation IDs, WAN egress optimization, cross-cloud private link, sovereign storage boundaries. |
| **[`05-multi-tenant-saas.md`](05-multi-tenant-saas.md)** | Enterprise B2B Multi-Tenant SaaS Platforms | Per-tenant metric tagging, tenant trace isolation, noisy-neighbor detection, FinOps cost-per-tenant. |
| **[`06-financial-payments.md`](06-financial-payments.md)** | Regulated Payment Processing (PCI-DSS, Core Banking, SWIFT) | Zero PAN logging, HSM cryptographic hardware telemetry, dual-entry ledger reconciliation observability. |
| **[`07-healthcare-clinical.md`](07-healthcare-clinical.md)** | Healthcare & Clinical Systems (FHIR, HL7, HIPAA, EHR) | High-entropy PHI masking, patient journey tracing, HIPAA audit trails, clinical latency guarantees. |
| **[`08-edge-iot.md`](08-edge-iot.md)** | Industrial IoT & Edge Computing (MQTT, CoAP, K3s) | Store-and-forward buffers, intermittent WAN connectivity, bandwidth-constrained downsampling. |
| **[`09-data-pipeline-mesh.md`](09-data-pipeline-mesh.md)** | Data Mesh & Analytical Lakehouses (Spark, Snowflake, dbt) | Data freshness SLIs, automated schema drift alerts, row-count reconciliation, lineage tracking. |
| **[`10-legacy-modernization.md`](10-legacy-modernization.md)** | Mainframe & Strangler Fig Coexistence (CICS, IBM MQ) | Bridging IBM MQ RFH2 headers to W3C OpenTelemetry trace parents, mainframe CPU ms accounting. |
| **[`11-ai-ml-llm-observability.md`](11-ai-ml-llm-observability.md)** | Generative AI & LLMOps (LangChain, OpenAI, Vector DBs) | Prompt/completion token tracking, embedding latency, RAG vector retrieval recall, semantic drift. |
