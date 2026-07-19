# Skills and Use Cases | TRES Finance Help Center

Source: https://help.tres.finance/article/skills-and-use-cases

# Skills and Use Cases

Skills are the building blocks of the TRES Claude Plugin. Each skill is a specialized capability that handles a specific workflow end-to-end. You trigger them by describing what you need in natural language, and Claude figures out which skill to use and walks you through it.

See the skills and how they are connected to each other: https://tres-finance-public.github.io/tres-claude-plugin/plugin-ecosystem/

## 1. Skills Overview

Below is a summary of all available skills. The “Just Say” column shows an example phrase you can use to trigger each skill.

Just Say...

What It Does

Wallet Upload

"Add my wallets to TRES"

Onboard on-chain wallets or exchange accounts from a file or manual entry. Validates addresses, checks for duplicates, and submits in batch.

Data Collection (Commit)

"Collect data for my wallets"

Triggers on-chain data collection (full history or balances only) for all or selected wallets.

Balance Validation

"Validate my balances"

Cross-checks TRES balances against DeBank for EVM wallets and produces a color-coded discrepancy report.

Reconciliation Status

"Check my reconciliation"

Reports on-chain vs. book balance gaps per wallet and asset, showing plug transactions that explain discrepancies.

Recon Gaps

"Show me reconciliation gaps"

Fetches, displays, and helps resolve reconciliation gaps with an interactive dashboard. Supports plug/auto-fill actions.

Cost Basis

"What is my cost basis strategy?"

View/change costing strategy (FIFO, LIFO, AVG, etc.), trigger calculations, review financial issues, and manage reevaluations.

ERP Rule Suggestions

"Create ERP rules for my org"

Maps every transaction type to the correct chart of accounts entries using the TRES layered rule engine.

Invoice/Bill Matching

"Match this invoice to a tx"

Links blockchain transactions to ERP invoices/bills (AP/AR) and optionally syncs to Xero, QuickBooks, or NetSuite.

Transaction Search

"Find my ETH transactions from March"

Searches and filters transactions by date, wallet, asset, classification, fiat value, or status.

Transaction Story

"Explain this tx: 0xabc..."

Fetches a transaction by hash, renders a visual flow diagram of all asset movements, and explains in plain English.

Explorer to Ledger

"Add this Etherscan tx to my ledger"

Parses a blockchain explorer URL and records the transaction in TRES with the correct sub-transactions.

Report Advisor

"Which report do I need?"

Recommends the right TRES report for your goal (month-end close, audit, tax filing, etc.).

Report Analyzer

"Analyze this TRES report"

Upload a TRES XLSX export and get an automatic findings summary: anomalies, key metrics, and action items.

Export 3rd-Party Contacts

"Export unidentified addresses"

Extracts all unidentified counterparty addresses from your transactions and exports them as an XLSX for labeling.

Import Contacts

"Import my contacts file"

Reads a CSV/XLSX of labeled addresses and pushes them into the TRES address book.

Tag Suggestions

"Suggest tags for my transactions"

Finds untagged transactions, groups them, and suggests tags (matching existing rules or proposing new ones).

Rollup Rules

"Create a rollup rule"

Consolidates high-volume micro-transactions into clean daily or monthly summaries. Non-destructive.

Portfolio Overview

"Show me my portfolio"

Displays all wallets, token holdings, and USD balances in a clear summary.

Settings Management

"Show my org settings"

View and update organization and platform-level settings (feature flags, commit strategy, pricing, sync boundaries).

## 2. The Onboarding Flow

The fastest way to get value from TRES Finance is to follow the onboarding flow below. Each step builds on the previous one, and Claude guides you through every step conversationally. You don’t need to remember commands or navigate menus, just follow the sequence and tell Claude what you need.

Tip: You can complete the entire onboarding in a single Claude conversation. Just work through the steps one by one. Claude remembers the context and suggests the next step automatically.

### Step 1 Upload Wallets

Say: "Add my wallets to TRES"

Start by registering your on-chain wallets or exchange accounts. You can upload a CSV/Excel file with your wallet addresses, or type them in manually. Claude validates every address format, checks for duplicates against your existing wallets, and previews the batch before submitting. Supports all major chains (Ethereum, Solana, Bitcoin, Tron, Tezos, and many more) as well as 47+ exchange integrations.

