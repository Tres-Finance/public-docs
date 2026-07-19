# Onchain V2 Service
A high-performance service that provides real-time and historical blockchain data for wallet balances and positions across multiple blockchain networks (EVM and non-EVM). 
**Purpose:** Helps users and applications track cryptocurrency balances and DeFi positions across different blockchain networks and protocols, enabling comprehensive portfolio tracking and financial reporting.

---

## 1) User Flows

### Flow A — Fetching Token Balances
- **When:** User needs to check token balances for a wallet
- **Preconditions:** 
  - Valid blockchain network connection
  - Valid wallet address (format varies by blockchain)
  - Optional: Historical timestamp for past balances
- **Steps:**
  1) Client sends request with wallet address and token addresses
  2) Service validates inputs and network support
  3) Service fetches current or historical balances
  4) Returns formatted balance data
- **Result:** User receives token balances with amounts and metadata
- **Pitfalls:**
  - Historical data may not be available for all networks
  - Some networks may have rate limits or performance constraints
  - Invalid addresses will be rejected

### Flow B — Retrieving DeFi Positions
- **When:** User needs to check their DeFi protocol positions
- **Preconditions:**
  - Valid blockchain network connection
  - Valid wallet address (format varies by blockchain)
  - Supported DeFi protocols
- **Steps:**
  1) Client requests positions for specific protocols or bulk fetch
  2) Service validates protocol support and inputs
  3) Service aggregates position data across protocols
  4) Returns standardized position information
- **Result:** User receives current positions with values and protocol details
- **Pitfalls:**
  - Protocol-specific features may not be available across all networks
  - Complex positions may require additional API calls
  - Historical position data availability varies by protocol

---

## 2) Q&A (Short & Direct)

- **Q:** Can I fetch historical balances for any timestamp?
  **A:** Historical balances are supported but availability varies by network. The service validates historical support before processing requests.

- **Q:** What's the maximum number of addresses I can query at once?
  **A:** The service supports bulk queries with a 10MB request size limit. Optimize requests by batching addresses efficiently.

- **Q:** How are errors handled for unsupported protocols?
  **A:** The service returns clear error messages for unsupported protocols or networks, with specific error codes for different scenarios.

- **Q:** What address formats are supported for different networks?
  **A:** Each network uses its native address format: 0x-prefixed hex for EVM networks (e.g., Ethereum, Polygon), Base58 for Solana, Bech32 for Cosmos, Base58 for Bitcoin, and Bech32 for Cardano. The service automatically validates addresses according to the network's format.

- **Q:** How are DeFi positions structured in the response?
  **A:** Positions are returned as a hierarchical tree structure that represents the complete holdings. Each position includes token metadata (names, addresses), amounts, and for complex positions like LP tokens or wrapped assets, it includes the underlying tokens with their respective types, states, and amounts. This nested structure allows for representing complex DeFi positions like staked LP tokens or wrapped tokens with their underlying assets.

  **Example Position Types:**
  - **Simple Token Position:**
    ```
    Position
    └── Token (e.g., USDC)
        ├── Amount
        ├── Token Address
        └── Metadata (name, symbol, decimals)
    ```
  
  - **Liquidity Pool Position:**
    ```
    Position
    └── LP Token (e.g., USDC-ETH LP)
        ├── Amount
        ├── Token Address
        └── Underlying Tokens
            ├── USDC
            │   ├── Amount
            │   └── Token Data
            └── ETH
                ├── Amount
                └── Token Data
    ```

  - **Staked Position:**
    ```
    Position
    └── Staked Token
        ├── Amount
        ├── Reward Tokens
        │   └── Token Data & Amounts
        └── Underlying Token
            └── Original Token Data
    ```

  **Portfolio Tracking Benefits:**
  - Complete visibility of all position components
  - Accurate valuation of complex DeFi positions
  - Real-time tracking of rewards and yields
  - Historical position analysis
  - Risk assessment across different protocols

---

## 3) Detailed Explanation

### Concepts
- **Blockchain Network:** Any supported blockchain network (EVM or non-EVM) where balances and positions are tracked
- **Historical Support:** Capability to fetch data from past blockchain states
- **Bulk Operations:** Ability to query multiple addresses or tokens in a single request
- **Cross-Chain Support:** Ability to track positions and balances across different blockchain networks in a unified way

### How it Works (High-Level)
- The service runs as a NestJS application exposing REST endpoints for balance and position queries
- Balance controller handles token balance requests across different networks
- Position controller manages DeFi protocol position data with protocol-specific adapters
- Both controllers support historical queries where available
- Error handling includes network-specific validations and clear error messages

### Data (Public Expectations)
- **Entities:**
  - Balances (token amounts and metadata)
  - Positions (protocol positions and details)
  - Networks (supported blockchain networks)

- **Important fields:**
  - `walletAddress`: The address to query
  - `network`: Target blockchain network
  - `timestamp`: For historical queries
  - `tokenAddresses`: List of tokens to query

- **Limits:**
  - Request body size: 10MB maximum
  - Rate limits vary by network
  - Historical data availability varies by network

### Errors & Troubleshooting
| Exact Message | Likely Cause | Fix |
|---|---|---|
| `Historical data not supported` | Network doesn't support historical queries | Use current timestamp only |
| `Invalid address` | Malformed wallet address | Verify address format and checksum |
| `Method not implemented` | Unsupported protocol feature | Check protocol documentation for supported features |
