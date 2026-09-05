# OpenTelemetry GenAI Semantic Conventions Architecture

## 1. Standardizing Distributed AI Traces

To avoid vendor lock-in across proprietary AI monitoring tools, systems must instrument tracing using standard **OpenTelemetry (OTel) Semantic Conventions for Generative AI**:

```mermaid
flowchart TD
    RootSpan["Span: 'chat /v1/completions' (Trace ID: 4bf92f3577...)"] --> ChildSpan1["Child Span: 'retrieval.vector_search'\n- db.system: 'qdrant'\n- gen_ai.retrieval.top_k: 5"]
    RootSpan --> ChildSpan2["Child Span: 'gen_ai.client.chat'\n- gen_ai.system: 'openai'\n- gen_ai.request.model: 'gpt-4o'\n- gen_ai.usage.input_tokens: 1420\n- gen_ai.usage.output_tokens: 382\n- gen_ai.response.finish_reasons: ['stop']"]
    RootSpan --> ChildSpan3["Child Span: 'tool.execution'\n- gen_ai.tool.name: 'get_account_balance'"]
```

---

## 2. Standardized OTel Attributes
* `gen_ai.system`: Identifier of the provider (`openai`, `anthropic`, `vertex_ai`, `vllm`).
* `gen_ai.request.model`: The specific model version requested.
* `gen_ai.usage.input_tokens`: Exact integer count of prompt tokens.
* `gen_ai.usage.output_tokens`: Exact integer count of completion tokens.
* `gen_ai.server.time_to_first_token`: Microseconds elapsed before first token emission.
