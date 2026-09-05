# Mathematical Foundations for Enterprise AI Architects

## 1. Executive Summary

Architects do not write gradient descent backpropagation code, but they must calculate:
* **Vector space distances** to configure vector search engines.
* **VRAM memory consumption** to provision GPU nodes.
* **Quantization precision trade-offs** to balance latency, cost, and perplexity.

---

## 2. High-Dimensional Vector Spaces & Distance Metrics

Embeddings map unstructured text, audio, or images into vectors in $\mathbb{R}^d$ (typically $d \in [384, 1536, 3072]$). Measuring similarity between vectors $u$ and $v$ dictates retrieval accuracy:

### 2.1 Cosine Similarity
$$\text{Cosine}(u, v) = \frac{u \cdot v}{\|u\|_2 \|v\|_2} = \frac{\sum_{i=1}^d u_i v_i}{\sqrt{\sum_{i=1}^d u_i^2} \sqrt{\sum_{i=1}^d v_i^2}}$$
* **Properties**: Measures the angle between vectors, ignoring magnitude. Range $[-1, 1]$.
* **Architectural Use**: Standard for text embeddings where document length variations should not distort semantic relevance.

### 2.2 Dot Product (Inner Product)
$$\text{Dot}(u, v) = u \cdot v = \sum_{i=1}^d u_i v_i$$
* **Properties**: Computationally faster than cosine similarity. Equivalent to cosine similarity **if and only if vectors are normalized to unit length ($\|u\|_2 = 1$)**.
* **Architectural Guidance**: Pre-normalize embeddings during ingestion to allow high-throughput dot-product SIMD instructions in vector search engines.

### 2.3 Euclidean Distance ($L_2$ Norm)
$$d_{L_2}(u, v) = \sqrt{\sum_{i=1}^d (u_i - v_i)^2}$$
* **Properties**: Measures physical distance in geometric space. Range $[0, \infty)$.
* **Architectural Use**: Clustering, image feature embeddings, and anomaly detection.

---

## 3. Numerical Precision & Quantization Formats

Foundation model weights are stored in floating-point representations. Lowering precision dramatically reduces VRAM footprint and bandwidth bottlenecks:

| Format | Bits per Weight | Relative Memory | Typical Use Case | Perplexity Impact |
| :--- | :---: | :---: | :--- | :--- |
| **FP32** | 32 bits | $1.0\times$ (Baseline) | Initial model pretraining and gradient updates. | Zero |
| **BF16 / FP16**| 16 bits | $0.5\times$ | Standard enterprise production inference baseline. | Negligible ($< 0.1\%$) |
| **INT8** | 8 bits | $0.25\times$ | Quantized serving (e.g., bitsandbytes, AWQ). | Minimal ($< 0.5\%$) |
| **FP8** | 8 bits | $0.25\times$ | Native NVIDIA Hopper (H100) / Blackwell serving. | Near zero |
| **INT4 (AWQ/GPTQ)** | 4 bits | $0.125\times$ | Extreme edge serving, local developer workstations. | Minor degradation ($1-3\%$) |

### VRAM Estimation Rule of Thumb:
$$\text{VRAM}_{\text{weights}} \approx \text{Parameters (Billions)} \times \text{Bytes per Parameter} \times 1.2 \text{ (Overhead)}$$
* Example: A 70B parameter model in 16-bit (2 bytes) requires: $70 \times 2 \times 1.2 \approx 168\text{ GB VRAM}$ (minimum $2\times 80\text{GB H100}$ GPUs).
* In 4-bit (0.5 bytes): $70 \times 0.5 \times 1.2 \approx 42\text{ GB VRAM}$ (fits comfortably on a single $80\text{GB H100}$).
