# Integrations Page | TRES Finance Help Center

Source: https://help.tres.finance/article/integrations

# Integrations Page

The Integrations page is your central hub for connecting TRES with external systems and services to streamline your financial workflows. By integrating with ERP systems, payment platforms, communication tools, and development APIs, you can automate data synchronization, reduce manual entry, and ensure accurate financial records across all your business systems.

Key benefits of Integrations:

Sync with ERP systems (QuickBooks, Xero, Netsuite) for seamless accounting.

Automate invoice and salary management with Request Finance or Deel integration.

Build custom workflows using the GraphQL API.

### Tabs and Status

The Integrations page organizes available services into two main tabs.

#### 1. Connected Tab

Displays only the integrations that are currently active and connected to your TRES account.

View Configuration: Access detailed settings and sync status (e.g., QuickBooks).

Disconnect: Remove the integration (e.g., Slack).

#### 2. All Integrations Tab

Displays the complete catalog of available integrations, including both connected and available-to-connect services.

### ERP Integrations

TRES Finance's ERP integrations transform raw blockchain data into structured, compliant accounting entries:

Automated Data Synchronization: TRES automatically pulls transaction data from connected wallets, processes it, and stages it for export to your ERP system. This drastically reduces manual data entry and minimizes human error.

Chart of Accounts (COA) Mapping: This is the core accounting function. The integration allows you to map specific crypto transactions (e.g., staking rewards, gas fees, sales proceeds) to the correct account codes (e.g., Revenue, Expense, Asset accounts) within your ERP's COA. This ensures accurate categorization and journal entries.

Real-time Status Monitoring: You can monitor the status of every transaction as it moves from TRES into the ERP, checking for transactions that are Completed, Pre-Sync, Failed, or Ignored. This ensures data integrity and helps resolve sync errors promptly.

AP/AR Management: Integrations help match incoming and outgoing crypto payments to outstanding invoices and bills (Accounts Payable/Accounts Receivable) within your ERP.

Compliance & Audit Readiness: By ensuring every transaction is properly valued, categorized, and recorded in your system of record, the integration makes your crypto holdings audit-ready and simplifies tax preparation.

After successfully connecting an ERP system (like QuickBooks, Xero, or Netsuite), the TRES Finance platform provides a dedicated management interface to monitor sync health, define accounting rules, and manage operational tasks. For more information, refer to this guide.

#### Available Integrations:

QuickBooks ERP - User-friendly accounting software for small businesses and freelancers.

Automated transaction syncing, custom mapping rules, real-time ERP status monitoring.

Xero - Easy-to-use online accounting software designed specifically for small businesses.

Cloud-based, real-time reporting, multi-currency support.

Netsuite ERP - Cloud-based ERP solution for comprehensive business management and scalability.

Enterprise-grade financial management, advanced multi-entity and multi-currency capabilities.

Universal ERP - Allows manual upload and management of your chart of accounts for any ERP system not directly integrated.

Upload chart of accounts, enabling mapping of transactions to accounts, and export-ready transaction.

### Finance Integrations

These integrations link the operational side of your business (paying people, sending bills) directly to the financial reporting and accounting layer in TRES. By connecting these systems, TRES automatically tracks the purpose (invoice, salary) and the counterparty for payments, making the resulting transactions instantly ready for classification and audit.

Request Finance - Seamlessly adds invoices and salaries to transactions for easy ERP export.

Invoice management, salary payment integration, direct ERP export functionality.

Deel - Hire and pay anyone, anywhere with accounting that stays in sync.

Global payroll management, automatic transaction sync with TRES, compliance management.

### Communication and Developer Tools

The Communication and Developer Tools integrations are designed to extend the TRES platform's data and notification capabilities beyond the TRES application itself.

Slack - Turns TRES updates into real-time Slack messages.

Real-time notifications for transaction updates, reconciliation alerts, cost basis completion.

GraphQL Playground - Automate crypto finance workflows using the TRES GraphQL endpoint.

Full API access, query transactions/wallets/assets programmatically, build custom dashboards.
