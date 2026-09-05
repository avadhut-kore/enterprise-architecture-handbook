# Enterprise AI Architecture Anti-Patterns (`ai-anti-patterns/`)

## Executive Summary

This directory documents 22 lethal architecture anti-patterns observed in enterprise generative AI and agent deployments. Each anti-pattern is analyzed across:
* **Architectural Symptoms**: How to recognize the anti-pattern in production.
* **Root Causes**: The flawed assumptions or hype that created it.
* **Catastrophic Impact**: Cost runaway, data breaches, hallucinations, or system crashes.
* **Refactoring Path**: Concrete, step-by-step architectural remedy to restore enterprise resilience.

---

## Anti-Pattern Catalog

* **[AI for Everything Anti-Pattern](ai-for-everything.md)** — Attempting to solve classical deterministic software problems using expensive, non-deterministic LLMs instead of simple code or rules engines.
* **[Agent for Deterministic Workflows Anti-Pattern](agent-for-deterministic-workflows.md)** — Replacing predictable business state machines with autonomous agents that fail intermittently and burn tokens.
* **[RAG Without Access Control Anti-Pattern](rag-without-access-control.md)** — Indexing enterprise documents into a shared vector database without tenant metadata filtering, causing massive cross-tenant data leaks.
* **[Vector Database by Default Anti-Pattern](vector-database-by-default.md)** — Provisioning a dedicated vector database cluster before evaluating existing relational (pgvector) or search engines.
* **[Huge Unbounded Prompts Anti-Pattern](huge-unbounded-prompts.md)** — Dumping hundreds of pages of uncompressed context into a prompt, triggering attention dilution ('lost in the middle') and 10x cost inflation.
* **[No Automated Evaluation Anti-Pattern](no-automated-evaluation.md)** — Relying on manual 'vibe checks' to evaluate AI features, ensuring that prompt or model updates silently degrade production output.
* **[No Prompt Versioning Anti-Pattern](no-prompt-versioning.md)** — Hardcoding prompt strings in application code without semantic versioning, Git tracking, or CI/CD regression gates.
* **[No Model Versioning Anti-Pattern](no-model-versioning.md)** — Calling unpinned model aliases (e.g., 'gpt-4o' instead of 'gpt-4o-2024-08-06'), causing silent breaking changes when providers update weights.
* **[No Cost Controls Anti-Pattern](no-cost-controls.md)** — Deploying generative AI features without token rate limiters, semantic caching, or budgetary fences, resulting in surprise $50,000 monthly invoices.
* **[No Output Validation Anti-Pattern](no-output-validation.md)** — Passing raw LLM string completions directly to downstream databases, frontend browsers, or APIs without JSON Schema validation.
* **[Unrestricted Tool Access Anti-Pattern](unrestricted-tool-access.md)** — Granting AI agents unrestricted write/delete permissions across production databases and APIs without scoped RBAC/ABAC.
* **[Autonomous Financial Transactions Anti-Pattern](autonomous-financial-transactions.md)** — Allowing AI agents to execute funds transfers, credit adjustments, or contract signatures without mandatory human sign-off.
* **[Logging Sensitive Prompts Anti-Pattern](logging-sensitive-prompts.md)** — Logging unredacted user prompts containing passwords, SSNs, and credit cards directly into centralized observability APMs.
* **[Treating LLM as Trusted Entity Anti-Pattern](treating-llm-as-trusted.md)** — Positioning foundation models inside internal security boundaries and assuming their outputs are free from malicious injection.
* **[No Human Approval for High-Risk Actions Anti-Pattern](no-human-approval-high-risk.md)** — Automating irreversible, high-consequence business actions without human-in-the-loop pause-and-resume escalation gates.
* **[Multi-Agent Complexity Without Value Anti-Pattern](multi-agent-complexity-without-value.md)** — Deploying complex multi-agent frameworks with chatty peer choreography when a single well-prompted model accomplishes the task.
* **[Fine-Tuning When RAG is Sufficient Anti-Pattern](fine-tuning-when-rag-sufficient.md)** — Spending months fine-tuning a model to 'memorize' enterprise facts that change weekly, instead of using a dynamic RAG pipeline.
* **[RAG When Structured Query is Sufficient Anti-Pattern](rag-when-structured-query-sufficient.md)** — Attempting to vectorize relational database tables to answer aggregate financial questions ('total Q3 revenue') instead of executing SQL.
* **[Self-Hosting Without Economic Justification Anti-Pattern](self-hosting-without-economic-justification.md)** — Spending $500,000 on dedicated GPU clusters for low-volume workloads (< 10M tokens/day) that cost $50/month on cloud APIs.
* **[Vendor Abstraction Without Portability Anti-Pattern](vendor-abstraction-without-portability.md)** — Building an elaborate internal abstraction layer while coupling prompt formats to a single proprietary vendor's unique tool syntax.
* **[AI Gateway as a Bottleneck Anti-Pattern](ai-gateway-bottleneck.md)** — Buffering full streaming token responses inside a centralized gateway, destroying user perceived latency (TTFT).
* **[Treating LLM as Deterministic Software Anti-Pattern](treating-llm-as-deterministic.md)** — Assuming an identical prompt will always yield identical outputs, leading to brittle unit test suites and unhandled edge-case failures.
