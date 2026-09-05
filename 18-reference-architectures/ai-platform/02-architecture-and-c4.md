# C4 Architecture Model & Cloud Mapping: Enterprise AI Platform

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
title System Context: Enterprise AI Platform
Person(worker, "Enterprise User", "Interacts via Web, Mobile, or Slack")
System(ai_platform, "Enterprise AI Platform", "Centralized GenAI Gateway, RAG Engine, and GPU Serving Fabric")
System_Ext(idp, "Corporate IdP", "Okta / Azure AD for OIDC Authentication")
System_Ext(data_sources, "Enterprise Repositories", "SharePoint, Confluence, Salesforce, S3")
System_Ext(cloud_llm, "External Frontier Models", "OpenAI, Anthropic, Google Vertex")

Rel(worker, ai_platform, "Submits queries & prompt requests", "HTTPS / WSS")
Rel(ai_platform, idp, "Validates user tokens & scopes", "OAuth 2.0")
Rel(ai_platform, data_sources, "Ingests documents & syncs ACLs", "REST / Webhooks")
Rel(ai_platform, cloud_llm, "Routes sanctioned, anonymized prompts", "mTLS REST")
```

---

## 2. C4 Level 2: Container Diagram

```mermaid
C4Container
title Container Diagram: Enterprise AI Platform
Container(gateway, "AI Gateway", "Go / Envoy", "Enforces rate limiting, prompt firewall, and dynamic routing")
Container(cache, "Semantic Cache", "Redis Stack", "Stores exact match & vector cosine embeddings of prompt/responses")
Container(rag_engine, "RAG Orchestrator", "Python / FastAPI", "Executes hybrid retrieval, reranking, and context synthesis")
Container(vector_db, "Vector Database", "Qdrant Cluster", "HNSW indexed dense vector embeddings + metadata payload")
Container(gpu_cluster, "Self-Hosted Model Fabric", "vLLM on Kubernetes", "Serves open-source models (Llama 3, Mistral) on Nvidia GPUs")
Container(ingestion, "Ingestion Worker", "Celery / Ray", "Extracts, chunks, embeds, and indexes documents asynchronously")

Rel(gateway, cache, "Checks query embedding similarity", "RESP")
Rel(gateway, rag_engine, "Forwards complex contextual queries", "gRPC")
Rel(gateway, gpu_cluster, "Direct inference for standard prompts", "HTTP/2")
Rel(rag_engine, vector_db, "Retrieves top-K chunks", "gRPC")
Rel(ingestion, vector_db, "Upserts document vectors", "gRPC")
```

---

## 3. Technology-Neutral to Cloud Provider Mapping

| Component | Technology-Neutral | AWS Implementation | Azure Implementation | GCP Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **AI Gateway** | Envoy / Kong / LiteLLM | Amazon ECS / EKS | Azure Container Apps | Cloud Run / GKE |
| **GPU Inference** | vLLM / TensorRT-LLM | EKS (G5 / P4de Instances) | AKS (NCv3 / NDv4 Instances) | GKE (G2 / A3 Instances) |
| **Vector Database**| Qdrant / Milvus | Amazon OpenSearch / Qdrant Cloud| Azure AI Search / Qdrant | Vertex AI Vector Search |
| **Document Storage**| Object Storage | Amazon S3 | Azure Blob Storage | Google Cloud Storage |
| **Message Queue** | Apache Kafka | Amazon MSK | Azure Event Hubs | Google Cloud Pub/Sub |
| **Cache & KV** | Redis Cluster | Amazon ElastiCache | Azure Cache for Redis | Cloud Memorystore |
