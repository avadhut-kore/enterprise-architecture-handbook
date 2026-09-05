# AI Guardrails & Defensive Runtimes (`guardrails/`)

## Executive Summary

Guardrails are deterministic and neural safety verification filters placed around foundation models to inspect inputs before inference and validate completions before client delivery.

---

## Directory Catalog

* **[Input & Output Guardrails Architecture](input-and-output-guardrails.md)** — Pre-inference sanitization, post-inference schema enforcement, and content safety filters.
* **[Guardrail Frameworks Comparison](guardrail-frameworks-comparison.md)** — Comparing NeMo Guardrails, Llama Guard 3, Guardrails AI, and Azure AI Content Safety.
* **[Canary Tokens & Egress Monitoring](canary-tokens-and-egress-monitoring.md)** — Detecting system prompt exfiltration and confidential data leaks using invisible cryptographic tokens.
