# Structured Outputs & JSON Mode Architecture

## 1. The Critical Flaw of Prompt-Based JSON

Instructing an LLM via prompt text (`"Please respond in valid JSON matching this schema..."`) is inherently unreliable. Under temperature variations, models frequently hallucinate markdown backticks (` ```json `), include preamble text (`"Here is your JSON:"`), or produce trailing commas that crash downstream JSON parsers (`JSON.parse()`).

Enterprise architectures must mandate **Guaranteed Structured Outputs via Constrained Decoding**.

```mermaid
flowchart TD
    Schema["Strict JSON Schema\n(Pydantic / Zod / JSONSchema)"] --> Grammar["Convert Schema to Context-Free Grammar (CFG) / FSM"]
    
    subgraph SamplingLoop ["Autoregressive Sampling Loop"]
        Logits["Raw Model Next-Token Logits (Vocabulary ~ 128k tokens)"] --> Masker["Grammar Logit Masker\n(Sets probability of illegal tokens to -Infinity)"]
        Grammar --> Masker
        Masker --> FilteredLogits["Filtered Valid Logits Only\n(e.g., only '\"' or '{' allowed next)"]
        FilteredLogits --> Sample["Sample Next Token"]
    end

    Sample --> Out["100% Mathematically Guaranteed Valid JSON Output"]
```

---

## 2. Invariants for Production JSON Generation
1. **Never Parse Unconstrained Strings**: Always use constrained grammar engines (e.g., Outlines, Guidance, OpenAI Structured Outputs, vLLM Guided Decoding).
2. **Schema Rejection at Boundary**: If a model fails to satisfy the schema or times out, reject the payload at the AI Gateway before it touches internal message buses or databases.
