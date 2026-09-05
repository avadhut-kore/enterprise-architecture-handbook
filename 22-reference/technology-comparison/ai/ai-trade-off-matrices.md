# Comprehensive AI & Modern Architecture Trade-Off Matrices

## 1. AI vs. Traditional Software Engineering

| Dimension | Traditional Software | AI / Machine Learning |
| :--- | :--- | :--- |
| **Logic Formulation** | Human writes rules/algorithms explicitly. | Model infers statistical relationships from training data. |
| **Determinism** | 100% deterministic; reproducible state. | Probabilistic; non-deterministic sampling. |
| **Failure Mode** | Clear exception stack trace; reproducible bugs. | Hallucination; plausible falsehoods; silent degradation. |
| **Maintenance Cost** | Low to medium code refactoring. | Ongoing data curation, evaluation drift, model updates. |

---

## 2. RAG vs. Fine-Tuning

| Dimension | Retrieval-Augmented Generation (RAG) | Model Fine-Tuning (SFT / LoRA) |
| :--- | :--- | :--- |
| **Primary Goal** | Knowledge injection; accessing dynamic facts. | Style, tone, domain syntax, and schema adherence. |
| **Data Freshness** | Instantaneous (update vector index via CDC). | Static (requires complete retraining pass). |
| **Hallucination Control** | High (grounded with verifiable citations). | Low (model can still hallucinate memorized facts). |
| **Compute Cost** | High per-query retrieval; low offline cost. | High upfront GPU compute; lower inference prompt tokens. |

---

## 3. Autonomous Agents vs. Deterministic Workflows

| Dimension | Deterministic Workflow (Temporal) | Autonomous Agent (ReAct) |
| :--- | :--- | :--- |
| **Execution Path** | Fully pre-defined DAG or state machine. | Dynamically chosen at runtime by foundation model. |
| **Reliability** | 99.999% predictable. | 80% – 90% variable reliability. |
| **Debugging** | Exact deterministic state history replay. | Probabilistic reasoning trace inspection. |
| **Token Cost** | Negligible (CPU cycles only). | High (recursive multi-turn tool loops). |

---

## 4. Centralized Cloud AI vs. Edge AI Inference

| Dimension | Centralized Cloud AI (Hyperscalers) | Edge AI Inference (Wasm / WebGPU) |
| :--- | :--- | :--- |
| **Model Capacity** | 70B to 405B+ parameter frontier models. | 1B to 3B parameter quantized SLMs. |
| **Latency SLA** | 500ms – 3,000ms (network + queue). | **Sub-50ms (zero network transit)**. |
| **Data Privacy** | Cloud provider trust & ZDR compliance. | **Absolute local device privacy (zero egress)**. |
| **Compute Cost** | Billed per token (OpEx). | Client device hardware (Zero server cost). |
