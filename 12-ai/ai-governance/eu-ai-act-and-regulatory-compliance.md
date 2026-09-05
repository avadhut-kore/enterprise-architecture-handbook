# EU AI Act & Regulatory Architecture

## 1. The 4 Risk Tiers of the EU AI Act

```mermaid
quadrantChart
    title EU AI Act Risk Tiering
    x-axis Low Societal Impact --> High Societal Impact
    y-axis Low Autonomy --> High Autonomous Decision Making
    quadrant-1 Unacceptable Risk (Banned)
    quadrant-2 High Risk (Heavily Regulated)
    quadrant-3 Minimal Risk (Unregulated)
    quadrant-4 Limited Risk (Transparency Mandates)
```

### 1.1 High-Risk AI Systems (Article 6)
* **Scope**: AI used in credit scoring, employment recruiting, medical devices, critical infrastructure, and biometric identification.
* **Architectural Obligations**:
  * Mandatory automated logging of all decision inputs/outputs.
  * Human-in-the-loop oversight mechanisms with emergency stop buttons.
  * Continuous technical documentation and model risk assessments.
  * High-accuracy training datasets free from demographic bias.
