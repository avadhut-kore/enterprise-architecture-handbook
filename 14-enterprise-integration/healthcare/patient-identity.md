# Enterprise Master Patient Index (EMPI) Architecture

## 1. The Patient Matching Challenge
Patients visit multiple clinics, emergency rooms, and laboratories, resulting in duplicate records with slight name variations, changed addresses, or mistyped social security numbers. An EMPI establishes a universal enterprise patient identifier.

## 2. Deterministic vs. Probabilistic Matching

| Methodology | Algorithm | Strengths | Weaknesses |
| :--- | :--- | :--- | :--- |
| **Deterministic** | Exact match on SSN + Date of Birth + Gender | Zero false positives | High false negative rate (misses mistyped digits) |
| **Probabilistic** | Fellegi-Sunter algorithm, Jaro-Winkler distance | Catches typos, hyphenated names, maiden names | Requires clerical review queues for borderline scores |

```
Incoming Record: "Jonathon Smyth, DOB: 1980-04-12"
                   │
                   ▼
       [EMPI Matching Engine]
       ├── Jaro-Winkler("Jonathon", "Jonathan") = 0.94
       ├── Soundex("Smyth", "Smith") = MATCH
       └── DOB Match = EXACT
                   │
                   ▼ (Combined Confidence Score: 92%)
       [Merge to Enterprise Patient ID: EPID-991827]
```
