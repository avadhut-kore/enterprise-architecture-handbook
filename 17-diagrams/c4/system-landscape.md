# C4 System Landscape Diagram

The **System Landscape Diagram** is an enterprise-level visualization showing all major software systems across the entire organization, identifying how value streams cut across organizational and technical boundaries.

```mermaid
flowchart TB
    subgraph Enterprise["Enterprise Software Landscape: Global Financial Institution"]
        subgraph RetailBanking["Retail Banking Domain"]
            OnlineBanking["Online & Mobile Banking
[System]"]
            LoanOrigination["Loan Origination System
[System]"]
            CreditCardEngine["Card Management System
[System]"]
        end

        subgraph WealthDomain["Wealth & Brokerage Domain"]
            WealthApp["Wealth Management Platform
[System]"]
            MarketFeeds["Market Data Ingestor
[System]"]
        end

        subgraph SharedCore["Shared Enterprise Services"]
            CoreLedger["Core Banking Ledger (Mainframe)
[System]"]
            EnterpriseIAM["Corporate Identity Provider (Okta)
[System]"]
            EnterpriseKafka["Enterprise Event Mesh (Kafka)
[System]"]
            DataLakehouse["Corporate Analytics Lakehouse
[System]"]
        end
    end

    OnlineBanking -->|Balances & Debits| CoreLedger
    LoanOrigination -->|Disbursements| CoreLedger
    CreditCardEngine -->|Authorizations| CoreLedger
    WealthApp -->|Settlement Fund Transfers| CoreLedger

    OnlineBanking -.->|Events| EnterpriseKafka
    WealthApp -.->|Events| EnterpriseKafka
    CreditCardEngine -.->|Events| EnterpriseKafka

    EnterpriseKafka -->|Raw Event Ingestion| DataLakehouse
    EnterpriseIAM -->|SSO Token Validation| OnlineBanking
    EnterpriseIAM -->|SSO Token Validation| WealthApp
```
