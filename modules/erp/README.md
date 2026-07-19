# ERP Module

## Overview

The ERP module handles integration with external accounting systems for transaction synchronization and chart of
accounts management.

## Supported ERPs

### Active Integrations

- **QuickBooks**: Small business accounting software
- **NetSuite**: Enterprise ERP system
- **Xero**: Cloud-based accounting platform
- **Manual ERP**: CSV upload for custom chart of accounts

### Integration Features

- **Chart of Accounts**: Sync account structures
- **Transaction Sync**: Push transactions to ERP
- **AP/AR Support**: Invoice and bill management (QuickBooks, Xero)
- **Multi-Entity**: Support for subsidiaries and departments

## Sync Flows

### 1. Chart of Accounts Refresh

The system automatically fetches your chart of accounts from your ERP system, including:

- Account names and codes
- Account types (asset, liability, income, expense)
- Platform-specific data like NetSuite classes and departments
- Xero departments and entities

### 2. Transaction Sync

- **Individual Sync**: Sync specific transactions to your ERP
- **Batch Sync**: Sync all transactions in a date range
- **Unsync**: Remove transactions from your ERP
- **Ignore**: Mark transactions to skip sync

### 3. AP/AR Sync

- **Invoices**: Sync customer invoices to your ERP
- **Bills**: Sync vendor bills to your ERP
- **Payments**: Sync payment transactions

## Rules System

### Rule Types

- **Specific Sub-Transaction**: Exact transaction matching
- **Internal Transfer**: Internal wallet transfers
- **Custom Rules**: User-defined mapping logic
- **Default**: Fallback rule for unmatched transactions

### Rule Configuration

- **Account Mapping**: Map transactions to ERP accounts
- **Filters**: Platform, asset class, wallet, contacts
- **Default Rules**: Fallback account assignments
- **Custom Rules**: User-defined mapping logic

### Rule Priority

1. **Specific Sub-Transaction**: Exact transaction matching
2. **Internal Transfer**: Internal wallet transfers
3. **Custom Rules**: User-defined rules
4. **Default**: Fallback rule

## Asset-to-GL Code Mapping

### Asset Class-Based Mapping (Required)

The system only allows you to create rules based on **asset classes**, not individual assets. This design ensures
efficient rule management and prevents the need to create hundreds of individual asset rules.

#### How Asset Class Mapping Works

- Assets are automatically grouped into asset classes (e.g., "Bitcoin", "Ethereum", "USDC")
- You create rules for asset classes, not individual assets
- All assets within the same class will use the same GL code mapping
- The system automatically applies the asset class rule to all assets in that class

#### Example Asset Class Rules

- **Asset Class Rule**: "Bitcoin" → "Digital Assets" GL account
- **Covers**: BTC, WBTC, renBTC, and any other Bitcoin-related assets
- **Result**: One rule handles multiple assets automatically

#### Available Asset Classes

The system includes predefined asset classes such as:

- **Bitcoin**: All Bitcoin-related assets
- **Ethereum**: All Ethereum-related assets
- **Stablecoins**: USDC, USDT, DAI, etc.
- **DeFi Tokens**: Uniswap, Aave, Compound tokens
- **Layer 1 Tokens**: Solana, Cardano, Polkadot, etc.
- **Exchange Tokens**: BNB, FTT, CRO, etc.

### Default Asset Mapping

The system includes a **default rule** that applies to all assets not covered by specific asset class rules:

**Default Rule Features:**

- Automatically maps assets to standard GL accounts
- Handles common asset types (cryptocurrency, stablecoins, etc.)
- Provides fallback mapping for assets without specific class rules

### Best Practices for Asset Class Rules

#### 1. Create Asset Class Rules Instead of Individual Asset Rules

**System Design:**

- Rules can only be created for asset classes
- Individual asset rules are not supported
- This prevents rule proliferation and ensures consistency

**Example Asset Class Rules:**

- Rule 1: "Bitcoin Asset Class" → "Digital Assets"
- Rule 2: "Ethereum Asset Class" → "Digital Assets"
- Rule 3: "Stablecoin Asset Class" → "Cash Equivalents"
- Rule 4: "DeFi Token Asset Class" → "Investment Securities"

#### 2. Leverage Default Rules

