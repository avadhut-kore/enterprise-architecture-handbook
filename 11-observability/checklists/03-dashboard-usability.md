# Checklist 03: Dashboard Usability & Cognitive Ergonomics

## 1. Overview
Audits Grafana and monitoring dashboards against human factors engineering principles, ensuring on-call engineers can assess system health within **5 seconds of opening the page**.

---

## 2. Verification Rubric

| Usability Rule | Inspection Guideline | Status |
| :--- | :--- | :--- |
| **The 5-Second Rule** | Can any engineer determine if the service is healthy within 5 seconds? | [ ] |
| **Standard Grid Layout** | Executive summary & SLI health status placed at the absolute top row? | [ ] |
| **Visual Hierarchy** | Critical Golden Signals (Traffic, Errors, Latency, Saturation) in rows 2-3? | [ ] |
| **Single Screen Baseline**| Core triage panels visible on standard 1080p display without excessive scrolling? | [ ] |
| **Color Semantics** | Green strictly reserved for nominal/good; Red strictly reserved for firing alerts? | [ ] |
| **Query Performance** | Does the entire dashboard render in $< 1.5$ seconds over a 6-hour query range? | [ ] |
| **Dynamic Templating** | Dashboard uses variables (`$environment`, `$cluster`, `$namespace`) rather than hardcoded hosts? | [ ] |
| **Contextual Deep-Links**| Do graph panels include contextual data links to jump directly to correlated logs/traces? | [ ] |
