# API & Integration Throughput Sizing Calculator

## 1. Formulas & Capacity Metrics

### A. Peak Requests Per Second (RPS)
$$\text{Peak RPS} = \frac{\text{Daily API Invocations}}{86,400} \times \text{Peak-to-Average Ratio (typically 3.0 to 5.0)}$$

### B. Gateway Bandwidth
$$\text{Network Bandwidth (Mbps)} = \frac{\text{Peak RPS} \times (\text{Request Size} + \text{Response Size}) \times 8}{1,000,000}$$
