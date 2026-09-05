# Configuration Architecture Principles

## 1. Core Principles
1. **Separation of Config from Code**: Never burn configuration into code binaries. A single container image must run identically in Dev, Staging, and Production.
2. **Hierarchy & Precedence**: Establish an explicit override hierarchy (Defaults $\rightarrow$ File $\rightarrow$ Environment Variables $\rightarrow$ Command-Line Arguments).
3. **Immutability per Instance**: An application should treat configuration objects as read-only once loaded.
