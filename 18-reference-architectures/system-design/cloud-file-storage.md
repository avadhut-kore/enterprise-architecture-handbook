# Reference Architecture: Cloud File & Object Storage (Dropbox / Google Drive)

## 1. System Overview
A massive-scale personal and enterprise cloud storage system providing file synchronization, block-level deduplication, versioning, conflict resolution, and cross-device sync across desktops and mobile devices.

## 2. Business Context
Enables seamless multi-device file access and real-time collaboration for hundreds of millions of users, minimizing bandwidth consumption over cellular and residential networks.

## 3. Functional Requirements
* **File Upload & Download**: Sync arbitrary files up to 50 GB.
* **Block-Level Sync**: Transmit only modified binary chunks rather than re-uploading entire files.
* **File Versioning**: Retain 30-day revision history with rollback capability.
* **Cross-Device Sync**: Push real-time file updates to all connected client devices.

## 4. Non-Functional Requirements
* **Durability**: 11 Nines ($99.999999999\%$) durability.
* **Sync Speed**: Sub-second notification of file modifications to peer devices.
* **Bandwidth Efficiency**: Maximize delta compression and content-addressable deduplication.

## 5. Constraints & Assumptions
* Average file size: 2 MB; large files up to 50 GB.
* 90% of edits modify less than 5% of a file's bytes.

## 6. Scale Estimation
* 50 Million Daily Active Users.
* Daily Sync Actions: 100 Million file updates/day.
* Ingress QPS: $\approx 1,157\text{ syncs/sec}$ average; $5,000\text{ syncs/sec}$ peak.

## 7. Capacity Planning
* Daily Ingest (at 2 MB/file): $100\text{M} \times 2\text{ MB} = \mathbf{200\text{ TB/day}}$.
* Deduplication Savings ($3\times$ reduction): $\approx \mathbf{66.6\text{ TB/day}}$ physical storage.
* 3-Year Physical Storage: $\approx \mathbf{73\text{ PB}}$.

## 8. High-Level Architecture
```mermaid
flowchart TD
    Client[Desktop / Mobile Client] --> SyncAgent[Local Sync Agent]
    SyncAgent -->|1. Chunk & Hash (4MB Chunks)| Client
    SyncAgent -->|2. Check Existing Chunks| MetaAPI[Metadata Service]
    MetaAPI --> MetaDB[(Metadata DB: CockroachDB)]
    
    SyncAgent -->|3. Upload Only Missing Chunks| BlockSvc[Block Storage Service]
    BlockSvc --> S3[(Cloud Object Store: AWS S3)]
    
    MetaAPI --> NotificationSvc[Notification Service: WebSockets]
    NotificationSvc --> PeerClients[Peer Client Devices: Remote Sync]
```

## 9. Component Architecture
* **Chunker**: Slices files into fixed or rolling-hash blocks ($4\text{ MB}$ chunks).
* **Metadata Service**: Manages file namespace, directory hierarchies, permissions, and chunk lists.
* **Block Storage Service**: Content-Addressable Storage (CAS) engine persisting raw binary chunks keyed by SHA-256.
* **Notification Service**: Long-lived WebSockets alerting linked devices to pull file deltas.

## 10. Data Flow
1. User modifies a 1 GB video file (changes 4 MB).
2. Local sync agent chunks file into 250 blocks (4 MB each) and hashes each chunk with SHA-256.
3. Queries Metadata API: "Do you have hashes $H_1 \dots H_{250}$?"
4. Server responds: "Missing only hash $H_{42}$."
5. Client uploads **only $H_{42}$ (4 MB)** $\rightarrow$ Metadata DB updates file manifest $\rightarrow$ Peer devices notified.

## 11. API Design
* `POST /v1/files/check-blocks`
  * Body: `{"block_hashes": ["e3b0c442...", "9f834abc..."]}`
  * Response: `{"missing_hashes": ["9f834abc..."]}`
* `PUT /v1/blocks/{hash}`
  * Headers: `Content-Type: application/octet-stream`

## 12. Data Model
```sql
CREATE TABLE file_versions (
    file_id      UUID NOT NULL,
    version      INTEGER NOT NULL,
    parent_path  TEXT NOT NULL,
    file_name    VARCHAR(255) NOT NULL,
    size_bytes   BIGINT NOT NULL,
    block_hashes TEXT[] NOT NULL, -- Ordered array of SHA-256 hashes
    created_at   TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY (file_id, version)
);
```

## 13. Storage Architecture
Hybrid Architecture: CockroachDB for ACID file namespace and chunk lists; AWS S3 for immutable raw content-addressed 4MB blocks.

## 14. Caching Architecture
Redis Cluster caches block presence lookups and active user WebSocket session routes.

## 15. Messaging & Async Processing
Kafka streams file update events to thumbnail generation workers, search indexing, and malware scanners.

## 16. Scalability Strategy
Content-Addressable Storage (CAS): Identical 4MB blocks uploaded by different users share the same physical S3 object, yielding massive cross-user deduplication.

## 17. Performance Optimization
* **Rolling Checksum (Rabin Fingerprints)**: Shifts chunk boundaries dynamically when bytes are inserted at the beginning of a file, preserving matching chunks.
* **Local Chunk Cache**: Desktop clients cache recently synced blocks locally.

## 18. Reliability & Fault Tolerance
* Zero Data Loss: S3 guarantees 11 nines durability; CockroachDB replicates metadata across 3 Availability Zones.

## 19. Consistency & Transactions
Strong Consistency for Metadata: Prevents two simultaneous client edits from corrupting directory trees. Conflict resolution creates a `"File (Conflicted Copy)"` when concurrent edits collide.

## 20. Security Architecture
* Zero-Knowledge Encryption: Client-side AES-256 encryption before block upload.
* Pre-signed URLs for direct block upload and download.

## 21. Observability Strategy
Metrics: `sync_upload_duration_seconds`, `deduplication_ratio`, `conflict_resolution_total`.

## 22. Disaster Recovery
Multi-region cross-region S3 replication; metadata replicated across 3 cloud regions.

## 23. Cost Optimization
Lifecycle policies: Chunks not referenced by any active file version for 30 days are garbage collected and permanently purged.

## 24. Trade-off Analysis
* **Fixed vs. Rolling Chunks**: Fixed chunks are simple ($O(1)$) but inserting 1 byte invalidates all subsequent chunks. Rolling hash (Rabin) handles insertions gracefully at the cost of client CPU.

## 25. Failure Scenarios
* **Partial Chunk Upload Crash**: The client resumes upload from the exact missing block hash; already uploaded chunks are never repeated.

## 26. Production Considerations
* Bandwidth throttling settings in desktop client preventing cloud sync from saturating home internet connections.
