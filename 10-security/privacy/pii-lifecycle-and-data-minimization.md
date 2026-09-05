# PII Lifecycle & Data Minimization Architecture

## Executive Summary

- **Data Minimization**: Collect only the absolute minimum PII required to fulfill the verified business transaction (e.g., do not collect birthdate if only age verification $> 18$ is required).
- **Automated PII Scrubbing**: Log forwarders (Fluentbit) execute regular expression masking against credit cards, SSNs, and email addresses before shipping logs to telemetry collectors.
