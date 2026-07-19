# Cost Basis Stack Per Asset and Cost Basis Stack Per Wallet | TRES Finance Help Center

Source: https://help.tres.finance/article/cost-basis-stack-report-guide

# Cost Basis Stack Per Asset and Cost Basis Stack Per Wallet

Individual tax lots (acquisition layers) for each asset in each wallet: purchase date, cost per unit, unrealized gains, and impairment data. If you track cost basis on a Universal (per Asset) configuration, you will use the Cost Basis Stack Per Asset report. If you track cost basis on a per Wallet configuration, you will use the Cost Basis Stack Per Wallet report.

### Why use this report?

Shows every individual tax lot in your portfolio: when it was acquired, at what price, how much remains, and the current unrealized gain or loss. This is the report you need for FIFO/LIFO analysis, tax-loss harvesting decisions, and lot-level audit. It also includes impairment and fair value data for accounting standards compliance.

### Excel Tabs (1)

What It Shows

raw_data

One per tax lot per wallet

22 columns (see Key Columns below)

Every open tax lot across all wallets.

### Key Columns

#### LOT IDENTITY

What It Contains

Asset Class Symbol / Asset Symbol

Asset class and specific token ticker.

Wallet Name / Wallet Address

Which wallet holds this lot.

Purchased By

Wallet that originally acquired this lot (may differ after internal transfers).

Purchase Platform

Blockchain where the acquisition happened.

#### COST DATA

Purchase Amount (T)

Token quantity in this lot (remaining after partial disposals).

Purchase Cost ($)

Total cost basis for this lot.

Purchase Cost Unit ($)

Cost per token at acquisition.

Purchase Timestamp

When this lot was acquired.

Purchase Hash

Transaction hash of the original acquisition.

#### FAIR VALUE & UNREALIZED GAINS

Fair Value ($)

Current fair market value of this lot.

Fair Value Unit ($)

Current price per token.

Fair Value Date

Date of the fair value pricing.

Unrealized Gains [Fair-Cost] ($)

Fair Value minus Purchase Cost. Positive = unrealized gain.

#### IMPAIRMENT (for accounting standards)

Min Price ($)

Lowest price observed during the holding period.

Min Price Date

When the minimum price occurred.

Min Price Start Date / End Date

Date range for the minimum price observation.

Min Pos. Value ($)

Position value at minimum price.

Unrealized Imp. [Cost-Min] ($)

Impairment: Cost minus Min Value. Used for ASC 350 impairment testing.

#### VERIFICATION

Verification

"verified" or "unverified". Whether the asset has confirmed pricing.

### Use Cases

Use Case

Alternative Report

Tax-loss harvesting

Filter by Unrealized Gains < 0 to find lots with unrealized losses. Sell to realize the loss before year-end.

FIFO/LIFO verification

Sort by Purchase Timestamp per asset. Under FIFO, the oldest lots should be consumed first.

Impairment testing (US GAAP)

Use Unrealized Imp. [Cost-Min] for ASC 350 impairment calculations. Min Price columns provide the evidence.

Fair value reporting (ASU 2023-08)

Use Fair Value and Unrealized Gains columns for fair value model reporting.

Lot-level audit

Provide to auditors as evidence of the full cost basis stack with acquisition details.

### Related Reports

Extra Columns vs. This Report

Best For

Cost Basis Stack Per Asset Cost Basis Stack Per Wallet

This report: Individual tax lots with purchase price and unrealized gains

Lot-level analysis, tax-loss harvesting

Cost Basis Inventory

Sub-transaction level inventory build-up

Inventory verification

Cost Basis Roll Forward

Period summary of cost basis changes

Financial statement reconciliation

Revaluation Report

Unrealized gains/losses for mark-to-market

Period-end revaluation

Note: This report shows open (remaining) lots only. Fully consumed lots do not appear. For the history of how lots were consumed, use the Cost Breakdown Raw Transactions report.

Tip: The Purchased By fields may differ from Wallet Name after internal transfers. This means the lot was originally acquired by one wallet and later transferred internally.
