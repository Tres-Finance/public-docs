# Asset Balances | TRES Finance Help Center

Source: https://help.tres.finance/article/asset-balances-report-guide

# Asset Balances

### RAW_BALANCES

Current snapshot of all asset holdings across your organization: quantity, fiat value, cost basis, and balance state per asset per wallet.

### Why use this report?

Your go-to report for answering 'what do we hold right now?' Provides the latest balance snapshot broken down by asset, wallet, platform, and position. Includes cost basis and unrealized gains. The 5 pre-built pivot tabs let you slice the data without building your own analysis.

### Excel Tabs (6)

What It Shows

By Asset

One per asset class + platform

Asset Class Symbol, Platform, Asset Symbol, Amount (T), Fiat Value ($), Unit Price ($), split by Balance State (wallet, locked, claimable, liquid)

Holdings grouped by asset. See total per token across all wallets.

By Wallet

One per wallet + platform + asset

Account Name, Platform, Asset Symbol, Amount (T), Fiat Value ($), split by Balance State

Holdings grouped by wallet. See what each wallet holds.

By Platform

One per platform + asset

Platform, Asset Symbol, Amount (T), Fiat Value ($), split by Balance State

Holdings grouped by blockchain network.

By Position

One per DeFi position + asset

Balance Name, Asset Symbol, Amount (T), Fiat Value ($), split by Balance State

Holdings grouped by staking/DeFi position.

Cost Basis

One per asset class

Asset Class Symbol, Sum of Amount (T), Sum of Fiat Value ($), Total Cost Basis ($)

Aggregate cost basis per asset class.

raw_data

One per balance record

36 columns (see Key Columns below)

The complete dataset: every balance record with full metadata.

### Key Columns

#### Asset Identity

What It Contains

Asset Symbol

Token ticker as it appears on-chain.

Asset Name

Full token name.

Asset Class Symbol

Normalized asset class (e.g., WETH maps to ETH).

Asset Type

native, token, or stable.

Contract Address

Token contract. Null for native coins.

Asset Verification Status

"verified" or "unverified".

#### Balance Data

Amount (T)

Token quantity held.

Fiat Value ($)

Current fiat value of the holding.

Unit Price ($)

Current price per token.

Balance State

wallet, locked, claimable, liquid, or delegated.

Balance Timestamp

When this balance was last fetched from chain.

Commit Time

When TRES committed this balance snapshot.

#### Wallet

Account Name

Wallet name as set in TRES.

Account Address

Blockchain address.

Account Tags

Tags assigned to this wallet.

#### Cost Basis

Total Cost ($)

Total cost basis for this holding.

Unrealized Gains ($)

Fiat Value minus Total Cost.

#### Position & Metadata

Platform

Blockchain network.

Position Name / Symbol

DeFi position name if applicable (e.g., staking position).

Application

DeFi application name.

Num of Transfers

Number of transactions for this balance.

Balance ID / Commit ID

TRES internal identifiers.

### Use Cases

Use Case

Alternative Report

Portfolio overview

Open the "By Asset" tab for a quick snapshot of total holdings per token.

Wallet audit

Use "By Wallet" tab to verify balances per wallet after onboarding or before month-end.

Cost basis review

Use the "Cost Basis" tab to see aggregate cost basis per asset. Compare against your accounting records.

Staking position check

"By Position" tab shows locked, claimable, and liquid balances per DeFi position.

Unverified token cleanup

Filter raw_data by Asset Verification Status = "unverified" to find tokens that may need attention.

### Time Capsule: Historical Balance Lookup

Asset Balances supports Time Capsule, check the Time Capsule box in the export dialog and set a past date. When enabled, TRES reconstructs your balances at that date without requiring a prior data collection (commit) to have been completed at that time. The exported report appears as "Historical Balance Format" in the report type column.

This is the easiest way to get historical balances for a specific date. Use it for month-end close, auditor balance confirmations, or any ad-hoc historical lookup.

If you specifically need balances from an actual commit snapshot (not reconstructed), use Asset Balances - Archives instead.

### Related Reports

Extra Columns vs. This Report

Best For

Asset Balances + Time Capsule

Reconstructed balances at any past date

Month-end close, auditor evidence, ad-hoc historical lookup

Asset Balances V2

Same data, improved layout + summary tab

Reporting and sharing

Asset Balances Archives

Historical snapshots from actual commit data

Multi-date comparison, commit-based audit evidence

Balance Trends

Same columns + previous balance for comparison

Period-over-period tracking

Wallet Balances

Per-wallet breakdown with balance states

Individual wallet verification

Note: This report shows the latest committed balance, not real-time. Balances are updated during each data collection cycle. Check the Balance Timestamp and Commit Time columns to see how fresh the data is.

Tip: The Balance State column is key: 'wallet' = freely available, 'locked' = staked/locked, 'claimable' = rewards ready to claim, 'liquid' = available in DeFi positions.
