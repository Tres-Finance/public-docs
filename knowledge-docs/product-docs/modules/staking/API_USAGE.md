# Staking Data API
Query staking rewards, commissions, and positions across supported blockchain platforms for comprehensive yield reporting.
**Purpose:** Data engineers managing staking operations need to extract and analyze reward data across multiple platforms to generate accurate financial reports, calculate returns, and monitor performance.

---

## 1) User Flows

### Flow A — Discover Available Staking Data
- **When:** You want to find all staking data payloads available for your organization
- **Preconditions:** Authenticated account with internal accounts (wallets) configured
- **Steps:**  1) Query `stakingYieldOptions` to get a list of all available combinations

  2) Optionally, include the `resolveStatus: true` parameter if you want to check data collection status for freshness
  
  3) Review the returned data structure containing platform, yield type, assets, and internal accounts

  4) If using `resolveStatus`, check the `status` field in the response for each account (COMPLETED, IN_PROGRESS, or FAILED)
  
  5) Note the date ranges (earliest and latest) available for each account

- **Result:** A complete list of all possible staking data queries you can perform with the associated accounts, assets, and date ranges. Use the `status` field to check data freshness if needed.

- **Pitfalls:**
  
  - If not checking status, ensure date ranges are accurate as the data will still be fetched within those dates.

### Flow B — Query Staking Data Report
- **When:** You need detailed staking data for a specific platform, account, and date range
- **Preconditions:** You know the platform, account identifier, asset, yield type, and valid date range from Flow A
- **Steps:**

  1) Call `stakingData` with required parameters: platform, identifier, start date, and end date

  2) Optionally specify `assetIdentifier`, defaults to platform native asset

  3) Keep `useDb: true`. This is the default, optimal for efficiency, and imposes no date range limit.

  4) Apply filters like `excludeZeroRewards` or `roundDecimals` as needed

  5) Retrieve results with daily summaries and per-validator breakdowns.

- **Result:** A complete staking data report with daily entries showing rewards, locked amounts, APR, and transaction ledger. Using the database ensures fast access.

- **Pitfalls:**
  
  - If fetching fresh data (`useDb: false`), the date range is limited to 7-day queries
  
  - Requesting data beyond the latest synced date when not using the database will fail—check the available date ranges first

### Flow C — Filter Available Data
- **When:** You want to find specific combinations of platforms or yield types
- **Preconditions:** Authenticated account
- **Steps:**
  1) Query `availableStakingDataReport` to see all platforms, yield types, and assets available
  2) Review internal accounts associated with each combination
  3) Use this information to discover what data can be collected for your accounts
- **Result:** A filtered list of available staking data options by platform, yield type, and asset
- **Pitfalls:**
  - Some combinations may not have internal accounts—data may be empty
  - This endpoint shows what's collectible, not what's already in the database

---

## 2) Q&A (Short & Direct)
- **Q:** How do I know what staking data is available before querying?
  **A:** Query `stakingYieldOptions` first to see all possible combinations of platforms, yield types, assets, and internal accounts with their date ranges.
- **Q:** What's the difference between using the database versus collecting fresh data?
  **A:** Database mode (`useDb: true`) is faster and fetches pre-collected data from storage. Collection mode (`useDb: false`) fetches data on-demand but is slower. Database mode also has a 7-day query limit.
- **Q:** Why did my query fail with a "range too big" error?
  **A:** When using collection mode, queries are limited to 7 days. Split your date range into multiple smaller queries.
- **Q:** What yield types are available?
  **A:** Common types include REWARD (staking rewards), COMMISSION (validator commissions), and platform-specific types like MEV, CONCENSUS, or EXECUTION for Ethereum-based platforms.
- **Q:** How do I check if my data is up to date?
  **A:** Query `stakingYieldOptions` with `resolveStatus: true`, then check the `status` field in the response for each account to see COMPLETED, IN_PROGRESS, or FAILED status.
- **Q:** What happens when I query data outside the available date range?
  **A:** The query will fail with a clear error message showing the available date range. Always verify the earliest and latest dates from `stakingYieldOptions` first.
- **Q:** Can I filter out zero-reward days from my results?
  **A:** Yes, use the `excludeZeroRewards: true` parameter to filter out days with no rewards.

---

## 3) Detailed Explanation
### Concepts
- **Platform:** Blockchain network (e.g., Ethereum, Solana, Binance) where staking occurs
- **Yield Type:** Category of staking yield (e.g., REWARD for staking rewards, COMMISSION for validator fees)
- **Internal Account:** Internal wallet identifier within the organization's system
- **Identifier:** Account address used in the platform-specific context
- **Asset Identifier:** Token or asset identifier (e.g., native platform tokens)
- **Staking Ledger:** Transaction details showing staking activity and rewards per day

### How it Works (High-Level)
The API provides a two-step approach to query staking data. First, discover what's available using `stakingYieldOptions`, which returns all possible combinations of platform, yield type, asset, and internal accounts with their associated date ranges. Then, use `stakingData` to fetch detailed reports for specific combinations.

The system collects staking data on a daily basis, processing blockchain transactions to calculate rewards, locked balances, claimable amounts, and APR. Data can be retrieved from pre-stored database records or collected fresh on-demand. The database approach is optimized for speed but has limitations on date range, while collection mode provides more flexibility but requires more processing time.

Results include both summary data (aggregated across all validators) and per-validator breakdowns, allowing for detailed analysis of staking performance at different granularities.

### Data (Public Expectations)
- **Entities:** platform, yield_type, asset, internal_account, identifier
- **Important Fields:**
  - platform — blockchain network
  - identifier — account address
  - start and end — date range
  - assetIdentifier — specific token/asset
  - yieldType — type of yield (REWARD, COMMISSION, etc.)
  - earliest and latest — available date range per option (from `stakingYieldOptions`)
  - status — data freshness status returned when querying with `resolveStatus: true` (COMPLETED, IN_PROGRESS, FAILED)
- **Limits:** Collection mode limited to 7-day query ranges; database mode provides faster access to historical data

### Errors & Troubleshooting
| Exact Message | Likely Cause | Fix |
|---|---|---|
| Range too big | Query exceeds 7-day limit in collection mode | Split date range into multiple queries of 7 days or less |
| DataNotInDB | Date range falls outside available data | Check `stakingYieldOptions` for correct date ranges |
| DataHasNotBeenCollectedException | Requesting data beyond last synced date | Use date prior to last synced timestamp |
| UnsupportedStakingCollectorType | Platform or yield type not supported | Verify platform and yield type from `availableStakingDataReport` |
| Invalid range | Start date is after end date | Correct date order in query parameters |
