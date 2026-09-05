# AWS S3 Deep-Dive Architecture

## 1. S3 Internal Partitioning & Prefixes
Amazon S3 partitions data automatically across internal storage clusters based on the **Object Key Prefix**:
* S3 automatically scales to support **3,500 PUT/POST/DELETE** and **5,500 GET requests per second per prefix**.
* By distributing files across distinct prefixes (e.g., `bucket/2026/09/`, `bucket/2026/10/`), an application can achieve hundreds of thousands of concurrent read/write transactions.
