# Foundation Models Architecture & Capabilities

## 1. The Foundation Model Paradigm

A **Foundation Model** is a large-scale neural network trained on vast, broad unstructured data at scale (typically using self-supervised learning) that can be adapted to a wide range of downstream tasks without task-specific architectural redesign.

```mermaid
flowchart TD
    RawData["Broad Uncurated Data\n(Internet Text, Books, Code, Papers)"] --> Pretrain["Self-Supervised Pretraining\n(Next-Token Prediction on Thousands of GPUs)"]
    Pretrain --> BaseFM["Base Foundation Model\n(High World Knowledge, Unaligned Autocompleter)"]
    
    BaseFM --> Align["Post-Training Alignment\n(SFT + RLHF / DPO + KTO)"]
    Align --> InstructFM["Instruct / Chat Foundation Model\n(Safe, Helpful, Conversational Assistant)"]
    
    InstructFM --> T1["Downstream: Enterprise RAG"]
    InstructFM --> T2["Downstream: Code Refactoring"]
    InstructFM --> T3["Downstream: Autonomous Agents"]
    InstructFM --> T4["Downstream: Structured Extraction"]
```

---

## 2. Empirical Scaling Laws (Chinchilla & Kaplan)
Architects must understand compute scaling laws to forecast model efficiency:
* **Compute-Optimal Training (Chinchilla Law)**: For optimal performance, model parameter count and training dataset token count must be scaled in equal proportion. For every doubling of model parameters, training tokens must also double.
* **Inference Efficiency**: A smaller model trained on more tokens (e.g., Llama-3-8B trained on 15T tokens) often outperforms older, larger models (e.g., Llama-1-65B trained on 1.4T tokens) while requiring $8\times$ less GPU VRAM during production serving.
