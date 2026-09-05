# Operational Architecture Patterns (`operational-patterns/`)

## Executive Summary

This directory documents core operational architecture patterns that ensure system stability, automated resilience, and rapid recovery under stress.

---

## Pattern Index
- **Circuit Breaker Pattern**: Isolates failing dependencies to prevent cascading thread exhaustion.
- **Bulkhead Pattern**: Partitions connection pools and memory to prevent localized failure from spreading.
- **Progressive Delivery (Canary)**: Shifts small percentages of traffic to new releases with automated metric verification.
- **Multi-Window Multi-Burn-Rate Alerting**: Pages on-call engineers based on consumption rate of Error Budgets.
- **Expand-Contract Database Migrations**: Decouples database schema migrations into backward-compatible phases.
- **Autonomous Self-Healing**: Automated node replacement, pod rescheduling, and connection pool recycling.
