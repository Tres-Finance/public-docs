# Assets Page

## Overview

The Assets page provides a comprehensive view of all digital and traditional assets held across your organization's wallets and accounts. This page allows you to track balances, monitor performance, analyze wallet distribution, and manage asset-level data across different asset classes and networks.

## Tabs

The Assets page organizes assets into six distinct categories:

### 1. Coins

Native blockchain currencies such as Bitcoin (BTC), Ethereum (ETH), Solana (SOL), and other Layer 1 blockchain tokens. These are the fundamental currencies that power their respective blockchain networks.

**Key Features:**

- View total balance in both native currency and USD equivalent
- See price per unit in USD
- Track which wallets hold each coin
- Monitor reconciliation status
- View network distribution

### 2. Tokens

ERC-20, SPL, and other token standards built on top of blockchain networks. This includes governance tokens, utility tokens, and other fungible assets.

**Key Features:**

- Comprehensive token information including symbol and full name
- Real-time pricing in USD
- Wallet holdings breakdown
- Network identification
- Balance tracking across multiple wallet addresses

### 3. Fiat

Traditional government-issued currencies (USD, EUR, GBP, etc.) held in bank accounts or payment processors.

**Key Features:**

- Fiat currency balances
- Multi-currency support
- Integration with traditional financial accounts

### 4. Stablecoins

Cryptocurrency tokens designed to maintain a stable value by being pegged to fiat currencies or other stable assets (USDT, USDC, DAI, etc.).

**Key Features:**

- Track stablecoin holdings across networks
- Monitor peg stability
- View total value in USD
- Network-specific balances

### 5. NFT

Non-fungible tokens including digital art, collectibles, domain names, and other unique digital assets.

**Key Features:**

- NFT collection overview
- Individual asset identification
- Floor price and value tracking
- Network and wallet location

### 6. Positions Asset

Complex financial positions including DeFi protocol positions, liquidity pool tokens, yield farming positions, and derivative positions.

**Key Features:**

- Track DeFi protocol positions
- Monitor liquidity pool participation
- View staked assets and rewards
- Analyze position performance

## Filters

The Assets page offers four filtering options to help you quickly find and analyze specific assets:

### Asset Class

Filter assets by their classification (Coin, Token, Stablecoin, NFT, etc.). This allows you to focus on specific asset types based on your analysis needs.

### Wallet

Filter assets by the wallet(s) that hold them. This is useful for analyzing asset distribution across different wallets or focusing on specific wallet portfolios.

### Networks

Filter assets by blockchain network (Ethereum, Solana, Arbitrum, Polygon, etc.). This helps you understand your asset distribution across different blockchain ecosystems.

### Show Zero Balances

Toggle to show or hide assets with zero balances. Enabling this option displays all assets that were previously held but currently have zero balance, which is useful for historical tracking and audit purposes.

## Asset Details

When you expand an asset by clicking on it, you'll see detailed information organized into two sub-tabs:

### Overview Tab

The Overview tab provides comprehensive information about the selected asset:

#### General Info

- **Networks**: Which blockchain network(s) the asset exists on
- **Balances**: Total number of balances and wallets holding this asset (e.g., "3 balances in 1 wallet")
- **Total transactions**: The number of transactions involving this asset (clickable to view transaction details)
- **Reconciled**: Current reconciliation status indicator showing whether the asset balances are reconciled or unbalanced

#### Financial Performance

- **Realized gains**: Total realized profit or loss from transactions involving this asset (in USD)
- **Unrealized gains**: Current unrealized profit or loss based on market value changes (in USD)
- **Cumulative cost FIFO**: The cumulative cost basis calculated using the First-In-First-Out (FIFO) method (in USD)

### Wallet Breakdown Tab

The Wallet Breakdown tab displays a detailed table showing how the asset is distributed across wallets and networks:

| Column              | Description                                                        |
| ------------------- | ------------------------------------------------------------------ |
| **Wallet**          | The name or identifier of the wallet holding the asset             |
| **Network**         | The blockchain network where the balance exists                    |
| **Current Balance** | The current balance in both the asset's native units and USD value |

The table footer shows a summary row with:

- Total number of wallets holding the asset
- Aggregated balance across all wallets

## Actions

### Global Actions (Header)

Located in the page header, these actions apply to selected assets or the entire portfolio:

#### Export Report

Generate and download a comprehensive report of your assets. This report can be customized and exported in various formats for accounting, tax, or analysis purposes.

#### Actions Menu

**Calculate cost basis**

- Trigger a cost basis calculation for your assets
- Uses configured cost basis method (FIFO, LIFO, etc.)
- Updates unrealized gains/losses based on current market prices

**Revaluate**

- Refresh asset valuations using current market prices
- Updates USD values across all assets
- Useful when you need to ensure all prices are up-to-date

### Per-Asset Actions

Each asset has a three-dot menu button (⋮) that provides asset-specific actions:

**View asset transactions**

- Navigate to the Ledger page filtered to show only transactions for this specific asset
- Useful for auditing and understanding the asset's transaction history

**Mark as SPAM**

- Flag an asset as spam or unwanted
- Helps filter out airdropped tokens or spam NFTs from your main asset view
- Marked assets can be hidden from reports and analytics

## Asset Status Indicators

Assets display visual indicators to communicate their current status:

### Reconciliation Status

- **Reconciled** (✓): Asset balances match expected values based on transaction history
- **Unbalanced** (⚠): Discrepancy detected between calculated and actual balances - may require investigation

### Network Icons

Each asset displays icon(s) representing the blockchain network(s) it exists on, making it easy to identify multi-chain assets at a glance.

## Tips for Using the Assets Page

1. **Regular Monitoring**: Check the Assets page regularly to monitor your portfolio composition and performance.

2. **Use Filters Effectively**: Combine filters to create custom views (e.g., show only Ethereum tokens in a specific wallet).

3. **Track Reconciliation**: Pay attention to "Unbalanced" indicators and investigate discrepancies promptly.

4. **Expand for Details**: Click on assets to view detailed breakdowns and performance metrics before making decisions.

5. **Clean Up Spam**: Use the "Mark as SPAM" action to keep your asset list clean and focused on meaningful holdings.

6. **Cost Basis Management**: Run "Calculate cost basis" after significant trading activity to keep tax reporting accurate.

7. **Zero Balance Toggle**: Use the "Show zero balances" toggle when conducting audits or reviewing historical holdings.

8. **Export for Reporting**: Regularly export asset reports for accounting, tax preparation, or portfolio analysis.

## Related Features

- **Ledger**: View detailed transaction history for any asset
- **Positions**: Track complex DeFi positions and their performance
- **Reports**: Generate comprehensive portfolio reports
- **Accounts**: Manage wallets and addresses that hold these assets
