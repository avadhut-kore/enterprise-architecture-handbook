# ADR-0001: Standardizing on OpenTelemetry as Universal Telemetry Standard

* **Status**: Accepted
* **Date**: 2026-03-15
* **Deciders**: Enterprise Architecture Review Board, Head of Platform Engineering, Lead SRE Architect
* **Technical Story**: [ARCH-OBS-001] Establish Enterprise Telemetry Standard

---

## Context and Problem Statement
The enterprise operates 1,200 polyglot microservices across Java, Go, Python, Node.js, and .NET. Telemetry instrumentation is fragmented across three proprietary SaaS agents (Datadog, AppDynamics, New Relic) and bespoke logging libraries. This creates severe vendor lock-in, inflated annual licensing costs ($4.8M/yr), and incompatible distributed trace headers across service boundaries.

## Decision Drivers
* Total elimination of proprietary vendor instrumentation lock-in.
* Standardized W3C distributed trace propagation across all polyglot microservices.
* Capability to route telemetry simultaneously to multiple cloud storage backends.
* Industry adoption and longevity guaranteed by CNCF backing.

## Considered Options
1. **Option 1**: Retain proprietary SaaS vendor agents (Status Quo).
2. **Option 2**: Standardize on **OpenTelemetry (OTel)** across all languages and infrastructure.
3. **Option 3**: Build an internal proprietary enterprise telemetry SDK wrapper.

## Decision Outcome
**Chosen Option**: **Option 2: OpenTelemetry (OTel)**.

### Positive Consequences
* **Vendor Portability**: Changing storage backends (e.g., SaaS to open-source Thanos/Tempo) requires only an OTel Collector configuration change with zero code refactoring.
* **W3C Trace Standardization**: Clean trace propagation across all polyglot RPC and messaging boundaries.
* **Ecosystem Vibrancy**: Massive open-source community support and native cloud provider integrations.

### Negative Consequences
* Initial engineering migration effort across 1,200 repositories.
* Requires developing and maintaining internal starter libraries with corporate defaults.

---

## Pros and Cons of the Options

### Option 1: Proprietary SaaS Vendor Agents
* Pros: Turnkey automatic instrumentation out of the box.
* Cons: Extreme financial lock-in; proprietary trace headers; cannot inspect source code.

### Option 2: OpenTelemetry (OTel)
* Pros: Open CNCF standard; vendor-neutral; polyglot support; decoupled collector architecture.
* Cons: Collector pipeline requires initial operational governance and capacity planning.

### Option 3: Internal Proprietary SDK
* Pros: Tailored exactly to internal corporate quirks.
* Cons: Massive internal maintenance overhead; reinventing the wheel.

---

## Links
* OpenTelemetry Specification: https://opentelemetry.io/docs/specs/otel/
* Cross-reference: [`../opentelemetry/collector-architecture.md`](../opentelemetry/collector-architecture.md)
