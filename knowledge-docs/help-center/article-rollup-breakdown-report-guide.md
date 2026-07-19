# Rollup Breakdown | TRES Finance Help Center

Source: https://help.tres.finance/article/rollup-breakdown-report-guide

# Rollup Breakdown

### ROLLUP_BREAKDOWN

Expands rollup (aggregated) transactions back into their original individual on-chain transactions.

### Why use this report?

When TRES aggregates many small transactions into a single rollup entry (common for high-frequency wallets or staking rewards), this report lets you see the original individual transactions that were combined. Use it to verify rollup accuracy or when you need the raw on-chain detail behind a rollup.

### Excel Tabs (1)

What It Shows

raw_data

One per original transaction within a rollup

Same 46 columns as Transaction Ledger

The individual transactions that were aggregated into rollup entries.

### Key Columns

#### Same as Transaction Ledger

What It Contains

Timestamp

On-chain block timestamp of the original transaction.

Transaction Hash

Original on-chain tx hash (before rollup).

Belongs To / 3rd Party

Wallet and counterparty for each original transaction.

Original Amount / Currency Symbol

Token quantity and ticker for each individual movement.

Balance Impact (T) / Total Fiat Amount ($)

Signed quantity and fiat value per original transaction.

Direction / Event Label

Classification of each original transaction.

Platform

Blockchain network.

Is Rollup?

Will be False here since these are the expanded originals.

### Use Cases

Use Case

Alternative Report

Rollup verification

Compare the sum of expanded transactions against the rollup entry in the Transaction Ledger to verify accuracy.

Granular staking analysis

When staking rewards are rolled up daily, use this to see each individual reward event.

Audit detail

Auditors may request individual transaction hashes rather than aggregated entries.

### Related Reports

Extra Columns vs. This Report

Best For

Transaction Ledger

46 columns: includes rollup entries as single rows

Day-to-day monitoring with rollups

Rollup Breakdown

This report: same columns, different scope

Expanding rollups to individual txs

Note: This report only contains data if your organization uses rollup aggregation. If no transactions have been rolled up, the export will be empty.

Tip: To find which transactions in the Transaction Ledger are rollups, filter Is Rollup? = True. Then use this report to see what they contain.
