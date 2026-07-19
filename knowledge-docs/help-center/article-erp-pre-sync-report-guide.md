# ERP Pre-Sync | TRES Finance Help Center

Source: https://help.tres.finance/article/erp-pre-sync-report-guide

# ERP Pre-Sync

Preview of journal entries before they are synced to your ERP: chart of accounts mapping, debit/credit amounts, and configuration status.

### Why use this report?

Your control check before committing journal entries to the ERP. Shows every transaction mapped to its chart of accounts, with debit and credit amounts, classification rule used, and a configuration status flag. Catch errors (missing accounts, missing fiat values, wrong mappings) before they reach your ERP.

### Excel Tabs (2)

What It Shows

Chart of Accounts Summary

One per account

Chart of Account Type, Chart of Account Name, Sum of Debit, Sum of Credit

Aggregated debits and credits per account. Quick check: do the totals make sense?

raw_data

One per journal line (2+ lines per transaction)

58 columns (see Key Columns below)

Every journal entry line with full transaction context and COA mapping.

### Key Columns

#### TRANSACTION DATA (same as Transaction Ledger)

What It Contains

Timestamp / Transaction Hash / Sbx ID

Transaction identification.

Belongs To / 3rd Party

Wallet and counterparty.

Original Amount / Currency Symbol

Token quantity and ticker.

Balance Impact (T) / Total Fiat Amount ($)

Signed quantity and fiat value.

Direction / Event Label / Platform

Classification and chain.

#### JOURNAL ENTRY (unique to this report)

Is Well Configured?

Status flag: "Yes" or "Error: <reason>". Reasons: no_account_matched, missing_fiat, missing_cost_basis.

Line Amount Type

"Cost" or "Fair Value". Each transaction generates at least 2 lines.

Debit amount for this journal line.

Credit amount for this journal line.

Chart of Account Name

The account this line maps to (e.g., Fixed Assets, Finance Charge Income).

Chart of Account Type

Account type: asset, expense, income, liability, equity.

Chart of Account Code

Account code from your COA.

Is Inventory?

Whether this line affects inventory accounts.

Classification Rule Creator

Which rule created this mapping (or 'Error' if no rule matched).

#### METADATA

class_name / department_name

ERP classification and department mapping.

Transaction ID

TRES internal transaction ID.

### Use Cases

Use Case

Alternative Report

Pre-sync review

Filter Is Well Configured? != "Yes" to find transactions that will fail or produce incorrect journal entries.

Missing account mapping

Filter for "Error: no_account_matched" to find transactions without COA rules. Create rules before syncing.

Debit/credit verification

Use the Chart of Accounts Summary tab to verify total debits = total credits.

Rule testing

After creating new COA rules, regenerate this report to verify they map correctly before syncing.

### Related Reports

Extra Columns vs. This Report

Best For

ERP Pre-Sync

This report: preview before syncing

Control check, error detection, rule testing

ERP Post-Sync

Record of what was actually synced

Reconciliation, sync status tracking

Realized Gains & Losses

Transaction data with cost basis (no COA mapping)

Tax and gains analysis

Note: Transactions with Is Well Configured? = 'Error' will either fail to sync or produce incorrect entries. Always resolve errors before syncing to your ERP.

Tip: Each transaction produces at least 2 journal lines (one 'Cost' and one 'Fair Value'). Some produce more. The Chart of Accounts Summary tab gives you the aggregated view.
