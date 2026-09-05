# GPU & Hardware Infrastructure Architecture (`gpu-infrastructure/`)

## Executive Summary

Deploying foundation models on enterprise infrastructure requires a deep understanding of GPU hardware constraints: High-Bandwidth Memory (HBM), NVLink interconnect fabrics, Tensor Core architectures, and PCIe host bottlenecks.

This module provides systems architects with the mathematical formulas and sizing frameworks required to design cost-effective GPU clusters.

---

## Directory Catalog

* **[GPU Hardware Architecture for Architects](gpu-hardware-architecture-for-architects.md)** — NVIDIA Hopper (H100/H200) and Blackwell (B200) architectures, SXM vs. PCIe form factors, and NVLink bandwidth.
* **[VRAM Sizing & KV Cache Calculations](vram-sizing-and-kv-cache-calculations.md)** — Mathematical formulations for calculating model weight VRAM, KV cache growth, and concurrency limits.
* **[Distributed GPU Parallelism](distributed-gpu-parallelism.md)** — Tensor Parallelism (TP), Pipeline Parallelism (PP), and Data Parallelism (DP) topologies.
