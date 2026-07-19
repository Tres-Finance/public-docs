# Management Page

## Overview

The Management page serves as the central hub for administrative control and organizational configuration. It provides comprehensive tools for managing system settings, controlling data collection, configuring financial calculations, and overseeing user access and permissions within your TRES organization.

The Management page enables you to:

- **Configure system-wide settings** affecting how TRES calculates and processes your financial data
- **Control data collection** across networks and automate data retrieval
- **Manage fiat value calculations** and pricing sources
- **Set lock periods** to protect finalized financial records
- **Manage user access** and invite team members
- **Configure notifications** for important system events

Access to the Management page is restricted to administrators only. You can access it via the user profile menu (top-right corner) by clicking "System controls" or directly navigating to `/management`.

## Page Structure

The Management page is organized into two main tabs:

### 1. Settings Tab

The **Settings** tab contains all system configuration options organized into two main sections:

#### System Settings

- **Cost basis**: Configure how cost basis is calculated
- **Data Collect**: Control data collection from blockchain networks
- **Fiat Value**: Manage fiat value calculations and price sources
- **Lock Periods**: Define periods when financial records are locked

#### Notification Settings (if Slack integration is available)

- **Report notifications**: Configure alerts when reports complete
- **Data collection notifications**: Get notified when manual data collection completes

### 2. Users Tab

The **Users** tab allows you to manage user access and permissions:

- View all users in your organization
- Invite new users
- Change user permissions and roles
- Manage user access

**Global Action:** "Invite User" button in the page header to quickly add new team members

## System Settings

### 1. Cost Basis

**Enable/Disable Cost Basis:**

- Toggle switch to enable or disable cost basis calculation for your organization
- When enabled, TRES tracks gains, losses, and asset value over time
- Provides accurate financial reporting and tax calculations

**Cost Basis Configuration:**

- Configure how cost basis is calculated for your organization
- Set calculation methods and strategies
- Define which currencies/assets should have cost basis tracking
- Configure calculation rules and preferences

**Use Cases:**

- Accurate tax reporting and compliance
- Track investment performance and gains/losses
- Financial analysis and portfolio valuation

### 2. Data Collect

Control how and when TRES collects transaction data from blockchain networks.

#### Network Data Collection

**Purpose:** Disable data collection on specific networks across your account

**Features:**

- Select which networks to disable data collection for
- Control transaction fetching on a per-network basis
- Reduce data collection costs and processing time
- Focus data collection on relevant networks only

**Use Cases:**

- Disable collection for networks you no longer use
- Temporarily stop collection for problematic networks
- Optimize data collection costs
- Focus resources on priority networks

#### Auto Data Collection

**Purpose:** Set and manage daily automatic updates, ensuring data is retrieved and refreshed with no manual effort

**Features:**

- Schedule automatic daily data collection
- Configure collection timing and frequency
- Enable automatic transaction updates
- Reduce manual intervention required

**Use Cases:**

- Maintain up-to-date transaction data
- Automate regular data refresh cycles
- Ensure consistent data availability
- Reduce manual maintenance efforts

### 3. Fiat Value

Configure how TRES calculates and displays fiat values for your digital assets.

#### Fiat Value Swap Alignment

**Purpose:** Use a customizable threshold to achieve Fiat value alignment between Swap assets

**Features:**

- Set alignment thresholds for swap transactions
- Configure value matching between swapped assets
- Ensure consistent fiat value representation
- Adjust sensitivity and tolerance levels

**Use Cases:**

- Improve accuracy of swap transaction valuations
- Align fiat values across paired assets
- Reduce discrepancies in swap reporting

#### Peg Stablecoins to a Fiat Value

**Purpose:** Map Stablecoin value to a specific Fiat value for more consistent and reliable asset stability

**Features:**

- Configure stablecoin pegging rules
- Define fiat value mappings for stablecoins
- Set target fiat values for specific stablecoins
- Ensure consistent valuation of stable assets

**Use Cases:**

