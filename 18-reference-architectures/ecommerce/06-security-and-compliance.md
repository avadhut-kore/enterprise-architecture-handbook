# Security & PCI-DSS Compliance: E-Commerce Platform

## 1. Zero-Scope PCI-DSS v4.0 Architecture (SAQ A)
- Cardholder data (PAN, CVV) **never enters the enterprise network or cloud servers**.
- Frontend forms embed hosted tokenization fields (iFrames) directly from the PCI Level 1 payment gateway.
- The browser exchanges card credentials directly with the processor, receiving an opaque one-time payment token (`tok_123456`).
- The e-commerce backend only receives and stores the non-sensitive token, drastically reducing compliance audit scope from 300+ controls (SAQ D) to ~30 controls (SAQ A).
