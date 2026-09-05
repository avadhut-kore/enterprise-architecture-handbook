# Quantization Architectures: AWQ, GPTQ & FP8

## 1. The Quantization Landscape

Quantization compresses model weight representations from 16-bit floating-point (FP16) down to 8-bit or 4-bit integers.

| Format | Bits per Weight | Typical Serving Framework | Perplexity Loss | Hardware Acceleration |
| :--- | :---: | :--- | :--- | :--- |
| **FP8 (E4M3 / E5M2)**| 8 bits | vLLM, TensorRT-LLM | **Zero (< 0.05%)** | Native in NVIDIA Hopper (H100) & Ada Lovelace. |
| **AWQ (Activation-Aware)**| 4 bits | vLLM, TGI | Minimal (< 0.5%) | Optimized INT4 tensor kernels. |
| **GPTQ (One-Shot Post-Training)**| 4 bits | AutoGPTQ, vLLM | Low (< 1.0%) | Highly optimized for consumer/older GPUs. |

---

## 2. Why Activation-Aware Quantization (AWQ) Outperforms Naive INT4
Naive quantization rounds all weights uniformly, severely distorting the 1% of weights ("salient weights") that correspond to large activation outliers. **AWQ** identifies which weights protect output perplexity and preserves them at higher numerical precision while aggressively quantizing the remaining 99% of weights.
