# Enterprise AI Use-Case Risk Classification Framework

## 1. Architectural Intake Assessment

Before any engineering team begins implementing an AI capability, the use case must pass through the **Architecture Review Board (ARB) AI Risk Scorecard**:

| Risk Score | Tier | Criteria | Architectural Review Requirements |
| :---: | :--- | :--- | :--- |
| **Tier 1** | **Critical / High Risk** | Directly influences financial credit, employment decisions, healthcare, or autonomous state mutations. | Full ARB review; dual-LLM guardrails; mandatory human sign-off on every action; WORM compliance logging. |
| **Tier 2** | **Moderate Risk** | Customer-facing conversational agents, internal RAG on proprietary codebases, automated document synthesis. | Standard ARB review; automated evaluation gates (faithfulness $\ge 90\%$); PII redaction mandatory. |
| **Tier 3** | **Low / Minimal Risk** | Internal developer productivity tools, code autocomplete, spell checking, meeting summarization. | Fast-track self-service intake; standard enterprise gateway rate limiting. |