- Maintain consistent stablecoin valuations
- Improve USD-pegged asset representation
- Ensure accurate fiat value calculations for stablecoins

#### Price Sources Configuration

**Purpose:** Choose your organization's principal market and define specific sources per asset class

**Features:**

- Select primary price source for your organization
- Define price sources per asset class (coins, tokens, NFTs, etc.)
- Configure backup price sources
- Set custom price feeds for specific assets

**Price Source Options:**

- Primary market selection
- Asset-specific price sources
- Backup sources for redundancy
- Custom price feed configuration

**Use Cases:**

- Use preferred exchange prices (e.g., Coinbase, Binance)
- Select most liquid markets for accurate pricing
- Configure reliable price sources for each asset type
- Set up custom price feeds for unique assets

### 4. Lock Periods

**Purpose:** Defined periods when financial records are finalized, and changes are restricted to uphold data integrity and ensure accurate reporting

**Features:**

- Define time periods to lock financial records
- Prevent modifications to historical data
- Ensure data integrity for accounting and audit purposes
- Configure lock dates and expiration rules

**Lock Time Periods:**

- Set start and end dates for locked periods
- Define which transaction types should be locked
- Configure automatic locking rules
- View locked period history

**Use Cases:**

- Protect finalized financial periods (quarters, fiscal years)
- Ensure accounting data integrity
- Comply with audit requirements
- Prevent accidental modification of historical data

**Important:** Once a period is locked, transactions within that period cannot be modified or deleted without administrator override.

## Notification Settings

When Slack integration is available, you can configure notification preferences for important system events.

### Report Notifications

**Purpose:** Receive notifications via email and Slack when reports are ready

**Configuration Options:**

- Notify when report is complete
- Choose to get notified for all reports or only for recurring ones
- Select notification channels (email, Slack)
- Configure notification frequency

**Use Cases:**

- Stay informed when scheduled reports are generated
- Receive notifications for important report types
- Track report generation progress
- Ensure timely access to completed reports

### Data Collection Notifications

**Purpose:** Send notification via Slack when manual data collect is complete

**Configuration:**

- Enable Slack notifications for data collection completion
- Receive alerts when manual data collection finishes
- Stay informed about data collection status

**Use Cases:**

- Monitor data collection progress
- Receive confirmation when data updates complete
- Track manual data collection activities

## Users Management

The Users tab provides comprehensive user access management for your organization.

### Viewing Users

- View all users in your organization
- See user roles and permissions
- View user status (active, invited, etc.)
- Check user email addresses and access levels

### Inviting Users

**Invite User Button:**

- Click "Invite User" in the page header
- Modal opens for entering user details
- Enter email addresses of users to invite
- Select user role and permissions
- Send invitations via email

**User Roles:**

- **Admin**: Full access to all features including Management settings
- **User**: Standard access to most features
- **Viewer**: Read-only access (if available)

**Use Cases:**

- Add team members to your organization
- Grant access to external accountants or auditors
- Invite contractors or consultants
- Provide read-only access to executives or stakeholders

### Managing User Access

- **Change user type**: Update user roles and permissions
- **Remove users**: Deactivate or remove user access
- **Resend invitations**: Resend invitation emails for pending invitations
- **Update user details**: Modify user information and settings

## Accessing the Management Page

### Via User Profile Menu

1. Click on your profile avatar in the top-right corner of the page
2. A dropdown menu will appear
3. If you have admin permissions, you'll see **"System controls"** option
4. Click "System controls" to navigate to the Management page

### Direct Navigation

- Navigate to `/management` or `/management/settings`
- The page will show the Settings tab by default
- Switch to Users tab to manage user access

**Note:** Access to the Management page is restricted to administrators. Regular users will not see the "System controls" option in their profile menu.

## Common Workflows

### Setting Up Cost Basis Calculation

1. Navigate to Management > Settings
2. Under "System Settings," find "Cost basis"
3. Toggle the "Enable cost basis" switch to ON
4. Click "Cost basis Configuration"
5. Configure calculation settings:
   - Select calculation strategy
   - Choose currencies to track
   - Set calculation rules
