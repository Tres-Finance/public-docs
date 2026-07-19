# Blockchain data validation | TRES Finance Help Center

Source: https://help.tres.finance/article/blockchain-data-validation

# Blockchain data validation

What is asset reconciliation?

Reconciliation is a method that validates the completeness and accuracy of account balances and transaction history (also known as ledger).

TRES has 4 three-step process to ensure the customers have full visibility of their reconciliation status:

1. Transaction collection - The TRES data collector connects to public and private data sources to gather all transactions executed by the customer, blocks validated by the customer, and transactions that involved the customer (i.e. assets/rewards sent to the customer).

2. Balance collection - In addition to transactions, TRES also collects the balance state for all the assets that the customer has, including liquid, locked, and unclaimed assets.

3. Comparison - to make sure that TRES collected accurate transactions and balances, TRES’ system compares three metrics:

Running Balance - summary of all the transactions from Genesis to the “Target Date”.

Reversed Balance - current balance minus summary of all the transactions from "Current Balance” to “Target Date”

Asset Balance - the actual balance state at the “Target Date”

If all three metrics are equal, TRES refers to transactions and balances as reconciled (also known as verified).

“Current Balance” - the asset balance state as of right now.

“Target Date” - the date at which the customer wants to reconcile their data. Can also be “Current”

4. Presentation - as part of TRES's goal to provide its customers full visibility into the status of their reconciliation, customers can review the reconciliation status in the Asset tab:

Asset page in the UI - When the transactions and asset balances are reconciled, TRES’s UI presents a green checkmark.

When the transactions and assets balances are not reconciled, TRES’s UI presents a warning and the gap size.

Summary -

In case TRES indicates an unbalanced asset, the user can close the gap using the following feature: Reconciliation
