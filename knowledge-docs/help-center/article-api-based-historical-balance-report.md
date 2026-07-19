# API Based Historical Balance Report | TRES Finance Help Center

Source: https://help.tres.finance/article/api-based-historical-balance-report

# API Based Historical Balance Report

In this article, we outline the steps required to fetch historical balances for all wallets in your entity using Archived Nodes.

Important: Only networks with an available Archived Node will be accessible via the API.

For networks without an Archived Node, you can download a report from S3 to access running balance metrics.

[Learn more about Historical Balance reporting options here.]

### Steps to Fetch Historical Balances

Generate a UUID4 ("commitId")

Create a unique identifier (commitId) using UUID4. This identifier will help us track the Historical Balance process. [Generate UUID]

Initiate the Historical Balance Report Collection

Make a request to start the historical balance report collection. [API Doc Link]

Set the following parameters:

commitId: The UUID4 generated in Step 1.

balanceDate: The cutoff date for the balance report.

exportName: (Optional) Use this to specify a custom file name for downloading the report as an Excel file.

Retrieve Your Data Collection Status

Query the commit to monitor the data collection process. [API Doc Link]

Fetch Balances by Commit ID

Once the process is complete, filter the balances using the commitId. [API Doc Link]

You can check all the Historical Balance processes we produced [API Doc Link] and their timestamps.
