# Reports Page

## Overview

The Reports page is your central hub for generating, accessing, and analyzing financial reports. It provides a comprehensive interface for exporting various types of financial data into downloadable formats (Excel, CSV) for accounting, compliance, and business intelligence purposes.

All reports are automatically generated and can be downloaded, analyzed with AI assistance through TRES Analyst, or managed through various filtering and search capabilities.

## Report Table

The Reports page displays all generated reports in a table format with the following columns:

### Columns

- **Name**: The custom or auto-generated name of the report
- **Category**: The classification of the report (assets, accounts, ledger, general, positions)
- **Type/Format**: The specific report type (e.g., Balance Trends, Transaction Ledger, ERP Rules)
- **Created at**: Timestamp showing when the report was generated
- **Status**: Current state of the report (Done, Processing, Failed)

## Available Report Types

The "Export Report" button in the header opens a modal displaying all available report types organized by category. Below are the main report types:

### Ledger Reports

Reports focused on transaction data and accounting entries:

- **Transaction Ledger**: Comprehensive export of all transaction data with detailed information about inflows, outflows, fees, tags, and transaction metadata
- **ERP Pre-Sync**: Pre-synchronization report for ERP systems, containing formatted transaction data ready for export to accounting software
- **Cost Basis Review**: Detailed review of cost basis calculations for digital assets

### Assets Reports

Reports focused on asset balances, valuations, and historical trends:

- **Balance Trends**: Historical balance trends showing asset values over time, useful for portfolio analysis and performance tracking
- **Cost Basis Stack Per Asset**: Detailed cost basis stacks for each asset, showing acquisition costs and layering for tax calculations
- **Asset Balances - Archives**: Archived balance snapshots showing historical asset holdings at specific points in time

### Accounts Reports

Reports focused on wallet and contact management:

- **ERP Rules**: Export of all ERP mapping rules and configurations
- **Account Summary**: Overview of all wallets, contacts, and account structures

### General Reports

Cross-category reports and error logs:

- **Cost Basis Error Log**: Log of all cost basis calculation errors, warnings, and issues requiring attention
- **Inventory Reports**: Custom inventory reports for specific assets

### Positions Reports

Reports focused on derivatives, lending positions, and complex financial instruments (if applicable to your organization).

## Filters

The Reports page provides multiple filtering options to help you find specific reports:

### 1. Date Range Filter

Filter reports by creation date:

- **Last 30 days** (default): Shows reports created in the last month
- **All Time**: Displays all reports regardless of creation date
- Custom date ranges (if available)

### 2. Category Filter

Filter by report category:

- **assets**: Asset-related reports
- **accounts**: Account and wallet reports
- **ledger**: Transaction and ledger reports
- **general**: Miscellaneous and error logs
- **positions**: Position-specific reports

### 3. Type Filter

Filter by specific report type (Balance Trends, ERP Rules, Transaction Ledger, etc.)

### 4. Search Functionality

Use the search bar at the top to search for reports by name or keywords.

### 5. Clear All

Click "Clear all" to reset all applied filters.

## Per-Report Actions

Each report row includes the following actions:

### 1. TRES Analyst (AI Chat)

Click the chat icon button to open TRES Analyst, an AI-powered assistant that can analyze and answer questions about your report data. This feature allows you to:

- Ask questions about report data
- Get insights and summaries
- Query specific transactions or balances
- Perform advanced analysis without downloading the report

See the "TRES Analyst Feature" section below for more details.

### 2. Download Report

Click the download link to download the report file directly to your computer. Reports are typically exported as:

- **Excel files (.xlsx)**: Most common format for financial reports
- **CSV files (.csv)**: For archived balances and simple data exports

### 3. Delete Report

Click the delete button (trash icon) to remove the report from your list. This action cannot be undone, but reports can be regenerated using the "Export Report" button.

## TRES Analyst Feature

**TRES Analyst** is an AI-powered report analysis tool that helps you interact with your financial data using natural language queries. Instead of downloading and manually analyzing reports, you can ask TRES Analyst questions and get instant answers.

### How to Use TRES Analyst

