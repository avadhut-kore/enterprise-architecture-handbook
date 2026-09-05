# Golden Paths: Paved Roads for Enterprise Engineering

## Executive Summary

A **Golden Path (Paved Road)** is an opinionated, well-supported, and pre-approved path to building and deploying software inside the enterprise.

---

## 1. Paved Road vs Escape Hatch

```mermaid
graph TD
    Choice[Developer Starting New Service] --> Path{Follow Golden Path?}
    Path -->|Yes: Standard Node.js / Java REST API| Paved[Paved Road: Pre-Configured CI/CD, Zero-Approval Security, Instant Deployment]
    Path -->|No: Custom C++ Engine / Exotic Protocol| OffRoad[Escape Hatch: Team Assumes 100% Operational & Compliance Burden]
```

---

## 2. The Golden Path Invariant
- **Voluntary Adoption**: The platform team must never force teams to use the Golden Path via corporate mandates. The Golden Path must be so superior, frictionless, and reliable that developers actively prefer it.
