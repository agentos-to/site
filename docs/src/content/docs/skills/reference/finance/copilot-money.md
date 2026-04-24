---
title: Copilot Money
description: "Read accounts, transactions, and balance history from Copilot Money, a personal finance app for macOS/iOS"
sidebar:
  label: copilot-money
---

| Metadata | Value |
|---|---|
| **Category** | `finance` |
| **Capabilities** | `sql` |
| **Website** | <https://copilot.money> |

## Returns shapes

- [`financial_account[]`](/shapes/reference/financial_account/) — from `load_accounts`
- [`transaction[]`](/shapes/reference/transaction/) — from `fetch_transactions`

## Readme

Read accounts, transactions, and balance history from [Copilot Money](https://copilot.money/).

## Requirements

- **macOS only** — reads from Copilot's local SQLite database and widget JSON files
- **Copilot installed and synced** — the app must be installed, logged in, and have synced at least once
- **Full Disk Access** — System Settings > Privacy & Security > Full Disk Access (for the agentOS server process)

## Data Sources

| Data | Source |
|------|--------|
| Accounts | `~/Library/Group Containers/group.com.copilot.production/widget-data/widgets-account-account_*.json` |
| Transactions | `CopilotDB.sqlite` → `Transactions` table |
| Balance history | `CopilotDB.sqlite` → `accountDailyBalance` table |

## Capabilities

```
OPERATION              ENTITY TYPE    DESCRIPTION
---------------------  -------------  ----------------------------------------
account.list           account        All accounts with balances and institution
transaction.list       transaction    Recent transactions with optional filters
transaction.search     transaction    Search by merchant, category, or notes
```

## Notes

- This skill is **read-only**
- Data reflects what Copilot has synced from Plaid — real-time balances may lag slightly
- Accounts are tagged `financial` on the graph and linked to institution organizations
