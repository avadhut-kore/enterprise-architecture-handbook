# Distance Metrics & Similarity Calculations

## 1. Comparing Geometric Metrics

| Metric | Mathematical Formula | Range | When to Use | Computational Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Cosine Similarity** | $\frac{u \cdot v}{\|u\|_2 \|v\|_2}$ | $[-1, 1]$ | Text embeddings with variable chunk lengths. | Medium (Requires normalization). |
| **Dot Product** | $\sum_{i=1}^d u_i v_i$ | $(-\infty, \infty)$ | Normalized vectors ($\|u\| = 1$). | **Fastest** (Single hardware SIMD pass). |
| **Euclidean ($L_2$)** | $\sqrt{\sum (u_i - v_i)^2}$ | $[0, \infty)$ | Image embeddings, physical spatial data. | Slow (Square root computation). |

---

## 2. Invariant: Vector Normalization
Always pre-normalize embedding vectors to unit length ($\|u\|_2 = 1.0$) during the offline ingestion pipeline. When vectors are pre-normalized, **Cosine Similarity is mathematically identical to Dot Product**, allowing search engines to execute blazing-fast dot product instructions without on-the-fly normalization.
