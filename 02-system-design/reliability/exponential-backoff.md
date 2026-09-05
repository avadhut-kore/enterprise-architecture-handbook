# Exponential Backoff

## 1. The Mathematical Model
Exponential backoff increases the delay between successive retry attempts exponentially, giving struggling downstream services time to recover and drain their queues.

### The Equation
$$T_{\text{wait}}(a) = \min\left(T_{\text{max}}, T_{\text{base}} \times 2^a\right)$$
Where:
* $a$ = Current attempt number ($0, 1, 2, \dots$)
* $T_{\text{base}}$ = Initial base delay (e.g., $100\text{ ms}$)
* $T_{\text{max}}$ = Hard maximum backoff ceiling (e.g., $10,000\text{ ms}$)

```mermaid
flowchart LR
    Fail0[Attempt 0: Failed] -->|Wait: 100ms| Fail1[Attempt 1: Failed]
    Fail1 -->|Wait: 200ms| Fail2[Attempt 2: Failed]
    Fail2 -->|Wait: 400ms| Fail3[Attempt 3: Failed]
    Fail3 -->|Wait: 800ms| Fail4[Attempt 4: Success or Terminate]
```

---

## 2. Progression Table Example ($T_{\text{base}} = 100\text{ ms}$, $T_{\text{max}} = 5000\text{ ms}$)
| Retry Attempt ($a$) | Mathematical Wait Time | Cumulative Elapsed Time |
| :--- | :--- | :--- |
| **Attempt 0 (Immediate)** | $0\text{ ms}$ | $0\text{ ms}$ |
| **Attempt 1** | $100\text{ ms} \times 2^0 = 100\text{ ms}$ | $100\text{ ms}$ |
| **Attempt 2** | $100\text{ ms} \times 2^1 = 200\text{ ms}$ | $300\text{ ms}$ |
| **Attempt 3** | $100\text{ ms} \times 2^2 = 400\text{ ms}$ | $700\text{ ms}$ |
| **Attempt 4** | $100\text{ ms} \times 2^3 = 800\text{ ms}$ | $1,500\text{ ms}$ |
| **Attempt 5** | $100\text{ ms} \times 2^4 = 1,600\text{ ms}$ | $3,100\text{ ms}$ |
