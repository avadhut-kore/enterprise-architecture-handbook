# AI Memory Systems Architecture (`ai-memory/`)

## Executive Summary

Foundation models are inherently stateless: every API call starts from a clean slate. Enabling conversational continuity, personalized user experiences, and long-running agent tasks requires an external **AI Memory Architecture**.

This module details short-term working memory, long-term episodic/semantic user memory, memory poisoning attack surfaces, and GDPR right-to-be-forgotten compliance.

---

## Directory Catalog

* **[Short-Term vs. Long-Term Memory](short-term-vs-long-term-memory.md)** — Architectural trade-offs: context buffer memory, summarization memory, and vector-backed episodic memory.
* **[Episodic & Semantic User Memory](episodic-and-semantic-user-memory.md)** — Extracting user preferences, factual profiles, and past session summaries.
* **[Memory Poisoning & Security Perimeters](memory-poisoning-and-security.md)** — Preventing attackers from injecting persistent malicious instructions into long-term agent memory.
* **[Memory Privacy & GDPR Erasure Compliance](memory-privacy-and-gdpr-erasure.md)** — Cryptographic shredding, tenant isolation, and right-to-be-forgotten data deletion.
