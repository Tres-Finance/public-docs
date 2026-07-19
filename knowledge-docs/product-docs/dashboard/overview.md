# Overview Page (Dashboard)

## Overview

The Overview page serves as your centralized dashboard, providing a comprehensive, real-time view of your organization's digital asset portfolio. It's the first page you encounter upon logging into TRES, designed to give you immediate insights into your financial health, net worth, asset distribution, and recent activity.

The Overview page enables you to:

- **Monitor total net worth** across all your wallets and accounts
- **Track portfolio exposure** by network and asset class
- **Analyze cash flow** through inflow/outflow charts and transaction activity
- **View recent activity** from ERP integrations, reports, and system updates
- **Monitor staking rewards** and delegated assets
- **Calculate cost basis** for financial performance analysis
- **Manage multi-entity operations** for organizations with multiple legal entities

The page automatically updates to reflect real-time changes in your portfolio, ensuring you always have the latest financial snapshot.

## Page Structure

The Overview page is organized into several key sections and tabs, each offering different perspectives on your financial data:

### Header Summary

At the top of the page, you'll see:

**Net Worth Overview:**

- **Total Net Worth** in USD (e.g., 120,931,692 USD)
- **Net Worth by Category:**
  - **Liquid**: Assets immediately available (e.g., 70,152,401 USD)
  - **Claimable**: Assets ready to be claimed (e.g., 37,824 USD)
  - **Locked**: Assets locked in contracts or staking (e.g., 50,741,466 USD)

**Quick Stats:**

- Wallet count (e.g., 44 wallets)
- Account count (e.g., 58 accounts)
- Total transaction count (e.g., 692 transactions)

### Main Tabs

The Overview page features six tabs, each focusing on different aspects of your financial data:

1. **General** - Net worth over time, activity, exposure, and asset breakdown
2. **Positions** - Staking positions, delegated assets, and rewards
3. **Staking Activity** - Historical staking rewards and performance by platform
4. **Alert Center** - Recent alerts and notifications
5. **Cost Basis** - Financial performance calculations and inventory tracking
6. **Multi Entity** - Manage multiple legal entities within a single organization
7. **Vested Assets** - Track vested tokens and future vesting schedules

## Tab 1: General

The **General** tab provides a comprehensive overview of your portfolio's financial health and recent activity.

### Net Worth Over Time Chart

A large, interactive chart displays your portfolio's net worth evolution over a selected time period:

**Features:**

- **Date Range Selection**: Click the date range button to select your desired time period (e.g., Sep 28, 2025 to Oct 27, 2025)
- **Total Change Display**: Shows total change in USD and percentage (e.g., -10,972,785 USD or -9%)
- **Interactive Breakdown**: Click legend items to show/hide different data series
- **Expand Button**: Expand the chart to full-screen view for detailed analysis
- **Download Options**: Save chart as image or export data

**Chart Data:**

- **Daily Net Worth**: Line chart showing day-by-day net worth changes
- **Total Net Worth**: Aggregate portfolio value
- **Breakdown by Asset**: Pie chart or bar chart showing asset allocation

### Your Recent Activity

This section provides quick access to your most recent system activity:

#### ERP Integration Status

Shows the status of your connected ERP system (e.g., QuickBooks):

- **Integration Name**: The name of your connected ERP
- **Sync Counts by Status**:
  - **Completed**: Successfully synced transactions (e.g., 22)
  - **Pre-Sync**: Transactions pending synchronization (e.g., 28,217)
  - **Changed after sync**: Transactions modified after initial sync (e.g., 4)
- **View Button**: Click to navigate to full ERP configuration

#### Recent Reports

Displays your most recently generated reports:

- **Report Cards**: Shows up to 3 most recent reports
- Each card displays:
  - **Report Icon**: Visual indicator for report type
  - **Report Name**: Custom or auto-generated name
  - **Download Icon**: Click to download the report
- **View All Button**: Navigate to the full Reports page

#### Transactions Without FIAT Value

Highlights assets with transactions missing USD values:

- **Asset Cards**: Each card shows:
  - **Asset Icon**: Visual asset identifier
  - **Asset Name**: Name of the asset (e.g., Solayer, Geist FTM, Geist DAI)
  - **Transaction Count**: Number of transactions without fiat values (e.g., "41 TXN")
  - **View Button**: Click to navigate to ledger filtered to these transactions

#### Quick Links

Provides shortcuts to key features:

- **Explore Alerts**: Navigate to the Alerts page with description "Receive alerts on major changes"
- **Explore Automations**: Navigate to the Automations page with description "Streamline your workflows"
- **Integration Promotions**: Promotional cards for recommended integrations (e.g., Deel)

