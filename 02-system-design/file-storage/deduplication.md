# Content-Addressable Storage (CAS) & Deduplication

## 1. Hash-Based Storage Keys
In Content-Addressable Storage (like Git or Dropbox), the storage key is the cryptographic hash of the file payload:
$$\text{Storage Key} = \text{SHA-256}(\text{File Bytes})$$

```mermaid
flowchart TD
    FileA[User 1: Uploads Video.mp4] --> Hash{Compute SHA-256}
    FileB[User 2: Uploads Same Video.mp4] --> Hash
    Hash -->|Key: e3b0c44298fc1c14...| Storage[(Single Stored File on S3)]
```
* If 1,000 users upload the exact same 1 GB video file, the system stores **1 GB on physical disk** (saving 999 GB of storage!).
