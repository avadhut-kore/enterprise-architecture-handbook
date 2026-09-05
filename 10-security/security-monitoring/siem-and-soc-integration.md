# SIEM & SOC Architectural Integration

## Executive Summary

The Security Operations Center (SOC) relies on the SIEM for centralized correlation. To prevent log noise:
- **Mandate the Open Cybersecurity Schema Framework (OCSF)**: Ensure all log sources emit structured JSON adhering to standard event taxonomy.
- **Filter at Source**: Drop repetitive high-volume debug logs at the Fluentbit collector layer; stream strictly security-relevant events (`auth.failure`, `iam.policy_change`, `access_denied`).
