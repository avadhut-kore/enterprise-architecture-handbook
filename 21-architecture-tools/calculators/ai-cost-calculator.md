# Enterprise AI Cost & Sizing Calculator

## Executive Summary

Quantitative mathematical formulas and sizing models for forecasting Generative AI token expenditures, vector database memory footprints, and self-hosted GPU infrastructure requirements.

---

## 1. Token Expenditure Forecasting Formula

$$\text{Monthly Cost} = \text{Requests/Day} \times 30 \times \left[ (T_{\text{in}} \times P_{\text{in}}) + (T_{\text{out}} \times P_{\text{out}}) \right] \times (1 - C_{\text{hit}})$$

Where:
* $T_{\text{in}}$ = Average input tokens per request (System Prompt + Retrieved Chunks + User Query).
* $T_{\text{out}}$ = Average output tokens per response.
* $P_{\text{in}}$ = Provider price per input token ($USD).
* $P_{\text{out}}$ = Provider price per output token ($USD).
* $C_{\text{hit}}$ = Semantic cache hit ratio ($0.0$ to $0.60$).

### Example: High-Volume Customer Support Portal
* Volume: $100,000\text{ requests/day}$
* $T_{\text{in}} = 1,200\text{ tokens}$, $T_{\text{out}} = 300\text{ tokens}$
* Model: GPT-4o-mini ($P_{\text{in}} = \$0.15/\text{M}$, $P_{\text{out}} = \$0.60/\text{M}$)
* Semantic Cache Hit Rate: $35\%$ ($C_{\text{hit}} = 0.35$)
$$\text{Cost/Request} = (1,200 \times 0.00000015) + (300 \times 0.00000060) = \$0.00018 + \$0.00018 = \$0.00036$$
$$\text{Net Daily Cost} = 100,000 \times \$0.00036 \times (1 - 0.35) = \$23.40 / \text{day} \implies \mathbf{\$702 / \text{month}}$$

---

## 2. Vector Database RAM Sizing Formula

$$\text{RAM}_{\text{Total}} = N_{\text{vectors}} \times \left( d \times 4\text{ bytes} \right) \times 1.5\text{ (HNSW graph overhead)} \times 1.2\text{ (OS/Buffer headroom)}$$

### Example: 10 Million Vectors ($d = 1536$)
$$\text{Raw Vectors} = 10,000,000 \times 1,536 \times 4\text{ bytes} \approx 61.44\text{ GB}$$
$$\text{Total RAM Required} = 61.44\text{ GB} \times 1.5 \times 1.2 \approx \mathbf{110.6\text{ GB RAM}}$$

---

## 3. GPU VRAM Sizing Formula for Model Serving

$$\text{VRAM}_{\text{Total}} = \left( \text{Params (Billions)} \times \text{Bytes/Param} \right) + \left( \text{Concurrency} \times \text{Context Tokens} \times \text{Bytes/Token} \right) + 2\text{ GB Overhead}$$
