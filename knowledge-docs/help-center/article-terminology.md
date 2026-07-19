# Advanced Terminology: Accounting & Crypto Concepts | TRES Finance Help Center

Source: https://help.tres.finance/article/terminology

# Advanced Terminology: Accounting & Crypto Concepts

### Advanced TRES Finance Terminology: Bridging Crypto & Accounting

#### Positions (DeFi & Staking)

Concept: Beyond simple "held" assets, these are assets actively deployed in smart contracts, such as Liquidity Pools (LPs) or Staking protocols.

Accounting Context: This is often the hardest area for accountants. Is an LP token a new asset (taxable exchange) or a receipt for a deposit? Is staked ETH different from liquid ETH? TRES aggregates these to track the Principal separately from the Rewards.

📍 Location: Positions Page or Overview --> Positions Tab.

#### Claimable Rewards (vs. Liquid)

Concept: Yield or rewards that have accrued on-chain (e.g., from staking) but have not yet been "claimed" or withdrawn to the wallet.

Accounting Context: Revenue Recognition Timing. In some jurisdictions, income is taxable when it accrues (becomes Claimable); in others, only when it is received (becomes Liquid). TRES tracks these states separately to support either tax position.

📍 Location: Overview Page --> General Tab (Assets Distribution table).

#### Vested Assets

Concept: Tokens allocated to the organization (e.g., SAFTs, team allocations) that are locked by a smart contract and released over time.

Accounting Context: These represent Future Economic Benefit but are illiquid. They are often tracked "off-balance sheet" or in a separate schedule until they vest and become liquid assets.

📍 Location: Overview Page --> Vested Assets Tab.

#### Slashing

Concept: A penalty in Proof-of-Stake networks where a validator loses a portion of staked principal due to downtime or technical errors.

Accounting Context: This is an Involuntary Disposal or Loss of Principal. It is distinct from market volatility loss and must be booked as a specific realized loss or expense event.

📍 Location: Alerts Page --> Slashing Monitoring.

#### Spam Tokens

Concept: Malicious or low-value tokens airdropped to wallets without consent, often to manipulate metrics or phish users.

Accounting Context: These create "noise" in the ledger, inflating the asset count and potentially skewing tax reporting if they are assigned a false market value. Accountants need to filter these out to ensure the Balance Sheet reflects true value.

📍 Location: Assets Page --> Asset Menu --> Mark as SPAM.

### Crypto-Specific Accounting Mechanics

#### Transaction Roll-Up

Concept: An automation that consolidates high-volume, low-value on-chain events (e.g., thousands of daily mining payouts) into a single summary entry.

Accounting Context: Ledger Management. Traditional ERPs (QuickBooks/NetSuite) often crash or charge high fees for massive data volumes. Roll-ups allow for accurate financial reporting (Total Revenue) without clogging the General Ledger with thousands of individual line items.

📍 Location: Automations Page --> Create Transaction Roll-Up.

#### Gas Fees (Capitalization vs. Expense)

Concept: The fluctuating cost paid to the network to process a transaction.

Accounting Context: While usually an Expense (Bank/Network Fees), gas fees incurred during the acquisition of an asset may sometimes need to be Capitalized (added to the Cost Basis of the asset) depending on the accounting policy. TRES tracks fees separately to allow for granular mapping.

📍 Location: Overview Page --> Inflow/Outflow Widget ("Fees" metric).

Fair Market Value (FMV) & Pricing Precision

Concept: The USD value of a digital asset at a specific timestamp.

Accounting Context: Because crypto markets trade 24/7/365, "End of Day" pricing is often insufficient. TRES uses specific historical timestamps to value every transaction at the moment it occurred to calculate accurate Realized Gains/Losses.

📍 Location: Ledger Page (USD Value column) & Overview Page.

### Reconciliation & Data Integrity

#### TRES Balance (Calculated / Book Balance)

Concept: The balance derived mathematically by aggregating the entire transaction history indexed by the platform (Initial Balance + Inflows - Outflows). It represents what the platform thinks you have based on the transactions it has seen.

Accounting Context: Book Balance (Sub-Ledger). This is the equivalent of your General Ledger balance. In a perfect accounting world, this matches the bank; however, in crypto, this balance might drift due to missing data (e.g., a specific DeFi interaction not picked up by an API). If this number is different from reality, your books are "Unbalanced" and require a journal entry or manual fix.

📍 Location: Assets Page --> Asset Details (Overview Tab).

#### On-Chain Balance (Node / Actual Balance)

Concept: The live, immutable balance currently residing in the wallet address as reported directly by the blockchain network node (the "Source of Truth").

Accounting Context: Bank Statement Balance. This serves as the external control figure. Just as an accountant reconciles the GL against the monthly Bank Statement, TRES reconciles the TRES Balance against the On-Chain Balance. Any deviation here triggers an "Unbalanced" (⚠) status, alerting the accountant that the ledger does not reflect reality.

📍 Location: Assets Page --> Asset Details (Overview Tab - displayed for comparison in reconciliation checks).
