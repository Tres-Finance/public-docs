# Data Collection (Commit)
Data Collection is the process by which your organization's wallet data is automatically synchronized from supported platforms into the system. Once data is collected, it appears in your dashboard, reports, and can be used for all downstream features. This process is also referred to as a "commit" in technical contexts.
**Purpose:** For accounting and treasury teams to keep their multi-wallet crypto portfolios up-to-date automatically without manual data entry.

---

## 1) User Flows

### Flow A — Adding a New Wallet
- **When:** You want to track a wallet that's not currently in your organization
- **Preconditions:** You need the wallet address and know which platform/network it's on
- **Steps:**
  1) Add wallet through the UI (or API) by providing platform, wallet address, and optional metadata (name, tags)
  2) System schedules collection for the next data collection (or trigger manually for immediate sync)
  3) Historical transactions and current balances are collected during the data collection
  4) Data appears in your dashboard when data collection completes
- **Result:** Wallet appears in your organization with all collected transactions and balances
- **Pitfalls:** Incorrect network or address can cause errors; some platforms require additional credentials (API keys); very old wallets with extensive history may take longer for full historical sync

### Flow B — Daily Sync (Automatic Data Collection)
- **When:** Scheduled automatic sync runs daily for all active wallets
- **Preconditions:** Wallets must be active and platforms must be accessible
- **Steps:**
  1) System checks for wallets that need syncing (not updated in the last sync window)
  2) Starts parallel collection for all wallets across all platforms
  3) Collects only new transactions and updated balances since last sync
  4) Processes and enriches collected data (classifications, balances, fiat values)
  5) Data appears in dashboard when processing completes
- **Result:** Your organization's data is updated with the latest activity across all wallets
- **Pitfalls:** Large wallets or high transaction volumes can slow completion; API rate limits may delay some platforms; network issues can cause temporary failures

### Flow C — Manual Data Collection Trigger
- **When:** You want to force an immediate sync without waiting for the scheduled time
- **Preconditions:** You have permission to trigger data collections; your organization may have daily data collection limits
- **Steps:**
  1) Trigger data collection through UI or API for specific wallets or all wallets
  2) System validates no other data collection is currently in progress
  3) Starts collection process immediately with selected scope (all wallets or specific subset)
  4) Progress can be monitored through data collection status and logs
  5) Notification when complete
- **Result:** Latest data synchronized on demand and available in dashboard
- **Pitfalls:** Cannot trigger if a data collection is already running; hitting daily data collection limits blocks new triggers; specifying date ranges limits the scope of data collected

---

## 2) Key Information for Customer Support

### Adding Wallets
- **Process:** Add wallet through UI or API by providing platform (network), wallet address, and optional metadata (name, tags)
- **Data Collection Timing:** Collection occurs during the next data collection (automatic or manual); can be manually triggered for immediate sync if needed
- **Credentials:** Most blockchain wallets require only addresses; exchanges and custodians require API keys for access
- **API Key Requirements:** For exchanges, API keys must be read-only (no trading or withdrawal permissions)
- **Verification:** Customers can verify wallet addition success by checking if it appears in their wallet list

### Platform Support
- **Coverage:** The system supports a comprehensive list of blockchain networks, exchanges, custodians, and financial services
- **Updates:** New platforms are added regularly as networks launch and develop
- **Complete List:** For the full list of supported platforms, see the dedicated supported platforms documentation

### Wait Times and Performance
- **New Wallets:** Added wallets will be fully collected in the next data collection (either automatic daily data collection or manual data collection)
- **Data Collection Duration:** Data collections can take from minutes to several hours to complete depending on:
  - Transaction history volume (more history = longer processing)
  - Platform API response times and rate limits
  - Network congestion
  - Size of token portfolio
  - Number of wallets being synced

### Sync Behavior
- **Automatic Sync:** Runs daily on schedule for all active wallets
- **Parallel Processing:** All wallets collect simultaneously during data collection (not sequential)
- **Data Consistency:** All wallets sync to the same timestamp window for consistent reporting
- **Incremental Sync:** Only fetches new/changed data since last sync (not full history each time)
- **Full History:** First-time wallet sync retrieves complete historical data; subsequent syncs are incremental

