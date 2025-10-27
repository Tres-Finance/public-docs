# Ledger Page

## Overview

The Ledger page is the central hub for viewing and managing all digital asset transactions across your organization. It provides comprehensive financial transaction tracking with detailed information about inflows, outflows, fees, tags, ERP integration status, and more.

The Ledger page displays all transaction data in a table format, organized into five main tabs, each serving a specific purpose for financial management and reporting.

## Tabs

### 1. Transactions Tab

The **Transactions** tab displays the complete transaction history with the most comprehensive view of all your digital asset transactions.

#### Light Ledger Toggle

A toggle switch is available in the Transactions tab header to switch between two views:

- **Regular Ledger View**: Shows full transaction details with all columns
- **Light Ledger View**: Simplified accounting view for easier review and tracking

#### Table Columns

The Transactions table displays the following columns:

- **Checkbox**: Select individual transactions for bulk operations
- **Transaction ID/Name**:
  - Transaction identifier (hash or custom name)
  - Timestamp in format: HH:MM:SS am/pm, Mon DD, YY
  - Transaction hash (truncated with ellipsis)
  - External link to blockchain explorer (Etherscan, Solscan, Mintscan, etc.)
- **Inflow**: Amount received and its USD equivalent (shows asset symbol and amount, then USD value)
- **Outflow**: Amount sent and its USD equivalent
- **Fees**: Transaction fees (displays as negative values with asset symbol and amount)
- **Tags**: Classification tags applied to transactions (e.g., OPERATIONS, STAKING REWARDS, LOWCASETAG, YONI!, etc.)
- **ERP**: ERP system integration status with action buttons

#### Pagination

The table supports pagination with:

- Items per page selector (default: 20)
- Total count display (e.g., "out of 620")
- Page navigation controls (First, Previous, Current Page of Total, Next, Last)
- Current page indicator (e.g., "1 of 31")

#### Actions

- **Expand all**: Expand all collapsed transaction rows to view detailed information
- **Row interaction**: Click on any transaction row to view additional details

### 2. Cost Basis Tab

The **Cost Basis** tab provides detailed cost basis calculations for your digital assets. This tab is only visible when cost basis calculation is enabled in your organization settings.

**Note**: The tab is disabled if no cost basis currencies are configured in your organization settings.

### 3. Pending Transactions Tab

The **Pending Transactions** tab shows transactions that are pending data collection. These transactions appear as regular transactions once the data collection process is complete.

#### Features

- Information icon with a tooltip explaining pending transactions
- Ability to manually trigger data collection if needed
- Transactions marked with pending status
- Same table structure as the Transactions tab

### 4. Roll Forward Tab

The **Roll Forward** tab enables you to create powerful roll-forward tables based on time periods, cost basis, or asset movement. This feature is available through the Actions menu.

#### Creating Roll Forward Tables

- Click the "Insert data table" button (green plus icon) next to the Roll Forward tab
- Complete the three-step form:
  1. **Step 1**: Configure basic roll-forward settings
  2. **Step 2**: Define data table parameters
  3. **Step 3**: Review and confirm

#### Viewing Roll Forward Data

- When no roll-forward tables exist, you'll see an empty state with the option to "Insert Data Table"
- When tables exist, they display in the Roll Forward view with edit, delete, and duplicate options

### 5. Pivot Tables Tab

The **Pivot Tables** tab allows you to create pivot tables from your ledger data for analysis and reporting.

#### Creating Pivot Tables

- Click the "Insert table" button (green plus icon) next to the Pivot Tables tab
- Pivot tables help analyze transaction data from different perspectives
- Limited to transactions under a certain threshold for performance

#### Availability

- This tab is only available when the pivot table feature is enabled
- Requires data to be loaded in the ledger before creating pivot tables

## Filters

The Ledger page provides comprehensive filtering options to help you find specific transactions quickly.

### Main Filter Buttons

1. **Date Range**: Default "Last 30 days" with custom date picker
2. **AI Search**: Natural language search for transactions
3. **Hash**: Search by transaction hash
4. **From/To**: Filter by sender or recipient addresses
5. **Assets**: Filter by specific digital assets
6. **Tags**: Filter by transaction tags
7. **Networks**: Filter by blockchain networks
8. **Integrations**: Filter by ERP integration status
9. **Amount Transferred**: Filter by transaction amount ranges
10. **More Filters**: Additional advanced filtering options

### Saved Filters

- **Save filters**: Save your current filter configuration for quick access later
- Saved filters can be loaded and applied instantly

## Actions Menu

The Actions button in the top-right corner provides access to various ledger management functions:

### Available Actions

1. **Add transaction**: Manually add a new transaction to the ledger
   - Opens a modal with options to add transactions via CSV upload or manual entry
   - CSV upload feature includes AI-powered mapping for automatic field detection
2. **Calculate cost basis**: Trigger cost basis calculation for your configured currencies
   - Opens the cost basis calculation modal
   - Shows progress and status of calculation
3. **Insert data table**: Create a new roll-forward data table
   - Opens the roll-forward table creation wizard
   - Create customizable roll-forward reports based on time periods
4. **Insert table**: Create a new pivot table
   - Available when certain conditions are met (data threshold, permissions)
   - Create pivot tables for data analysis
