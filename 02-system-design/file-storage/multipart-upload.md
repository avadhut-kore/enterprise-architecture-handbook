# Multipart Upload Architecture

## 1. Parallel Chunked Upload Protocol
Multipart upload slices large files into discrete chunks ($5\text{ MB}$ to $5\text{ GB}$ per part) uploaded concurrently in parallel:

```mermaid
sequenceDiagram
    autonumber
    Client->>S3: 1. InitiateMultipartUpload
    S3-->>Client: UploadID: abc123xyz
    
    par Parallel Chunk Uploads
        Client->>S3: UploadPart (Part 1, 10MB) -> ETag: e1
        Client->>S3: UploadPart (Part 2, 10MB) -> ETag: e2
        Client->>S3: UploadPart (Part 3, 10MB) -> ETag: e3
    end
    
    Client->>S3: 2. CompleteMultipartUpload (UploadID, Parts: [e1, e2, e3])
    S3->>S3: Reassembles Parts into Single Unified Object
    S3-->>Client: Upload Complete HTTP 200 OK
```

* If Part 2 fails due to a network glitch, **only Part 2 is retried**; Parts 1 and 3 are preserved!
