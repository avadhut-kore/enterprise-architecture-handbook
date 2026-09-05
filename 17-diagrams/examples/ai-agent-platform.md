# Enterprise Generative AI Agent Platform Architecture

This reference architecture models a secure enterprise Generative AI agent platform orchestrating multi-agent collaboration, semantic RAG retrieval, sandboxed external tool execution, and real-time prompt guardrails.

## 1. Business Context & Architectural Drivers
* **Autonomous Task Execution**: Enable autonomous agents to deconstruct high-level business goals, select appropriate APIs, and execute multi-step workflows.
* **Enterprise Security & DLP**: Prevent Prompt Injection (OWASP LLM01) and redact sensitive PII/secrets before sending context to external foundation models.
* **Deterministic Sandboxing**: Isolate all LLM-generated code execution inside ephemeral, network-restricted microVMs with strict memory and CPU caps.

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph EnterpriseUsers ["Knowledge Workers & Developers"]
        Engineer["Software Engineer<br/>[Person]<br/>Requests code refactoring and bug investigation"]
        Analyst["Financial Analyst<br/>[Person]<br/>Requests multi-quarter earnings syntheses"]
    end

    subgraph AIAgentPlatform ["Enterprise GenAI Agent Platform"]
        AgentCore["Agent Orchestration Platform<br/>- Multi-Agent Orchestrator (ReAct Loop)<br/>- Enterprise RAG Knowledge Hub<br/>- Ephemeral Code Sandbox Runner<br/>- Prompt Guardrails & Auditing"]
    end

    subgraph ModelAndTools ["External Foundation Models & Tools"]
        AzureOpenAI["Azure OpenAI (GPT-4o)"]
        AnthropicClaude["Anthropic Claude 3.5 Sonnet"]
        InternalGit["Enterprise GitHub Enterprise"]
        InternalSQL["Corporate PostgreSQL Data Mart"]
    end

    Engineer --> AgentCore
    Analyst --> AgentCore
    AgentCore <-->|"Inference API"| AzureOpenAI
    AgentCore <-->|"Inference API"| AnthropicClaude
    AgentCore <-->|"Clones repos & reads code"| InternalGit
    AgentCore <-->|"Executes analytical queries"| InternalSQL
```

## 3. C4 Level 2: Multi-Agent Orchestration & Sandboxed Tool Execution

```mermaid
graph TB
    subgraph ClientLayer ["Client Interface"]
        WebCopilot["Enterprise Copilot Chat UI (React / Next.js)"]
    end

    subgraph SecurityGateTier ["Perimeter AI Gateway & Guardrails"]
        AIGW["LiteLLM AI Gateway"]
        Guardrails["NeMo Guardrails & Presidio PII Redactor"]
        WebCopilot --> AIGW
        AIGW --> Guardrails
    end

    subgraph AgentOrchestrationMesh ["Agent Orchestration Core (LangGraph / Python)"]
        Supervisor["Agent Supervisor / Planner Node"]
        ResearcherAgent["Research Agent (RAG Vector Search)"]
        CoderAgent["Coding Agent (Code Synthesis & Testing)"]
        DataAnalystAgent["SQL Analyst Agent (DB Query Generation)"]

        Guardrails --> Supervisor
        Supervisor --> ResearcherAgent
        Supervisor --> CoderAgent
        Supervisor --> DataAnalystAgent
    end

    subgraph ToolSandboxTier ["Sandboxed Tool Execution (Firecracker microVMs)"]
        SandboxMgr["MicroVM Sandbox Manager (Fly.io / Firecracker)"]
        PyREPL["Ephemeral Python Execution Pod"]
        SQLRunner["Read-Only DB Proxy Runner"]

        CoderAgent --> SandboxMgr
        DataAnalystAgent --> SandboxMgr
        SandboxMgr --> PyREPL
        SandboxMgr --> SQLRunner
    end

    subgraph KnowledgeAndModels ["Enterprise Knowledge & Models"]
        VectorDB[("Pinecone / Milvus Hybrid Vector DB")]
        FoundationLLM["Foundation LLMs (GPT-4o / Claude 3.5)"]

        ResearcherAgent <--> VectorDB
        Supervisor <--> FoundationLLM
        CoderAgent <--> FoundationLLM
    end
```

## 4. Multi-Agent Collaborative Task Execution Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Financial Analyst
    participant Super as Supervisor Agent
    participant Researcher as Research Agent (RAG)
    participant Coder as Python Code Agent
    participant Sandbox as Firecracker microVM
    participant LLM as Foundation Model (GPT-4o)

    User->>Super: "Analyze Q3 Revenue Growth and Plot a Bar Chart"
    Super->>LLM: Deconstruct Goal into Multi-Step Plan
    LLM-->>Super: Plan: 1. Fetch Q3 Numbers -> 2. Write & Execute Matplotlib Code
    
    Super->>Researcher: Step 1: Retrieve Q3 Financial Filings
    Researcher->>Researcher: Hybrid Vector Search (Cosine + BM25)
    Researcher-->>Super: Q3 Financial Summary Context Extracted
    
    Super->>Coder: Step 2: Generate Python Matplotlib Chart
    Coder->>LLM: Prompt: Generate code for Q3 Revenue chart
    LLM-->>Coder: Python Code Payload
    
    Coder->>Sandbox: Spin up Ephemeral microVM & Execute Code
    Sandbox->>Sandbox: Execute script, render chart.png
    Sandbox-->>Coder: Return Base64 chart.png + Exit Code 0
    Sandbox->>Sandbox: Destroy microVM immediately
    
    Coder-->>Super: Chart Rendered Successfully
    Super-->>User: Synthesized Financial Analysis + Embedded chart.png
```

## 5. Architectural Decisions
* **MicroVM Sandboxing**: All user- or LLM-generated code runs in ephemeral Firecracker microVMs that boot in 5ms and are destroyed immediately after execution.
* **Hybrid Search with Document ACLs**: Vector retrieval includes enterprise user authorization metadata, preventing analysts from accessing restricted executive filings.
