# AI & LLM Security Architecture (`ai-security/`)

## Executive Summary

Generative AI and Large Language Models introduce fundamentally novel threat vectors that bypass classical network perimeters, API firewalls, and WAFs. Attackers do not need to exploit memory buffer overflows or SQL injection syntax; they can hijack system control simply by providing **cleverly phrased natural language prompts**.

This module establishes the comprehensive security architecture required to protect enterprise LLM applications, agent runtimes, and RAG knowledge bases.

---

## Directory Catalog

* **[OWASP Top 10 for LLM Applications](owasp-top-10-for-llms.md)** — Architectural analysis and enterprise mitigations for all 10 OWASP LLM vulnerabilities.
* **[Prompt Injection & Jailbreak Defense](prompt-injection-and-jailbreak-defense.md)** — Direct prompt injection, jailbreaking techniques, and multi-tier perimeter defenses.
* **[Indirect Prompt Injection & RAG Poisoning](indirect-prompt-injection-and-rag-poisoning.md)** — Poisoned web/PDF documents, delimiter escape, and secondary data injection.
* **[Sensitive Data Disclosure & Exfiltration](sensitive-data-disclosure-and-exfiltration.md)** — Preventing models from leaking proprietary intellectual property or PII in completions.
* **[AI Threat Modeling Framework](ai-threat-modeling-framework.md)** — Adapting STRIDE and attack trees specifically for foundation models and agentic workflows.
* **[AI Guardrails Subsystem](guardrails/)** — Dedicated guardrail architecture, framework comparisons (NeMo, Llama Guard), and egress canary tokens.
