# MLOps Architecture & Machine Learning Delivery

MLOps bridges machine learning data science with automated DevOps engineering, treating data, model weights, and code as co-dependent versioned artifacts.

## 1. The Machine Learning CI/CD/CT Lifecycle

```
[Feature Store (Feast / Hopsworks)] ──► Real-Time Feature Ingestion
                                                  │
                                                  ▼
[Data Versioning (DVC / LakeFS)] ───────► Continuous Training (CT) Pipeline
                                                  │
                                                  ▼
[Model Training & Hyperparameter Tuning] ──► Distributed GPU Nodes
                                                  │
                                                  ▼
[Model Registry (MLflow / W&B)] ────────► Cryptographic Model Weights Artifact
                                                  │
                                                  ▼
[Model Evaluation Gate (Accuracy, Bias)] ──► Passes Minimum F1-Score
                                                  │
                                                  ▼
[Model Serving (Triton / TorchServe / vLLM)] ──► Real-Time Inference Gateway
                                                  │
                                                  ▼
[Data & Concept Drift Monitoring (Evidently)] ──► Triggers Automated Retraining
```

## 2. Core Architectural Principles
- **Data Version Control**: You cannot reproduce an ML model without reproducing the exact snapshot of training data that produced it.
- **Model Registry as Artifact Store**: Treat trained model weights (`.safetensors`, `.onnx`) as immutable OCI artifacts in enterprise registries.

## Related Resources
- [AI Platform Architecture](../../12-ai/README.md)
- [AIOps Architecture](../aiops/README.md)
