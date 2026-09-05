# Account Services Integration Architecture

## 1. Scope of Account Services
Account integration services encapsulate account creation, status transitions (`ACTIVE`, `FROZEN`, `DORMANT`, `CLOSED`), interest accrual calculation, hold placements, and multi-currency balances.

## 2. Canonical Account Service Contract (OpenAPI Specification)
```yaml
openapi: 3.0.3
info:
  title: Enterprise Account Integration Service
  version: 1.0.0
paths:
  /v1/accounts/{accountId}/holds:
    post:
      summary: Place an authorization hold against account balance
      parameters:
        - name: accountId
          in: path
          required: true
          schema: { type: string }
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [hold_id, amount, currency, expires_at]
              properties:
                hold_id: { type: string, format: uuid }
                amount: { type: number, format: decimal }
                currency: { type: string, example: "USD" }
                expires_at: { type: string, format: date-time }
      responses:
        '201':
          description: Hold placed successfully
        '409':
          description: Insufficient available funds
```
