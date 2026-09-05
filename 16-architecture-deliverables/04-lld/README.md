# 04-LLD: Low-Level Design

## 1. Overview & Purpose

A **Low-Level Design (LLD)** translates the component structures of the High-Level Design (HLD) into concrete, implementation-ready specifications for software engineers without becoming stale source code comments.

An LLD defines:
* **Package and Module Structure**: Code organization and directory layouts.
* **Class & Interface Specifications**: Methods, signatures, parameter validation, and immutability.
* **Sequence Logic**: Step-by-step internal execution workflows.
* **Concurrency & Transaction Boundaries**: Thread pools, database locks, and rollback isolation.
* **Error Handling & Retry Models**: Specific exception hierarchies and HTTP/gRPC status mappings.
* **Configuration Specifications**: Environment variable schemas and feature flags.

---

## 2. Directory Contents

* **[template.md](template.md)**: Master Low-Level Design template (16 implementation sections).
* **[service-template.md](service-template.md)**: Microservice internal class and dependency injection template.
* **[module-template.md](module-template.md)**: Domain module and Hexagonal/Clean architecture template.
* **[database-template.md](database-template.md)**: Table DDL, SQL migration, and indexing specification template.
* **[api-template.md](api-template.md)**: Internal controller and DTO serialization specification.
* **[sequence-template.md](sequence-template.md)**: Internal method invocation sequence template.
* **[error-handling-template.md](error-handling-template.md)**: Exception hierarchy and error mapping specification.
* **[configuration-template.md](configuration-template.md)**: Environment variable and secrets schema template.
* **[review-checklist.md](review-checklist.md)**: 20-Point LLD code readiness checklist.
* **[examples/](examples/)**: Production-grade reference examples:
  - [order-processing-service-lld.md](examples/order-processing-service-lld.md) — Implementation specification for Order Processing Microservice.
