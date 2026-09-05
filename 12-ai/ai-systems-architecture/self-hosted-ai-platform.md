# Self-Hosted AI Platform Architecture

## 1. Executive Summary & When to Self-Host

While public cloud foundation model APIs (Azure OpenAI, AWS Bedrock, Google Vertex AI) offer rapid time-to-market, global enterprises with **extreme data residency mandates, air-gapped defense networks, high sustained query volumes (> 100M tokens/day), or strict cost-per-token ceilings** must architect a private, self-hosted AI platform.

```mermaid
flowchart TD
    subgraph Ingress ["Internal Corporate Network (VPC / On-Prem)"]
        InternalApps["Internal Banking / Core Systems"] --> LoadBalancer["Internal Envoy / Istio Ingress"]
    end

    subgraph K8sCluster ["Private Kubernetes GPU Cluster (Air-Gapped)"]
        LoadBalancer --> RouterPod["AI Gateway & Router Pods"]
        
        subgraph GPUWorker1 ["Node 1: 8x NVIDIA H100 (80GB SXM5)"]
            vLLM1["vLLM Serving Instance\n(Llama-3-70B-Instruct-FP8)\nTensor Parallelism = 8"]
        end

        subgraph GPUWorker2 ["Node 2: 8x NVIDIA H100 (80GB SXM5)"]
            vLLM2["vLLM Serving Instance\n(Mistral-Large-FP8)\nTensor Parallelism = 8"]
        end

        RouterPod --> vLLM1
        RouterPod --> vLLM2
    end

    subgraph StorageBacking ["High-Performance Shared Storage"]
        NVMeNFS[("Parallel File System (Ceph / Lustre / PureStorage)\nLoads 70B Model Weights in < 15 seconds")]
        NVMeNFS -.-> GPUWorker1
        NVMeNFS -.-> GPUWorker2
    end
```

---

## 2. Infrastructure Sizing & Hardware Realities

### 2.1 Tensor Parallelism Across GPUs
For a 70B parameter model in FP16 (requiring $\sim 140\text{GB}$ VRAM for weights plus $40\text{GB}$ for KV cache), the model cannot fit on a single GPU. It must be split across multiple GPUs using **Tensor Parallelism (TP)**:
* Standard configuration: $8\times 80\text{GB H100}$ interconnected via high-speed **NVLink** ($900\text{GB/s}$ bidirectional bandwidth).
* **Warning**: Never attempt Tensor Parallelism across standard PCIe slots or separate nodes without InfiniBand interconnects; the inter-GPU communication latency will destroy generation throughput.

### 2.2 Fast Model Weight Loading
Standard Docker images should not bundle 140GB model weights. Kubernetes pods should mount high-speed shared NVMe storage (NFS/Ceph) or use memory-mapped files (`mmap`) to initialize and scale inference pods in seconds rather than downloading multi-gigabyte files across the network.
