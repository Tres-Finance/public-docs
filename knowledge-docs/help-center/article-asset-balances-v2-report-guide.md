# Asset Balances V2 | TRES Finance Help Center

Source: https://help.tres.finance/article/asset-balances-v2-report-guide

# Asset Balances V2

Enhanced asset balance snapshot with a cleaner layout, summary pivot table, and cost basis tab. Same underlying data as Asset Balances.

### Why use this report?

An improved version of the Asset Balances report with a cleaner Excel layout designed for sharing with stakeholders. The summary pivot table and cost basis tab make it easier to get high-level numbers without diving into raw data. Same underlying data, better presentation.

### Excel Tabs (3)

What It Shows

Asset Balances - PT

Pivot table summary

Aggregated balances by asset class and platform with fiat values

High-level summary: total holdings per asset. Designed for executive/board reporting.

Cost Basis

One per asset class

Asset Class Symbol, Sum of Amount (T), Sum of Fiat Value ($), Sum of Total Cost ($)

Aggregate cost basis per asset class with totals.

raw_data

One per balance record

36 columns (same as Asset Balances)

The complete dataset: every balance record with full metadata.

### Key Columns

#### SAME AS ASSET BALANCES

What It Contains

Asset Symbol / Asset Name

Token ticker and full name.

Amount (T)

Token quantity held.

Fiat Value ($)

Current fiat value.

Unit Price ($)

Current price per token.

Balance State

wallet, locked, claimable, liquid, or delegated.

Platform

Blockchain network.

Account Name / Account Address

Wallet name and address.

Total Cost ($) / Unrealized Gains ($)

Cost basis and unrealized gain/loss.

Balance Timestamp / Commit Time

When fetched and when committed.

Position Name / Application

DeFi position and application if applicable.

Asset Verification Status

"verified" or "unverified".

### Use Cases

Use Case

Alternative Report

Board / executive reporting

Use the Asset Balances PT tab for a clean summary without raw data noise.

Cost basis summary

The Cost Basis tab aggregates by asset class: perfect for financial statement line items.

Sharing with external parties

The cleaner layout makes this better than V1 for sharing with auditors or investors.

### Related Reports

Extra Columns vs. This Report

Best For

Asset Balances

Same data, more pivot tabs (By Wallet, By Platform, By Position)

Detailed analysis and wallet-level audit

Asset Balances V2

This report: cleaner layout, summary + cost basis tabs

Reporting and sharing

Asset Balances Archives

Historical snapshots at any past date

Month-end close, time capsule

Note: The raw_data tab is identical to Asset Balances V1. The difference is in the pivot tabs: V2 has a cleaner summary layout while V1 has more granular breakdowns (By Wallet, By Platform, By Position). Choose based on your audience.

Tip: If you need both the detailed pivot breakdowns (V1) and the clean summary (V2), export both. They use the same data snapshot.
