# Ledger Reconciliation | TRES Finance Help Center

Source: https://help.tres.finance/article/ledger-reconciliation-report-guide

# Ledger Reconciliation

#### Full reconciliation of on-chain (historical) balances against book (running) balances for every asset in every wallet, with five built-in check layers and a 57-column raw dataset.

### Why use this report?

The master reconciliation report in TRES. Compares your book balances (running ledger) to on-chain balances (historical snapshots) at both the opening and closing dates of a period, then validates flows in between. Six pivot tabs break the reconciliation into inventory, token, fiat, historical, and roll-forward checks so you can pinpoint exactly where a gap originates. Essential for month-end close sign-off, auditor deliverables, and investigating balance discrepancies.

### Excel Tabs (7)

What It Shows

12 attribute rows

Attribute, Running Fiat ($), Running Token (T), Historical Fiat ($), Historical Tokens (T)

Organization-level totals: opening balance, inflows, outflows, fees, realized gains, closing balance, expected closing, and the check result. One-glance pass/fail for the entire org.

Inventory Reconciliation

One per asset

Asset Class ID, Asset Name, Open/Close Total Inventory (T), Open/Close Org Cost Basis ($), Inflow/Outflow/Fees (T and $), Open/Close Unrealized Gains ($), Realized Gains ($), Check (T), Check ($)

Cost-basis-aware reconciliation per asset: ties opening inventory and cost basis to closing through flows and gains.

Running Token Reconciliation

Asset Class ID, Asset Name, Open/Close Running Balance (T), Inflow/Outflow/Fees (T), Check (T)

Token quantity check: does Opening + Inflows - Outflows - Fees = Closing for each asset's running balance?

Running Fiat Reconciliation

Asset Class ID, Asset Name, Open/Close Running Balance Fiat ($), Inflow/Outflow/Fees ($), Realized Gains ($), Open/Close Unrealized Gains ($), Check ($)

Fiat value check: same flow validation in reporting currency, including realized and unrealized gains.

Historical Token Reconciliation

Asset Class ID, Asset Name, Open/Close Running Balance (T), Open/Close Historical Balance (T), Check Open (T), Check Close (T)

On-chain vs. book token comparison: flags assets where the running balance drifts from the historical (on-chain) balance.

Historical Fiat Reconciliation

Asset Class ID, Asset Name, Open/Close Running Balance Fiat ($), Open/Close Historical Balance ($), Check Open ($), Check Close ($)

Same on-chain vs. book comparison in fiat terms.

Roll Forward Reconciliation

One per balance ID (wallet + asset)

Balance ID, Wallet Name/Address, Asset Name/Symbol, Platform, Asset Address, Open/Close Historical Balance (T), Inflow/Outflow/Fees (T), Expected Close (T), Historical Close - Expected Close

Per-wallet roll forward with an expected-vs-actual close check. The most granular reconciliation layer.

### Key Columns

#### IDENTITY

What It Contains

Asset Name / Asset Symbol / Asset Class ID

Token identity and internal asset class grouping.

Wallet Name / Wallet Address / Wallet Tags

Wallet identity and any applied tags.

Platform

Blockchain network.

Balance ID

TRES internal balance identifier (unique per wallet + asset + platform).

#### OPENING POSITION

Open Timestamp

Start date of the reconciliation period.

Open Running Balance (T) / ($)

Book balance (from the TRES ledger) at period start: token quantity and fiat value.

Open Historical Balance (T) / ($)

On-chain balance at period start: token quantity and fiat value.

Open Reversed Balance (T) / ($)

Reversed (adjusted) balance at period start, if applicable.

Open Diff (T) / ($)

Difference between running and reversed balances at open.

Open Unit Price ($)

Token price at period start.

Open Org Cost Basis ($) / Open Total Inventory (T)

Cost basis and inventory quantity at period start.

Open Last TX Hash / Open Last Tx Timestamp

Last transaction before the opening date.

#### CLOSING POSITION

Close Timestamp

End date of the reconciliation period.

Close Running Balance (T) / ($)

Book balance at period end.

Close Historical Balance (T) / ($)

On-chain balance at period end.

Close Reversed Balance (T) / ($)

Reversed balance at period end.

Close Diff (T) / ($)

Difference between running and reversed at close.

Close Unit Price ($)

Token price at period end.

Close Org Cost Basis ($) / Close Total Inventory (T)

Cost basis and inventory at period end.

Close Last TX Hash / Close Last Tx Timestamp

Last transaction before the closing date.

#### PERIOD FLOWS

Inflow (T) / Inflow ($)

Total tokens and fiat received during the period.

Outflow (T) / Outflow ($)

Total tokens and fiat sent during the period.

Fees (T) / Fees ($)

Gas and network fees during the period.

Realized Gains ($)

Realized gains/losses during the period.

Total Internal Transfers (T)

Token volume moved between your own wallets (should net to zero org-wide).

#### UNREALIZED GAINS & CHECKS

Open / Close Unrealized Gains ($)

Unrealized gains at period start and end.

Unrealized Gains Gap ($)

Change in unrealized gains across the period.

Open Balance with Close Unit Price ($)

Opening balance repriced at closing price: isolates price movement from quantity movement.

Open / Close Check Historical Balance (T) / ($)

Difference between running and historical balances. Zero means on-chain and book agree.

Slippage (T) / ($)

Unexplained gap between expected and actual balances after all flows are accounted for.

#### METADATA

Has Price?

Whether TRES has pricing for this asset. Missing pricing causes fiat check gaps.

Asset Address

Token contract address or "native".

Fiat Currency

Reporting currency used for fiat columns.

### Use Cases

Use Case

Alternative Report

Month-end close sign-off

Start with the Summary tab: if all Check rows are zero, balances are reconciled. Drill into specific tabs for any non-zero checks.

On-chain vs. book discrepancy

Use the Historical Token/Fiat Reconciliation tabs. Non-zero Check columns mean the running balance has drifted from the on-chain balance: investigate missing transactions or data collection gaps.

Roll-forward validation

Use the Roll Forward Reconciliation tab. The "Historical Close - Expected Close" column flags wallets where Opening + Inflows - Outflows - Fees does not equal the actual closing balance.

For cost-basis-focused roll forward, use Cost Basis Roll Forward.

Auditor deliverable

Export the full report: the Summary tab provides the organization-level check, and the five reconciliation tabs provide the supporting detail auditors need.

Slippage investigation

Filter raw_data by Slippage (T) or Slippage ($) != 0 to find wallets/assets with unexplained balance gaps after all known flows are accounted for.

### Related Reports

Extra Columns vs. This Report

Best For

Ledger Reconciliation

This report: 57 columns, 7 tabs, full on-chain vs. book reconciliation

Month-end close, auditor deliverable, discrepancy investigation

Asset Roll Forward

19 columns: opening/closing balances with flows and safety check

Simpler period-over-period quantity reconciliation

Cost Basis Roll Forward

29 columns: same structure focused on cost basis movement

Cost basis reconciliation, P&L tie-out

Asset Balances Archives

36 columns: historical balance snapshots

Point-in-time balance verification

Note: This is the most comprehensive reconciliation report in TRES. It cross-references running (book) balances, historical (on-chain) balances, reversed balances, and cost basis inventory across five different reconciliation layers. If you only need a simple roll-forward check, use Asset Roll Forward instead.

Tip: Start from the Summary tab and work your way down. If the org-level checks pass, you are reconciled. If not, move to Inventory Reconciliation to find the asset, then to Roll Forward Reconciliation to find the specific wallet.
