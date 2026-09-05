# PCI-DSS Architectural Overview for Payment Systems

## 1. The Scope Reduction Imperative
PCI-DSS v4.0 enforces 300+ rigorous technical controls on any system component that stores, processes, or transmits Cardholder Data (CHD). 

```
                                  [Internet / Client]
                                           │
                        ┌──────────────────┴──────────────────┐
                        ▼                                     ▼
           [Untrusted SaaS / Merchant Web]         [Third-Party Hosted Fields]
                        │                                     │
           (Never sees cardholder data)            (Captures PAN directly)
                        │                                     │
                        │                                     ▼
                        │                            [Tokenization Vault]
                        │                                     │
                        │ <──────── Returns Token ────────────┘
                        │   ("tok_visa_991827")
                        ▼
           [Enterprise Order API] 
           (In Scope for SAQ A / SAQ A-EP, NOT SAQ D!)
```

## 2. Strategic Compliance Architecture
By utilizing iframe-hosted tokenization fields (Stripe Elements, Adyen Drop-in, Braintree Hosted Fields), the merchant's backend microservices never touch or store raw credit card numbers, dramatically reducing compliance audit costs and regulatory liability.
