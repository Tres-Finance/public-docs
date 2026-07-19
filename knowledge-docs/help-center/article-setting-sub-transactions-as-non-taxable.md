# Setting Sub-transactions as Non-taxable | TRES Finance Help Center

Source: https://help.tres.finance/article/setting-sub-transactions-as-non-taxable

# Setting Sub-transactions as Non-taxable

This feature was created to provide the ability to manage activities that are not meant to create a taxable event.

There are two options when selecting the "Non-taxable" button.

Non-taxable + Impact Inventory: This option will allow you to avoid any gains and losses by changing the FMV of the outflow transaction to be equal to the COGS and will remove the lot from your cost basis stack.

Non-taxable + Non Impact Inventory: this option will allow you to avoid any gains and losses while pausing the cost basis stack from being impacted.

### Example Use Case for Option 1

Off-ramping your digital assets from an internal wallet in TRES to an internal wallet not listed in TRES.

In the event of a transaction like this, a taxable event has not happened and no gains or losses should be realized. However the cost basis stack should be impacted because the asset is no longer under the possession of a TRES monitored wallet and therefore that lot should not be used to calculate realized gains / losses in the future.

The result of this action will force realized gains / losses to be zero and the lot transferred out will be removed from the cost basis stack.

How to mark transactions as "Non-taxable + Impact Inventory"?

1. Click on the transaction and open the sub-transaction.

2. Mark the sub transaction and click on "Mark as non-taxable".

3. Choose "Non-taxable + Impact Inventory".

4. Rerun cost basis calculations.

### Example Use Case for Option 2

Staking activities: Staking a digital asset does not trigger a taxable event and no realized gains/losses should be recognized as a result of such an event.

If staking rewards and staking lockup/return sub-transactions take place in the same transaction, the ability to mark the staking lockup/return sub-transaction as non-taxable is critical. Such transactions are not taxable events and should not impact the cost basis stack.

To avoid staking lockup and return sub-transactions from impacting the cost basis stack using TRES, mark the sub-transaction as "Non-taxable + Non Impact Inventory". This action will ignore the marked sub-transaction during the cost basis calculation.

Important: If you mark a staking lockup as non-taxable + non-impact inventory, you must also mark the corresponding staking return as non-taxable + non-impact inventory. Otherwise, there will be a mismatch between your token amount inventory and cost basis inventory that can cause a negative inventory error.

How to mark transactions as "Non-taxable + Non Impact Inventory"?1. Click on the transaction and open the sub-transaction.

3. Choose "Non-taxable + Non Impact Inventory".

4. Rerun cost basis calculations .

What this means is no realized gain or loss will be calculated and the inventory stack will not be affected. Essentially the cost basis of the assets involved in the sub-transaction marked as “Non-Taxable” will not change. You may mark multiple sub-transactions as “Non-Taxable + Non Impact Inventory”.

It is important to note that the wallet running balances will always be impacted even if a sub-transaction is marked as "non-taxable". The cost basis stack is what will be impacted.

Tres Finance and its affiliates do not provide tax or accounting advice. This material has been prepared for informational purposes only, and is not intended to provide, and should not be relied on for tax or accounting advice. Please consult with your own tax and accounting advisors before taking any action related to taxable and/or non-taxable events.
