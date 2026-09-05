# Implementation Example: Payment Orchestration Engine

## 1. Smart Routing Decision Code (Python)
```python
class PaymentOrchestrator:
    def __init__(self, routing_rules, acquirer_clients):
        self.rules = routing_rules
        self.clients = acquirer_clients

    def route_payment(self, payment_request: dict) -> dict:
        currency = payment_request["currency"]
        amount = payment_request["amount"]
        
        # Select best acquirer based on cost and health
        target_acquirer = self.select_acquirer(currency, amount)
        client = self.clients[target_acquirer]
        
        try:
            response = client.authorize(payment_request)
            return {"status": "AUTHORIZED", "acquirer": target_acquirer, "data": response}
        except AcquirerTimeoutException:
            # Fallback to secondary acquirer
            fallback_acquirer = self.select_fallback(target_acquirer)
            fallback_client = self.clients[fallback_acquirer]
            response = fallback_client.authorize(payment_request)
            return {"status": "AUTHORIZED", "acquirer": fallback_acquirer, "data": response}
```
