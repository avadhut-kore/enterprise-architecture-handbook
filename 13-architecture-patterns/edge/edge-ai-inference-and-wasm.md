# Edge AI Inference & WebAssembly (Wasm)

## 1. Shifting AI from Cloud to Client Edge

Executing foundation model inference in the cloud incurs severe token API bills and data privacy liabilities. Emerging edge architectures compile Small Language Models (SLMs: 1B–3B parameters) into **WebAssembly (Wasm)** or **WebGPU**, executing inference directly on client devices (laptops, smartphones):

```mermaid
flowchart TD
    WebUser["User Opens Web Application"] --> WasmDownload["Browser Downloads 1.5GB Quantized Model Weights (INT4)"]
    WasmDownload --> WebGPU["WebGPU Kernel / ONNX Runtime Web"]
    
    subgraph ClientSandbox ["Client Browser Memory (Zero Cloud Egress)"]
        Prompt["User Enters Sensitive Healthcare Data"] --> LocalModel["Local Wasm SLM Execution"]
        LocalModel --> LocalResponse["Private Instant Output (30 tokens/sec)"]
    end

    WebGPU --> ClientSandbox
```

---

## 2. Invariant: Absolute Data Privacy
Because model weights execute entirely inside client device memory, sensitive personal records **never leave the user's physical machine**, completely satisfying extreme GDPR and HIPAA data residency constraints.
