# Storage Lifecycle Tiering Architecture

## 1. Automated Cost Optimization Lifecycle
```mermaid
flowchart LR
    S3_Std[S3 Standard: $0.023/GB - 0 to 30 Days] -->|Lifecycle Rule| S3_IA[S3 Infrequent Access: $0.0125/GB - 31 to 90 Days]
    S3_IA -->|Lifecycle Rule| S3_Glacier[Glacier Deep Archive: $0.00099/GB - 91+ Days]
```
* **Savings**: Storing 1 Petabyte on S3 Standard costs $\$23,000/\text{month}$. Storing 1 Petabyte on Glacier Deep Archive costs **$\$990/\text{month}$** ($95.7\%$ cost reduction!).
