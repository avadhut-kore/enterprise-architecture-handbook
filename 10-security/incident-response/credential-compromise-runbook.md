# Security Runbook: Stolen Cloud IAM / API Credentials

## Executive Summary

This emergency runbook executes immediately when a developer API key or cloud IAM credential is detected as compromised (e.g., found on GitHub or alerted by GuardDuty).

---

## 1. Step-by-Step Emergency Execution Sequence
1. **Immediate Revocation (Minute 0–5)**:
   - Attach an inline `DenyAll` policy directly to the compromised IAM user or role:
     ```json
     {"Effect": "Deny", "Action": "*", "Resource": "*"}
     ```
   - Invalidate all active AWS console sessions and revoke all temporary STS sessions issued prior to `current_time`.
2. **Blast Radius Forensics (Minute 5–30)**:
   - Query CloudTrail in Athena for all actions executed by the compromised identity in the last 72 hours:
     ```sql
     SELECT eventTime, eventSource, eventName, sourceIPAddress 
     FROM cloudtrail_logs 
     WHERE userIdentity.arn = 'arn:aws:iam::123456789:user/compromised-user'
     ORDER BY eventTime DESC;
     ```
3. **Eradication & Remediation (Minute 30–60)**:
   - Identify any secondary backdoors created by the adversary (new IAM users, modified SSH keys, unauthorized Lambda functions).
   - Rotate the credential and replace with Workload Identity Federation.
