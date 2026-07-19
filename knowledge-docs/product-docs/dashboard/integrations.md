# Integrations Page

## Overview

The Integrations page is your central hub for connecting TRES with external systems and services to streamline your financial workflows. By integrating with ERP systems, payment platforms, communication tools, and development APIs, you can automate data synchronization, reduce manual entry, and ensure accurate financial records across all your business systems.

Integrations enable you to:

- **Sync with ERP systems** (QuickBooks, Xero, Netsuite) for seamless accounting
- **Automate invoice and salary management** with Request Finance or Deel integration
- **Build custom workflows** using the GraphQL API

## Tabs

The Integrations page organizes available integrations into two main tabs:

### 1. Connected Tab

The **Connected** tab displays only the integrations that are currently active and connected to your TRES account. This provides a quick view of all your active connections and their current status.

**Features:**

- View all active integrations at a glance
- Access configuration settings for connected integrations
- Monitor connection status and health

### 2. All Integrations Tab

The **All integrations** tab displays the complete catalog of available integrations, including both connected and available-to-connect services.

**Features:**

- Browse all available integrations
- See which integrations are already connected
- Connect new integrations with a single click
- Discover recommended integrations for your workflow

## Available Integrations

### ERP Integrations

ERP (Enterprise Resource Planning) integrations sync your digital asset transactions with your accounting software, enabling automated journal entries, reconciliation, and financial reporting.

#### QuickBooks

**Description:** User-friendly accounting software designed for small businesses and freelancers.

**Status:** Connected (in demo environment)

**Key Features:**

- Automated transaction syncing to your Chart of Accounts
- Real-time ERP status monitoring
- Custom mapping rules for transaction categorization
- Invoice and bill management (AP/AR)
- Sync status tracking with detailed breakdown

**Configuration Options:** View Configuration button available (see detailed section below)

#### Xero

**Description:** Easy-to-use online accounting software designed specifically for small businesses.

**Status:** Available to connect

**Key Features:**

- Cloud-based accounting platform
- Real-time financial reporting
- Bank reconciliation
- Multi-currency support
- Automated transaction categorization

**Note:** Connection currently disabled in demo environment

#### Netsuite

**Description:** Cloud-based ERP solution for comprehensive business management and scalability.

**Status:** Available to connect

**Key Features:**

- Enterprise-grade financial management
- Advanced multi-entity and multi-currency capabilities
- Comprehensive reporting and analytics
- Scalable for growing organizations
- Full Chart of Accounts integration

**Note:** Connection currently disabled in demo environment

#### Universal ERP

**Description:** Upload and manage your chart of accounts manually, allowing you to use the TRES platform seamlessly with any ERP system not directly integrated.

**Status:** Available to connect

**Key Features:**

- Manual Chart of Accounts upload
- Works with any ERP system
- Custom account mapping
- Flexible categorization rules
- Export-ready transaction formats

**Note:** Connection currently disabled in demo environment

**Use Case:** Ideal for organizations using proprietary or less common ERP systems, or those who prefer manual control over account mapping.

### Payment and Finance Integrations

#### Request Finance

**Description:** Seamlessly add invoices and salaries to transactions and easily export to your ERP system.

**Status:** Connected (in demo environment)

**Key Features:**

- Invoice management and tracking
- Salary payment integration
- Direct ERP export functionality
- Automated transaction categorization
- Payment reconciliation

**Configuration:** Learn More button available for additional details

#### Deel

**Description:** Hire and pay anyone, anywhere—with accounting that stays in sync.

**Status:** Available to connect

**Badge:** 🏆 Recommended Integration

**Key Features:**

- Global payroll management
- Contractor and employee payment processing
- Multi-currency payment support
- Automatic transaction sync with TRES
- Compliance management for international payments

**Benefits:** Ideal for organizations with distributed teams, remote workers, or international contractors. Payments made through Deel automatically sync with TRES for seamless accounting.

