# Proof of Funds
A high-scale automated service that enables organizations to track, reconcile, and report historical balances across multiple blockchain networks, custodians, and exchanges. 
**Purpose:** Helps financial institutions and digital asset companies maintain accurate records of client assets, automate reconciliation processes, and generate audit-ready reports.

---

## 1) User Flows

### Flow A — Automated Balance Snapshots
- **When:** Organization needs regular balance tracking across multiple wallets and assets
- **Preconditions:** 
  - Organization setup with snapshot policy
  - Configured networks and tokens
  - Optional: Custodian integration (e.g., Fireblocks)
- **Steps:**
  1) System fetches wallet list from configured sources (custodian/manual)
  2) Collects balances for all accounts at specified intervals
  3) Stores snapshot data in dedicated MongoDB database
  4) Generates aggregated metrics for dashboard
- **Result:** Complete historical balance record with aggregated insights
- **Pitfalls:**
  - API rate limits for centralized exchanges
  - Network-specific token configurations required
  - Historical data storage requirements

### Flow B — Custodian Integration
- **When:** Organization wants to automatically sync wallets from custodial services
- **Preconditions:**
  - Valid custodian credentials
  - Supported custodian (e.g., Fireblocks, Coinbase Prime)
- **Steps:**
  1) System connects to custodian API
  2) Syncs wallet addresses and metadata
  3) Updates account registry with custodial information
  4) Maintains ongoing sync for new wallets
- **Result:** Automated wallet discovery and metadata enrichment
- **Pitfalls:**
  - Custodian API availability
  - Read-only access requirements
  - Metadata format variations

### Flow C — Data Access and Reporting
- **When:** Organization needs to analyze or export balance data
- **Preconditions:**
  - Valid MongoDB read credentials
  - Existing snapshot data
- **Steps:**
  1) Connect to dedicated MongoDB instance
  2) Query/filter required data
  3) Export to desired format (JSON/CSV)
  4) Access dashboard for visualizations
- **Result:** Flexible data access for analysis and reporting
- **Pitfalls:**
  - Large dataset handling
  - Query optimization needs
  - Export size limitations

---

## 2) Q&A (Short & Direct)

- **Q:** How frequently can balance snapshots be taken?
  **A:** Snapshots can be configured at any interval, with most organizations choosing either daily (end-of-day) or monthly (end-of-month) frequencies.

- **Q:** What types of assets can be tracked?
  **A:** The service tracks token balances across all supported networks, staking positions when specifically configured, and balances from centralized exchanges with read-only API access.

- **Q:** How is historical data handled?
  **A:** All snapshots are permanently stored in dedicated MongoDB databases, allowing organizations to access historical data at any time for analysis or audit purposes.

- **Q:** How far back can I get historical snapshots?
  **A:** The system can generate balance snapshots from any historical point in time across supported networks, limited only by the blockchain's data availability. This means you can retrieve accurate balance data from years ago, down to the exact block timestamp.

- **Q:** What data is included in historical balance records?
  **A:** Each historical balance record includes: the token balance amount, token contract address, historical fiat price at that exact timestamp, corresponding blockchain block number, and block timestamp. This comprehensive data enables full verification of historical positions directly on the blockchain.

- **Q:** How is data accuracy ensured across different networks?
  **A:** The system employs multi-source validation, particularly for networks like Bitcoin and Cardano, where data is verified across multiple independent sources. For example, Bitcoin balances are cross-validated across different block explorers, while Cardano data is verified through multiple stake operators. Any discrepancies trigger immediate alerts for review.

- **Q:** How can I programmatically access my organization's data?
  **A:** A dedicated REST API service is available for programmatic access. The API supports account management, snapshot control, and data querying. Organizations receive secure API credentials for accessing their specific data endpoints.

---

## 3) Detailed Explanation

### Concepts
- **Snapshot Policy:** Organization-level configuration defining networks, tokens, and timing for balance collection
- **Account Registry:** System of record for tracked wallets, including metadata and source information
- **Custodian Integration:** Automated sync with institutional custody providers
- **Balance Aggregation:** Process of combining and summarizing snapshot data for reporting

