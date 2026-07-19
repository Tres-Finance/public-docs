# product-docs index

> Product & module documentation — dashboard guides (v1/v2) and module deep-dives (cost-basis, ERP, proof-of-funds, staking…)

## dashboard

- [dashboard/accounts.md](dashboard/accounts.md) — Accounts page reference: Wallets tab (cards, pending sync, edit/copy/collect/delete/clean actions, filters, pagination), Contacts tab, Unidentified Addresses tab
- [dashboard/alerts.md](dashboard/alerts.md) — Alerts page: create/manage alert cards; four types — asset-class exposure, tx activity thresholds, price change, validator slashing monitoring; email/Slack delivery
- [dashboard/assets.md](dashboard/assets.md) — Assets page: six tabs (Coins, Tokens, Fiat, Stablecoins, NFT, Positions); filter by asset class/wallet/network; balances, USD prices, reconciliation status
- [dashboard/automations.md](dashboard/automations.md) — Automations page: three templates — recurring report generation, condition-based transaction tagging (platform/asset/wallet/contact/method ID), transaction roll-ups
- [dashboard/frameworks.md](dashboard/frameworks.md) — Frameworks page: 1099 tax form generation (1099-MISC/NEC, payer TIN, per-tax-year tracking); Audit Prep, SoDA, MiCA, DORA listed as coming soon
- [dashboard/integrations.md](dashboard/integrations.md) — Integrations page: ERPs (QuickBooks, Xero, NetSuite, Universal), Request Finance, Deel, Slack, GraphQL Playground; QuickBooks rules/AP-AR/settings config and troubleshooting
- [dashboard/ledger.md](dashboard/ledger.md) — Ledger page: Transactions tab (columns, light-ledger toggle, pagination), plus Cost Basis, Pending Transactions, Roll Forward, and Pivot Tables tabs
- [dashboard/management.md](dashboard/management.md) — Admin-only Management page: cost basis, data collection, fiat value, and lock period settings; Slack notification settings; Users tab for invites and roles
- [dashboard/overview.md](dashboard/overview.md) — Overview dashboard: net worth summary (liquid/claimable/locked) and tabs — General, Positions, Staking Activity, Alert Center, Cost Basis, Multi Entity, Vested Assets
- [dashboard/reports.md](dashboard/reports.md) — Reports page: report table and statuses, export report types by category (ledger, assets, accounts, general, positions), date/category/type filters, search
- [dashboard/tres-analyst.md](dashboard/tres-analyst.md) — Tres Analyst AI chat assistant: access points (global button, per-report, per-transaction in Ledger, Overview widgets) with capabilities and example prompts for each

## dashboard-v2

