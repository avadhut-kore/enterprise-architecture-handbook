# Data Retention Policy Specification

| Data Category | Regulatory Basis | Operational Store | Long-Term Archive | Deletion Cadence |
|---|---|---|---|---|
| **Financial Ledger** | SOX / IRS | 3 Years | 7 Years (Parquet / S3) | Purged at 7yr + 1d |
| **User Access Logs** | SOC 2 / ISO 27001 | 90 Days | 365 Days | Automated monthly |
