# Infrastructure as Code & GPU Node Fleet Management

## 1. Kubernetes GPU Pool Architecture (AWS EKS Example)
- **Node Group**: AWS `g5.12xlarge` (4x Nvidia A10G 24GB GPUs) with Karpenter autoscaling based on queue latency.
- **Serving Engine**: vLLM deployed with continuous batching and PagedAttention to maximize GPU memory utilization.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-llama3-serving
  namespace: ai-platform
spec:
  replicas: 4
  template:
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:v0.5.0
        args: ["--model", "meta-llama/Meta-Llama-3-70B-Instruct", "--tensor-parallel-size", "4", "--max-model-len", "8192"]
        resources:
          limits:
            nvidia.com/gpu: "4"
            memory: "128Gi"
        ports:
        - containerPort: 8000
```