- [dashboard-v2/accounts/add-manual-wallet.md](dashboard-v2/accounts/add-manual-wallet.md) — How-to: add a read-only manual wallet via Accounts > Actions > Add wallet, choosing Manual type and entering name, description, and address
- [dashboard-v2/accounts/export-accounts-report.md](dashboard-v2/accounts/export-accounts-report.md) — How-to: export a wallets/accounts report from the Accounts page Export Report button; set report name, filters, and format in the modal
- [dashboard-v2/accounts/view-contacts-tab.md](dashboard-v2/accounts/view-contacts-tab.md) — How-to: open the Contacts tab on Accounts to browse and search saved blockchain addresses, grouped alphabetically with pagination
- [dashboard-v2/accounts/view-custodians-tab.md](dashboard-v2/accounts/view-custodians-tab.md) — How-to: open the Custodians tab on Accounts to review integration sync status, last sync time, linked wallets, and synced data types
- [dashboard-v2/accounts/view-unidentified-addresses.md](dashboard-v2/accounts/view-unidentified-addresses.md) — How-to: review addresses not yet linked to contacts via the Unidentified Addresses tab; requires cost basis settings enabled for the org
- [dashboard-v2/ledger/add-tags-to-transaction.md](dashboard-v2/ledger/add-tags-to-transaction.md) — How-to: apply existing tags or create new ones from the tag dropdown in the ledger tags column; multiple tags per transaction supported
- [dashboard-v2/ledger/delete-manual-transaction.md](dashboard-v2/ledger/delete-manual-transaction.md) — How-to: delete a manual transaction from the Ledger actions menu with confirmation; requires admin/write permission; restore option for deleted items
- [dashboard-v2/ledger/filter-transactions-by-date.md](dashboard-v2/ledger/filter-transactions-by-date.md) — How-to: apply a custom date-range filter to the ledger (vs the All Time view) to analyze transactions from a specific period
- [dashboard-v2/ledger/navigate-ledger-pages.md](dashboard-v2/ledger/navigate-ledger-pages.md) — How-to: use ledger pagination (prev/next, page numbers, page-size selector); controls appear past 10 transactions and the URL tracks the current page
- [dashboard-v2/ledger/switch-to-accounting-view.md](dashboard-v2/ledger/switch-to-accounting-view.md) — How-to: toggle the switch next to the Transactions tab to a simplified accounting view of the ledger; preference persists across visits
- [dashboard-v2/ledger/view-cost-basis.md](dashboard-v2/ledger/view-cost-basis.md) — How-to: open the Cost Basis tab in the Ledger to see fair market value, inventory, cumulative cost, realized/unrealized gains; needs cost-basis currencies configured
- [dashboard-v2/ledger/view-transaction-details.md](dashboard-v2/ledger/view-transaction-details.md) — How-to: click a ledger transaction row to expand its subtransaction table (amounts, source/destination accounts, gains); click again to collapse
- [dashboard-v2/ledger/view-transactions.md](dashboard-v2/ledger/view-transactions.md) — How-to: open the Transactions tab in the Ledger to browse history with dates, types, inflow/outflow amounts, tags, fees, and ERP sync status
- [dashboard-v2/overview/view-overview.md](dashboard-v2/overview/view-overview.md) — How-to: open the Portfolio Overview page showing net worth, asset allocation breakdown, and recent account activity

## modules

