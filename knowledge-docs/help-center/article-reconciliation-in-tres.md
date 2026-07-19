# Reconciliation in TRES | TRES Finance Help Center

Source: https://help.tres.finance/article/reconciliation-in-tres

# Reconciliation in TRES

Closing your financial books is a crucial process for any business. It involves finalizing your financial statements and reconciling accounts to ensure that all transactions are accurately recorded.

Reconciliation is the process of comparing the transaction records gathered by TRES Finance and aligning them to the blockchain/exchange balance to ensure they are in agreement and any discrepancies are identified and resolved. It’s the first step when closing your organization’s books.

How to verify your balances are reconciledThere are a few places where you can spot indications of unbalanced assets:

### Ledger:

Choose from a selection of month-end timestamps for which you intend to reconcile all your transactions up until. For example: July 31st, 2023.

Select specific wallets or assets to reconcile. By default, the account will include all assets and wallets.

2. Review the reconciliation gapReview the list of assets that are unreconciled and close the gap by adding manual transactions. TRES provides you with two options:

a. Reconcile all: You can reconcile all your assets at once by clicking Reconcile all. That action creates a set of manual transactions that will close all gaps between blockchain data and TRES ledger data.

b. Reconcile one by one: You can review each asset individually and close the gaps one by one.

3. Add manual transactions

TRES supports the manual transaction feature. This feature allows you to create transactions to close reconciliation gaps. Here is an example:

TRES may fetch ledger transactions from one of your organization's Etherum wallets and find this wallet should contain 300 USDC. However, when querying the blockchain data, you might find that the wallet actually contains 301 USDC. By adding a manual transaction for 1 USDC, you are able to close the reconciliation gap and continue to the next steps to close your books.​

4. Review your transactionsOnce you select the preferred option to closing the reconciliation gap, review the manual transactions that will be added.

5. Run “data collect”Finally, when you’ve completed adding all transactions to close the gaps, click Confirm at the bottom of the panel. This will trigger the data collection process.

​Once the data collection process is finalized, the manual transactions will be part of the ledger.

### Accounts --> Asset Breakdown:

When hovering the 'View Reason' you'll see the reconciliation gap data, and the option to Resolve Gap.

There are two options to resolve a gap:

Create an automation - See this guide for all the details.

Add manual TX - As described in the Ledger section above.
