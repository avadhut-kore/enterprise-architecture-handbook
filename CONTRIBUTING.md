# Contribution & Maintenance Guidelines

Even though this repository serves as a personal professional reference, all contributions, updates, and expansions must adhere to strict software engineering and architecture governance standards.

---

## 1. Core Contribution Rules

1. **Depth Over Breadth**: Never create shallow "glossary-style" definitions. Every technical guide must satisfy the [9 Mandatory Inquiries](DOCUMENTATION-STANDARD.md#1-documentation-philosophy) (Problem, When to Use, When Not to Use, Alternatives, Trade-offs, Failure Modes, Operations, Cost, Scalability/Security).
2. **First-Principles Rigor**: Validate all performance claims with empirical numbers (e.g., latency budgets, memory overhead, network RTT) or formal citations.
3. **No Uncommitted Decisions**: Architecture patterns without documented trade-offs are invalid.
4. **Living Artifact Maintenance**: When a technology status changes on the [Technology Radar](TECHNOLOGY-RADAR.md), update all cross-referenced documents.

---

## 2. Document Creation Workflow

When authoring a new document:
1. **Identify the Domain Directory**: Consult [`ARCHITECTURE.md`](ARCHITECTURE.md) and [`INDEX.md`](INDEX.md) to locate the exact numbered directory.
2. **Apply the Standard Schema**: Follow [`DOCUMENTATION-STANDARD.md`](DOCUMENTATION-STANDARD.md).
3. **Include the Document Header**:
   ```markdown
   # Title

   > **Domain**: [e.g., 06-data/sql]  
   > **Status**: [Draft | In-Review | Approved]  
   > **Last Updated**: [YYYY-MM-DD]  
   > **Author**: [Name / Role]
   ```
4. **Audit Against Relevant Checklist**: Before marking as `Approved`, run the document through the corresponding checklist in [`21-architecture-tools/checklists/`](21-architecture-tools/checklists/).

---

## 3. Naming Conventions

* **General Markdown Files**: Strictly use lowercase `kebab-case` (e.g., `distributed-lock-patterns.md`, `cache-stampede-prevention.md`).
* **Root Policies & Primary Deliverable Templates**: Use uppercase `KEBAB-CASE` (e.g., `README.md`, `ADR-TEMPLATE.md`, `SOLUTION-ARCHITECTURE-TEMPLATE.md`).
* **ADR Files**: Save under `16-architecture-deliverables/adr/` using a 4-digit zero-padded index:
  * Format: `ADR-XXXX-[kebab-case-title].md`
  * Example: `ADR-0001-use-postgresql-for-core-ledger.md`
* **Diagram Assets**: When using static image exports alongside Mermaid, place them in `17-diagrams/[subcategory]/` with descriptive `kebab-case` names.

---

## 4. Folder Placement & Domain Boundaries

Ensure documents reside strictly within their primary domain of concern:

| Topic Type | Correct Directory | Incorrect Directory |
| :--- | :--- | :--- |
| Theoretical CAP theorem or Raft consensus | `00-foundations/distributed-systems/` | `02-system-design/` |
| Concrete Kafka Partitioning & Retries | `07-integration/kafka/` | `00-foundations/` |
| End-to-End Retail Platform SAD | `18-reference-architectures/ecommerce/` | `01-architecture/` |
| Practical Go/Rust Benchmark Code Spike | `99-experiments/` | `03-backend/` |
| Architectural Decision for Project X | `16-architecture-deliverables/adr/` | `01-architecture/` |

---

## 5. Diagramming Standards

* **Default to Mermaid**: Use native GitHub-compatible ````mermaid```` code blocks to ensure diagrams are versionable, diffable, and editable as code.
* **Diagram Clarity Guidelines**:
  * For distributed request flows: Use `sequenceDiagram`.
  * For system container and component topologies: Use `flowchart TD` or `flowchart LR` following the C4 Model hierarchy.
  * For state transitions: Use `stateDiagram-v2`.
  * Avoid unreadable spaghetti diagrams; decompose large systems into Level 1 (Context) and Level 2 (Container) views.
* **Node Labels**: Always enclose labels with spaces or punctuation in double quotes (e.g., `id["API Gateway (Envoy)"]`).

---

## 6. Architecture Decision Records (ADRs)

* Every foundational decision that alters architecture boundaries, persistence choices, or integration protocols mandates an ADR.
* Use the official [`ADR-TEMPLATE.md`](16-architecture-deliverables/ADR-TEMPLATE.md).
* Never delete or overwrite an approved ADR. If a decision is superseded, create a new ADR (e.g., `ADR-0012`) and mark the earlier ADR as `Superseded by ADR-0012`.

---

## 7. Code Examples & Experiments

* All code snippets embedded in documentation must be idiomatic, complete, and syntactically valid for modern runtimes (.NET 8+, Java 21+, Python 3.11+, TypeScript 5+).
* Avoid "magic code" or omitted imports where critical for understanding.
* Large runnable proof-of-concept codebases, benchmarks, and load test scripts must be placed in [`99-experiments/`](99-experiments/) with their own runnable execution scripts and READMEs.

---

## 8. Avoiding Content Duplication

* **Single Source of Truth (SSOT)**: If a concept is comprehensively explained in `00-foundations/`, reference it via a relative Markdown link rather than copy-pasting the explanation into `13-architecture-patterns/` or `18-reference-architectures/`.
* **Cross-Referencing**:
  * Correct: *"For deep mechanics on distributed consensus, see [Consensus Internals](../../00-foundations/distributed-systems/consensus.md)."*
  * Incorrect: Duplicating three pages of Raft algorithm mechanics inside a database guide.

---

## 9. Content Currency & Periodic Audit

* **Quarterly Radar Audit**: The [Technology Radar](TECHNOLOGY-RADAR.md) must be audited and updated every quarter.
* **Deprecation Policy**: When a pattern or library is obsoleted, update its metadata status to `Deprecated`, document the replacement, and provide a clear migration recommendation.
* **Link Validation**: Run automated link checks to ensure all relative links between documents, checklists, and templates remain healthy.
