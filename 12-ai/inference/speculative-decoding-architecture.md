# Speculative Decoding Architecture

## 1. The Core Insight: Verification is Faster than Generation

In autoregressive generation, generating 5 tokens requires 5 serial, memory-bound forward passes through a large model. However, **verifying** 5 candidate tokens requires only **1 single parallel forward pass**.

**Speculative Decoding** uses a tiny, ultra-fast "Draft Model" to speculate candidate tokens, which are verified in parallel by the large "Target Model".

```mermaid
sequenceDiagram
    autonumber
    participant Draft as Draft Model (Llama-3-8B / 100 tps)
    participant Target as Target Model (Llama-3-70B / 20 tps)

    Note over Draft: Draft model rapidly generates 4 speculative tokens:<br/>["Enterprise", "architecture", "requires", "discipline"]
    Draft->>Target: Pass 4 candidate tokens in a single forward pass
    Note over Target: Target model evaluates all 4 tokens in PARALLEL.<br/>Accepts tokens 1, 2, and 3; corrects token 4 to "rigor".
    Target-->>Draft: Accepted 3 tokens + 1 new generated token = 4 tokens total!
    Note over Target: Achieved 4 tokens in the time of 1 target forward pass!
```

---

## 2. Performance Impact
Speculative decoding achieves a **$2.0\times - 2.8\times$ wall-clock speedup** for large models with **100% mathematical equivalence** to running the large model alone (zero accuracy degradation).
