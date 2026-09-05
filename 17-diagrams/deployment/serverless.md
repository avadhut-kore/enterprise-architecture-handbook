# Serverless Event-Driven Deployment Topology

Illustrates an autonomous, zero-server deployment leveraging managed cloud functions, event buses, and distributed NoSQL databases.

```mermaid
flowchart TD
    subgraph Ingress["Client Ingress"]
        ClientApp["Mobile / Web Single Page App"]
        CloudFront["CloudFront CDN Edge"]
        APIGateway["Amazon API Gateway (HTTP APIs)"]
    end

    subgraph Compute["Event-Driven Serverless Compute"]
        AuthFn["Auth Authorizer
[AWS Lambda (Node.js 20)]"]
        OrderFn["Create Order Function
[AWS Lambda (ARM64 / Rust)]"]
        ProcessFn["Payment Processor
[AWS Lambda (Python 3.12)]"]
    end

    subgraph EventMesh["Event Bus & Decoupling"]
        EventBridge["Amazon EventBridge Event Bus"]
        SQS["Payment Retry Dead-Letter Queue"]
    end

    subgraph Storage["Managed Serverless Persistence"]
        DynamoDB[("Amazon DynamoDB
[On-Demand Capacity / Global Tables]")]
        S3Bucket[("Amazon S3 Receipt Bucket
[Encrypted SSE-KMS]")]
    end

    ClientApp --> CloudFront --> APIGateway
    APIGateway -->|Validate Token| AuthFn
    APIGateway -->|Invoke Route| OrderFn

    OrderFn -->|ACID Single-Table PutItem| DynamoDB
    OrderFn -->|Publish OrderPlaced| EventBridge

    EventBridge -->|Filter Rule: OrderPlaced| ProcessFn
    ProcessFn -->|Process Charge| DynamoDB
    ProcessFn -->|Store Invoice PDF| S3Bucket
    ProcessFn -.->|On Failure (3x)| SQS
```
