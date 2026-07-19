# Asset Balances - Archives | TRES Finance Help Center

Source: https://help.tres.finance/article/asset-balances-archives-report-guide

# Asset Balances - Archives

Historical balance snapshots from actual commit data. Contains every balance snapshot TRES has committed, letting you compare balances across multiple past dates.

### Why use this report?

This report stores every balance snapshot from actual data collection (commit) cycles. Unlike Asset Balances with Time Capsule (which reconstructs balances), Archives shows the exact data that was collected at each commit. Use Archives when you need commit-based snapshots or want to compare balances across multiple past dates in one export.

### Excel Tabs (4)

What It Shows

Fiat Value Summary

One per asset class

Asset Class Symbol, Asset Verification Status, Sum of Fiat Value ($) for each Commit Time

Fiat value over time per asset: one column per commit date. Track value changes across snapshots.

Amount Summary By Application

One per application + asset

Application, Balance Name, Asset Class Symbol, Verification Status, Amount (T) for each Commit Time

Token quantities over time grouped by DeFi application.

Amount Summary

Asset Class Symbol, Verification Status, Sum of Amount (T) for each Commit Time

Token quantities over time per asset class.

raw_data

One per balance record per commit

36 columns (same as Asset Balances)

Every historical balance record. Multiple rows per asset: one per commit date.

### Key Columns

#### SAME AS ASSET BALANCES

What It Contains

Asset Symbol / Asset Name / Asset Class Symbol

Token identity and asset class grouping.

Amount (T)

Token quantity at this commit date.

Fiat Value ($)

Fiat value at this commit date.

Unit Price ($)

Token price at this commit date.

Balance State / Platform / Account Name

Balance state, chain, and wallet.

Total Cost ($) / Unrealized Gains ($)

Cost basis and unrealized gains at this date.

#### TIME DIMENSION (key to this report)

Balance Timestamp

When the on-chain balance was fetched.

Commit Time

When TRES committed this snapshot. This is the date you filter on to get a point-in-time view.

### Use Cases

Use Case

Alternative Report

Month-end close

Filter raw_data by Commit Time closest to month-end date. This gives your balance snapshot for that date.

Asset Balances + Time Capsule (if no commit exists for that date)

Historical balance verification

Compare Commit Time snapshots to verify that balances reported at a past date were correct.

Balance trend analysis

The Fiat Value Summary and Amount Summary tabs show value/quantity across all commit dates as columns: instant trend view.

Audit evidence

Export the snapshot at a specific date as evidence of holdings at that point in time.

### Related Reports

Extra Columns vs. This Report

Best For

Asset Balances

Current snapshot only

Portfolio overview today

Asset Balances + Time Capsule

Reconstructed historical balances (no commit needed)

Quick historical lookup without needing a prior commit

Balance Trends

Current snapshot + previous balance comparison

Day-over-day change tracking

Note: This report contains one row per balance per commit date, so it can be very large. If you only need the latest snapshot, use Asset Balances instead. Filter by a specific Commit Time range to keep the export manageable.

Tip: For a quick one-off historical lookup at a specific date, use Asset Balances with Time Capsule enabled -- it's simpler and doesn't require a prior commit. Use Archives when you need to compare across multiple commit dates or need the exact data that was collected.