### Communication Integrations

#### Slack

**Description:** Turn updates into Slack messages to get real-time notifications on changes in TRES.

**Status:** Available to connect

**Key Features:**

- Real-time notifications for transaction updates
- Alerts for reconciliation issues
- Cost basis calculation completion notifications
- Integration status alerts
- Team collaboration on financial data changes

**Important Note:** Make sure to select a public channel when connecting Slack to ensure proper message delivery.

### Developer Integrations

#### GraphQL Playground

**Description:** Automate your crypto finance workflows with the TRES platform by using our GraphQL endpoint.

**Status:** Available (always accessible)

**Key Features:**

- Full API access to TRES platform data
- Query transactions, wallets, assets, and reports programmatically
- Build custom dashboards and integrations
- Automate repetitive tasks
- Real-time data access

**Action:** Click "Play" to open the GraphQL Playground interface

**Use Cases:**

- Custom reporting and analytics
- Automated data exports
- Integration with internal business intelligence tools
- Building custom financial applications on top of TRES data

## Integration Configuration: QuickBooks Example

When you connect an ERP integration like QuickBooks, you gain access to a comprehensive configuration interface. Here's what you can manage:

### General Information

View essential connection details:

- **ERP connected:** Name of the connected ERP system (e.g., QuickBooks)
- **Account name:** Your organization's account name in the ERP system
- **Mail:** The email address associated with the ERP connection
- **ERP currency:** The base currency configured in your ERP system (e.g., USD)

### Syncing Status

Monitor the synchronization status of your transactions with a detailed breakdown:

- **Total transactions:** Total number of transactions being managed
- **Completed:** Transactions successfully synced to your ERP system
- **Pre-Sync:** Transactions staged and ready to be synced (awaiting approval or final review)
- **Failed:** Transactions that encountered errors during sync (requires attention)
- **Ignored:** Transactions excluded from sync based on your rules or settings

**Status Visualization:** The syncing status section displays a progress indicator showing the distribution across all statuses, making it easy to identify any sync issues at a glance.

### Configuration Sections

Click on any of these sections to manage specific aspects of your ERP integration:

#### 1. Rules

**Purpose:** Add default and custom rules to control how you manage transaction data to different Chart of Accounts.

**Features:**

- Create mapping rules for automatic transaction categorization
- Define default accounts for different transaction types
- Set up custom rules based on wallets, assets, or tags
- Override default categorization for specific scenarios

**Use Case:** Automatically map all exchange transactions to a specific revenue account, or route all NFT purchases to a separate asset account.

#### 2. AP/AR (Accounts Payable/Accounts Receivable)

**Purpose:** Explore and review all your linked invoices and bills from your ERP systems.

**Features:**

- View all invoices synced from your ERP
- Review outstanding bills and payables
- Match invoices to transactions
- Track payment status
- Reconcile invoice payments with blockchain transactions

**Use Case:** Match a USDC payment transaction to a specific vendor invoice in QuickBooks.

#### 3. Settings

**Purpose:** Sync and advanced settings for fine-tuning your integration.

**Features:**

- Configure sync frequency and timing
- Set up automatic sync triggers
- Manage authentication and connection details
- Define data mapping preferences
- Configure notification settings

**Use Case:** Set up daily automatic syncs at end of business day, or configure manual approval for all syncs.

## Connecting a New Integration

To connect a new integration:

1. Navigate to the "All integrations" tab
2. Browse the available integrations
3. Find the integration you want to connect
4. Click the "Connect" button next to the integration
5. Follow the authentication flow (you'll be redirected to the service's login page)
6. Grant TRES the necessary permissions
7. Complete any additional configuration steps
8. Return to the Integrations page to verify the connection status

**Note:** Some integrations may require additional setup or configuration after the initial connection.

## Managing Connected Integrations

### Viewing Configuration

For ERP integrations (like QuickBooks), click "View Configuration" to access:

