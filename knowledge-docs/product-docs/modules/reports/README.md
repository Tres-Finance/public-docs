# TRES Reports Module

This documentation covers all available reports in the TRES platform, including their purposes, use cases, and detailed column explanations.

**Conventions:**
- (T) = token/native units
- Columns like "Fiat Value (USD)" show the report's selected fiat currency
- true/false fields are literal booleans unless noted
- Names/codes may be blank if data is unavailable for a row

---

## Reports Catalog

### Basic Raw Transactions
Provides a granular, line-by-line view of sub-transactions with wallet context, counterparties, decoded call data, and token/fiat valuations. Used for operational forensics, audit trails, reconciliation, and custom analysis.

**Columns:**
- **Timestamp**: Exact sub-transaction time (UTC)
- **Year/Month/Day/Time**: Date-time components of Timestamp
- **Belongs To**: Internal wallet/display name that owns the transaction leg
- **Belongs To Address**: Internal wallet address/identifier
- **Belongs To Tags / Description**: Internal wallet tags or description
- **3rd Party**: Counterparty name (if known/labeled)
- **3rd Party Address**: Counterparty address
- **3rd Party Tags / Description**: Counterparty tags/description if labeled
- **Platform**: Network/platform (e.g., ethereum, polygon)
- **Direction**: Inflow/outflow relative to the internal wallet
- **From Address (Name/Address)**: Source address and its label
- **To Address (Name/Address)**: Destination address and its label
- **Event Label**: Human-readable event description
- **Original Amount**: Raw transaction amount in token units
- **Original Currency Symbol/Name**: Token symbol and full name
- **Currency Group Symbol**: Grouped currency symbol for similar tokens
- **Asset Address**: Token contract address
- **Contract Address**: Smart contract address involved
- **Type ID**: Internal type classification
- **Transfer Unit Fiat Price**: Fiat price per token unit at transaction time
- **Balance Impact (T)**: Net balance change in token units
- **Total Fiat Amount**: Total fiat value of the transaction
- **Transaction Hash**: Blockchain transaction hash
- **Sub Transaction Label**: Internal sub-transaction identifier
- **Transaction Activity/Label**: High-level activity classification
- **Success**: Whether the transaction succeeded on-chain
- **Protocols**: DeFi protocols involved
- **Applications**: Applications/protocols involved
- **Asset Verification Status**: Verification status of the asset
- **Fiat Currency**: Base fiat currency for valuations
- **Method ID**: Smart contract method identifier
- **Function Name**: Decoded function name
- **Comments**: Additional notes or comments
- **Sbx ID**: Internal system identifier
- **Block Number**: Blockchain block number
- **External Account ID**: External account reference
- **Additional Data**: Extra transaction metadata

**Suggested Pivots:**
- By Platform/Direction → sum(Total Fiat Amount), count(Transaction Hash)
- By Belongs To → sum(Balance Impact), avg(Transfer Unit Fiat Price)
- By Event Label → sum(Original Amount), count(Success)
- By Date → sum(Total Fiat Amount), count(Transaction Hash)

---

### Extended Raw Transactions
An accounting-ready extension of the basic export that adds running balances, cost basis, realized gains, and COGS, along with ERP mapping hints. Use it for close and tax workflows to quantify P/L at the sub-transaction level, explain inventory impacts, and connect on-chain activity to ledger accounts.

**Columns:** All Basic Raw Transactions columns plus:
- **Running Balance (T)**: Cumulative balance after this transaction
- **Cost Basis**: Purchase price for tax purposes
- **Realized Gain/Loss**: Realized P&L from this transaction
- **COGS**: Cost of goods sold for this transaction
- **ERP Account**: Suggested ERP account mapping
- **Internal Transfer**: Whether this is an internal transfer
- **Counter Transfer**: Related internal transfer transaction
- **Inventory Impact**: Impact on inventory valuation

**Suggested Pivots:**
- By ERP Account → sum(Realized Gain/Loss), sum(COGS)
- By Date → sum(Realized Gain/Loss), avg(Cost Basis)
- By Internal Transfer → sum(Total Fiat Amount), count(Transaction Hash)

---

### Extended Raw Transactions with Cost Breakdown
Enhanced version with detailed cost breakdowns, including gas fees, protocol fees, and other transaction costs. Useful for comprehensive cost analysis and fee optimization.

**Columns:** All Extended Raw Transactions columns plus:
- **Gas Fee**: Transaction gas cost
- **Protocol Fee**: Protocol-specific fees
- **Total Cost**: Sum of all transaction costs
- **Cost Breakdown**: Detailed breakdown of all fees
- **Fee Optimization**: Suggestions for fee reduction

**Suggested Pivots:**
- By Platform → sum(Gas Fee), sum(Protocol Fee)
- By Date → avg(Total Cost), sum(Total Cost)

