# Event-Driven AI Pipelines & Streaming Inference

## 1. Asynchronous Event-Driven Architecture

In high-throughput enterprise systems, invoking synchronous LLM calls during user transaction paths destroys throughput. Event-driven architectures decouple the ingestion of requests from AI inference.

```mermaid
flowchart LR
    EventProducer["Transactional API"] -->|Publish Event: 'claim.submitted'| KafkaTopic[("Kafka Topic: 'incoming-claims'")]
    
    subgraph ConsumerGroup ["K8s Consumer Pods (HPA Autoscaled on Consumer Lag)"]
        Worker1["AI Processing Worker 1"]
        Worker2["AI Processing Worker 2"]
    end

    KafkaTopic --> ConsumerGroup
    ConsumerGroup --> AIGateway["Enterprise AI Gateway"]
    AIGateway --> LLM["Model Inference"]
    
    ConsumerGroup -->|Publish Result: 'claim.scored'| OutTopic[("Kafka Topic: 'claim-decisions'")]
    ConsumerGroup -.->|On Failure after 3 Retries| DLQ[("Dead Letter Queue (DLQ)")]
```
