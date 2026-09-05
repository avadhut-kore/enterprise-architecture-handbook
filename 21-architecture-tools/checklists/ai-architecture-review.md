# AI Architecture Review Checklist

## Executive Summary

Mandatory review checklist for the enterprise Architecture Review Board (ARB) evaluating any proposal introducing Artificial Intelligence, Machine Learning, Large Language Models, or Autonomous Agents.

---

## 1. Business Context & Suitability
- [ ] Has the problem been evaluated against the [AI Suitability Framework](../../12-ai/decision-frameworks/ai-suitability-framework.md)?
- [ ] Has a deterministic software or rules engine alternative been formally evaluated and rejected?
- [ ] Is the expected business value $\ge 10\times$ the estimated monthly AI operating cost?
- [ ] What is the organization's tolerance for non-deterministic errors or hallucinations?

## 2. Data & Knowledge Governance
- [ ] Are all data sources classified by sensitivity tier (Public, Internal, Confidential, Restricted)?
- [ ] Is multi-tenant access control enforced at the database query layer via mandatory metadata pre-filtering?
- [ ] Is personal identifiable information (PII) masked before sending prompts to external model providers?
- [ ] Is there an automated pipeline to handle document deletions and GDPR Article 17 Right-to-be-Forgotten requests?

## 3. Model & Modality Selection
- [ ] Is the parameter size justified (e.g., why an 8B Small Language Model cannot fulfill the task)?
- [ ] Are model endpoints configured behind a centralized [Enterprise AI Gateway](../../12-ai/ai-systems-architecture/ai-gateway.md)?
- [ ] Are commercial cloud vendor contracts verified for **Zero Data Retention (ZDR)** and zero model retraining?
- [ ] Are model version aliases pinned to exact immutable versions (e.g., `gpt-4o-2024-08-06`)?

## 4. Security & Guardrails
- [ ] Have STRIDE threats for AI been modeled (direct injection, indirect injection, data leakage, tool abuse)?
- [ ] Are user inputs encapsulated in structural delimiters (XML tags with random nonces)?
- [ ] Are outbound completions validated against strict JSON Schemas using constrained decoding or grammar masks?
- [ ] Are canary tokens embedded in system instructions to detect system prompt exfiltration?

## 5. Operations, SRE & Observability
- [ ] Are distributed traces instrumented conforming to OpenTelemetry GenAI Semantic Conventions?
- [ ] Are SRE multi-window burn-rate alerts configured on token budgets and error rates?
- [ ] Is the P99 Time-to-First-Token (TTFT) SLA $< 800\text{ms}$ on interactive streaming endpoints?
- [ ] Is an automated fallback cascade configured to failover to secondary cloud providers within 150ms on 429/503 errors?

## 6. Continuous Evaluation & Testing
- [ ] Does a version-controlled Golden Dataset ($\ge 200$ test cases) exist in Git?
- [ ] Are automated evaluation gates (RAG Triad: Faithfulness $\ge 0.95$, Relevance $\ge 0.88$) integrated into CI/CD?
- [ ] Is human-in-the-loop sign-off required for high-risk autonomous transactions?