### Exposure Section

Displays your portfolio's distribution across different dimensions:

#### Networks

Shows your total exposure value across all blockchain networks:

- **Network List**: Scrollable list of all networks where you hold assets
- **Network Information**:
  - **Network Icon**: Visual network identifier
  - **Network Name**: e.g., Ethereum, Solana, Avalanche P Chain
  - **Total Value**: FMV in USD (e.g., 54,279,802 USD for ethereum)
- **Clickable Networks**: Click any network to view detailed breakdown
- **27+ Networks**: Supports all major blockchain networks

#### Asset Allocation

Two complementary views of your asset distribution:

**Chart View:**

- Interactive pie or donut chart
- **Top Assets List**:
  - Shows top 5 assets by value
  - Each item displays asset icon, name, and USD value (e.g., Ethereum 34,849,545 USD)
  - Click any asset to drill down into details
- **"Other" Category**: Aggregate of remaining assets (e.g., "Other (309 assets): 42,179,870 USD")
- **View All Button**: Navigate to full Assets page

#### Assets Distribution Table

A comprehensive table showing all your assets:

**Table Columns:**

- **ASSET**: Asset icon and name
- **LIQUID**: Liquid balance (native amount and USD)
- **LOCKED**: Locked balance (native amount and USD)
- **CLAIMABLE**: Claimable balance (native amount and USD)
- **TOTAL**: Total balance across all states

**Features:**

- **Search Functionality**: Search bar to filter assets by name
- **Pagination**: Navigate through multiple pages
- **Sortable Columns**: Click column headers to sort
- **Detailed View**: Click any asset to view full details

### Inflow/Outflow Chart

A financial flow analysis section:

**Features:**

- **Date Range**: Select custom time period (e.g., Oct 21, 2025 to Oct 27, 2025)
- **Summary Metrics**:
  - **Inflow**: Total incoming funds (e.g., 2,849,543 USD)
  - **Outflow**: Total outgoing funds (e.g., 16,615,715 USD)
  - **Fees**: Total transaction fees (e.g., 3,881 USD)
- **Chart Display**: Dual-axis line chart showing:
  - Generated Rewards line
  - Staked + Claimable line
  - Both visible with toggle option
- **Download Options**: Download SVG, PNG, or CSV
- **Note**: "\* Amount appears in USD"

### Top Wallets

Displays your highest-value wallets:

**Wallet Cards**: Shows top 10 wallets by fair market value

Each card displays:

- **Wallet Icon**: Visual wallet identifier
- **Wallet Name**: Custom or auto-generated name (e.g., "UNI-V2", "Solanasto1")
- **Fair Market Value**: Current USD value (e.g., 35,033,388 USD)
- **Add New Wallet Button**: Direct access to wallet addition workflow

## Tab 2: Positions

The **Positions** tab focuses on your staking and delegation activities across different blockchain networks.

### Positions Breakdown

**Summary Metrics:**

- **Total Net Worth**: Aggregate value of all positions (e.g., 121M USD)
- **Pie Chart**: Visual breakdown by position type
- **Position Categories**:
  - **Wallet/Liquid**: Available funds (e.g., 70,152,401 USD)
  - **Locked**: Staked or locked assets (e.g., 50,741,466 USD)
  - **Claimable**: Rewards ready to claim (e.g., 37,824 USD)

### Top Positions

Lists your largest staking positions:

**Position Cards**: Each card shows:

- **Position Icons**: Network and validator icons
- **Position Name**: e.g., "Avalanche P Chain Stake"
- **Position Type Badge**: e.g., "Staking"
- **Amount**: Native currency amount (e.g., 277,572 AVAX)
- **USD Value**: Fair market value (e.g., 5,665,058 USD)
- **Actions Menu**: Three-dot menu for position-specific actions

### Rewards Claimed Chart

Tracks your staking rewards over time:

**Features:**

- **Date Range Selection**: Custom time period
- **Platform Filter**: Select specific staking platforms
- **Chart View**: Dual-line chart showing:
  - **Generated Rewards**: Rewards earned over time
  - **Staked + Claimable**: Total staked amount vs claimable rewards
- **Multi-Asset Tracking**: Separate lines for different assets (e.g., SOL, AVAX)
- **Download Options**: Export chart as SVG, PNG, or CSV

### Delegated Assets

Detailed breakdown of your delegation activities:

**Assets Under Delegation Table:**

- **NETWORK**: Blockchain network icon and name
- **AMOUNT**: Total delegated amount in native currency
- **TOTAL FIAT**: USD value of delegated assets
- **% OF TOTAL**: Percentage of total portfolio delegated
- **Select Network**: Click any row to drill down into network-specific validators

