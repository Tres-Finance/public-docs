# Trial Balances | TRES Finance Help Center

Source: https://help.tres.finance/article/trial-balances

# Trial Balances

### Overview

The Trial Balances tab acts as a bridge between your crypto data in TRES and your ERP. It provides a summarized view of your trial balance organized by Account Type.

Primary Use Case: This tool is designed for Reconciliation. It allows you to compare TRES "Pre-Sync" balances against your current ERP balances to ensure accuracy before you finalize and sync your data.

Note: This tab is only visible if you have an Active ERP Connection.

### What It Shows

The table provides a high-level financial summary with the ability to drill down into specifics.

#### Structure:

Account Type Summary: The main view groups data by high-level ERP categories: Assets, Liabilities, Equity, Revenue, and Expenses.

Balance Columns:

TRES Pre-Sync: Displays the Debit and Credit totals based on the data currently processed in TRES but not yet synced.

ERP Balances: Displays the actual Debit and Credit totals currently sitting in your ERP for comparison.

Grand Totals: The footer of the table shows the aggregate totals for Debits, Credits, and the Difference, ensuring your trial balance is zeroed out.

Expandable Rows: You can click on any Account Type row (e.g., "Assets") to expand it. This reveals the specific Account-Level Balances (e.g., "Digital Asset Inventory", "Gas Fees") that make up that category.

### How to Use It

1. Upon loading, the system automatically fetches the latest trial balance status and summary.

#### 2. Filtering the View

Use the filter bar at the top to define your reconciliation scope:

Date: Select the Snapshot Date for the trial balance. (Defaults to the latest available date).

Important Note on Date Filtering: The Trial Balance calculation is computed for the entire history of your ledger to ensure ongoing accuracy. When you apply a Date filter, the table displays a cumulative snapshot of your balances as of that specific date. It represents the state of your accounts at that exact point in time.

Account Name: Filter to view specific ERP accounts only.

Account Type: Filter to isolate specific categories (e.g., check only "Expenses").

#### 3. Recalculating Data

If you have made changes to transactions or mappings, you need to refresh the numbers.

Click the "Recalculate" button.

Status Indicators: You may see a "Running" status. The system is calculating the latest Pre-Sync data (and fetching ERP data if supported). The table will auto-refresh once the status changes to "Complete."

#### 4. Analysis & Review

Drill Down: Expand the rows to compare specific accounts.

Check Discrepancies: Look for differences between the TRES column and the ERP column to identify missing transactions or mapping errors.

#### 5. Exporting

For external analysis or audit documentation:

Click the Three-Dot Menu (Ellipsis) in the top right.

Export as CSV.