1. Click the chat icon button next to any report in the table
2. The TRES Analyst modal will open, showing suggested prompts
3. Select a suggested prompt or type your own question
4. TRES Analyst will analyze the report and provide answers based on your data

### Example Use Cases

TRES Analyst can help with various analysis tasks:

**Portfolio Analysis:**

- "What was my total daily networth between [date] and [date]?"
- "What was my daily networth per internal account between [date] and [date]?"
- "What was my daily exposure to [asset] between [date] and [date]?"

**Transaction Queries:**

- "Show all transactions on the [platform] between [date] and [date]"
- "Show all transactions sent to contact address [address] between [date] and [date]"
- "Show all transactions received from contact address [address] between [date] and [date]"

**Data Management:**

- "Set tag for transaction hash [hash] on the [network] to be [tag-name]"
- "Display wallets on [network]"
- "Create internal accounts [address] on [network] with name [wallet-name]"
- "Trigger data collect"

### Suggested Prompts

When you open TRES Analyst, you'll see a list of suggested prompts categorized by:

- **Networth Analysis**: Daily networth, account-level networth, asset class breakdowns
- **Exposure Analysis**: Asset-specific exposure over time
- **Transaction Queries**: Platform-specific, contact-specific, and date-range filtered transactions
- **Data Operations**: Tagging, wallet creation, data collection triggers

### Request Custom Prompts

If you can't find a suitable prompt for your specific need, use the "Request prompt" button to submit a request for a new prompt type. The TRES team will review and potentially add it to the available prompts.

## Status Indicators

Reports display various status indicators:

- **Done**: Report has been successfully generated and is ready for download or analysis
- **Processing**: Report is currently being generated (may take several minutes for large datasets)
- **Failed**: Report generation encountered an error and needs to be regenerated

## Generating New Reports

To generate a new report:

1. Click the "Export Report" button in the page header
2. A modal will open showing all available report types organized by category
3. Select the report type you want to generate
4. Configure any report-specific options (date range, filters, assets, etc.)
5. Click "Generate" or "Export"
6. The report will appear in the reports table with a "Processing" status
7. Once complete, the status will change to "Done" and you can download or analyze it

## Common Workflows

### Generating a Monthly Transaction Ledger

1. Click "Export Report"
2. Navigate to the "Ledger" category
3. Select "Transaction Ledger"
4. Set the date range to the desired month
5. Configure any additional filters (wallets, assets, tags)
6. Click "Generate"
7. Wait for the report to complete
8. Download the Excel file for your records

### Analyzing Balance Trends with TRES Analyst

1. Locate a "Balance Trends" report in the table (or generate a new one)
2. Click the TRES Analyst button (chat icon)
3. Select a suggested prompt like "What was my total daily networth between [dates]?"
4. Review the AI-generated analysis
5. Ask follow-up questions to dig deeper into specific trends

### Preparing for ERP Sync

1. Click "Export Report"
2. Navigate to the "Ledger" category
3. Select "ERP Pre-Sync"
4. Set the appropriate date range (e.g., last month, last quarter)
5. Generate the report
6. Download the formatted Excel file
7. Import into your ERP system (e.g., NetSuite, QuickBooks, SAP)

### Reviewing Cost Basis Errors

1. Click "Export Report"
2. Navigate to the "General" category
3. Select "Cost Basis Error Log"
4. Generate the report
5. Download and review all errors
6. Navigate to the Ledger page to resolve flagged transactions
7. Regenerate the cost basis

## Tips

- **Regular Exports**: Generate monthly reports for consistent record-keeping and easier reconciliation
- **Use TRES Analyst First**: Before downloading large reports, use TRES Analyst to query specific data points and save time
- **Archive Important Reports**: Download and store critical reports (year-end, audit-related) locally for compliance purposes
- **Filter by Date**: Use the date filter to find recent reports quickly
- **Descriptive Names**: When generating reports, use descriptive custom names to make them easier to find later
- **Monitor Status**: Large reports may take several minutes to process; check back later if status shows "Processing"
- **Clean Up Old Reports**: Periodically delete old or unnecessary reports to keep the page organized
