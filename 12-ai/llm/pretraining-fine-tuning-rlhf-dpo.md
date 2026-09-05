# Pretraining, Fine-Tuning & Alignment (RLHF / DPO)

## 1. The 3-Tier Post-Training Pipeline

Deploying an LLM involves three progressive training tiers:

```mermaid
flowchart TD
    Stage1["1. Unsupervised Pretraining\n- Massive web/code corpus (15 Trillion tokens)\n- Millions of GPU hours ($10M - $100M)\n- Produces: Base Foundation Model"]
    --> Stage2["2. Supervised Fine-Tuning (SFT)\n- Curated high-quality instruction prompt-response pairs\n- Teaches model to act as a conversational assistant\n- Produces: Instruct Model"]
    --> Stage3["3. Preference Alignment (RLHF / DPO)\n- Pairs of model completions ranked by human or AI preference\n- Direct Preference Optimization (DPO) aligns safety and helpfulness\n- Produces: Production-Ready Aligned Model"]
```

---

## 2. Architectural Decision: Fine-Tuning vs. RAG

A frequent architectural anti-pattern is attempting to "teach" an LLM new private enterprise facts via fine-tuning. 
* **Fine-Tuning is for Style, Format, and Tone**: Teach a model domain-specific syntax, specialized output schemas, or conversational voice.
* **RAG is for Knowledge, Facts, and Dynamic Data**: Inject real-time account balances, internal product documentation, and tenant-scoped records.
* **Rule**: *Never fine-tune a model to memorize facts that change frequently.*
