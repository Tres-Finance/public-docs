# Cost Basis Inventory | TRES Finance Help Center

Source: https://help.tres.finance/article/cost-basis-inventory-report-guide

# Cost Basis Inventory

Per-sub-transaction inventory view showing how each acquisition builds up the cost basis stack.

### Why use this report?

Shows the cost basis inventory at the sub-transaction level: each inflow that added to your inventory, its quantity, and the cumulative inventory size. Use this to verify that all acquisitions are correctly tracked in the cost basis engine and to audit the inventory build-up over time.

### Excel Tabs (1)

What It Shows

raw_data

One per sub-transaction

11 columns (see Key Columns below)

Every sub-transaction that contributes to inventory, with running totals.

### Key Columns

#### IDENTIFICATION

What It Contains

sub transaction id

TRES internal ID for this sub-transaction.

tx identifier

Transaction hash on-chain.

timestamp

When this transaction occurred.

wallet name

Which wallet received this inflow.

#### INVENTORY DATA

balance impact

Token quantity added by this sub-transaction.

inventory size

Cumulative inventory quantity after this sub-transaction.

#### FLAGS

non taxable state

Whether this sub-transaction is marked non-taxable.

internal transfer sub transaction id

Linked sub-transaction ID if this is an internal transfer.

marked internal by tres

Whether TRES auto-detected this as internal.

marked internal by user

Whether a user manually marked this as internal.

severity

Data quality severity flag if any.

### Use Cases

Use Case

Alternative Report

Inventory verification

Check that all acquisitions are present and the running inventory size matches your expected balance.

Internal transfer audit

Use the internal transfer columns to verify that internal movements are correctly paired and not double-counted.

Non-taxable tracking

Filter by non_taxable_state to see which inflows are excluded from cost basis calculations.

### Related Reports

Extra Columns vs. This Report

Best For

Cost Basis Inventory

This report: sub-transaction level inventory build-up

Inventory verification, internal transfer audit

Cost Basis Stack Per Asset

Cost Basis Stack Per Wallet

Individual tax lots with purchase price and unrealized gains

Lot-level analysis, tax-loss harvesting

Cost Basis Roll Forward

Period summary: opening/closing cost basis with flows

Period reconciliation, financial statements

Note: This report shows inventory at the sub-transaction level, not at the lot level. For individual tax lots with purchase prices and unrealized gains, use Cost Basis Stack per Asset or Cost Basis Stack per Wallet instead.

Tip: The inventory size column is cumulative: each row shows the total inventory after that sub-transaction. The last row for each wallet/asset combination is the current inventory.
