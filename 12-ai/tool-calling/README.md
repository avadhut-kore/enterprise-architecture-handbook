# Tool Calling & Model Context Protocol (MCP) Architecture (`tool-calling/`)

## Executive Summary

Foundation models possess no direct access to the physical world or enterprise systems. They interact with environments exclusively by emitting structured tool invocation requests.

This module details tool schema definitions, sandboxed execution perimeters, idempotency safeguards, and the emerging **Model Context Protocol (MCP)** standard for enterprise tool integration.

---

## Directory Catalog

* **[Tool Definitions & JSON Schemas](tool-definition-and-json-schemas.md)** — Crafting unambiguous, strictly typed tool descriptions using JSON Schema.
* **[Sandboxed Execution & Tool Security](sandboxed-execution-and-security.md)** — MicroVMs (Firecracker), container isolation (gVisor), and network egress controls.
* **[Idempotency & Transactional Safety](idempotency-and-transactional-safety.md)** — Preventing duplicate API mutations caused by LLM retries or hallucinated loops.
* **[Model Context Protocol (MCP) & Tool Discovery](mcp-protocol-and-tool-discovery.md)** — Architectural patterns for standardized client-server tool and context exchange.