---

### Raw Balance
Shows current balances across all wallets and assets with historical context. Essential for balance sheet preparation, audit verification, and real-time portfolio tracking.

**Columns:**
- **Wallet Name**: Internal wallet display name
- **Wallet Address**: Wallet address/identifier
- **Asset Symbol**: Token symbol
- **Asset Name**: Full token name
- **Asset Address**: Token contract address
- **Balance (T)**: Current balance in token units
- **Fiat Value**: Current fiat value of the balance
- **Last Updated**: When the balance was last refreshed
- **Source**: Data source for the balance
- **Verification Status**: Balance verification status

**Suggested Pivots:**
- By Wallet → sum(Fiat Value), count(Asset Symbol)
- By Asset → sum(Balance), sum(Fiat Value)

---

### Historical Balance
Time-series balance data showing how balances changed over time. Critical for trend analysis, performance measurement, and regulatory reporting.

**Columns:**
- **Date**: Balance date
- **Wallet Name/Address**: Wallet identifier
- **Asset Symbol/Name/Address**: Asset details
- **Balance (T)**: Balance in token units on this date
- **Fiat Value**: Fiat value on this date
- **Change (T)**: Balance change from previous period
- **Change %**: Percentage change from previous period

**Suggested Pivots:**
- By Date → sum(Fiat Value), avg(Change %)
- By Asset → sum(Balance), trend(Fiat Value)

---

### Internal Accounts Balances
Shows balances across internal account structures, useful for multi-entity organizations and complex accounting setups.

**Columns:**
- **Account Name**: Internal account name
- **Account Type**: Account classification
- **Parent Account**: Parent account reference
- **Balance (T)**: Account balance in token units
- **Fiat Value**: Account fiat value
- **Last Transaction**: Last activity date
- **Status**: Account status

**Suggested Pivots:**
- By Account Type → sum(Fiat Value), count(Account Name)
- By Parent Account → sum(Balance), avg(Fiat Value)

---

### Pre-Sync Journal
Shows transaction data before synchronization with external systems. Useful for identifying discrepancies and ensuring data integrity.

**Columns:**
- **Transaction ID**: Internal transaction identifier
- **Sync Status**: Synchronization status
- **External Reference**: External system reference
- **Discrepancy Amount**: Amount of discrepancy if any
- **Last Sync Attempt**: Last synchronization attempt
- **Error Message**: Sync error details if applicable

**Suggested Pivots:**
- By Sync Status → count(Transaction ID), sum(Discrepancy Amount)
- By Date → count(Last Sync Attempt), count(Error Message)

---

### Post-Sync Journal
Shows transaction data after synchronization with external systems. Used for verification and audit trails.

**Columns:**
- **Transaction ID**: Internal transaction identifier
- **Sync Status**: Final synchronization status
- **External Reference**: External system reference
- **Sync Timestamp**: When synchronization completed
- **Verification Status**: Data verification status

**Suggested Pivots:**
- By Sync Status → count(Transaction ID), count(Verification Status)
- By Date → count(Sync Timestamp), avg(Sync Timestamp)

---

### Reconciliation
Shows reconciliation status between internal and external data sources. Essential for audit compliance and data accuracy.

**Columns:**
- **Internal Reference**: Internal transaction reference
- **External Reference**: External system reference
- **Reconciliation Status**: Current reconciliation status
- **Discrepancy Amount**: Amount of discrepancy
- **Reconciliation Date**: When reconciliation was performed
- **Reconciled By**: User who performed reconciliation

**Suggested Pivots:**
- By Reconciliation Status → count(Internal Reference), sum(Discrepancy Amount)
- By Date → count(Reconciliation Date), count(Reconciled By)

---

### Asset Roll Forward
Shows how asset balances rolled forward from one period to the next. Useful for accounting close processes and audit trails.

**Columns:**
- **Asset Symbol/Name**: Asset identifier
- **Beginning Balance**: Balance at start of period
- **Additions**: Additions during period
- **Disposals**: Disposals during period
- **Ending Balance**: Balance at end of period
- **Period**: Accounting period
- **Roll Forward Date**: When roll forward was calculated

**Suggested Pivots:**
- By Asset → sum(Beginning Balance), sum(Ending Balance)
- By Period → sum(Additions), sum(Disposals)

---

### Cost Basis
Shows cost basis information for tax and accounting purposes. Critical for tax reporting and P&L calculations.

**Columns:**
- **Asset Symbol/Name**: Asset identifier
- **Purchase Date**: When asset was acquired
- **Purchase Price**: Original purchase price
- **Cost Basis**: Current cost basis
- **Unrealized Gain/Loss**: Unrealized P&L
- **Holding Period**: How long asset has been held
- **Tax Lot**: Tax lot identifier

