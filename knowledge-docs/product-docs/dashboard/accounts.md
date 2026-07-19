# Accounts Page

## Overview

The Accounts page is your central hub for managing wallets, contacts, and addresses across your digital asset ecosystem. It provides comprehensive visibility into all accounts, their holdings, reconciliation status, and relationships between addresses and contacts.

The page is organized into three main tabs: **Wallets**, **Contacts**, and **Unidentified Addresses**, each serving a specific purpose for account and relationship management.

## Tabs

### 1. Wallets Tab

The **Wallets** tab displays all your connected wallets and accounts in a card-based layout, providing a comprehensive overview of your digital asset accounts.

#### Wallet Card Information

Each wallet card displays the following information:

**Header Section:**

- **Network Icons**: Visual indicators showing which blockchain networks the wallet is active on (e.g., Ethereum, Solana, Avalanche). Multiple icons indicate multi-chain activity, with a "+N" badge showing additional networks
- **Wallet Name**: Custom name assigned to the wallet
- **Wallet Address**: Truncated blockchain address (e.g., "0xe831 ... df7697") with a copy icon
- **Description/Note**: Optional text description providing context about the wallet's purpose
- **Total Value**: Current USD value of all assets in the wallet

**Details Section:**

- **Added Date**: When the wallet was first added to the system (e.g., "Added: Dec 05, 23")
- **Wallet Type Badge**: Special indicators like "MANUALLY ADDED" or "Wallet Disabled"
- **Assets Count**: Total number of different assets held (e.g., "313 ASSETS")
- **Reconciliation Status**:
  - **Reconciled**: Wallet is balanced and all transactions match expected values
  - **Unbalanced**: Discrepancies detected that need attention
- **Group Tags**: Organization labels for categorizing wallets (e.g., "ENTITY 1", "VALIDATOR", "CLIENT A CEFI")
  - Multiple tags can be assigned
  - Overflow tags are shown with a "+N" indicator (e.g., "+28" means 28 more tags)

#### Pending Wallets Section

At the top of the wallet list, you'll see a **Pending wallets** section that displays wallets currently being synced or collected:

- Shows wallet name/identifier
- Displays the sync status: **In progress**
- Provides visual progress indicator
- Once collection completes, wallets move to the main list

#### Wallet Actions

Each wallet has a dropdown menu (three dots icon) providing the following actions:

1. **Edit Wallet**: Modify wallet name, description, groups, and settings
2. **Copy Address**: Copy the wallet's blockchain address to clipboard
3. **View Transactions**: Navigate to the Ledger page filtered for this wallet's transactions
4. **Collect Transactions**: Manually trigger transaction collection (may be disabled if collection is already in progress)
5. **Delete Wallet**: Remove the wallet from the system (requires confirmation)
6. **Clean Wallet**: Remove all cached transaction data and re-collect from scratch

#### Filters

The Wallets tab provides powerful filtering options to help you find specific wallets:

- **Archived Balances**: Toggle to show/hide wallets with archived or zero balances
- **Name/identifier**: Search wallets by name or address
- **Asset Classes**: Filter by types of assets held (e.g., tokens, NFTs, stablecoins)
- **Networks**: Filter by blockchain networks (e.g., Ethereum, Solana, Avalanche)
- **Groups**: Filter by assigned group tags

#### Pagination

- Default display: 20 wallets per page
- Adjustable page size via dropdown
- Navigation controls: First, Previous, Next, Last page buttons
- Current page indicator (e.g., "1 of 3")

#### Expand All Feature

Click the **Expand all** button to simultaneously expand all wallet cards and view their detailed information at once.

### 2. Contacts Tab

The **Contacts** tab helps you manage known addresses and associate them with real-world entities, making transaction tracking more meaningful.

#### Search Functionality

A powerful search bar allows you to find contacts by:

- Contact name
- Associated address
- Assigned group

**Search placeholder**: "Search by Name / Address / Group"

#### Contact Display

Contacts are organized alphabetically by first letter, with letter headers separating each section.

Each contact entry displays:

- Contact name
- Associated addresses
- Group assignments
- Transaction activity indicators

#### Contact Actions

For each contact, you can:

- **Change Name**: Rename the contact
- **Edit Contact**: Modify contact details, addresses, and groups
- **Set Tags**: Assign or modify group tags
- **Delete Contact**: Remove the contact (may require confirmation if active in transactions)

#### Empty State

If no contacts exist, an empty state message appears with:

- Explanation text
- Link to "Name addresses" (redirects to Unidentified Addresses tab)

#### Pagination

Similar to the Wallets tab, contacts support pagination with adjustable page sizes.

### 3. Unidentified Addresses Tab

The **Unidentified Addresses** tab helps you identify and categorize addresses that appear in your transactions but haven't been assigned to a contact yet.

#### Sender/Receiver Toggle

Switch between two views:

- **SENDER**: Addresses that have sent assets to your wallets
- **RECEIVER**: Addresses that have received assets from your wallets

