# AI Production Readiness Checklist

## Executive Summary

Production gate checklist verifying that an AI application or platform component is hardened, compliant, observed, and ready for customer-facing traffic.

---

## Pre-Flight Readiness Criteria

### 1. Security & Compliance
- [ ] **Guardrails Active**: Both inbound prompt injection and outbound secret/PII filters are active in production config.
- [ ] **Tenant Isolation Verified**: Automated tests confirm zero cross-tenant retrieval leakage in shared vector spaces.
- [ ] **ZDR Confirmed**: Cloud provider enterprise subscription confirms Zero Data Retention is active.
- [ ] **Risk Classification**: The system is registered in the enterprise AI inventory with an EU AI Act risk tier.

### 2. SRE & Resilience
- [ ] **Circuit Breakers Configured**: Upstream LLM timeouts are capped at 10 seconds with automated fallback.
- [ ] **Streaming Proxy Unbuffered**: Nginx/ALB ingress is configured with `X-Accel-Buffering: no` for smooth SSE token streaming.
- [ ] **Rate Limiting**: Distributed Tokens-Per-Minute (TPM) limits are active per tenant in Redis.
- [ ] **Runbooks Published**: Operational runbooks exist for LLM provider outages, high token burn, and hallucination containment.

### 3. Evaluation & Quality
- [ ] **Baseline Benchmark Passed**: The candidate prompt/model release scored $\ge 95\%$ on the Golden Dataset.
- [ ] **Adversarial Fuzzing Passed**: Automated red-teaming verified that jailbreak probes fail to bypass guardrails.

### 4. FinOps & Cost Controls
- [ ] **Hard Budget Caps**: Monthly token expenditure caps are configured in the AI Gateway.
- [ ] **Semantic Cache Active**: Semantic caching in Redis is enabled with similarity threshold $\ge 0.96$.
- [ ] **Cost Center Tagging**: Every outbound request attaches the calling application and department cost center.