**Suggested Pivots:**
- By Asset → sum(Cost Basis), sum(Unrealized Gain/Loss)
- By Purchase Date → avg(Purchase Price), count(Asset Symbol)

---

### Staking Data
Shows staking activities, rewards, and validator performance. Essential for staking strategy analysis and yield optimization.

**Columns:**
- **Validator**: Validator name/address
- **Staked Amount**: Amount staked
- **Rewards Earned**: Rewards earned from staking
- **APY**: Annual percentage yield
- **Staking Date**: When staking began
- **Unstaking Date**: When unstaking occurred (if applicable)
- **Status**: Current staking status

**Suggested Pivots:**
- By Validator → sum(Staked Amount), sum(Rewards Earned)
- By Date → avg(APY), sum(Rewards Earned)

---

### Audit Log
Shows system activity and user actions for compliance and security monitoring. Critical for audit trails and regulatory compliance.

**Columns:**
- **Timestamp**: When action occurred
- **User**: User who performed action
- **Action**: Action performed
- **Resource**: Resource affected
- **Details**: Action details
- **IP Address**: User's IP address
- **User Agent**: Browser/client information

**Suggested Pivots:**
- By User → count(Action), count(Resource)
- By Date → count(Action), count(User)

---

### Archived Balance
Shows historical balance snapshots for regulatory reporting and audit purposes.

**Columns:**
- **Archive Date**: When balance was archived
- **Wallet Name/Address**: Wallet identifier
- **Asset Symbol/Name**: Asset details
- **Balance (T)**: Archived balance in token units
- **Fiat Value**: Archived fiat value
- **Archive Reason**: Why balance was archived

**Suggested Pivots:**
- By Archive Date → sum(Fiat Value), count(Wallet Name)
- By Asset → sum(Balance), trend(Fiat Value)

---

### Balance Trends
Shows balance trends over time for trend analysis and forecasting.

**Columns:**
- **Date**: Trend date
- **Asset Symbol/Name**: Asset identifier
- **Trend Direction**: Up/down/stable
- **Change Amount**: Amount of change
- **Change Percentage**: Percentage change
- **Moving Average**: Moving average over period

**Suggested Pivots:**
- By Asset → trend(Change Amount), avg(Change Percentage)
- By Date → sum(Change Amount), count(Trend Direction)

---

### Chart of Accounts
Shows the organization's chart of accounts structure for accounting and reporting purposes.

**Columns:**
- **Account Code**: Account code/number
- **Account Name**: Account name
- **Account Type**: Account classification
- **Parent Account**: Parent account reference
- **Description**: Account description
- **Status**: Account status

**Suggested Pivots:**
- By Account Type → count(Account Code), count(Account Name)
- By Parent Account → count(Account Code), count(Status)

---

### Contacts
Shows contact information for counterparties and external parties.

**Columns:**
- **Contact Name**: Contact person name
- **Organization**: Organization name
- **Email**: Contact email
- **Phone**: Contact phone
- **Address**: Contact address
- **Tags**: Contact tags/labels
- **Last Contact**: Last contact date

**Suggested Pivots:**
- By Organization → count(Contact Name), count(Email)
- By Tags → count(Contact Name), count(Last Contact)

---

### Internal Account
Shows internal account structures and hierarchies.

**Columns:**
- **Account ID**: Internal account identifier
- **Account Name**: Account name
- **Account Type**: Account type
- **Parent Account**: Parent account
- **Description**: Account description
- **Created Date**: When account was created
- **Status**: Account status

**Suggested Pivots:**
- By Account Type → count(Account ID), count(Account Name)
- By Parent Account → count(Account ID), count(Status)

---

### Third-Party Addresses
Shows external addresses and their associated information.

**Columns:**
- **Address**: External address
- **Name**: Associated name
- **Type**: Address type
- **Tags**: Address tags
- **First Seen**: When address was first seen
- **Last Activity**: Last activity date
- **Risk Score**: Risk assessment score

**Suggested Pivots:**
- By Type → count(Address), count(Name)
- By Risk Score → count(Address), avg(Risk Score)

---

### Cost Basis Roll Forward
Shows how cost basis rolls forward from period to period for tax and accounting purposes.

**Columns:**
- **Asset Symbol/Name**: Asset identifier
- **Beginning Cost Basis**: Cost basis at start of period
- **Additions**: Cost basis additions
- **Disposals**: Cost basis disposals
- **Ending Cost Basis**: Cost basis at end of period
- **Period**: Accounting period
- **Roll Forward Date**: When roll forward was calculated

**Suggested Pivots:**
- By Asset → sum(Beginning Cost Basis), sum(Ending Cost Basis)
- By Period → sum(Additions), sum(Disposals)

