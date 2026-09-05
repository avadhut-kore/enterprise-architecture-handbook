# Storage Estimation

## 1. Scope & Fundamentals
Storage estimation determines the raw and effective disk, object store, and database capacity required to support an application over a multi-year planning horizon (typically 3 to 5 years). In enterprise systems, naive calculations that only sum application payload fields underestimate storage needs by $3\times\text{--}5\times$ because they omit database metadata, indexing overhead, transaction logs (WAL), replication factors, and filesystem block slack.

---

## 2. Mathematical Sizing Model

```mermaid
flowchart LR
    Payload[Raw Data Payload] -->|Add DB Metadata & UUIDs| Row[Logical Row Size]
    Row -->|Add Secondary Indexes: +30-60%| Indexed[Indexed Size]
    Indexed -->|Apply Replication Factor: RF=3| Replicated[Replicated Storage]
    Replicated -->|Add WAL, Backups & Headroom: +40%| Physical[Total Physical Disks]
```

### Complete Storage Equation
$$\text{Storage}_{\text{effective}} = \left( N_{\text{records}} \times S_{\text{row}} \times (1 + M_{\text{index}}) \times \text{RF} \right) \times (1 + M_{\text{slack}})$$

Where:
* $N_{\text{records}}$ = Total records over time horizon ($N_{\text{daily}} \times 365 \times \text{Years}$)
* $S_{\text{row}}$ = Raw record size in bytes
* $M_{\text{index}}$ = Index overhead multiplier (typically $0.30\text{--}0.60$)
* $\text{RF}$ = Replication Factor (typically 3 for high-durability distributed clusters)
* $M_{\text{slack}}$ = Compaction headroom, WAL, and filesystem slack ($0.25\text{--}0.40$)

---

## 3. Worked Enterprise Example: High-Scale IoT Telemetry Platform

### Sizing Parameters
* **Fleet**: $10,000,000$ active IoT devices.
* **Transmission Frequency**: 1 telemetry ping every 60 seconds.
* **Planning Horizon**: 3 years.
* **Payload Structure**:
  * `device_id`: UUID (16 bytes)
  * `timestamp`: int64 (8 bytes)
  * `temperature`: float32 (4 bytes)
  * `pressure`: float32 (4 bytes)
  * `status_code`: int16 (2 bytes)
  * `sensor_hash`: string/hash (16 bytes)
  * **Raw Payload**: $50\text{ bytes}$
  * **Engine Row Overhead (B-Tree/Columnar headers)**: $14\text{ bytes}$
  * **Effective Row Size ($S_{\text{row}}$)**: $64\text{ bytes}$

### Daily Ingestion Calculation
$$\text{Pings / Day} = 10,000,000 \times \left(\frac{86,400}{60}\right) = 14,400,000,000\text{ records/day} \quad (14.4\text{ Billion})$$
$$\text{Daily Raw Ingestion} = 14.4 \times 10^9 \times 64\text{ bytes} \approx 921.6\text{ GB/day} \approx 0.92\text{ TB/day}$$

### 3-Year Storage Projection
$$\text{Total 3-Year Raw} = 0.92\text{ TB/day} \times 365 \times 3 \approx 1,007.4\text{ TB} \approx 1\text{ PB}$$

Applying:
* Secondary Index Overhead ($M_{\text{index}} = 0.35$)
* Replication Factor ($\text{RF} = 3$)
* Compaction & WAL Headroom ($M_{\text{slack}} = 0.30$)

$$\text{Storage}_{\text{effective}} = 1,007.4 \times (1 + 0.35) \times 3 \times (1 + 0.30) \approx 5,304\text{ TB} \approx 5.3\text{ PB}$$

---

## 4. Multi-Tier Storage Partitioning

To avoid storing 5.3 PB on expensive NVMe SSDs, implement automated lifecycle storage tiering:

| Storage Tier | Retention Window | Storage Medium | Volume (Effective) | Relative Cost / GB |
| :--- | :--- | :--- | :--- | :--- |
| **Hot Tier** | 0 â€“ 30 Days | NVMe Distributed DB | $146\text{ TB}$ | $\$0.12\text{ / GB}$ |
| **Warm Tier** | 31 â€“ 180 Days | Standard Cloud Disk / Object | $730\text{ TB}$ | $\$0.023\text{ / GB}$ |
| **Cold Tier** | 181 Days â€“ 3 Years | Parquet on Object Storage (S3/GCS) | $4,428\text{ TB}$ (Compressed $\approx 880\text{ TB}$) | $\$0.004\text{ / GB}$ |

---

## 5. Architectural Gotchas & Failure Modes
* **Write Amplification in LSM Trees**: In systems like Apache Cassandra or RocksDB, background compactions can rewrite data $10\times\text{--}30\times$, demanding $50\%$ free disk headroom solely for compaction merge phases.
* **Filesystem Inode Exhaustion**: Storing millions of small files (<4KB) on a POSIX filesystem exhausts inode tables long before raw disk capacity is depleted.
* **Compression Ratios**: Never assume theoretical compression ratios. Real-world JSON compresses $4\text{--}6\times$; pre-encrypted binary or UUIDs compress at $1.0\times$ (0% savings).