- Configure comprehensive default rules for common asset types
- Only create specific asset class rules for unique cases
- Let the system handle the majority of assets through defaults

#### 3. Understand Asset Classification

- Assets are automatically classified into appropriate asset classes
- Similar assets are grouped together automatically
- You can see which asset class each asset belongs to in the system

#### 4. Regular Rule Review

- Periodically review and update asset class rules
- Ensure asset class rules cover your most important asset categories
- Update default rules to handle new asset types

### Rule Management for Asset Classes

#### Creating Asset Class Rules

1. **Identify Key Asset Classes**: Determine which asset classes are most important for your organization
2. **Map to GL Accounts**: Create rules mapping each asset class to appropriate GL accounts
3. **Configure Default Rules**: Set up comprehensive default rules for remaining assets
4. **Test and Validate**: Ensure rules work correctly with your transaction data

#### Monitoring Asset Class Usage

- Track which asset classes are being used most frequently
- Identify opportunities to create new asset class rules
- Monitor default rule usage for potential improvements

#### Scaling Considerations

- Asset class rules scale efficiently regardless of the number of individual assets
- Adding new assets automatically benefits from existing asset class rules
- Default rules handle new asset types without requiring new rules

### Asset Class Rule Examples

#### Example 1: Cryptocurrency Trading

- **Bitcoin Asset Class** → "Digital Assets - Bitcoin"
- **Ethereum Asset Class** → "Digital Assets - Ethereum"
- **Stablecoin Asset Class** → "Cash Equivalents - Stablecoins"
- **Default Rule** → "Digital Assets - Other"

#### Example 2: DeFi Operations

- **DeFi Token Asset Class** → "Investment Securities - DeFi"
- **Staking Token Asset Class** → "Investment Securities - Staking"
- **Liquidity Pool Asset Class** → "Investment Securities - LP"
- **Default Rule** → "Digital Assets - Other"

#### Example 3: Institutional Portfolio

- **Bitcoin Asset Class** → "Alternative Investments - Bitcoin"
- **Ethereum Asset Class** → "Alternative Investments - Ethereum"
- **Stablecoin Asset Class** → "Cash and Cash Equivalents"
- **Default Rule** → "Alternative Investments - Other"

## COA Refresh Process

### 1. Account Fetching

The system fetches your chart of accounts from your ERP system, including:

- Account names and codes
- Account types and categories
- Platform-specific organizational data

### 2. Account Types

- **Asset Accounts**: Inventory, cash, investments
- **Liability Accounts**: Payables, loans
- **Income Accounts**: Revenue, gains
- **Expense Accounts**: Costs, fees, losses

### 3. Platform-Specific Data

- **NetSuite**: Classes, departments, subsidiaries
- **QuickBooks**: Classes
- **Xero**: Departments, entities

### 4. Refresh Triggers

- **Manual Refresh**: User-initiated via UI
- **Connection Setup**: Automatic on first connection
- **Token Refresh**: Automatic on token renewal
- **Scheduled Refresh**: Periodic background updates

## How to Refresh COA When ERP Changes Are Made

### When to Refresh

You should refresh your chart of accounts when you make changes to your ERP system, such as:

- Adding new accounts
- Modifying account names or codes
- Creating new departments or classes (NetSuite)
- Adding new entities (Xero)
- Updating account types or categories

### How to Refresh

#### Option 1: Manual Refresh via UI

1. Go to your ERP integration settings
2. Click the "Refresh ERP data" button
3. The system will fetch the latest chart of accounts from your ERP
4. New accounts will be available for mapping immediately
5. Updated account names will be reflected in existing rules

#### Option 2: Automatic Refresh

The system automatically refreshes your COA in these scenarios:

- **First Connection**: When you initially connect your ERP
- **Token Renewal**: When authentication tokens are refreshed
- **Scheduled Refresh**: Periodic background updates

### What Gets Refreshed

- **Account List**: All accounts from your ERP
- **Account Names**: Updated names and codes
- **Account Types**: Asset, liability, income, expense categories
- **Platform Data**:
    - NetSuite: Classes, departments, subsidiaries
    - QuickBooks: Classes
    - Xero: Departments, entities
- **Company Information**: Company name and currency

### After Refresh

