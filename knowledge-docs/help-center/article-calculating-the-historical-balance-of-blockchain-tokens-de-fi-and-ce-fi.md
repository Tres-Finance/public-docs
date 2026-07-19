# Calculating the historical balance of Blockchain Tokens, DeFi, and CeFi | TRES Finance Help Center

Source: https://help.tres.finance/article/calculating-the-historical-balance-of-blockchain-tokens-de-fi-and-ce-fi

# Calculating the historical balance of Blockchain Tokens, DeFi, and CeFi

## Methodologies to calculate your historical balance

Before calculating the historical balance, let's align on essential terms:

1. Target Date - date and time in the past when you want to get your historical balance

2. Current Balance - Your balance today.

3. Running Balance - summary of all the transactions from Genesis to the “Target Date”.

4. Reversed Balance - current balance minus summary of all the transactions from “Target Date” to "Current Balance"

5. Historical Balance - the actual balance based on archived nodes.

6. Reconciled Asset - if all types of balances are equal we are reconciled. It means that all collected transactions can explain the asset balance. Why am I not reconciled?

In the TRES platform, there are three ways to calculate your historical balance:

Time Capsule Report

Stateless Historical Balance with API

Running Balance in the Ledger

API Based Historical Balance Report

For a live demo -> contact TRES team

### Time Capsule Report

This report compares the three types of balances mentioned above, along with their corresponding fiat values.

To generate the report, go to the "Assets" page, and click on the export button.

Once the "Export Report" dialog box appears, please follow these steps:

1. Verify that the export format is set to "Raw Balances".

2. Ensure that the "Time Capsule" checkbox is checked.

3. Select a specific "Target Date" for which you want to export the report.

### Stateless Historical/Real-Time Balance with API

Using TRES GraphQL API you can request on-demand balances for onchain assets:

#### Token/Native Coin Balance

Fetch historical or real-time balance for ERC20/ERC721/Native coins.

Important: For real-time balance, do not set "timestamp" parameter

Variables

Response

#### Staking/DeFi Positions

Fetch historical or real-time balance for Native Staking/DeFi applications.

### Running Balance in the Ledger

On the ledger page, you can figure out your organization/wallet running balance after each transaction.

1. Navigate to the ledger page and locate the transaction for which you want to determine the running balance.

2. Please ensure that the "running balance" feature is enabled in the ledger properties:

3. Open the Transaction, and check your "running balance":

## Why am I not Reconciled?

On the assets page, you can see two types of reconciliation badges:

1. Reconciled asset - if the "running balance" is equal to the "Current Balance"

2. Unbalanced asset - if the "running balance" is not equal to the "Current Balance"

There are different reasons which can cause unbalanced assets:

Compounding asset - An investment or token that enables exponential growth by reinvesting earnings. It results in the token balance increasing without requiring executed transactions. Examples include AAVE, stETH, and OUSD.

Missing data - Certain platforms' APIs used by TRES do not include all transactions.

Bug in TRES - Similar to any software, TRES is not flawless. There may be instances where transactions are omitted. Please notify us through the platform to prioritize bug fixing if you wish.

Do you need help with fixing unbalanced assets? Contact the TRES team.

## Why Tracking Historical Balances is important for Crypto Accounting?

Financial planning and performance tracking: Knowing the historical balance of your assets allows you to help you to analyze your asset balances over time, you can identify trends, track growth or decline, and make informed decisions about your financial future.

Accurate tax reporting: When you sell an asset, such as ERC20 Token or Native Coin, the historical balance helps determine your capital gains or losses, which impact your tax liability. By having a comprehensive record of your asset balances, you can ensure compliance with tax laws and maximize tax benefits.

Supporting financial documentation: Provide evidence of net worth for financial auditing. Having accurate historical records ensures transparency and facilitates financial transactions.
