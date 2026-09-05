# Chaos Engineering & Production Game Days

## Executive Summary

Chaos engineering intentionally injects failure into systems to build confidence in their automated resilience mechanisms.
- **Principles**: Formulate a steady-state hypothesis $\rightarrow$ simulate failure (kill AZ, inject 200ms latency, partition Redis) $\rightarrow$ verify that SLOs and automated failovers hold.
