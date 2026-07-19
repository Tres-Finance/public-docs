# ERP Post-Sync | TRES Finance Help Center

Source: https://help.tres.finance/article/erp-post-sync-report-guide

# ERP Post-Sync

Record of all journal entries that have been synced to your ERP: transaction hash, date, debit/credit, account mapping, and sync status.

### Why use this report?

The audit trail of what TRES actually sent to your ERP. Shows every synced journal entry with its status (success, failed, pending), the debit/credit amounts, and the chart of accounts mapping. Use this to reconcile what TRES sent against what your ERP received.

### Excel Tabs (1)

What It Shows

raw_data

One per synced journal line

8 columns (see Key Columns below)

Every journal entry line that was synced to the ERP.

### Key Columns

#### ALL COLUMNS

What It Contains

Transaction Hash

On-chain transaction hash. Join key with other reports.

Transaction Date

Date of the original transaction.

Syncing Status

"success", "failed", or "pending".

Debit amount for this journal line.

Credit amount for this journal line.

Chart of Account Code

Account code from your COA.

Chart of Account Name

Account name (e.g., Fixed Assets, Finance Charge Income).

Doc Number

ERP document/reference number (if returned by the ERP).

### Use Cases

Use Case

Alternative Report

Sync reconciliation

Compare this report against your ERP to verify all entries were received correctly.

Failed sync investigation

Filter Syncing Status = "failed" to find entries that need to be retried or fixed.

ERP audit trail

Provides evidence of exactly which journal entries TRES sent, when, and to which accounts.

### Related Reports

Extra Columns vs. This Report

Best For

ERP Post-Sync

This report: what was synced

Reconciliation, audit trail

ERP Pre-Sync

Preview before syncing

Control check, error detection

Note: This report only shows transactions that have been synced (or attempted). Transactions still in pre_sync status will not appear here. Use ERP Pre-Sync for those.

Tip: If Doc Number is empty, the ERP did not return a reference. This is normal for some ERP integrations. Use Transaction Hash + Transaction Date to match manually.
