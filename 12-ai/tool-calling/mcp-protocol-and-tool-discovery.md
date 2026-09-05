# Model Context Protocol (MCP) & Standardized Tool Integration

## 1. Beyond Proprietary Tool Plugins

Historically, connecting foundation models to enterprise systems required custom, proprietary integrations (OpenAI Assistants tools, LangChain tool wrappers, Semantic Kernel plugins).

The **Model Context Protocol (MCP)** establishes an open, vendor-neutral standard for exposing enterprise data, tools, and prompts to AI applications via a clean **Client-Host-Server architecture**.

```mermaid
flowchart TD
    subgraph HostApp ["MCP Host Application (IDE / AI Gateway / Chatbot)"]
        MCPClient["MCP Client Engine"]
    end

    subgraph MCPServers ["Isolated MCP Enterprise Servers"]
        direction TB
        Server1["MCP Server: Enterprise CRM\n- Tools: lookup_customer, update_lead\n- Resources: crm://customers/{id}"]
        Server2["MCP Server: PostgreSQL Core DB\n- Tools: execute_readonly_sql\n- Resources: db://schema/public"]
        Server3["MCP Server: Local Filesystem\n- Tools: read_file, search_directory\n- Resources: file:///workspace"]
    end

    MCPClient <-->|JSON-RPC 2.0 (stdio or SSE)| Server1
    MCPClient <-->|JSON-RPC 2.0 (stdio or SSE)| Server2
    MCPClient <-->|JSON-RPC 2.0 (stdio or SSE)| Server3
```

---

## 2. Core Architectural Primitives of MCP

### 2.1 Resources
* Read-only data payloads exposed via URI schemes (e.g., `postgres://prod-db/orders`). Provides direct contextual data without requiring tool execution.

### 2.2 Tools
* Executable functions that model clients can discover and invoke via standard JSON-RPC 2.0 requests.

### 2.3 Prompts
* Pre-packaged reusable prompt templates exposed by the server to guide clients on how to interact with the underlying enterprise domain.
