# When NOT to Use Multi-Agent Systems

## 1. The Multi-Agent Hype Trap

A pervasive architectural failure is deploying multi-agent frameworks (e.g., AutoGen, CrewAI) for tasks that are trivially solved by a single prompt or a deterministic Python script.

```mermaid
flowchart TD
    Problem["Task Requirement"] --> Test1{"Can the task be solved by a single prompt with structured tools?"}
    Test1 -->|Yes| Reject1["DO NOT USE MULTI-AGENT.\nUse a single well-prompted model."]
    Test1 -->|No| Test2{"Is the sequence of steps known in advance?"}
    Test2 -->|Yes| Reject2["DO NOT USE MULTI-AGENT.\nUse a deterministic workflow engine (Temporal)."]
    Test2 -->|No| Test3{"Does the business outcome justify 10x higher latency and cost?"}
    Test3 -->|No| Reject3["DO NOT USE MULTI-AGENT.\nSimplify the requirement."]
    Test3 -->|Yes| Allow["Multi-Agent System Justified."]
```

---

## 2. Lethal Failure Modes of Multi-Agent Deployments
1. **Echo Chambers**: Agent A hallucinates a false premise; Agent B accepts it as truth and elaborates; Agent C synthesizes a disastrously wrong final recommendation with high confidence.
2. **Non-Deterministic Debugging**: When an outage occurs, tracing which agent made the erroneous assumption across 20 asynchronous message exchanges requires hours of manual forensic analysis.
