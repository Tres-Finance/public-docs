# Asset Fiat Values | TRES Finance Help Center

Source: https://help.tres.finance/article/asset-fiat-values-report-guide

# Asset Fiat Values

Hourly pricing data for every asset in your organization over a selected 24-hour period.

### Why use this report?

Shows the price TRES pulled for every asset, at every hour, for a selected day. Use this to verify that pricing is accurate, investigate fiat value discrepancies in other reports, or provide auditors with evidence of the pricing source used.

### Excel Tabs (1)

What It Shows

raw_data

One per asset per hour per platform

9 columns (see Key Columns below)

Hourly pricing data for all assets.

### Key Columns

#### ALL COLUMNS

What It Contains

Asset Class

Asset class name (e.g., Ethereum).

Asset Name

Specific token name.

Asset Symbol

Token ticker.

Asset Address

Contract address or 'native'.

Platform

Blockchain network.

Token price in reporting currency at this hour.

Currency

Reporting currency (e.g., usd).

Price Source

Pricing source: "regular_flow", "manual", etc. "regular_flow" refers to the Pricing Source your TRES workspace is configured to, which is selected in the Settings.

Datetime

Timestamp for this price point (hourly).

### Use Cases

Use Case

Alternative Report

Pricing verification

Compare TRES prices against external sources (CoinGecko, exchange APIs) for specific hours.

Fiat value discrepancy investigation

When a transaction's fiat value looks wrong, check what price TRES had at that hour.

Audit evidence

Provide auditors with the exact pricing data used for all valuations.

Cross-platform price comparison

The same asset on different platforms (e.g., ETH on Ethereum vs Arbitrum) should have similar prices. Spot anomalies.

### Related Reports

Extra Columns vs. This Report

Best For

Asset Fiat Values

This report: hourly pricing data

Price verification, audit evidence

Asset Balances

Current balances with unit prices

Current pricing per holding

Revaluation Report

Unrealized gains using fair value pricing

Mark-to-market, impairment

Note: This report covers a single 24-hour period. For multi-day pricing, you need to generate multiple exports.

Tip: If Price Source = 'manual', the price was overridden by a user. Check your organization's manual price entries if values seem unexpected.
