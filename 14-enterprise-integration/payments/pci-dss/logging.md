# PCI-DSS Audit Logging, Sanitization, and WORM Storage

## 1. Mandatory Audit Events (Requirement 10)
- All user access to cardholder data.
- All actions taken by individuals with administrative privileges.
- Access to all audit logs.
- Invalid logical access attempts.
- Use of cryptographic key mechanisms.

## 2. Payload Sanitization
Log scrapers and logging libraries must implement regex filters that replace PAN patterns (`\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}`) with masked values (`****-****-****-1234`) before log lines are written to disk.
