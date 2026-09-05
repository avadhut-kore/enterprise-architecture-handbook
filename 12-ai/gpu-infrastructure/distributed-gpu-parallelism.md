# Distributed GPU Parallelism: TP, PP & DP

## 1. Parallelism Taxonomy

When a foundation model exceeds the memory or compute capacity of a single GPU, it must be parallelized across multiple GPUs:

```mermaid
flowchart TD
    subgraph TP ["1. Tensor Parallelism (TP) - Intra-Node"]
        TPDesc["Splits individual matrix multiplications across GPUs within a single node.\nRequires ultra-high bandwidth (NVLink 900 GB/s).\nStandard: TP=8 across 8x H100s."]
    end

    subgraph PP ["2. Pipeline Parallelism (PP) - Inter-Node"]
        PPDesc["Splits layers sequentially across nodes (e.g., Layers 1-40 on Node 1, 41-80 on Node 2).\nCan traverse slower InfiniBand / RoCE networks.\nIntroduces pipeline bubble latency."]
    end

    subgraph DP ["3. Data Parallelism (DP) / Replicas"]
        DPDesc["Replicates the entire model across multiple nodes to scale concurrent user throughput.\nEach replica handles independent user requests."]
    end
```

---

## 2. Production Recommendation
For standard enterprise serving (e.g., Llama-3-70B), deploy **Tensor Parallelism (TP = 8)** inside a single 8-GPU node. Scale out concurrent throughput by deploying multiple independent Data Parallel (DP) replicas behind the AI Gateway load balancer.
