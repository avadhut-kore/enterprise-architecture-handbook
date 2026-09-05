# Observability FinOps & Cost Engineering Checklist

## 1. Executive Summary
This 25-point checklist provides engineering managers, platform architects, and FinOps practitioners with an objective verification rubric for managing, auditing, and optimizing telemetry infrastructure costs.

---

## 2. The 25-Point Checklist

### Section 1: Ingestion & Cardinality Governance
- [ ] **01.** Automated metric relabeling rules drop high-cardinality labels (`user_id`, `email`, UUIDs).
- [ ] **02.** Path variables in URL routes (e.g., `/orders/12345`) are normalized to static templates (`/orders/:id`).
- [ ] **03.** Kubernetes scraping configs enforce hard `sample_limit` caps to prevent rogue pod cardinality explosions.
- [ ] **04.** High-volume repetitive events are converted from raw log strings into compact time-series counters.
- [ ] **05.** Kubernetes `/healthz` and `/ready` probes are filtered out from application access logging.

### Section 2: Data Lifecycle & Tiered Storage
- [ ] **06.** Telemetry storage enforces a 3-tier lifecycle: Hot (SSD), Warm (Standard/Compacted), Cold (Object Storage/S3).
- [ ] **07.** Hot log retention is bounded to the active incident triage window ($\le 7$ days).
- [ ] **08.** Thanos/Cortex automated downsampling aggregates metric data to 5-minute and 1-hour resolutions.
- [ ] **09.** Cold log archives are compressed in columnar formats (Parquet / Zstandard) for cost-effective long-term compliance.
- [ ] **10.** Automatic deletion policies purge non-compliance telemetry after its designated retention lifecycle expires.

### Section 3: Trace & Profile Sampling Optimization
- [ ] **11.** Tail sampling is configured on OpenTelemetry collectors to capture 100% of errors and latency outliers.
- [ ] **12.** Nominal, successful traces are sampled down to a sustainable fraction ($0.5\% - 2.0\%$).
- [ ] **13.** Continuous profiling agents sample at an anti-harmonic prime rate (19 Hz) with $< 1\%$ CPU overhead.
- [ ] **14.** Profiling profiles are collapsed and downsampled after 7 days to preserve macro-trends affordably.

### Section 4: Log Spend & Volume Reduction
- [ ] **15.** Production default log level is enforced at `INFO`; `DEBUG` and `TRACE` are prohibited in steady-state.
- [ ] **16.** Dynamic runtime log-level changes automatically revert back to `INFO` after 30 minutes.
- [ ] **17.** Large payload bodies and raw binary strings are stripped prior to log ingestion.
- [ ] **18.** Exception logging enforces token-bucket rate limits to prevent loop-driven disk flooding.
- [ ] **19.** Un-indexed log storage options are utilized for compliance logs that require archival without real-time search.

### Section 5: FinOps Attribution & ROI Culture
- [ ] **20.** Telemetry costs are tracked and attributed to individual engineering squads using resource tags (`owner_team`).
- [ ] **21.** Monthly showback/chargeback reports highlight top 5 telemetry spenders across the engineering fleet.
- [ ] **22.** OpenTelemetry Collectors are deployed as local node DaemonSets to eliminate cross-AZ egress bandwidth fees.
- [ ] **23.** SaaS monitoring vendor contracts are reviewed annually against self-hosted open-source TCO benchmarks.
- [ ] **24.** Squads allocate 10% of engineering bandwidth to telemetry hygiene if observability spend exceeds 20% of cloud budget.
- [ ] **25.** Quarterly audits review index mappings to ensure un-searched JSON fields are excluded from full-text inversion.
