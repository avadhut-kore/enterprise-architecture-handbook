# Large Language Model (LLM) Architecture (`llm/`)

## Executive Summary

Understanding the internal architecture of Large Language Models is essential for making defensible architectural trade-offs regarding context window sizing, latency optimization, and memory provisioning.

This module details transformer mechanics, multi-head attention dynamics, the post-training alignment pipeline, and specialized reasoning models from a systems architecture perspective.

---

## Directory Catalog

* **[Transformer Architecture for Architects](transformer-architecture-for-architects.md)** — Decoder-only architectures, token embedding layers, residual connections, and forward pass mechanics.
* **[Attention Mechanisms & Context Dynamics](attention-mechanisms.md)** — Multi-Head Attention (MHA), Multi-Query Attention (MQA), Grouped-Query Attention (GQA), and FlashAttention.
* **[Pretraining, Fine-Tuning & Alignment (RLHF/DPO)](pretraining-fine-tuning-rlhf-dpo.md)** — The training continuum: pretraining, continued pretraining, SFT, RLHF, DPO, and LoRA adapters.
* **[Reasoning Models Architecture](reasoning-models-architecture.md)** — Test-time compute scaling, chain-of-thought tokens, and the economics of deep reasoning (OpenAI o1, DeepSeek-R1).
* **[Tokens & Tokenization Internals](tokens-and-tokenization.md)** — Byte-Pair Encoding (BPE), vocabulary sizes, token-to-word ratios, and multilingual serialization overheads.
