# Transaction Ledger | TRES Finance Help Center

Source: https://help.tres.finance/article/transaction-ledger-report-guide

# Transaction Ledger

#### A complete list of every blockchain transaction across all wallets. One row per token movement, with sender, receiver, amount, fiat value, classification, and chain.

### Why use this report?

The foundational report in TRES. Every other transaction report builds on the same data with extra columns. This one is the lightest and fastest to generate: ideal for daily monitoring, sharing with external parties, or feeding downstream systems that only need core transaction fields.

### Excel Tabs (5)

What It Shows

Summary Per Asset

One per asset

Asset Symbol, Sum of Balance Impact (T), Sum of Total Fiat Amount ($), split by Platform

Net token flows and fiat totals per asset. Quick check: "how much moved per token?"

Summary per Tx Activity

One per wallet

Wallet Name, Sum of Total Fiat Amount ($), split by Transaction Activity

Fiat totals by activity type (transfer, swap, etc.) per wallet.

Summary per SubTx Label

Wallet Name, Sum of Total Fiat Amount ($), split by Sub Transaction Label

Fiat totals by sub-tx type (gas, native_transfer, token_transfer). Best for isolating fee spend.

Summary per 3rd Party

One per counterparty + asset

3rd Party, Original Currency Symbol, Sum of Balance Impact (T), split by Platform

Volume grouped by counterparty, asset, and chain. See who you transact with most.

raw_data

One per token movement

46 columns (see Key Columns below)

The complete dataset. Filter, sort, and build custom analysis on this tab.

### Key Columns (raw_data)

The raw_data tab has 46 columns. Below are the most important ones. Remaining columns (Year, Month, Day, Time, Block Number, Method ID, Function Name, External Account ID, Additional Data, etc.) provide supporting detail.

#### Identification

What It Contains

Timestamp

On-chain block timestamp (UTC). Format: YYYY-MM-DD HH:MM:SS.

Transaction Hash

On-chain tx identifier. Use to look up on a block explorer or join with other TRES reports.

TRES internal sub-transaction ID. Unique per row.

#### Wallet & Counterparty

Belongs To

Your wallet name (as set in TRES). Pair with Belongs To Address for the on-chain address.

3rd Party

Counterparty name (registered contact label or raw address). "native" appears for gas fees.

From / To Address

Sender and receiver blockchain addresses with resolved names where available.

#### Asset & Amount

Original Amount

Raw token quantity moved (always positive). Direction indicates sign.

Original Currency Symbol

Token ticker (ETH, USDC, etc.). Currency Group Symbol maps wrapped variants to the same class.

Contract Address

Token contract. Null for native coins.

Asset Verification Status

"verified" or "unverified". Unverified tokens may lack pricing.

#### Classification

Direction

inflow, outflow, or fees. Determines the sign of Balance Impact.

Event Label

Human-readable classification: "Send Coins", "Receive Coins", "Pay Fee", "Swap", "Claim Reward", etc.

Sub Transaction Label

Technical label: "gas", "native_transfer", "token_transfer", "swap_in", etc.

Transaction Activity

High-level grouping (e.g., "transfer native coins", "swap tokens").

#### Fiat Values

Transfer Unit Fiat Price ($)

Token price in reporting currency at time of transaction.

Balance Impact (T)

Signed token quantity change. Negative for outflows/fees, positive for inflows.

Total Fiat Amount ($)

Fiat value of the balance impact (Balance Impact x Unit Price).

#### Chain & Flags

Platform

Blockchain network: "ethereum", "polygon", "arbitrum", "bitcoin", "tezos", etc.

Protocols / Applications

JSON arrays of detected DeFi protocols and dApps.

Is Internal?

True if transfer is between two of your own wallets.

Is Rollup?

True if this row is an aggregated (rollup) entry rather than an individual tx.

Whether the tx succeeded on-chain. Failed transactions still show gas fees.

### Use Cases

Use Case

Alternative Report

Daily monitoring

Filter by date, sort by Timestamp. Use the "Summary per Tx Activity" tab for a one-glance breakdown.

Fee tracking

Filter Direction = "fees". The "Summary per SubTx Label" tab already isolates gas totals per asset.

Counterparty analysis

Use the "Summary per 3rd Party" tab. Identify unlabeled addresses (raw hex) and register them as contacts.

Audit / external sharing

Filter by Year, export as XLSX. Built-in pivot tabs give auditors summary views out of the box.

Pair with Asset Roll Forward and Ledger Reconciliation.

Data pipeline / ERP staging

Export as CSV for your data warehouse. Core 46 columns without cost basis complexity.

Need cost basis? Use Realized Gains & Losses.

### Related Reports

Four reports share the same transaction-level data. The difference is how many extra columns each adds:

Extra Columns vs. This Report

Best For

Transaction Ledger

Baseline: 46 columns

Daily ops, data exports, counterparty analysis

Realized Gains & Losses

+21 columns: cost basis, realized gains, running balance, ERP accounts

Tax reporting, capital gains, lot-level audit

Cost Breakdown

+28 columns: everything above + per-lot COGS breakdown (purchase date, hash, amount)

Tracing exactly which acquisition lot was consumed

Rollup Breakdown

Same 46 columns, different scope

Expanding rollup entries into their original transactions

This report does NOT include cost basis, realized gains, running balances, or ERP account mappings. If you need any of those, use Realized Gains & Losses or Cost Breakdown. For point-in-time balance snapshots, use Asset Balances or Balance Trends.

Export tip: XLSX for analysis (pivot tables work out of the box), CSV for data pipelines. For 100k+ transactions, filter by date/wallet first or use SFTP/Snowflake delivery.
