# Distributed Design Principle: Single Responsibility Principle (SRP)

## 1. Principle Definition at Architectural Scale

Originally articulated by Robert C. Martin for object-oriented design, the Single Responsibility Principle at the distributed systems level states:

> **A microservice should have only one reason to change, driven by a single business stakeholder or domain boundary.**

---

## 2. Sizing Microservices via SRP

A microservice is not defined by lines of code; it is defined by its responsibility boundary:
- A service that manages user authentication, issues invoices, and schedules marketing emails violates SRP.
- When multiple business stakeholders (Marketing, Accounting, Security) all request changes to the same microservice, that service must be decomposed.

---

## 3. Practical Guardrails

- **One Bounded Context per Service**: Avoid creating nano-services (e.g., a service that only capitalizes strings). The unit of responsibility should align with a discrete domain capability.
