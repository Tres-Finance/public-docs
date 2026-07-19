# Asset Roll Forward | TRES Finance Help Center

Source: https://help.tres.finance/article/asset-roll-forward-report-guide

# Asset Roll Forward

Period-over-period asset quantity movement: opening balance, inflows, outflows, fees, and closing balance per asset per wallet with a safety check.

### Why use this report?

Answers 'how did our holdings change during this period?' for every asset in every wallet. Shows the opening balance, all inflows, all outflows, fees, and the closing balance, both in token quantities and fiat values. The Safety Check column flags any discrepancies. This is the auditor-ready asset movement summary.

### Excel Tabs (2)

What It Shows

Overview

Organization-level summary

Creation date, period dates, high-level totals

Report metadata and period information.

raw_data

One per asset per wallet

19 columns (see Key Columns below)

Full asset roll forward with opening, flows, closing, and safety check.

### Key Columns

#### IDENTITY

What It Contains

Wallet Name / Wallet Address

Wallet identity.

Asset Name / Asset Symbol

Token identity.

Currency

Reporting currency.

#### OPENING BALANCE

Open Historical Balance (T)

Token quantity at period start.

Open Historical Balance ($)

Fiat value at period start.

#### PERIOD FLOWS

Inflow (T) / Inflow ($)

Total tokens and fiat received during the period.

Outflow (T) / Outflow ($)

Total tokens and fiat sent during the period.

Fees (T) / Fees ($)

Total gas/network fees during the period.

#### CLOSING BALANCE

Close Historical Balance (T)

Token quantity at period end.

Close Historical Balance ($)

Fiat value at period end.

#### VALIDATION

Safety Check (T)

True if Open + Inflow - Outflow - Fees = Close. False flags a discrepancy.

Safety Check ($)

Same validation in fiat terms.

### Use Cases

Use Case

Alternative Report

Auditor deliverable

The primary report auditors request for asset movement during a period. The Safety Check column highlights issues.

Month-end reconciliation

Verify that opening balances plus net flows equal closing balances for every wallet.

Discrepancy investigation

Filter Safety Check (T) = False to find wallets/assets with unexplained balance changes.

Treasury reporting

Summarize inflows, outflows, and fees per asset for board or treasury reports.

### Related Reports

Extra Columns vs. This Report

Best For

Asset Roll Forward

This report: asset quantity movement per period

Audit, reconciliation, treasury reporting

Cost Basis Roll Forward

Same structure but for cost basis (not quantities)

Cost basis reconciliation, P&L

Ledger Reconciliation

On-chain vs. book balance comparison

Balance verification

Note: The report supports multiple opening dates (columns like 'Open Historical Balance (T) - 2020-05-17'). The column header includes the date, so check it matches your intended period.

Tip: A Safety Check = False does not always mean an error: it can indicate balance diff transactions, plugs, or rollup adjustments. Investigate before flagging as a discrepancy.
