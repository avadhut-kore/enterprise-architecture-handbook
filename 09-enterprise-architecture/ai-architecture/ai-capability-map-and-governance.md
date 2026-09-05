# AI Capability Map & Enterprise Governance

How Enterprise Architects establish the AI Control Plane to prevent data leakage, model hallucinations, and runaway API costs.

---

## 1. The Enterprise AI Control Plane Architecture

```mermaid
flowchart LR
    App["Enterprise Apps & Squads"] --> Gateway["Enterprise AI Gateway<br/>(Central Model Router & Policy Enforcer)"]
    Gateway --> Guard["Guardrail Engine<br/>(PII Scrubbing, Prompt Injection Filter)"]
    Gateway --> Cache["Semantic Cache<br/>(35% Cost Reduction)"]
    Gateway --> Router["Model Router<br/>(Cheap SLM vs Frontier LLM)"]
    Router --> CloudModel["Commercial Hosted Models (OpenAI, Bedrock, Vertex)"]
    Router --> SelfModel["Self-Hosted Private Models (vLLM on Private K8s)"]
    Gateway --> Obs["AI Telemetry & Token Cost Allocation"]
```

---

## 2. EU AI Act Compliance Scorecard
Every AI use case deployed in the enterprise must be evaluated against the regulatory risk tiers:
* **Unacceptable Risk**: Real-time biometric surveillance, cognitive behavioral manipulation $	o$ **Prohibited**.
* **High Risk**: Credit scoring, CV hiring triage, medical diagnostic support $	o$ **Mandatory human-in-the-loop, bias audits, continuous logging**.
* **Limited / Minimal Risk**: Customer support summarization, code generation copilots $	o$ **Transparency notice required**.