6. Save your configuration

### Scheduling Automatic Data Collection

1. Navigate to Management > Settings
2. Under "Data Collect," click "Auto Data Collection"
3. Configure automatic updates:
   - Enable daily automatic collection
   - Set collection time
   - Choose which networks to include
4. Save settings

### Configuring Price Sources

1. Navigate to Management > Settings
2. Under "Fiat Value," click "Price Sources Configuration"
3. Select your organization's principal market (e.g., Coinbase, Binance)
4. Define specific sources per asset class:
   - Coins: Select primary exchange
   - Tokens: Choose token price source
   - NFTs: Configure NFT pricing source
5. Set backup sources for redundancy
6. Save configuration

### Locking a Financial Period

1. Navigate to Management > Settings
2. Under "Lock Periods," click "Lock time periods"
3. Configure the lock period:
   - Set start date
   - Set end date
   - Define what should be locked (transactions, balance changes, etc.)
4. Save the lock period configuration
5. The system will prevent modifications to transactions within that period

### Inviting a New User

1. Navigate to Management > Users tab
2. Click "Invite User" button in the page header
3. Enter the user's email address
4. Select user role (Admin, User, Viewer)
5. Click "Send Invitation"
6. The user will receive an email invitation to join your organization

## Tips

- **Configure Settings Before Use:** Set up system settings (cost basis, data collection, price sources) before importing significant amounts of data for optimal results
- **Lock Periods Early:** Define lock periods for fiscal quarters/years proactively to protect data integrity
- **Automate Data Collection:** Enable auto data collection to ensure your data stays up-to-date without manual intervention
- **Choose Appropriate Price Sources:** Select price sources that are most liquid and reliable for your asset types
- **Use Notification Settings:** Enable Slack notifications to stay informed about important events without constantly checking the system
- **Regular User Audits:** Periodically review the Users tab to ensure only authorized personnel have access
- **Test Settings Changes:** When changing significant settings like cost basis calculation, test with a small data set first
- **Document Custom Configurations:** Keep records of your system settings and why you chose specific configurations
- **Review Lock Periods Regularly:** Ensure lock periods align with your fiscal calendar and reporting requirements
- **Involve Your Team:** When configuring price sources or data collection settings, consult with your financial team to ensure alignment with accounting practices
- **Backup Before Major Changes:** Before making significant configuration changes, ensure you have data backups
- **Monitor Data Collection Costs:** Regularly review network data collection settings to optimize costs

## Important Notes

- **Administrator Access Required:** Only users with administrator permissions can access the Management page
- **Irreversible Changes:** Some settings changes (like disabling cost basis) may require confirmation and cannot be easily undone
- **Data Impact:** Changes to system settings can affect how historical transactions are displayed and calculated
- **Lock Period Effects:** Once a period is locked, transactions within that period cannot be modified without administrator override
- **User Management:** Changes to user permissions take effect immediately
- **Notification Requirements:** Slack notifications require the Slack integration to be connected (see Integrations page)
- **Testing Recommended:** Before implementing production settings, test changes in a development or staging environment if available

## Best Practices

### System Settings

- Test configuration changes with a small dataset first
- Document all configuration decisions and reasoning
- Implement lock periods aligned with your fiscal calendar
- Choose price sources with high liquidity and reliability
- Review and update settings regularly as your organization grows

### User Management

- Follow the principle of least privilege (grant minimum necessary access)
- Regularly review and audit user access
- Remove access promptly when users leave your organization
- Use appropriate roles (don't grant admin access to regular users)
- Keep user contact information up-to-date

### Data Collection

- Balance automatic collection with manual control
- Disable collection on networks you don't actively use
- Monitor data collection performance and adjust as needed
- Configure appropriate automatic update schedules

### Security

- Limit administrator access to trusted personnel only
- Regularly review who has admin permissions
- Use strong authentication methods
- Keep audit logs of configuration changes
- Implement data access controls as appropriate
