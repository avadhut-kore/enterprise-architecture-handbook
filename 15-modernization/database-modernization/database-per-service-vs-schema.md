# Database-per-Service vs. Schema-per-Service

## 1. Comparative Architecture

| Dimension | Schema-per-Service (Logical Isolation) | Database-per-Service (Physical Isolation) |
| :--- | :--- | :--- |
| **Physical Infrastructure**| Single DB instance/cluster, multiple schemas | Separate DB clusters (e.g. RDS instances) |
| **Blast Radius** | High (Instance crash impacts all services) | Minimal (Failure isolated to single domain) |
| **Operational Overhead** | Low (Single backup, single patching cycle) | High (Multiple clusters, connections, monitors) |
| **Cost Profile** | Low (Consolidated compute & memory) | Higher (Over-provisioned buffer pools) |
| **Noisy Neighbor Risk** | High (I/O spikes impact neighbor schemas) | Zero (Independent CPU and storage IOPS) |
| **Recommended Phase** | **Phase 1: Transition Step** | **Phase 2: Final Target Architecture** |
