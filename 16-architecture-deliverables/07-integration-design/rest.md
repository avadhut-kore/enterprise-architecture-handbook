# REST Integration Standards
* Set mandatory timeouts: Connect timeout <= 2s, Read timeout <= 5s.
* Implement Resilience4j circuit breakers: Open circuit when failure rate exceeds 50% over 100 requests.