- New accounts appear in your mapping rules
- Updated account names are reflected in existing rules
- Any deleted accounts are marked as inactive
- Platform-specific data (classes, departments) is updated

### Troubleshooting Refresh Issues

- **Connection Errors**: Reconnect your ERP integration
- **Authentication Issues**: Refresh your authentication tokens
- **Missing Accounts**: Check your ERP permissions and account visibility
- **Sync Failures**: Contact support if refresh consistently fails

## ERP Transaction Changes After Sync

### What Happens When You Modify Transactions in TRES After Sync

When you make changes to transactions in TRES after they have been synced to your ERP system, the system handles this
through a **"Changed After Sync"** status.

#### Common TRES Modifications That Trigger This Status

- **Fiat Value Changes**: Updating the USD/EUR value of a transaction
- **Chart of Accounts Changes**: Modifying which GL accounts transactions are mapped to
- **Transaction Classification Changes**: Updating transaction categories or tags
- **Amount Adjustments**: Modifying transaction amounts or descriptions within TRES

#### System Response

**1. Detection Process**

- When you modify a transaction in TRES that has already been synced to your ERP
- The system detects the change and updates the transaction status to "Changed After Sync"
- These transactions appear in the "Requires Attention" filter in your ledger

**2. User Notification**

- Modified transactions show an "Alert" status with "Update required" message
- The system displays: "Some data has been edited or changed, sync this transaction to update in [ERP]"
- You can view the current transaction details in TRES to see what was changed

**3. Resolution Options**

**Option A: Re-sync the Transaction**

- Click "Sync Now" to push the updated TRES data to your ERP
- This will update the transaction in your ERP with the new TRES data
- Use this when you want your ERP to reflect the changes made in TRES

**Option B: Keep Original ERP Data**

- Leave the transaction as "Changed After Sync"
- Your ERP will retain the original synced data
- The transaction won't be automatically re-synced in future batch operations

**Option C: Revert TRES Changes**

- Undo the changes made in TRES
- The transaction will return to "Success" status
- No re-sync is needed

#### Impact on ERP

**ERP Data Remains Unchanged**

- Changes made in TRES do not automatically update your ERP
- Your ERP system retains the original synced transaction data
- Manual TRES modifications are isolated to TRES until you choose to re-sync

**Reconciliation Considerations**

- Modified transactions may create reconciliation differences between TRES and ERP
- The system tracks these changes for audit purposes
- You can see which transactions have been modified in TRES

#### Best Practices

**For TRES Modifications**

1. **Document Changes**: Keep records of why modifications were made in TRES
2. **Review Regularly**: Check "Requires Attention" transactions periodically
3. **Consider Workflow**: Decide whether to re-sync or keep original ERP data
4. **Batch Operations**: Be aware that "Changed After Sync" transactions won't be included in automatic batch syncs

**For Maintaining Data Consistency**

1. **Make Changes Before First Sync**: When possible, finalize transaction data in TRES before initial sync
2. **Use Rules**: Configure mapping rules to minimize manual adjustments
3. **Monitor Status**: Regularly review transaction sync statuses
4. **Plan Modifications**: Consider the impact on ERP data before making changes

**For ERP System Changes**

- Changes made directly in your ERP system (like NetSuite) do not affect TRES
- TRES does not automatically detect or sync changes made in your ERP
- If you modify transactions in your ERP, you may need to manually reconcile differences

## Configuration

### Integration Setup

Connect your ERP system by providing authentication credentials. The system supports OAuth2 for most integrations.

### Rule Creation

Create mapping rules to automatically assign transactions to the correct ERP accounts based on:

- Transaction platform (Ethereum, Bitcoin, etc.)
- Asset class (cryptocurrency, stocks, etc.)
- Wallet or contact information
- Custom criteria you define

## Monitoring

### Sync Status

- **Pending**: Transactions waiting to sync
- **In Progress**: Currently syncing
- **Completed**: Successfully synced
- **Failed**: Sync errors
- **Ignored**: Marked to skip
- **Changed After Sync**: Modified in ERP after sync

### Error Handling

- **Authentication Errors**: Token refresh required
- **Rate Limits**: Retry with exponential backoff
- **Validation Errors**: Data format issues
- **Network Errors**: Connection timeouts

