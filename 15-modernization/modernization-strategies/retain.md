# The "Retain" Strategy: When Keeping Legacy Is Best

## 1. Architectural Definition
**Retain** (also known as *Revisit* or *Encapsulate*) is the conscious architectural decision to keep a legacy system operating in its current environment without initiating a code rewrite or infrastructure migration. It is not neglect; it is **active preservation**.

```
                           [Core Legacy System]
                           (Stable, High-ROI, Low-Change)
                                     ▲
                                     │ (Isolated via mTLS & API Gateway)
                                     ▼
                      [Modern API & Event Facade]
                                     ▲
                                     │
                    [Modern Digital Channels & Cloud Apps]
```

---

## 2. When to Choose "Retain"
- **High Stability & Zero Incidents**: The application has run for years with $\ge 99.99\%$ availability and zero severe incident tickets.
- **Low Change Velocity**: The business requests fewer than 2 minor feature updates annually.
- **High Migration Risk vs. Low Value**: The system processes complex, undocumented mathematical calculations (e.g., actuarial models, legacy tax rules) where any divergence creates severe legal liability.
- **Planned Sunset**: The business capability is scheduled to be decommissioned within 12 to 24 months.
- **Negative Modernization ROI**: A rewrite would cost $5M and save only $50k/year in hosting fees, resulting in a 100-year payback period.

---

## 3. The "Retain with Encapsulation" Pattern
If a retained system must integrate with modern cloud services, wrap it in a lightweight **API Facade**:
1. Place an API Gateway in front of the legacy system.
2. Expose modern REST / OpenAPI contracts to new cloud consumers.
3. Translate inbound JSON requests into legacy protocols (SOAP, MQ, CPYBOOK) within the facade.
4. Keep the legacy core completely untouched.
