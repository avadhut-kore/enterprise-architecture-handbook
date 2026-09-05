# Integration Architecture: Enterprise Connectors & Streaming

## 1. Asynchronous Ingestion & Event Mesh
Enterprise document updates (SharePoint file saved, Salesforce case closed, Confluence page edited) stream into Kafka topics (`enterprise.documents.raw`):
- Celery / Ray workers consume file events, download artifacts over mTLS, process chunks, and upsert vectors.
- Complete document deletion events trigger immediate vector payload purges by `doc_id` within 5 seconds to comply with GDPR right-to-be-forgotten.

---

## 2. Server-Sent Events (SSE) Protocol
Real-time streaming inference uses HTTP/2 SSE:
```http
POST /v1/chat/completions HTTP/2
Host: ai.enterprise.internal
Content-Type: application/json
Accept: text/event-stream

data: {"id":"chat-101","choices":[{"delta":{"content":"Based"}}]}
data: {"id":"chat-101","choices":[{"delta":{"content":" on your"}}]}
data: {"id":"chat-101","choices":[{"delta":{"content":" policy..."}}]}
data: [DONE]
```
