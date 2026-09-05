# LLM Application Engineering Architecture (`llm-applications/`)

## Executive Summary

Designing enterprise applications powered by LLMs requires moving beyond simple prompt-in/text-out wrappers. 

This module establishes the architectural patterns governing conversation state machines, streaming token delivery (SSE), optimistic user interfaces, and latency masking techniques.

---

## Directory Catalog

* **[LLM Application Design Patterns](llm-application-design-patterns.md)** — Architectural topologies: Copilots, Assistants, Synthesizers, and Embedders.
* **[State Management & Session Architecture](state-management-and-sessions.md)** — Managing conversational history, context window pruning, and Redis session stores.
* **[Streaming Tokens Architecture](streaming-tokens-architecture.md)** — Server-Sent Events (SSE), chunked HTTP/2 transfer encoding, and stream backpressure.
* **[Latency Masking Techniques](latency-masking-techniques.md)** — Optimistic rendering, step-by-step progress tickers, and skeleton streaming.
