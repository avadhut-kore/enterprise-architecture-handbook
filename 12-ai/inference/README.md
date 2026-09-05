# High-Performance Inference Architecture (`inference/`)

## Executive Summary

Optimizing foundation model inference requires extracting maximum token throughput and minimum latency from hardware.

This module details model quantization architectures, speculative decoding pipelines, and continuous batching schedulers.

---

## Directory Catalog

* **[Quantization Architectures: AWQ, GPTQ & FP8](quantization-architectures-awq-gptq-fp8.md)** — Reducing memory footprints by 75% with negligible accuracy degradation.
* **[Speculative Decoding Architecture](speculative-decoding-architecture.md)** — Accelerating generation speed by $2\times - 3\times$ using small draft models.
* **[Continuous Batching & Chunked Prefill](continuous-batching-and-chunked-prefill.md)** — Iteration-level scheduling and avoiding head-of-line blocking during inference.
