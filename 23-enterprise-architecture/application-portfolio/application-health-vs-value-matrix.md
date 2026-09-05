# Application Health vs Value Matrix (The TIME Model)

The industry-standard Gartner TIME model categorizes software assets into four actionable investment quadrants.

---

## 1. The TIME Portfolio Quadrant

```mermaid
quadrantChart
    title Application Portfolio TIME Matrix
    x-axis "Low Technical Health" --> "High Technical Health"
    y-axis "Low Business Value" --> "High Business Value"
    quadrant-1 "INVEST<br/>Enhance, scale, and integrate"
    quadrant-2 "MIGRATE / RE-ARCHITECT<br/>Modernize legacy, high strategic urgency"
    quadrant-3 "ELIMINATE<br/>Decommission, archive, cancel contracts"
    quadrant-4 "TOLERATE<br/>Maintain as-is, minimize capital spend"
    "Core Digital Bank Engine": [0.85, 0.90]
    "Mobile Onboarding App": [0.80, 0.85]
    "Legacy Underwriting Mainframe": [0.20, 0.92]
    "Custom Regional Invoicing App": [0.25, 0.75]
    "Lotus Notes Expense Tool": [0.15, 0.15]
    "Duplicate EMEA CRM": [0.30, 0.25]
    "Facilities Room Booking Tool": [0.75, 0.20]
    "Legacy Fixed Asset Register": [0.80, 0.30]
```

---

## 2. Action Playbooks by Quadrant

1. **INVEST (High Value, High Health)**:
   * Allocate primary innovation budgets. Extend capabilities via APIs, AI enablers, and feature enhancements.
2. **MIGRATE / RE-ARCHITECT (High Value, Low Health)**:
   * High priority modernization candidates. The business cannot survive without this capability, but the technology platform is a ticking operational timebomb. Allocate capital to strangler-fig re-architecting.
3. **TOLERATE (Low Value, High Health)**:
   * Stable, commodity utilities that cost little to maintain and run reliably. Do NOT spend capital modernizing them; leave them in run mode.
4. **ELIMINATE (Low Value, Low Health)**:
   * Technical debt sinks that provide negligible business return. Decommission immediately, consolidate onto standard SaaS, or turn off.
