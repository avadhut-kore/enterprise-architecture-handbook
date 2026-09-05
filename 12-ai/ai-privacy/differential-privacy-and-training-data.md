# Differential Privacy & Training Data Protection

## 1. The Model Memorization Hazard

Neural networks have been proven capable of **verbatim memorization** of rare training records (e.g., extracting social security numbers or private credit card numbers simply by prompting the model with prefix strings).

When fine-tuning models on proprietary enterprise datasets, architects must enforce **Differentially Private Stochastic Gradient Descent (DP-SGD)**.

```mermaid
flowchart LR
    Batch["Batch of Private Training Records"] --> Gradients["Compute Per-Sample Gradients"]
    Gradients --> Clip["Gradient Clipping (Bounds sensitivity)"]
    Clip --> Noise["Inject Calibrated Gaussian Noise (ε, δ Privacy Budget)"]
    Noise --> Update["Update Model Weights"]
    Update --> Guarantees["Mathematical Guarantee: Model output cannot reveal whether any individual record was in training set"]
```
