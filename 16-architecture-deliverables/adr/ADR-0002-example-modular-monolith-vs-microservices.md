# ADR-0002: Modular Monolith vs. Microservices for Core Order Management Platform

## Metadata
- **Status**: Accepted
- **Date**: 2026-09-05
- **Author(s)**: Lead Solution Architect (Enterprise Architecture Team)
- **Deciders**: Architecture Review Board (ARB), Head of Engineering, Principal Architects
- **Technical Story**: [ARCH-1042] Core Platform Modernization

---

## 1. Context and Problem Statement

The organization is modernizing its legacy 15-year-old order management application. The engineering organization currently consists of **18 full-time software engineers** organized into three feature squads (Checkout, Inventory, Billing). The projected peak throughput for Year 1 is **1,200 orders/minute (~20 TPS)** with a 3-year projected peak of **6,000 orders/minute (~100 TPS)**.

There is significant pressure within engineering leadership to immediately adopt a distributed Microservices architecture running on Kubernetes with independent databases per service. However, the operations and SRE team currently lacks mature distributed tracing infrastructure, service mesh capabilities, and 24/7 dedicated platform engineering. 

We must choose between a **Distributed Microservices Architecture** and a **Modular Monolith Architecture** as the foundational style for the modernization.

---

## 2. Decision Drivers

- **Driver 1: Time to Market & Developer Velocity**: Greenfield system must launch within 6 months.
- **Driver 2: Operational Overhead**: Total SRE/DevOps capacity is limited to 2 platform engineers.
- **Driver 3: Data Integrity**: Monetary billing transactions require strict ACID consistency across orders and payment reserves.
- **Driver 4: Clean Bounded Contexts**: The architecture must allow future extraction of individual services without major code rewrites if scale dictates.

---

## 3. Considered Options

- **Option A**: Distributed Microservices Architecture (7 independent services, Kubernetes, Kafka, 7 separate databases).
- **Option B**: Modular Monolith Architecture (Single deployable container, strict compile-time module isolation, shared PostgreSQL with isolated schemas, in-process event mediator).
- **Option C**: Traditional Monolithic Architecture (Single codebase, layered N-tier architecture, shared database without schema isolation).

---

## 4. Comparative Evaluation Matrix

| Decision Criteria | Option A: Microservices | Option B: Modular Monolith | Option C: Traditional Monolith |
|:---|:---:|:---:|:---:|
| **Initial Delivery Velocity** | 3 / 10 (High DevOps tax) | **9 / 10 (Fast local dev)** | 8 / 10 |
| **Operational Simplicity** | 2 / 10 (Distributed complexity)| **9 / 10 (Single container deployment)** | 10 / 10 |
| **ACID Consistency / Isolation** | 3 / 10 (Requires Sagas/2PC)| **10 / 10 (Single DB engine)** | 10 / 10 |
| **Long-Term Maintainability** | 7 / 10 | **9 / 10 (Enforced boundaries)**| 2 / 10 (Spaghetti risk) |
| **Cloud Hosting Cost** | $$$$ ($4,500/month baseline) | **$ ($650/month baseline)** | $ ($500/month) |
| **Evolutionary Extraction Path** | N/A (Already distributed) | **10 / 10 (Clean ports & interfaces)** | 2 / 10 |

---

## 5. Decision Outcome

**Chosen Option**: **Option B: Modular Monolith Architecture**

### Rationale and Justification
At 100 TPS peak load, the system is nowhere near the physical throughput limitations of a single well-indexed PostgreSQL instance (which easily supports 15,000+ writes/sec on modern cloud NVMe hardware). 

Adopting distributed microservices today would impose catastrophic operational friction: distributed transaction sagas, network latency overhead, complex local developer environments, and high cloud costs, which our 18-engineer team cannot sustain. 

The Modular Monolith provides the perfect architectural compromise:
1. Strict internal module boundaries enforced by automated fitness tests.
2. Direct in-memory invocation for sub-millisecond execution.
3. Isolated database schemas per module (`orders`, `billing`, `inventory`), making it trivial to extract any module into an independent microservice in the future if Conway's Law or scaling dictates.

---

## 6. Consequences & Trade-Offs

### Positive Consequences
- **Rapid Feature Delivery**: Engineers run and test the complete system locally with a single `docker compose up` command.
- **Transactional Simplicity**: Monetary updates across orders and billing utilize standard local database transactions without distributed saga failures.
- **Low Operational Cost**: Runs on 2 AWS ECS Fargate container instances behind an Application Load Balancer with an Aurora PostgreSQL primary and read-replica.

### Negative Consequences
- **Shared Failure Blast Radius**: A fatal memory leak or CPU spike in the Inventory module can crash the entire container process, temporarily impacting Billing.
- **Unified Deployment Cadence**: Deploying a bug fix to the Billing module requires deploying the single combined container artifact (mitigated by automated blue-green zero-downtime deployment pipelines).

### Mitigations
- Enforce strict memory limits and thread pool bulkheads inside the application.
- Enforce automated NetArchTest/ArchUnit rules to prevent cross-module coupling.

---

## 7. Compliance & Automated Fitness Functions

The architecture boundary rules are programmatically enforced via continuous integration:

```csharp
[Fact]
public void Modules_Should_Not_Have_Direct_Internal_Dependencies()
{
    var result = Types.InAssembly(typeof(Program).Assembly)
        .That().ResideInNamespace("Enterprise.Modules.Billing")
        .ShouldNot().HaveDependencyOn("Enterprise.Modules.Order.Internal")
        .GetResult();

    Assert.True(result.IsSuccessful, "Billing module directly referenced internal Order classes! Interaction must use IOrderService.");
}
```
