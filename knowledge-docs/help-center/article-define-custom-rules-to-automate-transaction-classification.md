# Define Custom Rules to Automate Transaction Classification | TRES Finance Help Center

Source: https://help.tres.finance/article/define-custom-rules-to-automate-transaction-classification

# Define Custom Rules to Automate Transaction Classification

Use custom rules to automate the classification of your transactions, rather than handle them manually. For example, you can enforce the following rule: “If (when) the asset is USDC coin, the transaction must be synced into my USDC asset account.”

Custom rules consist of two main components: the "when" and the "then".

### WHEN

In the web console, "When" includes the following lists from which you can make selections:

Wallet: A list of all your wallets.

Asset: A list of all your assets.

Contact: The contacts in your address book.

Network: Your networks, which can help differentiate between the same EVM wallet on different networks.

Transaction tag: All the tags associated with your transactions.

Action: All the actions performed in your transactions.

Contract: All the contracts that your transactions interacted with.

You can choose specific items within each list and include as many filters as you require within a rule.

### THEN

In the "Then" part, you can configure the chart of accounts classification for the rule. You can select just one specific type of chart of account or configure all of them. If you choose not to configure a dedicated type of chart of account for the rule, the default account will be used instead.

To create a custom rule:

In the sidebar of the Tres web console, click Integrations.

Click anywhere in the currently configured integration.

Click Rules > Custom Rules.

Click Add Rule.

Make settings in the following fields:

In the first field, type in a name for the rule.

Select a condition (‘When’): In the Category, Value, or Condition lists, select an item.

Select a sync rule in the event that the condition occurs: In the Asset, Income, or other list, select an item.

Add additional rules.

Click Save.

You can create as many rules as necessary to automate your workflows effectively.

The following are examples of basic and more complex rules creation.

### Example 1: Basic rules

This example demonstrates how to create the following simple rule: If the asset is USDC coin, sync the transaction into my USDC asset account.

Type USDC in the top-most field.

In the Category list, select Asset.

In the Value list, select USDC Coin.

You can also add sync rules for income, expenses, fees, gains, and losses but this is not required.

### Example 2: Complex rules

This example demonstrates how to create a more complex rule: Configure the P&L account for all salary sub-transactions.

Assign the name Salaries. Type it in the top-most field.

In the Category list, select Contact.

In the Values list, select Contact Names. These are taken from your address book.

In the third list, select is receiver.

In the P&L section, in the Expenses list, select Salaries.

Click Save
