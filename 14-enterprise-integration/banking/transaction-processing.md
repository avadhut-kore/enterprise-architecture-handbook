# Transaction Processing and Real-Time Posting Engine

## 1. Real-Time Balance vs. Available Balance
In banking integration, systems must strictly differentiate between:
- **Ledger Balance (Book Balance)**: Authoritative posted balance accounting for settled funds.
- **Available Balance**: Ledger balance minus active authorization holds and pending uncleared deposits.

$$	ext{Available Balance} = 	ext{Ledger Balance} - \sum 	ext{Active Holds} + \sum 	ext{Immediate Credit}$$

## 2. Double-Entry Posting Rules
Every integration transaction hitting the core ledger must produce balanced debits and credits:
```
Transaction: ATM Withdrawal $100
Debit:  Customer Demand Deposit Account (Liability)  $100.00
Credit: ATM Cash Vault Transit Account (Asset)       $100.00
Total Debit == Total Credit (Balanced)
```
