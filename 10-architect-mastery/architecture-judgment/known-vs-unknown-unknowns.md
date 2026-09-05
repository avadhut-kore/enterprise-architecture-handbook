# Managing Knowns, Unknowns, and Unknown Unknowns

The master architect systematically surfaces hidden assumptions and blind spots before they manifest as production catastrophes.

---

## 1. The Architectural Epistemology Matrix

```mermaid
quadrantChart
    title Architectural Knowledge Matrix
    x-axis "Unawareness (Blind Spots)" --> "Awareness (Known)"
    y-axis "Certainty (Validated)" --> "Uncertainty (Unproven)"
    quadrant-1 "KNOWN UNKNOWNS<br/>(Aware of gap; requires Spike/Test)<br/>• Peak network latency across regions<br/>• Vector DB QPS limits"
    quadrant-2 "UNKNOWN UNKNOWNS<br/>(Existential blind spots)<br/>• Third-party SaaS silent data corruption<br/>• Upstream network route flapping"
    quadrant-3 "UNKNOWN KNOWNS<br/>(Tacit knowledge in org, undocumented)<br/>• Undocumented COBOL edge-case logic<br/>• Tribal DB failover procedures"
    quadrant-4 "KNOWN KNOWNS<br/>(Established facts & verified NFRs)<br/>• Database ACID guarantees<br/>• Current active user count"
    "Known Knowns": [0.85, 0.20]
    "Known Unknowns": [0.85, 0.85]
    "Unknown Knowns": [0.25, 0.20]
    "Unknown Unknowns": [0.25, 0.85]
```

---

## 2. Exercises for Surfacing Unknown Unknowns

1. **The Pre-Mortem Simulation**:
   * Gather the team and state: *"It is 3 years from today. Our newly launched platform has suffered a catastrophic, unrecoverable failure and our stock dropped 15%. Write down exactly what caused the disaster."*
2. **Chaos & Failure Injection Hypotheses**:
   * Systematically ask: *"What happens if this network link drops packets? What happens if this queue fills up? What happens if this API returns HTTP 200 with an empty body?"*
3. **Cross-Disciplinary Red Teaming**:
   * Invite a senior SRE and a security penetration tester to review the architecture with the explicit mandate: *"Break this design."*
