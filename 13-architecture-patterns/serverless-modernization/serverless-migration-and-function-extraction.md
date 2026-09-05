# Serverless Migration & Function Extraction

## 1. When Serverless Excels vs. When it Fails

| Dimension | Ideal for Serverless | Anti-Pattern for Serverless |
| :--- | :--- | :--- |
| **Traffic Profile** | Spiky, unpredictable, sporadic (scales to zero). | Sustained 24/7 high-volume baseline traffic. |
| **Execution Duration**| Sub-second to 30 seconds. | Long-running background compute (> 15 minutes). |
| **Statefulness** | Completely stateless; external DB connections. | In-memory local session state; heavy local disks. |
| **Operational Goal** | Zero infrastructure management overhead. | Ultra-low predictable P99 latency (< 5ms). |
