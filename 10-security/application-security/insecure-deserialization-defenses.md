# Insecure Deserialization Architecture

## Executive Summary

Insecure deserialization occurs when untrusted byte streams are converted back into objects in memory, allowing attackers to instantiate malicious gadget chains that achieve Remote Code Execution (RCE).

---

## Architectural Mandates
1. **Ban Executable Object Serialization**: Completely eliminate Java Native Serialization (`ObjectInputStream`), Python `pickle`, Ruby `Marshal`, and PHP `unserialize()` from all networked systems.
2. **Standardize on Pure Data Formats**: Use pure data interchange formats that do not allow arbitrary class instantiation: **JSON**, **Protocol Buffers (Protobuf)**, or **Avro**.
