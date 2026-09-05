# 03-HLD: High-Level Design

## 1. Overview & Purpose

A **High-Level Design (HLD)** answers the foundational engineering question:

> **"How is the subsystem or service structured at a level sufficient for engineering teams to implement it without dictating internal source-code semantics?"**

While the Solution Architecture Document (SAD) covers enterprise-wide context and multi-tier business capabilities, the HLD focuses on a specific bounded context, service, or major feature. It defines component topologies, communication protocols, synchronous vs asynchronous flows, persistence mechanisms, security boundaries, and resilience patterns.

---

## 2. Directory Contents

* **[template.md](template.md)**: Master High-Level Design template (16 core sections).
* **[component-overview-template.md](component-overview-template.md)**: C4 Component modeling and responsibility mapping.
* **[deployment-overview-template.md](deployment-overview-template.md)**: Service runtime deployment and container topology.
* **[integration-overview-template.md](integration-overview-template.md)**: Inbound/outbound interface contracts and event schemas.
* **[review-checklist.md](review-checklist.md)**: 20-Point HLD engineering quality audit checklist.
* **[examples/](examples/)**: Production-grade reference examples:
  - [ecommerce-checkout-service-hld.md](examples/ecommerce-checkout-service-hld.md) — Real-time Distributed Checkout Service.
