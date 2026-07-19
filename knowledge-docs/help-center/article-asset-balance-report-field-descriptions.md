# Asset Balance Report - Field Descriptions | TRES Finance Help Center

Source: https://help.tres.finance/article/asset-balance-report-field-descriptions

# Asset Balance Report - Field Descriptions

The Asset Balance Report provides a comprehensive snapshot of asset balances across wallets and assets monitored in your account. Below is a description of each parameter included in the report to help you understand and use the data effectively.​

🔹 Wallet & Application Details

Wallet Name – The name of the wallet holding the asset.

Application – The platform or system associated with the wallet (e.g., Fireblocks, Aave).​

🔹 Asset & Platform Information

Asset Name – Full name of the asset (e.g., Ethereum, USDC).

Asset Symbol – Ticker symbol of the asset (e.g., ETH, USDC).

Asset Platform – Blockchain or network where the asset resides (e.g., Ethereum, Solana).

Asset Address – Contract address of the asset on the relevant blockchain.

Asset Class Name – Classification of the asset (e.g., Stablecoin, Token, Native Coin).

Asset Class Symbol – Abbreviation of the asset class.​

🔹 Balance Types

Running Balance (T) – Current total balance in token units (Asset value).

Running Balance Fiat Value ($) – Fiat value of the running balance (Fiat value).

Reversed Balance (T) – Balance calculated with reversed transactions for validation (Asset value).

Reversed Balance Fiat Value ($) – Fiat value of the reversed balance (Fiat value).

Historical Balance (T) – Balance snapshot based on Blockchain/Exchange records (Asset value).

Historical Balance Fiat Value ($) – Fiat value of the historical balance (Fiat value).​

🔹 Balance Comparisons (Asset Vs. Fiat value)

Running vs. Reversed Diff (T) / ($) – Difference between running and reversed balances (tokens / fiat).

Running vs. Historical Diff (T) / ($) – Difference between running and historical balances.

Reversed vs. Historical Diff (T) / ($) – Difference between reversed and historical balances.

#### 🔹 Balance state:

Locked: The balance currently staked, delegated, or locked in smart contracts.

Claimable: Rewards or earnings that have accrued but have not yet been claimed to your wallet.

Wallet: The balance currently available for immediate transfer or trade.

Delegated to Account: This balance represents the total amount of tokens staked with your validator by external third-party delegators.

🔹 Valuation & P/L

Total Cost Basis ($) – Total cost incurred to acquire the asset.

Total Running Inventory Quantity (T) – Quantity of asset currently held based on inventory tracking.

Total Realized P/L ($) – Realized profit or loss to date.

Unrealized P/L ($) – Profit or loss on current holdings based on market value.

Unit Price ($) – Price per unit used to calculate fiat values.​

🔹 Transaction Metadata

Balance ID – Unique ID for the specific balance entry.

Parent Balance ID – Reference to the parent balance grouping.

Timestamp – Date and time of the balance snapshot.

Last TX Hash – Hash of the most recent transaction.

Last Tx Timestamp – Time of the most recent transaction.

🔹 Additional Metadata

Currency – The reporting fiat currency (e.g., USD).

Asset Verification Status – Indicates if the asset is verified in the platform.

Specific Platform Wallet Address – Wallet address as specified per platform.

Wallet Tags – Custom tags assigned to the wallet.

Rolling ID – ID used to track rolling inventory movement.

External Account ID – Identifier linked to external systems or integrations.
