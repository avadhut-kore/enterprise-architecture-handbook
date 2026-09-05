# LLM Evaluation and Governance

Enterprise AI systems must be evaluated with continuous, quantitative metrics rather than subjective vibes.

## 1. The RAG Triad Evaluation Framework

1. **Context Relevance**: Does the retrieved context directly address the user query without irrelevant noise?
2. **Groundedness / Faithfulness**: Is the LLM response strictly supported by the retrieved context, or does it hallucinate external information?
3. **Answer Relevance**: Does the final answer directly and accurately resolve the initial user prompt?

## 2. Automated AI CI/CD Fitness Functions
- Integrate tools like Ragas or TruLens into build pipelines. Any prompt update that drops Faithfulness below 0.90 fails the PR automatically.

## Related Modules
- [Architecting Enterprise AI Systems](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/ai-architecture/architecting-enterprise-ai-systems.md)
- [Evolutionary Fitness Functions](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/evolution/fitness-functions-in-practice.md)