- Connection details
- Syncing status and statistics
- Configuration options (Rules, AP/AR, Settings)

### Disconnecting an Integration

To disconnect an integration:

1. Click on the integration card or "View Configuration"
2. Look for the settings or options menu (typically in the top-right corner)
3. Select "Disconnect" or "Remove Integration"
4. Confirm the disconnection

**Warning:** Disconnecting an integration will stop all data syncing. Historical data will remain in TRES, but no new data will be synced.

## Common Workflows

### Setting Up QuickBooks Integration

1. Navigate to the Integrations page
2. Find QuickBooks and click "Connect"
3. Log in to your QuickBooks account and authorize TRES
4. Once connected, click "View Configuration"
5. Review your account details in the General section
6. Navigate to "Rules" and set up your Chart of Accounts mapping
7. Configure any custom rules for transaction categorization
8. Review the Syncing Status to ensure transactions are processing correctly
9. Adjust settings as needed for sync frequency and preferences

### Monitoring Sync Status

1. Navigate to the Integrations page
2. Click "View Configuration" on your connected ERP integration
3. Review the Syncing Status section
4. Check for any "Failed" transactions and investigate errors
5. Review "Pre-Sync" transactions and approve them if needed
6. Monitor "Completed" count to ensure regular syncing

### Troubleshooting Failed Syncs

1. Open the integration configuration
2. Note the number of "Failed" transactions in Syncing Status
3. Click on the "Failed" status to view detailed error logs
4. Common issues:
   - Missing Chart of Accounts mapping (create a rule in the Rules section)
   - Authentication expired (reconnect the integration)
   - Invalid transaction data (review and correct in the Ledger)
5. After resolving issues, retry the sync or wait for the next automatic sync

### Setting Up Slack Notifications

1. Go to the "All integrations" tab
2. Find Slack and click "Connect"
3. Log in to your Slack workspace
4. Select a **public channel** for TRES notifications
5. Grant the necessary permissions
6. Configure notification preferences (which events to notify)
7. Test the connection by triggering a sample notification

## Tips

- **Start with ERP Integration:** Connect your accounting software first to establish a solid foundation for financial data management
- **Map Rules Early:** Set up your Chart of Accounts mapping rules before syncing large volumes of transactions
- **Monitor Sync Status Regularly:** Check the Syncing Status section weekly to catch and resolve any sync errors promptly
- **Use Pre-Sync for Review:** Keep transactions in "Pre-Sync" status if you prefer manual approval before they appear in your ERP
- **Leverage Slack Integration:** Enable Slack notifications to stay informed about critical changes and errors without constantly checking TRES
- **Explore GraphQL for Automation:** If you have technical resources, use the GraphQL API to build custom integrations and automate repetitive tasks
- **Consider Deel for Global Teams:** If you manage international contractors or employees, Deel integration can save significant time on payroll and accounting
- **Keep Authentication Fresh:** If you notice sync failures, first check if your ERP authentication has expired and needs to be renewed
- **Document Custom Rules:** Maintain documentation of your custom mapping rules to ensure consistency, especially when onboarding new team members
- **Test Before Bulk Sync:** When first connecting an ERP, test with a small batch of transactions to verify your rules and mappings are correct

## Integration Categories

### Financial/ERP

- QuickBooks
- Xero
- Netsuite
- Universal ERP

### Payments

- Request Finance
- Deel

### Communication

- Slack

### Developer Tools

- GraphQL Playground

## Security and Permissions

All integrations use secure OAuth authentication or API keys to protect your data. TRES never stores your ERP passwords. When you connect an integration, you grant specific permissions that define what data TRES can access. You can revoke these permissions at any time by disconnecting the integration.

**Best Practices:**

- Regularly review connected integrations and remove unused ones
- Use role-based access control in your ERP to limit what TRES can modify
- Monitor sync logs for any unusual activity
- Keep your ERP and TRES account credentials secure and separate
