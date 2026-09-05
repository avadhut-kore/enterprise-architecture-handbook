# SLA, SLO, and SLI Monitoring for Enterprise Integrations

## 1. Terminology Framework
- **SLI (Service Level Indicator)**: A quantifiable metric measuring service performance (e.g., successful API request latency).
- **SLO (Service Level Objective)**: Target reliability agreed upon internally (e.g., $99.95\%$ of requests complete in $< 500	ext{ms}$).
- **SLA (Service Level Agreement)**: Legally binding contract with financial penalties for breach (e.g., $99.9\%$ monthly uptime or 10% credit).

## 2. Error Budget Calculation
For a 99.9% monthly SLO:
$$	ext{Allowable Downtime} = 30 	imes 24 	imes 60 	imes (1 - 0.999) = 43.2 	ext{ minutes per month}$$

Integration teams must monitor the **Error Budget Burn Rate**: if 50% of the monthly error budget is consumed in 1 hour, immediately freeze non-critical deployments.
