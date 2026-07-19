# Realized Gains & Losses | TRES Finance Help Center

Source: https://help.tres.finance/article/realized-gains-losses-report-guide

# Realized Gains & Losses

### EXTENDED_RAW_TRANSACTIONS

Everything in the Transaction Ledger plus cost basis, realized gains/losses, running balances, and ERP account mappings. One row per token movement.

### Why use this report?

The most complete transaction-level export in TRES. Use it whenever you need not just what happened on-chain, but the financial impact: cost basis consumed, realized gain or loss, and how the inventory changed. Essential for tax filing, capital gains calculations, and lot-level audit trails.

### Excel Tabs (4)

What It Shows

Summary Per Asset

One per asset

Asset Symbol, Sum of Balance Impact (T), Sum of Total Fiat Amount ($), split by Platform

Net token flows and fiat totals per asset.

Summary Per Year

One per asset per year

Year, Currency Group Symbol, Sum of Balance Impact (T), Sum of Total Fiat Amount ($)

Annual breakdown of token flows. Useful for tax-year summaries.

Summary per Tx Activity

One per wallet

Wallet Name, Sum of Total Fiat Amount ($), split by Transaction Activity

Fiat totals by activity type per wallet.

raw_data

One per token movement

67 columns (see Key Columns below)

The complete dataset with all cost basis and gains columns.

### Key Columns

#### Identification

What It Contains

Timestamp

On-chain block timestamp (UTC).

Transaction Hash

On-chain tx identifier. Join key with other TRES reports.

TRES internal sub-transaction ID. Unique per row.

Transaction ID

TRES internal transaction-level ID (groups sub-transactions).

#### Wallet & Counterparty

Belongs To

Your wallet name.

3rd Party

Counterparty name or raw address. "native" for gas fees.

From / To Address

Sender and receiver addresses with resolved names.

#### Asset & Amount

Original Amount

Raw token quantity (always positive).

Original Currency Symbol

Token ticker (ETH, USDC, etc.).

Balance Impact (T)

Signed token quantity change to your wallet.

Total Fiat Amount ($)

Fiat value of the balance impact.

Transfer Unit Fiat Price ($)

Token price at time of transaction.

#### Classification & Chain

Direction

inflow, outflow, or fees.

Event Label

"Send Coins", "Receive Coins", "Swap", etc.

Platform

Blockchain network (ethereum, polygon, etc.).

Is Internal?

True if transfer between your own wallets.

#### Cost Basis & Gains (unique to this report)

Running Balance After (T)

Token balance in this wallet after this transaction.

Cost Basis Before ($)

Total cost basis in this wallet before this transaction.

Cost Basis After ($)

Total cost basis after. The difference reveals what was consumed.

Realized Gains ($)

Gain or loss realized on this disposal (proceeds minus COGS).

Short Term Realized Gains ($)

Portion of realized gains classified as short-term.

Long Term Realized Gains ($)

Portion classified as long-term.

COGS ($)

Cost of goods sold: the cost basis consumed by this outflow.

Proceeds ($)

Fair market value received (for disposals).

Acc. Running Balance After (T)

Accumulated running balance across all wallets for this asset.

Total Running Inventory Quantity (T)

Total inventory quantity across all wallets after this tx.

#### ERP Mapping (unique to this report)

ERP Flow Account Name

Chart of accounts: flow account mapped to this transaction.

ERP Inventory Account Name

Chart of accounts: inventory (asset) account.

ERP Gain/Loss Account Name

Chart of accounts: gain/loss account.

#### Flags

Financial Attribute

Financial classification metadata.

Counter Transfers

Related counter-transfers for swaps/trades.

Internal Transfer

Internal transfer pairing information.

### Use Cases

Use Case

Alternative Report

Tax reporting

Filter by Year. Use Realized Gains ($) for capital gains. Short/Long Term columns split by holding period.

Capital gains reconciliation

Sum Realized Gains ($) per asset per year. Compare against your tax advisor's calculations.

Cost basis audit

Review Cost Basis Before/After for each disposal. Verify COGS matches your cost basis method (FIFO, LIFO, etc.).

ERP pre-check

Review ERP Flow/Inventory/Gain-Loss account columns before syncing. Catch misclassified transactions early.

For the actual journal entry preview, use ERP Pre-Sync.

Lot-level analysis

Use Running Balance After and COGS to trace how inventory moves transaction by transaction.

For per-lot breakdown of which acquisition was consumed, use Cost Breakdown.

### Related Reports

Extra Columns vs. This Report

Best For

Transaction Ledger

Baseline: 46 columns (no cost basis)

Daily ops, simple exports

Realized Gains & Losses

This report: 67 columns

Tax, capital gains, cost basis audit

Cost Breakdown

+7 more columns: per-lot COGS detail

Tracing specific acquisition lots consumed

Rollup Breakdown

Same as Transaction Ledger, different scope

Expanding rollup entries

Note: This report includes all Transaction Ledger columns plus 21 additional cost basis and ERP columns. It takes longer to generate than the Transaction Ledger because it runs cost basis calculations. If you only need core transaction data, use the Transaction Ledger for faster exports.

Tip: The Short/Long Term Realized Gains split depends on your organization's cost basis method and holding period rules configured in TRES settings.
