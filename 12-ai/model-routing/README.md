# Dynamic Model Routing Architecture (`model-routing/`)

## Executive Summary

Routing every user request to a single monolithic foundation model creates severe cost, availability, and latency vulnerabilities.

**Dynamic Model Routing** treats foundation models as interchangeable execution backends, directing each inbound request to the most cost-effective, lowest-latency, and highest-availability model capable of satisfying the specific task contract.

---

## Directory Catalog

* **[Model Routing Decision Framework](model-routing-decision-framework.md)** — Decision matrices and selection rubrics across task complexity, latency SLAs, and cost budgets.
* **[Cascade & Fallback Routing](cascade-and-fallback-routing.md)** — Speculative cascades, circuit breaking, and multi-provider failover topologies.
* **[Task Complexity Classifiers](task-complexity-classifiers.md)** — Classifying prompt intent via lightweight BERT models, embedding clustering, and heuristic regex.
