# api-examples index

> Runnable API example scripts (Python/JS) — end-to-end usage of the Tres API

## root

- [detect_reconciliation_slippage.md](detect_reconciliation_slippage.md) — Python: paginate sub-transactions for a wallet/asset, fetch stateless historical balance at each tx timestamp, print txs where running balance diverges >0.1
- [dump_pof.md](dump_pof.md) — JS: export Proof-of-Funds accountBalances from MongoDB to CSV via aggregation pipeline, filtered by dates, networks, and token symbols (mongodb + json2csv)
- [gather_balances.md](gather_balances.md) — Python: login, list/create wallets, trigger commit, poll latest commits, fetch delegated_to_account asset balances (incl. pending), write BalanceOutput rows to CSV
- [gather_daily_cosmos_generated_rewards.md](gather_daily_cosmos_generated_rewards.md) — Python: pull Cosmos sub-transactions tagged STAKING REWARDS / ACCRUED STAKING REWARDS for a date range, split reward vs commission per validator, export to CSV
- [gather_ethereum2_rewards.md](gather_ethereum2_rewards.md) — Python: fetch all Ethereum2 reward sub-transactions for three specific validator pubkeys over a date range via get_all_sub_transactions, write to CSV
- [gather_internal_accounts.md](gather_internal_accounts.md) — Python: login, list all internal accounts (wallets) and export name, platforms, identifier, tags, total fiat value, description to CSV
- [gather_rewards.md](gather_rewards.md) — Python tour of reward queries: create/tag wallets, trigger commit, get balances and claimable rewards, query STAKING REWARDS by org, account, tag, and validator sender
- [gather_staking_data.md](gather_staking_data.md) — Python: iterate 365 daily timestamps over POSITIONS_TO_TEST, fetch stateless staking positions per day via ThreadPoolExecutor, dump position children to output.txt
- [gather_stateless_data.md](gather_stateless_data.md) — Python: minimal concurrent fetch of current stateless positions for each platform/wallet combo in POSITIONS_TO_TEST (ThreadPoolExecutor, no output file)
- [gather_stateless_positions.md](gather_stateless_positions.md) — Python: fetch daily stateless staking positions for a month window, enrich children with date/tag/display_name/validator address, write JSON to output.txt
- [gather_stateless_token_balance.md](gather_stateless_token_balance.md) — Python: query historical stateless token balances for a Solana wallet per asset per day; log results to output.txt and missing assets to missing_balances.txt
- [gather_sub_txs_by_identifier.md](gather_sub_txs_by_identifier.md) — Python: fetch sub-transactions matching a list of transaction hashes (tx_identifiers, limit 10000) and write results to CSV
- [gather_sub_txs_by_internal_account.md](gather_sub_txs_by_internal_account.md) — Python: fetch sub-transactions belonging to given wallet addresses (belongs_to_identifiers, limit 10000) and write results to CSV
- [monitor_polygon_delegators.md](monitor_polygon_delegators.md) — Python: monitor Polygon PoS delegators — paginate deposits/withdrawals vs staking contracts plus daily stateless positions, emit StakingPositionMonitoringOutput CSV
- [push_otc_manual_transactions.md](push_otc_manual_transactions.md) — Python: read OTC trades from CSV, create a manual transaction per order plus paired INFLOW/OUTFLOW manual sub-transactions for base/quote legs with USD notional
- [stakingData.md](stakingData.md) — JS (Node): login for JWT, fetch stakingYieldOptions, then stakingData per platform/yieldType/account; save results to JSON and flattened CSV
- [update_historical_fiat_values_for_txs_by_asset_class.md](update_historical_fiat_values_for_txs_by_asset_class.md) — Python: load asset-class/currency/price rows from CSV, find sub-transactions per asset class in a date range, batch-set manual fiat unit values via mutation
- [update_historical_fiat_values_for_txs_by_wallet.md](update_historical_fiat_values_for_txs_by_wallet.md) — Python: load wallet/asset/price rows from CSV, find each wallet's sub-transactions for that asset in a date range, batch-set manual fiat unit values

## core

- [core/__init__.md](core/__init__.md) — Package init: configures Python logging (INFO level, timestamped format) for the example scripts
- [core/csv/__init__.md](core/csv/__init__.md) — Package init: re-exports the csv helper module (`from .csv import *`)
- [core/csv/csv.md](core/csv/csv.md) — CSV helpers: flatten nested Pydantic models/dicts into dotted-key rows, build DictWriter headers, and write_output() dumping results to output.csv
- [core/graphql_functions.md](core/graphql_functions.md) — Shared client helpers: auth via getApiKey, create wallet, tag accounts, trigger commit, get balances/claimable rewards, sub-transactions, stateless positions/balances, manual txs
- [core/graphql_queries.md](core/graphql_queries.md) — GraphQL query/mutation strings: login, create wallet, internal wallets, trigger commit, collectAudit, assetBalance, transactions, stateless positions/balances, manual tx mutations
- [core/graphqlclient/__init__.md](core/graphqlclient/__init__.md) — Package init: re-exports the GraphQLClient class (`from .graphqlclient import *`)
- [core/graphqlclient/graphqlclient.md](core/graphqlclient/graphqlclient.md) — Minimal GraphQLClient: urllib-based POST of query+variables to an endpoint with injectable Authorization bearer token header
- [core/models/__init__.md](core/models/__init__.md) — Package init: re-exports basic, balance_response, transaction_response, and outputs model modules
- [core/models/balance_response.md](core/models/balance_response.md) — Pydantic models for assetBalance responses: Balance (amount, state, belongs_to, asset, fiat_value, block_number) and paginated BalanceResponse
- [core/models/basic.md](core/models/basic.md) — Base Pydantic models: CamelModel (camelCase aliases), Currency/Direction enums, FiatValue, InternalAccount, Account, Asset
- [core/models/enums.md](core/models/enums.md) — Case-insensitive StrEnums: the full Platform list (chains, exchanges, custodians) plus related enums used across the examples
- [core/models/outputs.md](core/models/outputs.md) — CSV output row models: StakingPositionMonitoringOutput, BalanceOutput (validator staking totals), InternalAccountOutput
- [core/models/stateless_response.md](core/models/stateless_response.md) — Pydantic models for stateless queries: StatelessPosition with StatelessAssetBalanceChild children, validator-address Extras, StatelessAssetDetails
- [core/models/transaction_response.md](core/models/transaction_response.md) — Pydantic models for transaction queries: Transaction, SubTransaction (computed balance_impact), SubTransactionResponse, GeneratedRewardsReportOutput

## data

- [data/demo.md](data/demo.md) — Demo config: WALLETS_TO_CREATE sample (Flow wallet) plus CLIENT_ID/CLIENT_SECRET placeholders used by the gather_* scripts
- [data/stateless_demo.md](data/stateless_demo.md) — Stateless demo config: POSITIONS_TO_TEST wallets per platform (NEAR, Cosmos, Celo, Eth2, Polkadot, Flow, Sui…), Polygon delegators and date range, credential placeholders
