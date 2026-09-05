# Transformer Architecture for Systems Architects

## 1. The Decoder-Only Dominance

While early transformer architectures (e.g., original Vaswani et al., T5) utilized an Encoder-Decoder structure, modern generative foundation models (GPT-4, Llama, Claude, Mistral) have converged almost universally on **Decoder-Only Autoregressive Architectures**.

```mermaid
flowchart TD
    InputText["Input Tokens: ['Enterprise', 'Architecture']"] --> Embed["Token Embedding + RoPE Positional Encoding"]
    Embed --> Block1["Transformer Block 1\n- RMSNorm\n- Grouped-Query Attention (GQA)\n- Residual Connection\n- SwiGLU Feed-Forward Network (FFN)\n- Residual Connection"]
    Block1 --> BlockN["Transformer Block N (e.g., 32 to 80 layers deep)"]
    BlockN --> FinalNorm["Final RMSNorm"]
    FinalNorm --> Unembed["Unembedding Projection Head (Linear Layer)"]
    Unembed --> Logits["Next-Token Logits across Vocabulary (Size ~ 128k)"]
    Logits --> Softmax["Softmax -> Probability Distribution"]
```

---

## 2. Key Architectural Invariants
* **Causal Masking**: Ensures token $t$ can only attend to previous tokens $1 \dots t-1$, preventing the model from seeing future tokens during autoregressive decoding.
* **Rotary Position Embedding (RoPE)**: Encodes relative position between tokens geometrically via complex rotation matrices, enabling extrapolation to long context windows (128k+ tokens) without catastrophic degradation.
