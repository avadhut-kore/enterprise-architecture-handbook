# Architecture Documentation Linters

## 1. Overview
The `linters/` directory provides automated static analysis tooling for Markdown-based architecture documentation, preventing broken relative links, malformed Mermaid diagrams, and syntax regressions.

---

## 2. Available Linters

### 2.1. Documentation & Link Linter
Audits Markdown files for:
* **Broken Relative Links**: Resolves relative file links against the local filesystem.
* **Syntax Corruptions**: Detects broken LaTeX artifacts (such as truncated LaTeX arrow sequences).
* **Unbalanced Code Blocks**: Detects unclosed code fences or broken Mermaid diagram blocks.
* **Architectural Completeness** (`--strict`): Confirms required architectural headings (Overview, Architecture, Trade-offs, Checklist) are present.

* **Script**: [`doc_linter.py`](doc_linter.py)
* **Usage**:
  ```bash
  # Scan a directory
  python doc_linter.py --target-dir 01-architecture

  # Scan a single file with strict heading checks
  python doc_linter.py --file 01-architecture/ai-architecture/README.md --strict
  ```

---

## 3. Related Modules
* [21-architecture-tools/generators/](../generators/README.md) — Automated ADR and NFR artifact generators.
* [DOCUMENTATION-STANDARD.md](../../DOCUMENTATION-STANDARD.md) — Universal repository documentation standard.