This helps you understand transaction flows and identify important counterparties.

#### Address Management

For each unidentified address, you can:

- **Approve Name**: Accept a suggested name from the system
- **Assign Contact**: Link the address to an existing contact
- **Remove Contact**: Unlink an address from a contact
- **Change Name**: Manually assign a custom name
- **Edit Contact**: Create a new contact for the address

#### AI-Powered Suggestions

The system may provide suggested names based on:

- On-chain data analysis
- Known exchange addresses
- Common contract addresses
- Transaction patterns

## Top-Level Actions

The Actions menu in the top-right corner provides two primary functions:

### 1. Add Wallet

Initiate the process to connect a new wallet to your account. Supports various wallet types:

- Blockchain addresses (Ethereum, Solana, Bitcoin, etc.)
- Exchange accounts
- Custodial wallets
- Validators and delegation accounts
- Manual wallets (for offline or paper wallet tracking)

### 2. Add Contact

Create a new contact entry to associate with one or more addresses. Useful for:

- Labeling exchange addresses
- Tracking counterparties
- Organizing business relationships
- Documenting fund sources

## Export Report

The **Export Report** button allows you to generate and download reports containing:

- Wallet summaries
- Holdings by wallet
- Group-based organization
- Current valuations

Reports can be exported in various formats (CSV, Excel, PDF depending on configuration).

## Wallet Status Indicators

Wallets may display special status badges:

### Wallet Disabled

Indicates that data collection for this wallet has been paused or disabled. Reasons include:

- Manual deactivation by user
- Collection errors
- API rate limit issues
- Unsupported network changes

To re-enable, use the **Edit Wallet** action.

### Manually Added

Indicates the wallet was added manually rather than through automated integration. These wallets may:

- Require manual transaction entry
- Have limited automated features
- Need periodic manual updates

## Reconciliation Status

### Reconciled

A wallet is marked as **Reconciled** when:

- All transactions are accounted for
- Asset balances match blockchain state
- No discrepancies detected
- ERP integration (if applicable) is synchronized

### Unbalanced

A wallet shows as **Unbalanced** when:

- Transaction data has gaps or inconsistencies
- Calculated balances don't match blockchain state
- Missing cost basis information
- ERP sync issues

**Action Required**: Review the wallet's transactions, verify balances, and run reconciliation tools to resolve discrepancies.

## Group/Tag Management

Groups and tags help organize wallets and contacts into logical categories:

### Common Use Cases

- **Entity-based**: Separate wallets by legal entity (e.g., "ENTITY 1", "ENTITY 2")
- **Purpose-based**: Group by function (e.g., "TRADING", "STAKING", "TREASURY")
- **Client-based**: Organize by customer or project (e.g., "CLIENT A CEFI", "PROJECT 1234")
- **Network-based**: Group by blockchain (e.g., "ETH", "VALIDATOR")

### Managing Groups

- Assign multiple groups to a single wallet
- Filter and search by group
- Groups appear as clickable buttons on wallet cards
- Overflow groups indicated by "+N" badge
- Click a group to edit or manage assignments

## Common Workflows

### Adding and Organizing a New Wallet

1. Click **Actions** → **Add wallet**
2. Select wallet type and provide connection details
3. Wait for initial sync (wallet appears in Pending section)
4. Once synced, assign groups and add description via **Edit Wallet**
5. Verify reconciliation status

### Identifying Unknown Addresses

1. Navigate to **Unidentified Addresses** tab
2. Toggle between SENDER and RECEIVER views
3. Review suggested names (if available)
4. Choose to:
   - Approve suggested name
   - Assign to existing contact
   - Create new contact
5. Address moves out of unidentified list

### Troubleshooting Unbalanced Wallets

1. Locate unbalanced wallet (red icon indicator)
2. Click dropdown menu → **View Transactions**
3. Review transaction history for gaps or errors
4. Use **Collect Transactions** to refresh data
5. If issues persist, use **Clean Wallet** to rebuild from scratch
6. Re-run reconciliation from the Ledger page

### Bulk Wallet Management

1. Use filters to isolate specific wallet groups
2. Apply **Export Report** for documentation
3. Perform actions on filtered results
4. Use groups to maintain organization

## Tips

- **Regular Reconciliation**: Check wallet reconciliation status regularly to catch issues early
- **Descriptive Names**: Use clear, descriptive names for wallets to make them easily identifiable
- **Consistent Tagging**: Establish a group/tag taxonomy and use it consistently across all wallets
- **Identify Addresses**: Regularly review and categorize unidentified addresses to improve transaction clarity
- **Pending Wallets**: Monitor the pending section for wallets that may be stuck in collection
- **Status Badges**: Pay attention to "Wallet Disabled" badges and re-enable if needed
- **Copy Address**: Use the copy address feature when you need to reference wallet addresses in other systems
- **View Transactions**: Quick access to filtered transaction views saves time when investigating specific wallets
