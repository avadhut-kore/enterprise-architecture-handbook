# Machine Learning Architecture & MLOps (`ml-architecture/`)

## Executive Summary

While Generative AI captures modern attention, **classical predictive and discriminative machine learning powers mission-critical enterprise workloads**: credit underwriting, real-time fraud detection, algorithmic trading, supply chain forecasting, and predictive maintenance.

This module details the end-to-end MLOps architecture required to train, version, deploy, serve, and monitor predictive models with high determinism and sub-50ms latency.

---

## Directory Catalog

* **[ML Pipeline Lifecycle](ml-pipeline-lifecycle.md)** — Architectural stages from data ingestion and feature engineering to continuous retraining.
* **[Feature Engineering & Feature Stores](feature-engineering-and-feature-stores.md)** — Online vs. offline feature stores (Feast, Hopsworks), point-in-time correctness, and feature consistency.
* **[Model Registry & Versioning](model-registry-and-versioning.md)** — Governance, cryptographic artifact hashing, lineage, and deployment staging gates.
* **[Real-Time vs. Batch Inference](realtime-vs-batch-inference.md)** — Architectural trade-offs between low-latency streaming inference and high-throughput batch scoring.
* **[Data & Concept Drift Monitoring](data-and-concept-drift-monitoring.md)** — Detecting covariate shift, prior probability shift, and concept drift in production.
