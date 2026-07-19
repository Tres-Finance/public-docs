# Cost Breakdown Raw Transactions | TRES Finance Help Center

Source: https://help.tres.finance/article/cost-breakdown-report-guide

# Cost Breakdown Raw Transactions

### COST_BREAKDOWN_RAW_TRANSACTIONS

Everything in Realized Gains & Losses plus a per-lot COGS breakdown showing which acquisition lot was consumed in each disposal.

### Why use this report?

The deepest transaction-level export in TRES. When a disposal happens, this report shows exactly which acquisition lot(s) were consumed: the purchase date, purchase hash, quantity from that lot, fiat value, and realized gain per lot. Essential for FIFO/LIFO verification and tax-lot tracing.

### Excel Tabs (1)

What It Shows

raw_data

One per token movement per lot consumed

74 columns (67 from Realized Gains + 7 COGS Breakdown columns)

The complete dataset. Rows may duplicate if a single disposal consumed multiple lots.

### Key Columns

#### All Realized Gains Columns

What It Contains

(All 67 columns)

Identical to the Realized Gains & Losses report: Timestamp, Transaction Hash, amounts, cost basis, realized gains, ERP accounts, etc.

#### COGS Breakdown (unique to this report)

COGS Breakdown Amount

Token quantity consumed from this specific acquisition lot.

COGS Breakdown Fiat Value

Fiat cost of the consumed quantity at the original purchase price.

COGS Breakdown Realized Gains

Realized gain/loss attributed to this specific lot.

COGS Breakdown Date of Purchase

Date when this lot was originally acquired.

COGS Breakdown Tx Hash

Transaction hash of the original acquisition.

COGS Breakdown Purchased By Name

Wallet name that originally acquired this lot.

COGS Breakdown Purchased By Identifier

Wallet address of the original acquisition.

COGS Breakdown Purchased By Platform

Blockchain network of the original acquisition.

### Use Cases

Use Case

Alternative Report

FIFO/LIFO verification

Check that COGS Breakdown Date of Purchase follows your cost basis method order. Oldest dates first = FIFO.

Tax-lot tracing

For any disposal, see exactly which acquisition(s) were consumed and the gain/loss per lot.

Cross-wallet lot tracking

The Purchased By Name/Identifier columns reveal if a lot was originally acquired by a different wallet (after internal transfers).

Auditor requests

When auditors ask 'where did this cost basis come from?', this report provides the full chain from acquisition to disposal.

### Related Reports

Extra Columns vs. This Report

Best For

Transaction Ledger

46 columns: core data only

Daily ops, simple exports

Realized Gains & Losses

67 columns: adds cost basis and gains

Tax reporting, capital gains

Cost Breakdown

This report: 74 columns

Per-lot COGS tracing, FIFO/LIFO verification

Note: This is the heaviest transaction report to generate. A single disposal that consumed 10 acquisition lots produces 10 rows. Expect larger files than Realized Gains & Losses. Only use this when you need lot-level detail. Note that you can filter the report for only one transaction hash or small timeframe to reduce report size and generation time.

Tip: Rows can repeat: if one outflow consumed 3 lots, you will see 3 rows with the same Transaction Hash but different COGS Breakdown values. The main columns (Realized Gains, COGS) show the total, while the breakdown columns show the per-lot split.
