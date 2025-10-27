# Binance Exchange
Binance Exchange is a supported platform for automated data collection from cryptocurrency exchange accounts. The system collects comprehensive trading history, balances, and account activity from Binance Exchange through API integration.
**Purpose:** For organizations using Binance Exchange to automatically track and reconcile trading activity, positions, balances, and all account movements without manual data entry.

---

## 1) User Flows

### Flow A — Adding a Binance Exchange Wallet
- **When:** You want to track your Binance Exchange account
- **Preconditions:** You have a Binance Exchange API key with read-only permissions configured
- **Steps:**
  1) Add wallet through UI or API specifying Binance Exchange platform
  2) Provide API key and secret (stored securely)
  3) Optionally specify master account email if managing sub-accounts
  4) System schedules collection for next data collection
  5) Historical transactions and balances are collected during data collection
  6) Data appears in dashboard when data collection completes
- **Result:** Binance Exchange account appears with all collected transactions, trades, positions, and balances
- **Pitfalls:** API key without proper read permissions causes errors; missing master email for sub-account setups prevents master/sub-account transfers from syncing; outdated API keys fail authentication

### Flow B — First-Time Data Collection for Binance Exchange
- **When:** Initial collection after adding a Binance Exchange wallet
- **Preconditions:** API credentials validated; account accessible
- **Steps:**
  1) System identifies account type (master or sub-account)
  2) Collects all spot trading history and deposits/withdrawals
  3) Gathers balances from spot, margin, futures, perpetual, and earn products
  4) Retrieves specialized transaction types (dividends, payments, funding fees)
  5) If master account, collects transfers between master and sub-accounts
  6) If sub-account, collects sub-account specific transactions
  7) Processes and classifies all collected data
- **Result:** Complete historical trading and account activity available in dashboard
- **Pitfalls:** Very active accounts with high trading volume may take hours to fully sync; missing product permissions (futures, margin) result in incomplete data; rate limiting may delay collection

---

## 2) Key Information for Customer Support

### Credentials and Setup
- **Required Credentials:** API key and API secret from Binance Exchange account
- **API Key Requirements:** Must have read-only permissions; no trading or withdrawal permissions allowed
- **API Key Timing:** For futures data collection, API key must be generated after futures trading is enabled on the account. If futures are enabled after API key creation, the key will not have access to futures data and a new API key must be created
- **Account Email:** Master account email required if managing multiple sub-accounts through master account
- **Verification:** System validates credentials and account type during initial setup
- **Security:** API credentials stored securely and used only for read access

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
- **Historical Data:** First-time sync retrieves complete trading and account history
- **Incremental Sync:** Subsequent data collections fetch only new activity since last sync
- **Multiple Products:** Balances and transactions collected from all enabled products simultaneously
- **Rate Limiting:** System respects Binance API rate limits; may cause temporary delays but handles gracefully
- **Filtering:** LD assets (lending/deposit) automatically filtered out to prevent duplicate balances

### Common Issues
- **Missing Transactions:** Usually due to missing API permissions for specific products (futures, margin, perpetual)
- **Authentication Errors:** Outdated or revoked API keys cause failures
- **Incomplete Balances:** Missing permissions for earn products or lending prevent balance collection
- **Futures Data Not Available:** If futures were enabled after API key creation, the key cannot access futures data - a new API key must be created
- **Sub-Account Transfers Missing:** Master email not configured or incorrect email address
- **Rate Limits:** High-frequency traders may experience temporary delays due to API throttling

### Error Messages
- **"Invalid API-key, IP, or permissions for action"**: API key lacks required permissions or IP whitelist restrictions
- **"Sub-account function is not enabled"**: Account doesn't have sub-account functionality activated
- **Missing product data**: Specific API permissions missing for that product type

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
When data collection runs for a Binance Exchange wallet:

1. **Authentication & Validation:** System authenticates using API credentials and identifies account type (master or sub-account)

2. **Balance Collection:** Retrieves balances from multiple sources:
   - Spot wallet balances
   - Margin account balances
   - Futures account balances
   - Perpetual account balances
   - Simple Earn flexible savings
   - Simple Earn locked savings
   - Any other enabled products

3. **Transaction Collection:** Fetches transaction history across product types:
   - Spot orders and fills
   - Margin transfers and trades
   - Futures orders and income
   - Perpetual orders and funding fees
   - Earn deposits, withdrawals, and interest
   - Transfers between master and sub-accounts
   - Deposits and withdrawals
   - Dividends and payments
   - VIP loans and repayments

4. **Processing:** All collected data is structured, classified, and linked to appropriate accounts in your organization

### Data (Public Expectations)
- **Entities:** Wallets, Sub-accounts, Transactions, Orders, Trades, Positions, Balances
- **Important fields:**
  - Account email (for master/sub-account relationships)
  - API credentials (key and secret)
  - Product permissions (determines which data is accessible)
- **Limits:** Respects Binance API risets for all endpoints; high-volume accounts may experience slower collection

### Errors & Troubleshooting
| Issue | Likely Cause | Fix |
|---|---|---|
| Authentication failed | Invalid or outdated API keys | Verify API keys are current and correct in Binance account |
| No spot orders appearing | Missing "Enable Reading" permission | Check API key permissions in Binance, ensure read access enabled |
| Futures positions missing | API key generated before futures enabled or missing futures market permissions | Create new API key after enabling futures trading; verify API key has futures market read access enabled |
| Sub-account transfers not syncing | Master email not configured | Add correct master account email when setting up master account wallet |
| Rate limit errors | Too many API requests | Wait for rate limit to reset; system handles automatically but delays completion |
| Missing earn balances | Permissions not granted | Ensure API key has read access to earn/savings products |
| Partial transaction history | Pagination limits reached | System handles automatically; high-volume accounts may take longer to fully sync |

**Note:** For Binance Exchange-specific issues not resolved above, contact customer support with details about missing data types or error messages received.

