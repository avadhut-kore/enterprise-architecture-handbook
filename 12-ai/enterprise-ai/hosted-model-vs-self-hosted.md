# Hosted Cloud Model APIs vs. Self-Hosted AI Architecture

## 1. The Financial Break-Even Analysis

A fundamental architectural question is: **At what scale does self-hosting open-weights models on dedicated GPU clusters become cheaper than consuming cloud APIs (e.g., Azure OpenAI / AWS Bedrock)?**

```mermaid
xychart-beta
    title Monthly Cost: Cloud Model API vs Self-Hosted GPU Cluster (8x H100)
    x-axis ["5M Tokens/day", "20M Tokens/day", "50M Tokens/day", "100M Tokens/day", "250M Tokens/day"]
    y-axis "Monthly Spend ($ USD)" 0 --> 120000
    line [3750, 15000, 37500, 75000, 187500]
    line [22000, 22000, 22000, 22000, 44000]
```

---

## 2. Decision Rubric

| Decision Dimension | Hosted Cloud API (Azure OpenAI / Bedrock) | Self-Hosted Cluster (Private K8s + vLLM) |
| :--- | :--- | :--- |
| **Token Volume Threshold** | **$< 50\text{M}$ tokens/day**: Cloud APIs are substantially cheaper (pay-as-you-go). | **$> 100\text{M}$ tokens/day**: Dedicated GPU clusters achieve $60\% - 80\%$ lower unit cost. |
| **Operational Staffing** | Zero GPU SRE staff required. | Requires 2–3 senior Kubernetes GPU/MLOps engineers. |
| **Time-to-Market** | Immediate (minutes via API key). | 2 to 6 months (hardware procurement, cluster setup). |
| **Data Sovereignty** | Governed by vendor contracts & cloud regions. | **Absolute air-gapped on-premise control**. |
| **Custom Weight Control** | None (black-box model weights). | Complete (custom architectures, deep fine-tuning). |
