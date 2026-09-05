# C4 Level 1: System Context Diagram

The **System Context Diagram** establishes the boundary between the software system under design and the rest of the world. It shows the system in its environment, identifying human users and external software systems with which it interacts.

## When to Use
- Executive briefings, business stakeholder alignment, and Architecture Review Board (ARB) kickoffs.
- Defining project scope and identifying third-party vendor integrations.
- Onboarding new engineering personnel to the high-level operational domain.

## When NOT to Use
- Detailed technical design sessions, debugging discussions, or infrastructure provisioning.
- Do NOT include internal databases, ports, protocols, cloud services, or code details.

---

## Architecture Example: Global Wealth Management System

```mermaid
flowchart TD
    subgraph Users["Human Personas"]
        RetailClient["Retail Investor
[Person]
Manages personal investments and reviews portfolio performance."]
        Advisor["Wealth Advisor
[Person]
Provides advisory services and executes high-value client trades."]
        ComplianceOfficer["Compliance Auditor
[Person]
Monitors trades for AML, insider trading, and regulatory adherence."]
    end

    subgraph CoreSystem["System Boundary"]
        WealthPlatform["Global Wealth Management Platform
[Software System]
Enables retail clients and advisors to manage portfolios, execute trades, and analyze market performance."]
    end

    subgraph ExternalSystems["External Dependencies"]
        CoreBanking["Core Banking Ledger
[External System]
Maintains fiat settlement accounts, deposits, and wire transfers."]
        MarketData["Bloomberg / Refinitiv Feed
[External System]
Supplies real-time equity quotes, FX rates, and economic indices."]
        TradingExchange["Stock & Bond Exchange
[External System]
Executes and settles market equity and fixed-income orders."]
        NotificationHub["Twilio / SendGrid
[External SaaS]
Delivers transactional emails, SMS, and push notifications."]
    end

    RetailClient -->|Views portfolios & submits trades| WealthPlatform
    Advisor -->|Manages client accounts & recommends allocations| WealthPlatform
    ComplianceOfficer -->|Audits suspicious trades & generates reports| WealthPlatform

    WealthPlatform -->|Debits/Credits client settlement funds| CoreBanking
    WealthPlatform -->|Streams real-time market data| MarketData
    WealthPlatform -->|Transmits order executions| TradingExchange
    WealthPlatform -->|Sends multi-channel alerts| NotificationHub
```

---

## Related References
- [Context Template](./context-template.md)
- [Level 2 Container Diagram](./container.md)
- [Diagram Selection Guide](../diagram-selection-guide.md)
