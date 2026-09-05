# Task Complexity Classifiers & Intent Recognition

## 1. The Architecture of Routing Classifiers

To route requests dynamically without adding unacceptable latency, the **Classifier** must execute in **$< 15\text{ms}$**. Invoking a secondary LLM to decide which LLM to route to is an architectural anti-pattern that doubles latency.

```mermaid
flowchart LR
    Prompt["Inbound Prompt"] --> FastCheck["1. Heuristic Regex & Rule Matcher (1ms)"]
    FastCheck -->|No Match| EmbeddingClassifier["2. Small Embedding + Linear Classifier (8ms)"]
    EmbeddingClassifier --> Score["Output: Complexity Score [0.0 - 1.0]"]
    
    Score --> RoutingTable{"Score Threshold"}
    RoutingTable -->|< 0.40| SLM["Route to SLM (Fast Extractive)"]
    RoutingTable -->|0.40 - 0.80| General["Route to General Model"]
    RoutingTable -->|> 0.80| Frontier["Route to Reasoning Model"]
```

---

## 2. Classifier Implementations
* **Regex / Heuristic Matching (1ms)**: Detects structured commands, keywords, or short prompts ($< 15\text{ words}$) that are known simple queries.
* **Logistic Regression over Embeddings (8ms)**: Computes a fast embedding (e.g., `text-embedding-3-small` or local ONNX MiniLM) and runs a single matrix multiplication against pre-trained logistic regression weights to classify complexity.
