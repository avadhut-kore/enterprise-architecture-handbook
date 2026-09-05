# Technology Lifecycle Tiers

The governance lifecycle that every technology product passes through within an enterprise.

---

## 1. The 5 Technology Lifecycle Tiers

```mermaid
graph LR
    T1["1. Strategic<br/>Target for future systems; primary innovation focus"] --> T2["2. Standard<br/>Approved for general production use; paved road support"]
    T2 --> T3["3. Tolerated<br/>Supported for legacy; no new projects permitted"]
    T3 --> T4["4. Restricted<br/>Active phase-out; requires formal exception waiver"]
    T4 --> T5["5. Retire<br/>Decommissioned; blocked by CI/CD fitness checks"]
```

---

## 2. Technology Radar vs Technology Portfolio
* **Technology Radar (Quarterly)**: Tracks *emerging trends* and recommendations (Adopt, Trial, Assess, Hold). (See [TECHNOLOGY-RADAR.md](../../TECHNOLOGY-RADAR.md)).
* **Technology Portfolio (Continuous)**: Manages *existing enterprise reality*—tracking versions, contracts, licenses, CVEs, and retirement pipelines for 100% of installed software.