- [modules/anvy/README.md](modules/anvy/README.md) — AnyV AI-powered CSV upload: map sample rows (date, amount, asset, network, direction, action, wallet) to teach the AI, transform the whole file, then review/approve
- [modules/cost-basis/README.md](modules/cost-basis/README.md) — Cost basis configuration: strategies (FIFO, FIFO_IMPAIRMENT, LIFO, AVG, MAX_GAINS, MAX_LOSSES), per-date-range strategies, per-internal-account calc, currencies, recalculation
- [modules/currency/README.md](modules/currency/README.md) — The 17 supported fiat currencies (USD, EUR, GBP, JPY, AED…) with symbols/decimals, plus selection hierarchy: report currency > org cost-basis > ERP > USD default
- [modules/custodian-integration/README.md](modules/custodian-integration/README.md) — Custodian integration knowledge base: Fireblocks, Coinbase Prime, Anchorage and others — data types per custodian, credential requirements, setup flows, troubleshooting
- [modules/dashboard/README.md](modules/dashboard/README.md) — Overview page internals: tab visibility conditions (Positions, Staking, Cost Basis, Reconciliation, Multi Entity, Vested Assets) and background/context per widget
- [modules/data-collection-commit/README.md](modules/data-collection-commit/README.md) — Data collection ("commit") flows: add wallet, daily automatic sync, manual trigger; CS notes on credentials, wait times, sync behavior, and daily limits
- [modules/erp/README.md](modules/erp/README.md) — ERP module: QuickBooks/NetSuite/Xero/Manual ERP; chart-of-accounts refresh, transaction and AP/AR sync flows, mapping rule types and priority order
- [modules/exchange-integration/README.md](modules/exchange-integration/README.md) — Exchange integration setup: required credentials per exchange (Binance, Coinbase, Coinbase Prime, Kraken…) and exchange vs custodian vs wallet distinctions
- [modules/matching/README.md](modules/matching/README.md) — Matching library: reconcile sub-transactions between two orgs via Django admin — simple rule strategies then constraint-programming M-to-N matching; config params, pitfalls
- [modules/notification-center/README.md](modules/notification-center/README.md) — Notification Center rules: transaction activity, asset exposure, price deviation, data commit completed, report ready, recurring report; email/Slack delivery
- [modules/onchain/README.md](modules/onchain/README.md) — Onchain V2 service: current/historical token balances and DeFi positions across EVM and non-EVM networks; address formats, bulk query limits, nested position tree
- [modules/platforms/BINANCE_EXCHANGE.md](modules/platforms/BINANCE_EXCHANGE.md) — Binance Exchange collection: read-only API keys, futures key timing gotcha, master/sub-account handling, product coverage (spot, margin, futures, earn), common issues
- [modules/pricing-providers/README.md](modules/pricing-providers/README.md) — Choosing pricing providers: CoinGecko (default), CoinMarketCap, exchange-specific sources (Kraken…) — strengths, limitations, and use cases of each
- [modules/pricing/README.md](modules/pricing/README.md) — Pricing module: sources (CoinGecko, CMC, DEX/LP, exchange feeds), strategy hierarchy, hourly-granularity price resolution flow, supported fiat currencies, org settings
- [modules/proof-of-funds/README.md](modules/proof-of-funds/README.md) — Proof of Funds service: scheduled balance snapshots across networks/custodians/exchanges, custodian wallet sync, MongoDB storage, data access and export flows
- [modules/report-analyst/README.md](modules/report-analyst/README.md) — Report Analyst: chat with completed exported reports (Excel/CSV) via the Analyst icon in Reports; question and comparison flows, supported types, 100MB limit
- [modules/reports/README.md](modules/reports/README.md) — Reports catalog with column-by-column reference: Basic/Extended Raw Transactions, balances, journals, reconciliation, roll forward, cost basis, staking data, audit log, and more
- [modules/rollup-transactions/README.md](modules/rollup-transactions/README.md) — Transaction rollups: rules by interval/direction/asset/platform, scheduled runs on synced data, pending→admin activation, inflow/outflow dating, fiat value summation
- [modules/spam-transactions/README.md](modules/spam-transactions/README.md) — Spam classification: auto-detection of spam tokens via GoPlus/Redefine/RugCheck on EVM chains and Solana, SPAM tags on assets/transactions, filtering, manual overrides
- [modules/stablecoin-pegging/README.md](modules/stablecoin-pegging/README.md) — Stablecoin pegging: fixed 1:1 fiat valuation for USDC/USDT/DAI/EURT etc., pricing override logic, supported stablecoin/currency table, effect on reports and cost basis
- [modules/staking/API_USAGE.md](modules/staking/API_USAGE.md) — Staking Data API: discover payloads via stakingYieldOptions, query stakingData reports (useDb vs fresh collection, 7-day fresh-fetch limit), availableStakingDataReport
- [modules/staking/OVERVIEW.md](modules/staking/OVERVIEW.md) — Staking Data module overview: collection and validation flows, data freshness Q&A, consumption paths — staking data report, Overview Staking Activity tab, API
- [modules/staking/SOLANA.md](modules/staking/SOLANA.md) — Solana staking data: rewards, MEV, commission, and block rewards; ledger tracks owner per stake account with the validator as original sender of rewards
- [modules/transaction-classification/README.md](modules/transaction-classification/README.md) — Transaction classification: auto-categorizes ledger transactions; rule building blocks (activity, platform, method, parties, asset+direction, priority); respects locked periods
- [modules/user-roles/README.md](modules/user-roles/README.md) — RBAC user roles: Admin, Member, Viewer, Associate, Pending — capabilities, permission scopes (admin/write/read), user management and dashboard access by role
