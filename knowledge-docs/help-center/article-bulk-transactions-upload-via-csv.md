# Bulk transactions upload via CSV | TRES Finance Help Center

Source: https://help.tres.finance/article/bulk-transactions-upload-via-csv

# Bulk transactions upload via CSV

For use cases that involved needing to upload a set of manual transactions, Tres provides a CSV template for easy uploading.

Let's go through the template column by column to help best understand what is needed for a successful upload.

Columns A-D are going to be the timestamp. Time needs to be HH:MM:SS. All transactions that share the same hash need to have the same timestamp.

Column E: This is the wallet address for the account that will show up in Tres as your wallet. This address can be anything of your choosing, in this example we have "my-manual-wallet." You can also add transactions to a wallet that is already connect to Tres, in which case you would want to use the wallet's address that is already in Tres. Be careful to not use the wallet's name here. So, for example, if on your accounts page in Tres you had a wallet named "Customer Funds" and the address was 0x1234abcd....123abc, you would use the 0x1234....123abc in Column E. Please be mindful that this column is case sensitive to how the wallet displays in your Tres entity. The best practice here is to copy the address from the Accounts page from your Tres UI.

Column F: This the 3rd party, or external wallet/address that the transaction is going to interact with. In some cases you may have an actual wallet address, in other cases you may want to use a generic tag, such as "native," or a separate indicator such as "John Smith's Wallet."

Column G: This is going to be the network that the transaction took place on. In most cases "manual" is going to be the entry you will use here. In certain circumstances the network may want to be ethereum, solana, etc. However, we want to try and use "manual" first. Within Tres, this will still allow for ETH tokens, for example, to be treated the same as ETH on ethereum, arbitrum, etc.

Column H: This is where we indicate the Direction of the transaction. Inflows to the Organizational Wallet (your wallet) will be marked as "receiver," and outflows as "sender."

Column I: This column as 2 options for entries: "token_transfer" and "gas." We use "token_transfer" for most transactions. "gas" is used for gas and other fee related transactions.

Column J: Asset Identifier: For manual networks, use symbols. For supported networks, use the asset addresses/contracts. If you are adding transactions that are the native token for a network, e.g. Ethereum on the ethereum network. You will use "native" in this column and "ethereum" as your network in column G. Asset Identifier needs to be in ALL CAPS.

Column K: This is the amount of tokens exchanged in the transaction. This number needs to be a positive number regardless of inflow or outflow, as the Direction, Column H, will handle the positive or negative value association.

Column L: This is an optional column to input Fiat Value if you have it for the transaction.

Column M: Tres current supports "usd," "eur," and "gbp" for Fiat Currencies.

Column N: This is the transaction hash. This can be anything you like in order to best identify your transactions. It can be a timestamp or an order id, for example.

Column O: The Transfer ID column is for when there are multiple subtransactions within the same parent transaction. A Swap would be a good example of this. In the example above we see 3 lines that share the same hash. In order to identify these different parts of the transaction separately, we increase the Transfer ID in integer amounts. For transactions that only have a single entry, we will want to have "1" in this column.

Column P: Here is the function name that will be associated with the transaction and interpreted by Tres. This can be any entry of your choosing. For example we may want to use "Withdrawal from FTX" here.

Column Q: Here is the Method ID of the function. This can be any entry of your choosing. Recommendations are for entries without spaces, such as "withdrawal," "deposit," or "swap."

Column R: "Activity name" is the transaction tag.

## Helpful Tips and Tricks:

Columns are generally case-sensitive and want to have entries in the lower case. Exceptions for this are columns for the wallet addresses (E, F), asset identifier (all CAPS, column J), and Columns P and Q.

If you are going to be adding transactions to a wallet that does not currently exist in your Tres account, you will first need to add it as a manual wallet on the UI. From the Accounts tab we will select

Uploading your CSV to Tres is done from the Ledger tab in the same way that a manual transaction from the UI would be added.

When uploading a file, we can see the status of the upload on the top right of the UI:

Once your file is uploaded, you can view the new transactions under /ledger/pendingTransactions. If all looks correct, incorporating the data into the primary ledger is done through a data collect which you can initiate on the top of your dashboard.

If there are errors, you can download the file with comments to determine what needs to be edited in order to be accepted by Tres. If you encounter errors that are unclear, please reach out to us and we would be happy to help clarify the necessary changes.
