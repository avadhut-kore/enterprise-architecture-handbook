# Enterprise Integration Platforms Architecture Library

## 1. Overview
Enterprise integration platforms serve as the operational connective tissue linking multi-cloud applications, SaaS services, on-premises datacenters, legacy mainframes, and external B2B partner networks. 

Architects must navigate the convergence of API Management, Event Streaming, Enterprise Service Buses (ESB), Integration Platform as a Service (iPaaS), and Managed File Transfer (MFT).

## 2. Directory Structure
- [integration-platform.md](integration-platform.md): Taxonomy of enterprise integration platform capabilities.
- [api-management.md](api-management.md): Full lifecycle API management: developer portals, rate limiting, and analytics.
- [api-gateway.md](api-gateway.md): High-performance ingress gateways (Envoy, Kong, Apigee, AWS API Gateway).
- [message-broker.md](message-broker.md): Traditional message queues (RabbitMQ, ActiveMQ, IBM MQ) vs. log streams.
- [event-streaming.md](event-streaming.md): Distributed append-only log backbones (Apache Kafka, Redpanda, AWS Kinesis).
- [integration-engine.md](integration-engine.md): Programmable integration engines (Apache Camel, MuleSoft, Spring Integration).
- [esb.md](esb.md): The rise, fall, and modern reincarnation of the Enterprise Service Bus.
- [workflow-engine.md](workflow-engine.md): Long-running distributed orchestrators (Temporal, Camunda, AWS Step Functions).
- [etl.md](etl.md): Extract, Transform, Load (ETL) vs. ELT vs. Real-Time Streaming (Flink, Spark).
- [managed-integration.md](managed-integration.md): Cloud iPaaS platforms (Workato, Boomi, MuleSoft Anypoint).
- [file-transfer.md](file-transfer.md): Enterprise Managed File Transfer (MFT), AS2, and secure B2B protocols.
- [integration-security.md](integration-security.md): Platform-level identity, network isolation, and encryption.
- [integration-observability.md](integration-observability.md): Centralized control planes, topology graphs, and alerts.
- [platform-governance.md](platform-governance.md): Contract versioning, producer-consumer agreements, and deprecation.
- [decision-framework.md](decision-framework.md): Integration platform selection matrix and evaluation scoring model.
