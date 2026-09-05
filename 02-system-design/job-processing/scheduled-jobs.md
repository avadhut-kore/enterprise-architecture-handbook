# Scheduled Jobs Architecture

## 1. Trigger Modalities
* **Time-Based (Cron)**: Executes at specific calendar times (e.g., `0 0 1 * *` - Midnight on the 1st of every month for billing cycles).
* **Interval-Based**: Executes periodically with fixed delays (e.g., poll third-party API every 15 minutes).
* **Event-Delayed**: Scheduled relative to a preceding event (e.g., send welcome email exactly 24 hours after user registration).