**Features:**

- Clickable network rows to view validator-specific breakdowns
- Validator information (when selected)
- Delegation status tracking
- Performance metrics

## Tab 3: Staking Activity

The **Staking Activity** tab provides detailed analytics on your historical staking performance.

### Filters

**Platform & Rewards Type Selector:**

- **Dropdown Menu**: Select specific staking platforms (e.g., "DYDX: REWARD")
- **Wallet Selector**: Filter by specific wallet
- **Export Report Button**: Generate downloadable staking activity report

### Detailed Staking Charts

For each staking position:

**Chart Sections:**

- **Platform Header**: Shows platform name, wallet name, and date range selector
- **Dual-Chart View**:
  - **Left Chart**: Generated Rewards over time
  - **Right Chart**: Staked + Claimable balances over time
- **Interactive Features**:
  - Toggle series visibility
  - Download options (SVG, PNG, CSV)
  - Legend interaction

**Chart Data:**

- Historical rewards over selectable date ranges
- Real-time staking balance tracking
- Performance trend analysis

## Tab 4: Alert Center

The **Alert Center** tab displays your recent system alerts and notifications:

**Features:**

- Real-time alert feed
- Alert filtering and categorization
- Action links to resolve alerts
- Critical alert highlighting

## Tab 5: Cost Basis

The **Cost Basis** tab provides financial performance analysis using FIFO (First-In-First-Out) accounting methodology.

### Financial Performance Header

**Controls:**

- **Show Zero Balances Toggle**: Show or hide assets with zero balance
- **Search Asset**: Find specific assets quickly
- **Select Date**: View cost basis at a specific point in time
- **Reload Button**: Refresh data
- **Clear Button**: Reset filters (disabled when no filters active)

### Financial Performance Table

Comprehensive cost basis analysis for each asset:

**Table Columns:**

- **Asset**: Asset icon and name
- **Fair Market Value (Liquid)**: Current USD value of liquid holdings
- **Total Inventory**: Total amount held (e.g., "5,625 ETH")
- **Cumulative Cost (FIFO)**: Total purchase cost basis (e.g., "21,287,608 USD")
  - Info button provides detailed cost breakdown
- **Realized Gains**: Gains from sold/disposed assets
  - Negative values shown in red (e.g., "-15,588,138 USD")
  - Positive values shown in green
- **Unrealized Gains**: Potential gains from current holdings
- **Actions**: Per-asset action buttons

**Actions Per Asset:**

- **Calculate Button**: Trigger cost basis recalculation
- **More Actions Menu**: Additional options:
  - View asset details
  - Edit cost basis manually
  - Export cost basis report

**Special Cases:**

- **Missing Fiat Values**: Assets requiring manual fiat value input
  - Warning icon and "Missing fiat values to update cost basis" message
  - "Add fiat value" button to configure
- **Negative Balance Found**: Highlights reconciliation issues
  - "Go to transaction" link to investigate
- **N/A Values**: Assets that cannot be calculated

**Pagination**: Navigate through large asset lists (e.g., "Items per page: 20 out of 179")

## Tab 6: Multi Entity

The **Multi Entity** tab enables management of multiple legal entities within a single TRES organization.

### Entity Management Table

**Table Columns:**

- **Entity**: Entity name or identifier
- **Total Networth ($)**: Combined net worth for that entity
- **Internal Accounts**: Number of accounts managed
- **Transactions**: Total transaction count
- **Data Collect**: Sync status:
  - **COMPLETED**: All data synced and up-to-date
  - **IN_PROGRESS**: Data collection in progress
- **Open Button**: Navigate to entity-specific overview

**Use Cases:**

- Organizations with multiple subsidiary companies
- Separate entity accounting
- Consolidated reporting
- Entity-level access control

## Tab 7: Vested Assets

The **Vested Assets** tab tracks token vesting schedules and future vesting schedules:

**Features:**

- Vesting schedule visualization
- Upcoming vesting events
- Historical vesting tracking
- Vesting calendar

## Global Actions

Throughout the Overview page, you have access to several global actions:

### Top Navigation Bar

- **TRES Analyst Button**: AI-powered financial assistant
  - Click to open chat interface
  - Ask questions about your portfolio
  - Get insights and recommendations

### Data Collection Banner

**Status Indicator:**

- **"Collecting data" Badge**: Shows when system is fetching new data
  - Refresh icon
  - Progress indicator
- **Organization Name**: Current organization context (e.g., "ta")
- **Quick Actions**: Access to notification center or settings

### Banner Notifications

**Promotional Banners:**

- **Integration Recommendations**: e.g., "New & Recommended Integration: Deel"
- **Feature Highlights**: New features or improvements
- **Dismissible**: Close button to hide banners

