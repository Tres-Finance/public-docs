# Binance Exchange
Binance Exchange is a supported platform for automated data collection from cryptocurrency exchange accounts. The system collects comprehensive trading history, balances, and account activity from Binance Exchange through API integration.
**Purpose:** For organizations using Binance Exchange to automatically track and reconcile trading activity, positions, balances, and all account movements without manual data entry.

---

## 1) User Flows

### Flow A — Adding a Binance Exchange Wallet
- **When:** You want to track your Binance Exchange account
- **Preconditions:** You have a Binance Exchange API key with read-only permissions configured
- **Steps:**
  1) Add wallet specifying Binance Exchange platform and provide API key/secret
  2) Specify master account email if managing sub-accounts
  3) Ensure API key was created after enabling any futures trading you want to track
  4) Wait for next data collection to complete
- **Result:** Binance Exchange account with all products, transactions, and balances available
- **Pitfalls:** API key created before enabling futures cannot access futures data; missing master email prevents sub-account transfers from syncing

### Flow B — First-Time Data Collection for Binance Exchange
- **When:** Initial collection after adding a Binance Exchange wallet
- **Preconditions:** API credentials validated with proper product permissions
- **Steps:**
  1) System detects if account is master or sub-account
  2) Collects spot trading history across all symbol pairs
  3) Gathers balances from all enabled products (spot, margin, futures, perpetual, earn)
  4) Retrieves product-specific transactions (funding fees for perpetual, dividends, payments)
  5) If master account, collects transfers between master and sub-accounts (requires master email)
  6) If sub-account, collects sub-account specific deposits/withdrawals and master transfers
- **Result:** Complete historical data from all enabled Binance products
- **Pitfalls:** Missing permissions for specific products results in incomplete data; very high trading volume may take several hours; rate limiting slows collection

---

## 2) Key Information for Customer Support

### Credentials and Setup
- **Required Credentials:** Binance Exchange API key and API secret
- **Read-Only Requirement:** API key must have read-only permissions (no trading or withdrawal allowed)
- **Futures API Key Timing:** API key must be generated after futures trading is enabled. If futures are enabled after API key creation, that key cannot access futures data (create a new API key)
- **Master Account Email:** Required when tracking sub-accounts; enables master/sub-account transfer collection

### Product Coverage
The system collects data from multiple Binance Exchange products:
- **Spot Trading:** All buy/sell orders and execution history
- **Margin Trading:** Margin account balances and margin trading activity
- **Futures Trading:** USD-M futures orders and income history
- **Perpetual Trading:** Perpetual futures orders and funding fees
- **Earn Products:** Simple Earn flexible and locked savings balances and interest
- **Lending:** Lending product balances and interest accrual
- **Additional Data:** Dividends, payments, transfers between accounts, deposits, withdrawals

### Sub-Account Management
- **Master vs Sub-Accounts:** System automatically detects if account is master or sub-account
- **Master Accounts:** Collect transfers between master and sub-accounts; require master email configuration
- **Sub-Accounts:** Collect sub-account deposits and withdrawals; transfers to/from master account
- **Configuration:** When adding master account, provide master account email for proper sub-account transfer tracking
- **Separate Wallets:** Each sub-account should be added as separate wallet if tracking individually

### Collection Behavior
- **Multiple Products:** Balances and transactions collected from all enabled Binance products simultaneously
- **Rate Limiting:** System respects Binance API rate limits which may cause temporary delays
- **LD Assets Filtering:** Lending/deposit assets automatically excluded to prevent duplicate balances
- **Account Type Detection:** System automatically detects master vs sub-account and collects appropriately

### Common Issues
- **Futures Data Not Available:** API key created before enabling futures on Binance account cannot access futures data - new API key required
- **Missing Product Data:** Missing Binance API permissions for specific products (futures, margin, perpetual) results in incomplete data for those products
- **Sub-Account Transfers Missing:** Master account email not configured prevents master/sub-account transfer collection on Binance
- **Incomplete Balances:** Missing earn or lending product permissions in Binance prevent those balance types from collecting
- **Rate Limit Delays:** Binance API rate throttling slows collection for high-frequency trading accounts

### Binance Error Messages
- **"Invalid API-key, IP, or permissions for action"**: Binance API key lacks required product permissions or IP whitelist restrictions configured
- **"Sub-account function is not enabled"**: Binance account doesn't have sub-account functionality activated in account settings
- **Missing product data**: Binance API permissions not enabled for specific product types being queried

---

## 3) Detailed Explanation

### Concepts
- **Master Account:** Primary Binance Exchange account that can manage multiple sub-accounts
- **Sub-Account:** Secondary account linked to a master account, commonly used for organizational structure
- **Spot Trading:** Standard cryptocurrency trading on Binance spot market
- **Margin Trading:** Leveraged trading using borrowed funds
- **Futures:** Derivatives trading with USD-M contracts
- **Perpetual:** Perpetual futures contracts without expiration
- **Earn Products:** Savings products including Simple Earn flexible and locked savings
- **LD Assets:** Lending/deposit assets that appear as duplicates in balance queries

### How it Works
When collecting data from Binance Exchange:

1. **Account Type Detection:** System uses API to identify if account is master or sub-account type

2. **Balance Collection:** Retrieves balances from all enabled Binance products:
   - Spot wallet
   - Margin account
   - Futures account
   - Perpetual account
   - Simple Earn flexible savings
   - Simple Earn locked savings
   - Lending products

3. **Transaction Collection:** Fetches transaction history across product types:
   - Spot orders and fills
   - Margin transfers and trades
   - Futures orders and income history
   - Perpetual orders and funding fees
   - Earn deposits, withdrawals, and interest
   - Master/sub-account transfers (if master account with email configured)
   - Sub-account deposits/withdrawals (if sub-account)
   - Withdrawals and deposits
   - Dividends and payments
   - VIP loans and repayments
   - BUSD conversions and token swaps

4. **Processing:** All collected data is structured, classified, and linked to appropriate accounts in your organization

### Data (Public Expectations)
- **Entities:** Master accounts, Sub-accounts, Spot/margin/futures/perpetual/earn balances, Orders, Trades, Positions
- **Important Fields:**
  - Master account email (enables sub-account transfer tracking)
  - Binance API credentials (key and secret)
  - Product permissions in Binance account (determines accessible data)
  - Trading pair symbols for spot and margin
  - Contract symbols for futures and perpetual
- **Limits:** Binance API rate limits apply; very high trading volumes slow collection

### Errors & Troubleshooting
| Issue | Likely Cause | Fix |
|---|---|---|
| Futures positions or orders missing | API key generated before futures enabled on Binance account | Create new Binance API key after enabling futures trading |
| No spot orders appearing | Missing "Enable Reading" permission in Binance | Enable read permissions for API key in Binance account settings |
| Sub-account transfers not syncing | Master account email not configured | Add correct Binance master account email when setting up wallet |
| Missing earn balances | API key lacks earn product permissions | Enable read access to Binance Earn/Savings products for API key |
| Missing margin trading data | API key lacks margin market permissions | Enable read access to Binance margin markets |
| Missing perpetual data | API key lacks perpetual/perps permissions | Enable read access to Binance perpetual futures for API key |
| Rate limit errors | Binance API throttling for high-frequency accounts | Binance rate limits will delay collection; system handles automatically |
| Incomplete order history | High trading volume across many pairs | System paginates automatically; very active accounts may take hours to fully sync |
