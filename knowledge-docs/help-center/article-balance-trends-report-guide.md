# Balance Trends | TRES Finance Help Center

Source: https://help.tres.finance/article/balance-trends-report-guide

# Balance Trends

Current balance snapshot plus the previous balance for comparison: see how each holding changed between two data collection cycles.

### Why use this report?

Adds a 'before and after' dimension to your balance data. For each holding, you see both the current balance and the previous balance, letting you instantly spot changes, detect anomalies, and track movement between data collection cycles. The same pivot tabs as Asset Balances plus 4 extra columns.

### Excel Tabs (6)

What It Shows

By Asset

One per asset class + platform

Asset Class Symbol, Platform, Asset Symbol, Amount (T), Fiat Value ($), Unit Price ($), split by Balance State

Holdings grouped by asset with balance state breakdown.

By Wallet

One per wallet + platform + asset

Account Name, Platform, Asset Symbol, Amount/Fiat, split by Balance State

Holdings per wallet.

By Platform

One per platform + asset

Platform, Asset Symbol, Amount/Fiat, split by Balance State

Holdings per blockchain network.

By Position

One per position + asset

Balance Name, Asset Symbol, Amount/Fiat, split by Balance State

Holdings per DeFi position.

Cost Basis

One per asset class

Asset Class Symbol, Amount (T), Fiat Value ($), Max of Total Cost ($)

Cost basis summary.

raw_data

One per balance record

40 columns (36 from Asset Balances + 4 trend columns)

Full dataset with previous balance comparison.

### Key Columns

#### ALL ASSET BALANCES COLUMNS

What It Contains

Asset Symbol / Amount (T) / Fiat Value ($)

Current balance data (same 36 columns as Asset Balances).

Balance State / Platform / Account Name

Balance state, chain, wallet.

Total Cost ($) / Unrealized Gains ($)

Cost basis and unrealized gains.

#### TREND COLUMNS (unique to this report)

Previous Balance Timestamp

When the previous balance snapshot was taken.

Previous Amount

Token quantity in the previous snapshot.

Previous Fiat Value

Fiat value in the previous snapshot.

Previous Unit Price

Token price in the previous snapshot.

### Use Cases

Use Case

Alternative Report

Anomaly detection

Compare Amount vs Previous Amount. Large changes may indicate unexpected transfers or data issues.

Daily monitoring

Run daily: the trend columns show what changed since the last data collection cycle.

Price impact analysis

Compare Previous Fiat Value to Fiat Value: when Amount is unchanged but value changed, it is purely a price movement.

Board reporting

Use the By Asset or By Platform tabs for high-level portfolio summaries with built-in comparison.

### Related Reports

Extra Columns vs. This Report

Best For

Asset Balances

Current snapshot, no previous comparison

Simple portfolio overview

Balance Trends

This report: current + previous snapshot

Day-over-day change tracking

Asset Balances Archives

All historical snapshots across all dates

Full historical analysis

Note: The 'previous' balance refers to the prior data collection cycle, not the previous calendar day. The gap depends on your data collection frequency.

Tip: To calculate the change: Amount minus Previous Amount = token quantity change. Fiat Value minus Previous Fiat Value = total value change (includes both quantity and price movement).
