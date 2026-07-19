# Upload Manual Transactions | TRES Finance Help Center

Source: https://help.tres.finance/article/upload-manual-transactions

# Upload Manual Transactions

To give you full visibility of all financial data, Tres lets you manually upload transactions that could not be scraped from the blockchain. These can be transactions involved on a network that is not yet supported by Tres. They can also be transactions associated with an archived wallet that is no longer accessible.

### Add a manual transaction

In the sidebar, click Ledger.

In the top-right corner of the screen, click Actions => Add transaction.​

Choose the method of upload in the dialog that appears:

The two ways to add manual transactions are:

Upload CSV

Add a single transaction

These are described on the following sections:

#### Single transactions

Fill in the dropdown parameters based on the transaction information.

Please make sure to correctly label the Organizational Wallet and Participating Wallet as receiver and sender to accurately track the direction of the transaction.

Add a sub-transaction: in the case of wanting to differentiate between fees or other transaction types, you may use the sub-transaction section by filling out the relevant parameters.

#### CSV bulk upload

Download the supported CSV format and update the file with your data.Do not edit the file format by adding columns or removing columns -- this will cause the upload to fail.

The "Transfer ID" column is used to separate transactions that have the same hash. For example, if the same hash is involved in the gas fee of a transaction as well as the outflow. In this case, one of the transactions would be labeled 1 and the other 2.

Once you have finished updating the file, upload it to the platform.

### Next steps

After a transaction is added, the transaction will enter a pending stage until the next data collect run. You can always collect data manually.

As long as the transaction is pending, the following data will not be calculated:

Cost Basis

Gains (realized and unrealized)

Asset balance

When manually adding transactions or sub-transactions, they will be assigned a 'pending' status until the next data collect run. Manual data collection is always an option.
