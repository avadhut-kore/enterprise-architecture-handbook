# Architecture Artifact Generators

## 1. Overview
The `generators/` directory contains lightweight, portable Python CLI utilities designed to scaffold standardized enterprise architecture deliverables, ensuring strict compliance with [`DOCUMENTATION-STANDARD.md`](../../DOCUMENTATION-STANDARD.md).

All tools are written using Python 3 standard library modules only, with zero external dependencies.

---

## 2. Available Generators

### 2.1. Architecture Decision Record (ADR) Generator
Generates a structured, production-grade ADR file with sequential numbering, Mermaid sequence diagrams, trade-off matrices, and validation fitness functions.

* **Script**: [`adr_generator.py`](adr_generator.py)
* **Usage**:
  ```bash
  python adr_generator.py --title "Adopt Kafka for Order Ingestion" --author "Enterprise Architect" --status ACCEPTED --out-dir ./adrs
  ```
* **Parameters**:
  * `--title`: Decision title (Required).
  * `--author`: Lead architect / decision owner (Default: `"Solution Architect"`).
  * `--status`: `PROPOSED`, `ACCEPTED`, `SUPERSEDED`, `REJECTED` (Default: `ACCEPTED`).
  * `--problem`: Context and problem statement.
  * `--throughput`: Expected transactions per second.
  * `--out-dir`: Destination folder (Default: `.`).

---

### 2.2. Non-Functional Requirements (NFR) Matrix Generator
Scaffolds measurable quality attribute tables (Performance, Availability, RTO/RPO, Security, FinOps) mapped to enterprise criticality tiers.

* **Script**: [`nfr_matrix_generator.py`](nfr_matrix_generator.py)
* **Usage**:
  ```bash
  python nfr_matrix_generator.py --system-name "Checkout Core Service" --tier Tier-1 --out-file checkout-nfr.md
  ```
* **Parameters**:
  * `--system-name`: Name of service or capability (Required).
  * `--tier`: `Tier-1` (Mission-critical), `Tier-2` (Standard enterprise), `Tier-3` (Internal non-critical).
  * `--out-file`: Output markdown filepath.

---

## 3. Related Modules
* [21-architecture-tools/templates/](../templates/README.md) — Raw Markdown architecture templates.
* [21-architecture-tools/linters/](../linters/README.md) — Automated quality and link linters.
* [16-architecture-deliverables/](../../16-architecture-deliverables/) — Architecture deliverables guide.