### How it Works (High-Level)
- Organization defines snapshot policy including networks, tokens, and timing
- System automatically discovers and tracks wallets from custodians and manual entries
- Regular snapshots collect balances across all configured sources
- Multi-source validation ensures data accuracy across different providers
- Data is stored in dedicated MongoDB instance with read-only access
- RESTful API service (running on port 8003) provides programmatic access
- Interactive dashboard offers data visualization and analysis

### Data Validation & Verification
- **Multi-Source Validation:**
  - For networks like Cardano and Bitcoin, data is validated across multiple independent sources
  - Automated cross-validation ensures consistency and accuracy
  - Discrepancies trigger alerts and manual review processes

- **Balance Verification Guide:**
  ```
  // Example: Verifying ETH balance at specific block
  1. Get historical record from API:
     {
       "balance": "1000000000000000000",  // 1 ETH
       "blockNumber": "17000000",
       "blockTimestamp": "1678234567"
     }
  
  2. Use block number with blockchain RPC:
     eth_getBalance(address, "0x1038850") // hex of 17000000
  
  3. Compare returned value with recorded balance
  ```

- **Cross-Network Validation:**
  - Bitcoin balances verified across multiple block explorers
  - Cardano data validated through multiple stake operators
  - EVM networks checked against multiple RPC providers
  - Automated reconciliation between different data sources

### API Capabilities
- **Account Management:**
  - Add/update wallet addresses for tracking
  - Configure token lists per network
  - Manage custodian integrations
  
- **Snapshot Control:**
  - Trigger manual snapshots
  - Update snapshot scheduling
  - Query historical snapshots
  
- **Data Access:**
  - Fetch balances for specific timestamps
  - Generate historical snapshots for any past timestamp
  - Query aggregated position data
  - Export data in JSON/CSV formats
  - Retrieve block-precise historical balances

### Dashboard Features
- **Balance Overview:**
  - Total portfolio value in preferred fiat
  - Network distribution charts
  - Token allocation views
  
- **Historical Analysis:**
  - Time-series balance charts
  - Network growth comparisons
  - Token value trends
  - Point-in-time snapshot generation for any historical timestamp
  - Historical balance reconstruction at block-level precision
  
- **Export Capabilities:**
  - Custom date range exports
  - Filtered data downloads
  - Multiple format support (CSV/JSON)
  
- **Filtering Options:**
  - By network/protocol
  - By token/asset type
  - By custodian/source
  - By time period
  
- **Customization:**
  - Preferred fiat currency
  - Chart visualization options
  - Default view settings

### Data (Public Expectations)
- **Entities:**
  - Organizations (policy and configuration)
  - Accounts (wallets and metadata)
  - Snapshots (historical balance records)
  - Aggregations (summarized data)

- **Important fields:**
  - `organizationId`: Organization identifier
  - `accountAddress`: Wallet address
  - `network`: Blockchain network
  - `source`: Origin of the account (custodian/manual)
  - `fiat`: Preferred fiat currency for valuation

- **Balance Record Fields:**
  - `balance`: Token balance amount
  - `tokenAddress`: Contract address of the token
  - `blockNumber`: Blockchain block number for verification
  - `blockTimestamp`: Timestamp of the block
  - `fiatPrice`: Historical token price in configured fiat currency
  - `fiatValue`: Calculated fiat value at the historical timestamp

- **Limits:**
  - Snapshot frequency customizable
  - Historical data retained indefinitely
  - Read-only access to exchange APIs
  - MongoDB query limitations apply

### Errors & Troubleshooting
| Exact Message | Likely Cause | Fix |
|---|---|---|
| `Custodian sync failed` | Invalid credentials or API issues | Verify custodian credentials and API status |
| `Network not supported` | Unconfigured network in policy | Add network to organization policy |
| `Invalid token address` | Incorrect token configuration | Verify token address for network |
