# Hallucination Mitigation Architecture

## 1. The Causes of Hallucination

Large Language Models are probabilistic token generators; they optimize for fluency and plausibility, not factual truth. Models hallucinate when:
* Prompt instructions conflict with pretraining data.
* Retrieved RAG context is noisy or incomplete.
* The model is forced to answer questions outside its knowledge boundary without an explicit permission to say *"I do not know"*.

---

## 2. The 4-Pillar Mitigation Architecture

```mermaid
flowchart TD
    Prompt["Inbound Question"] --> Grounding["1. RAG Grounding\nStrict instruction: 'Answer ONLY using provided text. If missing, say: I do not know.'"]
    Grounding --> Temp["2. Temperature Pinning\nSet Temperature = 0.0 for strict deterministic extraction"]
    Temp --> CoV["3. Chain-of-Verification (CoV)\nModel generates 3 verification questions against its own draft"]
    CoV --> Citation["4. Citation Enforcement\nEvery factual assertion must cite exact [Document ID, Paragraph #]"]
    Citation --> FinalAnswer["Grounded, Hallucination-Minimized Response"]
```
