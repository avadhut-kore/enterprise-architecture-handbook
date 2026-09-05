# Cold Storage & Archival Architecture

## 1. Automated Archival Pipeline
* Nightly batch extracts rows older than 90 days from operational PostgreSQL into Parquet files.
* Files compressed with ZSTD and written to AWS S3 Glacier Flexible Retrieval with Object Lock (WORM).
