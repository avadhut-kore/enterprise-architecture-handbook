# Technology Comparison: Storage Paradigms Trade-Off Matrix

## Executive Summary
This reference matrix evaluates the architectural trade-offs between object vs file vs block storage.

---

## Architectural Comparison Matrix

| Dimension | Block Storage (EBS) | File Storage (EFS / Azure Files) | Object Storage (S3 / Blob) |
| :--- | :--- | :--- | :--- |
| **Latency** | < 1ms (Sub-millisecond) | 2–10ms | 50–150ms |
| **Access Protocol** | SCSI / NVMe block device | NFSv4 / SMB network share | HTTP/HTTPS REST API |
| **Sharing** | Single VM attach | Thousands of concurrent nodes | Millions of worldwide clients |
| **Cost per GB/Month** | $0.08–$0.15 | $0.15–$0.30 | $0.00099–$0.023 |
