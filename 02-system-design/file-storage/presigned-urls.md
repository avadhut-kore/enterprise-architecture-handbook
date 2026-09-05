# Pre-Signed URLs Architecture

## 1. Bypassing Origin Application Servers
Routing multi-gigabyte video or image uploads through application servers consumes web worker threads, network bandwidth, and memory. **Pre-Signed URLs** enable direct client-to-storage transfers:

```mermaid
sequenceDiagram
    autonumber
    Client->>App: 1. Request Upload Auth (POST /files/auth)
    App->>App: Validate User Session & Storage Quotas
    App->>S3: 2. Sign S3 URL using AWS Secret Key (TTL: 15 mins)
    App-->>Client: 3. Return Pre-Signed URL
    Client->>S3: 4. Direct Upload via PUT to S3 Bucket
    S3-->>Client: HTTP 200 OK
```
