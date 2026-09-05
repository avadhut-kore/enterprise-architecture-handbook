# Payment Authorization Engines and Protocols

## 1. Dual-Message vs. Single-Message Authorization
- **Dual-Message System (DMS)**: Authorization occurs in real-time during checkout; Capture occurs hours or days later (standard in US/EU e-commerce and hotel bookings).
- **Single-Message System (SMS)**: Authorization and clearing/capture occur simultaneously in a single real-time message (standard in debit ATM withdrawals and grocery POS).

## 2. ISO 8583 / AS 2805 Message Format
Card network integrations frequently communicate via binary ISO 8583 message streams:
- `0100`: Authorization Request.
- `0110`: Authorization Response.
- `0200`: Financial Transaction Request.
- `0420`: Reversal / Timeout Advice.
