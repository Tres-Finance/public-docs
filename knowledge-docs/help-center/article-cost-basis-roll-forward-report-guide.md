# Cost Basis Roll Forward | TRES Finance Help Center

Source: https://help.tres.finance/article/cost-basis-roll-forward-report-guide

# Cost Basis Roll Forward

Period-over-period cost basis movement: opening balance, inflows, outflows, fees, realized gains, and closing balance per asset per wallet.

### Why use this report?

Bridges your opening cost basis to your closing cost basis for any date range. Shows exactly what came in (acquisitions), what went out (disposals with realized gains), and what remains. This is the report auditors and accountants need to reconcile cost basis movement and verify that realized gains tie to the P&L.

### Excel Tabs (3)

What It Shows

Open Timestamp, Close Timestamp, Open Org Cost Basis ($), Close Org Cost Basis ($)

Organization-level totals: opening and closing cost basis with timestamps.

Inventory Reconciliation

One per asset per wallet

Asset, Wallet, Open/Close Inventory (T), Open/Close Cost Basis ($), Inflow/Outflow/Fees (T and $), Realized Gains ($), Unrealized Gains ($)

The core reconciliation: ties opening to closing cost basis per wallet per asset.

raw_data

29 columns (see Key Columns below)

Full detail with platform, tags, balance IDs, and historical balance data.

### Key Columns

#### IDENTITY

What It Contains

Asset Name / Asset Symbol / Asset Class ID

Token identity.

Wallet Name / Wallet Address / Wallet Tags

Wallet identity.

Platform

Blockchain network.

#### OPENING POSITION

Open Timestamp

Start date of the period.

Open Total Inventory (T)

Token quantity at period start.

Open Org Cost Basis ($)

Cost basis at period start.

Open Historical Balance (T) / ($)

On-chain balance at period start (for reconciliation).

Open Unrealized Gains ($)

Unrealized gains at period start.

#### PERIOD FLOWS

Inflow (T) / Inflow ($)

Tokens and fiat value of acquisitions during the period.

Outflow (T) / Outflow ($)

Tokens and fiat value of disposals during the period.

Fees (T) / Fees ($)

Gas and network fees during the period.

Realized Gains ($)

Total realized gains/losses during the period.

#### CLOSING POSITION

Close Timestamp

End date of the period.

Close Total Inventory (T)

Token quantity at period end.

Close Org Cost Basis ($)

Cost basis at period end.

Close Historical Balance (T) / ($)

On-chain balance at period end.

Close Unrealized Gains ($)

Unrealized gains at period end.

### Use Cases

Use Case

Alternative Report

Period-end close

Use the Inventory Reconciliation tab to verify that Opening + Inflows - Outflows - Fees = Closing for each asset.

Realized gains reconciliation

Sum Realized Gains across all assets for the period. This should tie to your P&L.

Auditor deliverable

The Summary tab gives organization-level totals. The Inventory Reconciliation tab provides the breakdown. Together they form a complete cost basis roll forward.

Unrealized gains tracking

Compare Open vs Close Unrealized Gains to see how mark-to-market changed during the period.

### Related Reports

Extra Columns vs. This Report

Best For

Cost Basis Roll Forward

This report: period summary of cost basis movement

Period-end close, audit, P&L reconciliation

Asset Roll Forward

Same structure but for token quantities (not cost basis)

Asset quantity reconciliation

Cost Basis Stack Per Asset Cost Basis Stack Per Wallet

Individual tax lots at a point in time

Lot-level detail

Realized Gains & Losses

Transaction-level cost basis and gains

Per-transaction audit

Note: The period dates are set when you generate the report. Make sure Open Timestamp and Close Timestamp match your accounting period exactly.

Tip: The Safety Check formula: Open Inventory + Inflows - Outflows - Fees should equal Close Inventory. If it does not, investigate missing transactions.
