# Operational Runbook: Database Auth Outage Following Secret Rotation

## 1. Purpose & Scope
This runbook provides emergency mitigation procedures for resolving database auth outage following secret rotation impacting enterprise production workloads.

## 2. Incident Symptoms
- Microservices unable to connect to database immediately following automated password rotation.
- Alert fired: `SLO_Burn_Rate_Critical` or `ErrorRateHigh`.

## 3. Business Impact
- Direct impact on customer transactions, revenue generation, or SLA compliance penalties.

## 4. Prerequisites & Required Access
- Vault Enterprise admin token and database DBA credentials.

## 5. Initial Health Checks
1. Check real-time service status on Grafana dashboard.
2. Verify if a deployment occurred in the last 60 minutes via `#deployments` Slack channel.

## 6. Diagnostic Steps
1. Inspect container logs:
   ```bash
   kubectl logs -l app=order-service --tail=100 -n production
   ```
2. Check pod resource utilization:
   ```bash
   kubectl top pods -n production --sort-by=memory
   ```

## 7. Immediate Mitigation Actions
**EXECUTE IMMEDIATE ACTION:**
Revert Vault dynamic secret lease or update application database credentials to match rotated password; bounce connection pools.

## 8. Recovery Verification
- Confirm HTTP 5xx error rate drops below 0.05%.
- Validate synthetic health check probes return HTTP 200 within 150ms.

## 9. Rollback & Failsafe Criteria
- If mitigation does not restore service within 10 minutes, escalate to Incident Commander and initiate secondary disaster failover.

## 10. Escalation Path
- **Primary**: On-Call Squad SRE
- **Secondary**: SRE Team Lead / Domain Technical Architect
- **Executive**: Incident Commander / VP of Engineering

## 11. Communication Templates
- *Internal Slack (#incidents)*: "INVESTIGATING: Database Auth Outage Following Secret Rotation declared SEV-1. War room active. Next update in 15 mins."
- *External Status Page*: "We are investigating an issue affecting transaction processing. Engineers are actively mitigating."

## 12. Post-Incident Review (PIR) Actions
- Preserve logs and metrics snapshots.
- Schedule blameless PIR within 48 hours to identify systemic prevention actions.
