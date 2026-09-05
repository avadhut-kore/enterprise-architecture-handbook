# Mermaid Gantt Roadmaps & Migration Timelines

Gantt charts visually illustrate architecture roadmaps, technical debt retirement timelines, and multi-phase platform migrations.

## Enterprise Cloud Migration Roadmap

```mermaid
gantt
    title Enterprise Cloud Migration Architecture Roadmap (2026-2027)
    dateFormat  YYYY-MM-DD
    section Phase 1: Foundation
    Landing Zone Architecture (AWS Control Tower) :done, des1, 2026-01-01, 2026-02-15
    Direct Connect & Hybrid Routing              :done, des2, 2026-02-01, 2026-03-15
    Identity Federation (Okta to Azure AD)       :active, des3, 2026-03-01, 2026-04-30

    section Phase 2: Pilot Workloads
    Stateless Web Apps Migration                 :crit, des4, 2026-04-15, 2026-06-30
    CI/CD Pipeline Standardization (GitHub)      :des5, 2026-05-01, 2026-07-15

    section Phase 3: Core Modernization
    Core Banking Database Migration (Oracle to Aurora) :des6, 2026-07-01, 2026-11-30
    Legacy Mainframe Decommissioning             :des7, 2026-11-01, 2027-02-28
```

## Architectural Guidelines
* Use `done`, `active`, and `crit` flags to indicate completed, ongoing, and critical-path architecture milestones.