5. **Reconcile**: Open the reconciliation sidebar
   - Compare ledger balances with actual balances
   - Identify discrepancies and resolve issues
6. **Revaluate**: Revaluate your assets at current market prices
   - Opens the revaluation modal to update asset prices
   - Applies current market values to your assets
7. **Price feed**: Configure manual fiat value pricing
   - Opens the price feed configuration modal
   - Set custom price feeds for assets
8. **Spec ID Rules**: Configure Spec ID rules for transaction identification
   - Opens the Spec ID rules configuration modal
   - Define rules for automatic transaction categorization

## ERP Integration Column

The ERP column shows the integration status of each transaction with your ERP system (e.g., QuickBooks, NetSuite, Xero).

### Common Status Values

- **Ready to Sync**: Transaction is ready to be synced to ERP
- **Unable to Sync**: Transaction cannot be synced (may require attention)
- **Synced**: Transaction has been successfully synced
- **Sync Failed**: Sync attempt failed (check error details)
- **Changed after sync**: Transaction was modified after being synced

### ERP Action Buttons

Each transaction in the ERP column has action buttons that provide:

- Quick actions for syncing, unsyncing, or modifying the sync status
- Error details when sync fails
- Retry options for failed syncs

### Transaction-Level Actions

Clicking the "More actions" button (three dots) next to any transaction in the ERP column opens a context menu with the following options:

- **Mark as**: Mark the transaction with a specific status or attribute
- **Reclassify**: Change the transaction classification or category
- **Add note**: Add comments or notes to the transaction
- **Copy transaction hash**: Copy the transaction hash to clipboard
- **Copy method ID**: Copy the method ID to clipboard
- **Copy transaction link**: Copy the blockchain explorer link to clipboard
- **Delete transaction**: Permanently delete the transaction from the ledger
- **Manage sub-transactions**: Access sub-transaction management and editing options

### Bulk Actions

#### Row-Level Actions

When you select a transaction row (using the checkbox), additional bulk actions become available:

1. Click the checkbox next to one or more transactions
2. A bulk actions menu appears with options to:
   - Apply actions to all selected transactions simultaneously
   - Batch operations for efficient management
   - Export selected transactions

#### Inner Row Actions

For transactions with internal rows (sub-transactions), clicking on the inner row reveals additional context-specific actions:

- View detailed sub-transaction breakdown
- Edit individual sub-transaction details
- Add or remove sub-transactions
- Manage linked sub-transactions

## Export Functionality

The **Export Report** button in the header allows you to export your filtered ledger data:

- Export current view with applied filters
- Available only when data is loaded
- Supports various export formats (depending on configuration)

## Additional Features

### Reconciliation Sidebar

Click the "Reconcile assets" button at the bottom of the page to open the reconciliation sidebar, which helps you:

- Compare ledger balances with actual balances
- Identify discrepancies
- Reconcile assets across different accounts

### Transaction Details

Clicking on any transaction row expands to show:

- Detailed sub-transaction breakdown
- Additional metadata
- Comments and notes
- Related documents or invoices

## Workflow Examples

### Viewing Recent Transactions

1. Navigate to the Ledger page
2. Ensure you're on the Transactions tab
3. The default view shows "Last 30 days"
4. Scroll through transactions or use pagination

### Filtering by Network

1. Click the "Networks" filter button
2. Select the desired network(s) (e.g., Ethereum, Solana)
3. Apply the filter
4. View only transactions from selected networks

### Syncing Transactions to ERP

1. Find transactions with "Ready to Sync" status in the ERP column
2. Click the action button on the transaction
3. Select sync options if prompted
4. Monitor status change in the ERP column

### Creating a Roll Forward Table

1. Ensure you have transaction data loaded
2. Click the Actions menu
3. Select "Insert data table"
4. Follow the three-step wizard:
   - Configure date range or criteria
   - Define table structure
   - Name and save the table
5. Access your roll-forward tables in the Roll Forward tab

### Managing Individual Transactions

1. Find the transaction you want to manage in the table
2. Click the "More actions" button (three dots) in the ERP column
3. Choose from available options:
   - **Mark as**: Set transaction status or attributes
   - **Reclassify**: Change transaction category
   - **Add note**: Attach comments or notes
   - **Copy transaction hash**: Copy for reference
   - **Copy method ID**: Copy method identifier
   - **Delete transaction**: Remove from ledger (with confirmation)

### Performing Bulk Actions

1. Select one or more transactions using the checkboxes
2. A bulk actions menu automatically appears
3. Choose the action you want to apply to all selected transactions:
   - Batch update tags
   - Export selected transactions
   - Apply filters or classifications
   - Modify multiple transactions simultaneously

### Working with Sub-Transactions

1. Click on any transaction row to expand it and view sub-transactions
2. Click "Manage sub-transactions" from the More actions menu
3. In the sub-transactions view:
   - Edit individual sub-transaction details
   - Add new sub-transactions
   - Remove or merge sub-transactions
   - View linked transactions

## Tips

- Use the AI Search filter for natural language queries (e.g., "show all staking rewards in October")
- Save frequently used filter combinations for quick access
- Switch to Light Ledger view for simplified accounting transactions
- Use the expand all button to review detailed transaction information at once
- Check ERP sync status regularly to ensure all transactions are properly integrated
