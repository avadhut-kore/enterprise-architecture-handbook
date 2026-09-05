# Post-Mortem Analysis & Blameless RCA

## 1. Blameless Culture & Psychological Safety

Human error is never the root cause of an outage; human error is the *symptom* of a systemic flaw, missing guardrail, ambiguous documentation, or poor tooling.

A **Blameless Post-Mortem** focuses entirely on:
- What systemic conditions allowed the incident to occur?
- Why did existing alarms fail to catch it earlier?
- How do we structurally alter the architecture so this class of failure cannot recur?

---

## 2. Standard Enterprise Incident Timeline & 5-Whys Framework

```
[ Incident Timeline ]
14:02 UTC - Bad deployment released to production
14:08 UTC - Edge Gateway 502 alerts trigger on PagerDuty
14:15 UTC - Incident Commander initiates triage bridge
14:22 UTC - Canary traffic drained; rollback completed
14:26 UTC - Steady state restored
```

### The 5-Whys Root Cause Analysis
1. *Why did the gateway return 502?* Downstream User Service threads were exhausted.
2. *Why were threads exhausted?* Database queries to the `users` table took 30 seconds.
3. *Why did queries take 30 seconds?* A full table scan occurred on 50 million rows.
4. *Why was there a full table scan?* A new query was introduced without an index on `tenant_code`.
5. *Why was the query deployed without an index?* The CI pipeline linter did not enforce query execution plan checks on migration scripts. (Action Item: Add automated `EXPLAIN` query linter in CI/CD).
