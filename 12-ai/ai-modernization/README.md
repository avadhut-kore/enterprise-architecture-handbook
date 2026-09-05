# AI-Assisted Legacy Modernization Architecture (`ai-modernization/`)

## Executive Summary

Generative AI offers powerful capabilities for analyzing, refactoring, and migrating legacy software systems (COBOL, mainframe RPG, legacy Java/C++, stored procedures). 

However, architects must enforce strict human-in-the-loop validation: **AI-generated code is an untrusted draft, never production-ready software without verification**.

---

## Directory Catalog

* **[AI-Assisted Legacy Modernization](ai-assisted-legacy-modernization.md)** — Architectural methodology: code discovery, dependency extraction, refactoring, and test generation.
* **[Code Refactoring & Synthetic Test Generation](code-refactoring-and-test-generation.md)** — Generating characterization tests from legacy behavior before refactoring.
* **[AI Modernization Guardrails & Pitfalls](ai-modernization-guardrails-and-pitfalls.md)** — Lethal failure modes: subtle numerical bugs, hallucinated APIs, and lost business rules.