### Step 2 Collect Data (Commit)

Say: "Collect data for my wallets"

Once your wallets are registered, trigger a data collection commit. Choose between full data collection (transactions + balances) for a complete ledger, or balances-only for a fast snapshot. You can run the commit on all wallets or select specific ones. The job runs asynchronously in the background, and Claude gives you a commit ID to track it.

### Step 3 Validate Balances Against DeBank

Say: "Validate my balances"

After data collection finishes, cross-check your TRES balances against DeBank for all EVM wallets. Claude fetches data from both sources, compares per-asset token amounts, and produces a color-coded report showing matches, minor differences, major discrepancies, missing assets, and untracked tokens. This gives you confidence that your on-chain data is accurate.

### Step 4 Run Reconciliation

Say: "Check my reconciliation"

With validated balances in place, review the reconciliation status across all wallets and assets. Claude queries the on-chain vs. book balance gaps, shows plug transactions that may explain discrepancies, and groups results by wallet. If gaps exist, you can use the Recon Gaps skill to drill in and resolve them by plugging differences and triggering a data collect when done.

### Step 5 Configure Cost Basis

Say: "Help me with cost basis"

Set up your cost basis strategy (FIFO, LIFO, AVG, MAX_GAINS, MAX_LOSSES, or FIFO_IMPAIRMENT) and trigger the initial calculation. Claude checks whether a strategy is already defined, helps you pick one if not, runs the calculation, and reports when it’s done. You can also review financial issues (negative balances, missing fiat prices) and create reevaluations or impairments.

### Step 6 Export Unidentified Addresses

Say: "Export unidentified addresses"

Now that your ledger has transaction history, Claude extracts all external counterparty addresses that haven’t been named yet. It queries the same data source as the TRES UI’s “Unidentified Addresses” tab, deduplicates the results, enriches them with activity data (transaction counts, fiat volumes), and exports an XLSX workbook. You fill in the names and tags, then move to the next step.

### Step 7 Import Contacts

Say: "Import my contacts file"

Take the workbook you labeled in the previous step and import it back into TRES. Claude reads the file, validates each row, skips entries without a name, and creates the contacts in your TRES address book via the API. Your ledger now shows friendly names instead of raw addresses.

### Step 8 Create Rollup Rules

Say: "Create rollup rules"

Finally, clean up your ledger by consolidating high-frequency micro-transactions. Rollup rules collapse many small entries (gas fees, staking rewards, DeFi interactions) into a single aggregated transaction per day or per month. The original raw transactions are always preserved in the Rollup Breakdown report since rollups are non-destructive. This dramatically reduces ledger noise and makes your data ready for reporting and ERP sync.

### Onboarding at a Glance

1. Upload Wallets → 2. Commit → 3. Validate Balances → 4. Reconcile → 5. Cost Basis → 6. Export Contacts → 7. Import Contacts → 8. Rollup Rules

Each step flows naturally into the next. After completing a step, Claude suggests what to do next, but you’re always in control. You can skip steps, revisit earlier ones, or ask Claude anything along the way.

## 3. Tips for Getting the Most Out of the Plugin

### Be Conversational

You don’t need special commands. Just describe what you want in plain language: “Show me all untagged transactions from last week,” “What’s the gap on my Ethereum treasury?,” or “Change my cost basis to LIFO.” Claude understands context and routes your request to the right skill.

### Upload Files Directly

When working with wallet lists, contact files, or TRES report exports, just upload the file to the conversation. Claude detects the file type and triggers the appropriate skill automatically.

### Use It for Analysis

The plugin isn’t just for actions, it’s also great for understanding your data. Upload a TRES report and ask Claude to analyze it. Paste a transaction hash and ask “what happened here?” Ask “which report should I use for my auditor?” Claude combines your live TRES data with financial reasoning to give clear, actionable answers.

### Batch Operations

Most skills support batch operations. Upload 200 wallets at once, tag transactions in bulk, import hundreds of contacts from a spreadsheet, or create rollup rules across multiple wallets. Claude handles chunking and error recovery automatically.

### Always Confirm Before Changes

Every skill that modifies your data shows a clear summary and asks for confirmation before executing. You’re never surprised by unexpected changes. If something doesn’t look right, just say “wait” or “cancel” and Claude will stop.
