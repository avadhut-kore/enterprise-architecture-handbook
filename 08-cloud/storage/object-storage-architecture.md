# Object Storage Architecture: Multipart, Byte-Range & Prefix Scaling

## Executive Summary

Object storage stores unstructured data as discrete objects containing a unique key, data payload, and arbitrary metadata. High-throughput performance requires mastering **prefix scaling**, **multipart uploads**, and **byte-range parallelism**.

---

## 1. Object Storage Internals & High-Throughput Engineering

```mermaid
graph TD
    Client[High-Throughput Application]
    Client --> Multipart[Multipart Upload: Split 50GB File into 5MB Chunks]
    Multipart --> Chunk1[Upload Chunk 1 in Parallel]
    Multipart --> Chunk2[Upload Chunk 2 in Parallel]
    Multipart --> ChunkN[Upload Chunk N in Parallel]

    Client --> ByteRange[Byte-Range Fetch: GET Range: bytes=0-1048576]
    ByteRange --> Parquet[(Parquet / Iceberg Columnar Pruning)]
```

---

## 2. Partition Key & Prefix Scaling Mechanics

- **How Prefix Partitioning Works**: Object storage automatically partitions data by the object key's string prefix.
- In Amazon S3, each unique partition prefix supports **3,500 PUT/POST/DELETE requests/sec** and **5,500 GET requests/sec**.
- **Architectural Rule for High-Throughput**: To scale beyond 5,500 GETs/sec, distribute objects across distinct prefixes (e.g., `s3://my-bucket/orders/2026/01/...`, `s3://my-bucket/orders/2026/02/...`).
- **Byte-Range Requests**: Big Data query engines (Trino, Athena, BigQuery) never download multi-gigabyte files in full. They issue parallel HTTP `Range: bytes=X-Y` requests to fetch only specific columnar metadata footers from Parquet files.
