# Integrate Fireblocks with TRES Finance | TRES Finance Help Center

Source: https://help.tres.finance/article/integrate-fireblocks-with-tres-finance

# Integrate Fireblocks with TRES Finance

Pull wallet and vaults from Fireblocks into TRES to fetch on-chain data.

API users in your workspace must first be created in the Console.

Only the workspace Owner, Admins, and Non-Signing Admins can create API users.

To create an API user:

1. In the Fireblocks Console, go to Settings > Users.

2. Select Add User.

3. Toggle the user type to API User on the Add User dialog.

4. Complete the following fields:

Name: Enter the name you want to give the API user in your workspace. You can enter up to 30 characters.

Role: Select the user role as Viewer.

Attach CSR File: Attach TRES CSR file (link) - https://static.tres.finance/TresFireblocks.csr

5. Select Add User.

6. Send TRES the API Key that has been generated.

7. Share with TRES how you want to configure your environment:

Per each row - select one option

Wallet Selection Process:

By default, TRES will ingest all wallets from Fireblocks. However, if you wish to limit the wallets being ingested, prepend the prefix "TRES" to the name of each wallet you want to monitor. Only wallets with the "TRES" prefix will be included.

Additional Configuration:

For Internal Accounts - TRES will collect all onchain historical transactions and balances.

For Contacts - TRES will allow classification rules and Chart-of-accounts mapping.