### Data Collection Limits and Retries
- **Daily Limits:** Each organization has a maximum number of data collections per day (configurable per plan)
- **Parallel Limits:** System can process unlimited wallets simultaneously within a single data collection
- **Rate Limiting:** Respects external platform rate limits (may cause delays but not failures)

### Data Collection Scope
- **Transactions:** All transfers, exchanges, staking, rewards, delegations, fees
- **Balances:** Current token holdings for all assets on each platform
- **Additional Data (Platform-Dependent):**
  - DeFi positions and liquidity pools
  - Staking positions and validator information
  - Sub-accounts (e.g., Solana token accounts)
  - Exchange-specific activities (trades, fee rebates, interest payments)
  - Bank transactions and fiat movements
- **Enrichment:** All data automatically classified, categorized, and linked across your portfolio
- **Fiat Values:** Currency conversions and valuations computed for reporting
- **Manual Transactions:** Users can manually add transactions for any reason, including custom entries or addressing missing transactions in the system

### Blockchain vs Exchange/Custodian Differences
- **Blockchain Wallets:** 
  - Read directly from network nodes
  - No API credentials required
  - Public data accessible via address
  - Synchronizes transaction history and balances
  
- **Exchanges & Custodians:**
  - Require API credentials (API keys, secrets)
  - API keys must be read-only with no trading or withdrawal permissions
  - Access through provider APIs
  - May include additional data types (trading history, order details, fee breakdowns)
  - Credential management handled securely

---

## 3) Detailed Explanation

### Concepts
- **Data Collection (Commit):** A sync operation that collects, enriches, and processes data from one or more wallets across all or selected platforms
- **Internal Account:** Represents a wallet or account in your organization (can be blockchain addresses, exchange accounts, or other platform accounts)
- **Platform:** A supported network or service (blockchain, exchange, custodian, etc.)
- **Collection:** The process of fetching transaction history and current balances from external data sources
- **Enrichment:** The automated processing and classification of collected data to make it ready for reporting and analysis

### How it Works (High-Level)
When data collection is triggered (automatically or manually), the system processes your organization's wallets through these stages:

1. **Validation:** The system checks that no other data collection is running, daily limits aren't exceeded, and all required credentials are valid.

2. **Collection:** For each wallet, data is retrieved from the appropriate source:
   - For blockchain wallets: connects to network nodes to read transaction history and current balances
   - For exchanges/custodians: uses read-only API credentials to fetch account activity and holdings
   - Only retrieves data changed since last sync (or within specified date range for historical pulls)

3. **Processing & Enrichment:** Collected data is structured and enhanced:
   - Transactions are categorized and classified automatically
   - Balances are calculated and validated
   - Data is linked to your organization and proper wallet accounts
   - Currency conversions and fiat valuations are computed

4. **Finalization:** Once all data processing completes:
   - Data collection status updates to completed
   - New balances and transactions become visible in your dashboard
   - Organization timestamp updates to reflect sync completion
   - You receive notifications about results

Multiple wallets process simultaneously for faster completion.

### Errors & Troubleshooting
| Exact Message | Likely Cause | Fix |
|---|---|---|
| `There is already a running data collection` | Another data collection is in progress | Wait for current data collection to complete or check progress |
| `You have reached the maximum number of data collections for today` | Daily quota exceeded | Wait until next day or contact support |
| Data collection status: `FAILED` | External platform error or rate limit | System retries automatically; check platform credentials if persistent |
| Wallet not collecting data | Invalid credentials or API access issues | Verify API keys have read-only permissions and are configured correctly for the platform |
| No transactions appearing | Wallet may be empty or address is incorrect | Confirm wallet address and check on block explorer |
| Missing transactions | For exchanges: missing permissions in API key or outdated API keys; for blockchains: incomplete historical data or address mismatch | For exchanges, verify API key has all required read permissions and keys are current; for blockchains, ensure correct address format and allow time for historical sync; if persistent, contact support |

**Note:** For any unexpected failures or issues not resolved by the above, please contact customer support for assistance.

