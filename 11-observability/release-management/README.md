# Release Management & Progressive Delivery (`release-management/`)

## Executive Summary

Release management decouples deployment (getting code onto servers) from release (exposing features to users) using progressive delivery, feature flags, and database backward compatibility.

---

## Key Guides in this Directory

| Guide | Scope | Core Focus |
| :--- | :--- | :--- |
| [`progressive-delivery-and-canaries.md`](progressive-delivery-and-canaries.md) | Canary Releases | Automated metric analysis (Argo Rollouts / Flagger) |
| [`database-schema-backward-compatibility.md`](database-schema-backward-compatibility.md) | Database Safety | Expand-Contract pattern for zero-downtime DB migrations |
