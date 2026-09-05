# Attention Mechanisms & Memory Scaling (MHA, GQA & FlashAttention)

## 1. The Attention Bottleneck: $O(N^2)$ Complexity

Standard Multi-Head Attention (MHA) computes attention scores between every pair of tokens in a sequence:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
For a sequence of length $N$, computing $QK^T$ requires $O(N^2)$ computational operations and $O(N^2)$ memory storage. For long context windows ($N \ge 32\text{k}$), naive attention completely exhausts GPU memory.

---

## 2. Memory-Optimized Attention Topologies

```mermaid
flowchart TD
    subgraph MHA ["1. Multi-Head Attention (MHA)"]
        direction LR
        Q1["Q Heads (e.g., 32)"] --- K1["K Heads (32)"] --- V1["V Heads (32)"]
        Note1["1:1 Ratio. Highest KV Cache memory consumption."]
    end

    subgraph GQA ["2. Grouped-Query Attention (GQA) - Production Standard"]
        direction LR
        Q2["Q Heads (e.g., 32)"] ---> K2["K Groups (8)"] & V2["V Groups (8)"]
        Note2["Queries share KV heads. 75% reduction in KV Cache memory!"]
    end

    subgraph MQA ["3. Multi-Query Attention (MQA)"]
        direction LR
        Q3["Q Heads (e.g., 32)"] ---> K3["Single K Head (1)"] & V3["Single V Head (1)"]
        Note3["Extreme memory savings, slight accuracy penalty."]
    end
```

### 2.3 FlashAttention (IO-Aware Exact Attention)
* Traditional PyTorch attention writes intermediate $N \times N$ attention matrices to slow GPU High-Bandwidth Memory (HBM).
* **FlashAttention** tiles attention computation into blocks that fit entirely within ultra-fast on-chip SRAM cache ($19\text{ TB/s}$ bandwidth), computing softmax incrementally without ever writing the massive $N \times N$ matrix to HBM.
* **Result**: $3\times - 5\times$ speedup with exact mathematical parity.
