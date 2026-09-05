# AI & Modern Architecture Interview & Review Playbook

## Executive Summary

A comprehensive architectural playbook designed for conducting enterprise Architecture Review Board (ARB) hearings, technical design reviews, and Solution Architect qualification interviews on AI-enabled and AI-native systems.

---

## Core Scenarios & Architectural Challenges

### Scenario 1: The Runaway Token Bill
* **Challenge**: A team launches a RAG feature on a flagship model; monthly cloud API bills exceed $80,000 with low business return.
* **Architectural Remedy**: Introduce dynamic model routing (SLMs for 70% of traffic), semantic caching in Redis, context window compression (LLMLingua), and department-level token quotas.

### Scenario 2: Cross-Tenant Data Leakage in Vector DB
* **Challenge**: A customer searches for HR policies and retrieves another tenant's confidential salary data.
* **Architectural Remedy**: Replace post-retrieval filtering with gateway-injected metadata pre-filtering (`metadata.tenant_id == user.tenant_id`) and isolated vector namespaces.

### Scenario 3: The Hallucinating Financial Copilot
* **Challenge**: An internal banking assistant hallucinates incorrect interest rates in customer letters.
* **Architectural Remedy**: Pin temperature to 0.0, implement strict Parent-Child chunking, mandate citation validation, and require human-in-the-loop Maker-Checker sign-off.