## Common Workflows

### Monitoring Daily Portfolio Health

1. Navigate to Overview page
2. Review "Net Worth" header for total portfolio value
3. Check "Net Worth Over Time" chart for trend analysis
4. Verify "Exposure" section for network distribution
5. Review "Your Recent Activity" for any issues or updates

### Analyzing Cash Flow

1. Go to "General" tab
2. Scroll to "Inflow/Outflow" chart
3. Select desired date range
4. Review inflow, outflow, and fees totals
5. Click chart toggles to view specific metrics
6. Download chart for reporting if needed

### Checking Staking Performance

1. Navigate to "Staking Activity" tab
2. Select platform from dropdown (e.g., "DYDX: REWARD")
3. Choose specific wallet if applicable
4. Review generated rewards chart
5. Check staked + claimable balance trend
6. Export report for record-keeping

### Calculating Cost Basis

1. Go to "Cost Basis" tab
2. Use "Select Date" to choose historical date
3. Search for specific assets if needed
4. Review "Cumulative Cost (FIFO)" column
5. Check realized vs unrealized gains
6. Click "Calculate" for assets needing recalculation
7. Click info button on Cumulative Cost for detailed breakdown

### Managing Multiple Entities

1. Navigate to "Multi Entity" tab
2. Review entity list with net worth and status
3. Click "Open" on any entity to view entity-specific dashboard
4. Monitor "Data Collect" status for each entity
5. Track transaction and account counts

### Exploring Assets

1. In "General" tab, scroll to "Assets Distribution" table
2. Use search bar to find specific assets
3. Click any asset row to view detailed asset information
4. Review liquid, locked, and claimable balances
5. Navigate to "Assets" page for full asset management

### Setting Up Quick Links

1. In "Your Recent Activity" section
2. Review quick links:
   - Explore Alerts
   - Explore Automations
   - Integration promotions
3. Click any quick link to navigate directly
4. Set up alerts or automations as needed

## Tips and Best Practices

### Daily Monitoring

- Check the Overview page daily for portfolio health
- Review "Your Recent Activity" for ERP sync status
- Monitor "Net Worth Over Time" for trend analysis
- Set up alerts for significant portfolio changes

### Cost Basis Management

- Use "Cost Basis" tab for tax planning
- Calculate cost basis regularly after trades
- Review realized gains for tax reporting
- Check for missing fiat values and resolve promptly

### Staking Optimization

- Review "Positions" tab weekly for reward trends
- Check "Delegated Assets" for diversification
- Monitor claimable rewards and claim regularly
- Track staking performance across platforms

### Multi-Entity Organization

- Keep entities clearly named and organized
- Monitor data collection status for each entity
- Use entity-specific views for reporting
- Maintain separate books for compliance

### Performance Tracking

- Use "Inflow/Outflow" charts for financial analysis
- Export charts and reports for record-keeping
- Compare performance across different time periods
- Track wallet-level performance in "Top Wallets"

### Alert Management

- Review "Transactions Without FIAT Value" regularly
- Resolve missing fiat values promptly
- Monitor "ERP Integration Status" for sync issues
- Set up automations for common tasks

## Important Notes

### Data Freshness

- All data is updated in real-time as transactions occur
- Some historical data may require manual refresh
- Use "Reload" button in Cost Basis tab to refresh data

### Net Worth Calculation

- Based on fair market values from live price feeds
- Includes liquid, locked, and claimable assets
- Excludes unrealized gains until realized

### Cost Basis Method

- Uses FIFO (First-In-First-Out) accounting
- Tracks purchases and sales for accurate basis
- Requires fiat values for accurate calculations
- Can be manually adjusted if needed

### Multi-Entity Considerations

- Each entity maintains separate financial records
- Consolidated reporting available
- Entity-level permissions apply
- Data collection status shown per entity

### Performance Metrics

- "Net Worth Over Time" chart shows portfolio evolution
- "Inflow/Outflow" tracks cash flow patterns
- "Staking Activity" monitors reward generation
- "Cost Basis" calculates financial performance

## Summary

The Overview page is your financial command center, providing real-time insights into your digital asset portfolio. Whether you're monitoring daily net worth, analyzing cash flow, tracking staking rewards, calculating cost basis, or managing multiple entities, the Overview page offers comprehensive tools and visualizations to support informed financial decision-making.

Use the tabs and interactive features to drill down into specific aspects of your portfolio, set up automations and alerts for proactive management, and maintain accurate records through the cost basis and reporting tools. Regular monitoring of the Overview page ensures you stay informed about your organization's financial health and can respond quickly to important changes or opportunities.
