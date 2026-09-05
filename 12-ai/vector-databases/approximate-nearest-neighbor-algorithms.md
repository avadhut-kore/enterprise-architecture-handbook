# Approximate Nearest Neighbor (ANN) Algorithms: HNSW vs. IVF

## 1. The $O(N)$ Exact Search Bottleneck

Finding the exact nearest neighbor to a query vector requires computing distance against every single vector in the database (Flat Search):
$$\text{Complexity} = O(N \times d)$$
Across 10,000,000 vectors, exact search takes seconds and is completely unusable for interactive applications. **Approximate Nearest Neighbor (ANN)** algorithms trade a minute fraction of recall accuracy ($< 1\%$) for a **1,000x latency reduction**.

---

## 2. HNSW vs. IVF-PQ

```mermaid
flowchart TD
    subgraph HNSW ["1. Hierarchical Navigable Small World (HNSW)"]
        L3["Layer 2 (Long-range sparse expressway links)"]
        L2["Layer 1 (Medium-range regional links)"]
        L1["Layer 0 (Dense nearest neighbor graph)"]
        L3 --> L2 --> L1
        Note1["Pros: Blazing fast sub-5ms queries, highest recall (> 99%).\nCons: High memory usage (graph pointers require 1.5x vector size)."]
    end

    subgraph IVFPQ ["2. Inverted File Index with Product Quantization (IVF-PQ)"]
        Centroids["Voronoi Centroid Cells (e.g., 4096 clusters)"]
        Quantize["Quantize vectors into compressed 8-bit codes (PQ)"]
        Centroids --> Quantize
        Note2["Pros: Extremely low memory (compresses vectors by 90%).\nCons: Lower recall (90-95%), slower query speeds, requires training."]
    end
```

### Architectural Recommendation
Use **HNSW** for systems with $< 10\text{M}$ vectors where query speed and maximum accuracy are critical. Use **IVF-PQ** or scalar-quantized HNSW (SQ-HNSW) when scaling to tens of millions of vectors under strict RAM budgets.
