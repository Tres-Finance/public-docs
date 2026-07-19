# API-Based Stateless Transaction | TRES Finance Help Center

Source: https://help.tres.finance/article/api-based-stateless-transaction

# API-Based Stateless Transaction

## Stateless Transaction Lookup API

Query any on-chain transaction by its hash — without persisting anything to the database. The API fetches the transaction directly from the blockchain RPC, parses it into a structured format with sub-transactions, balance changes, and enriched asset metadata, and returns it in a single GraphQL call.

### GraphQL Endpoint

#### Query

#### Variables

Variable

Required

Description

The transaction hash (e.g. 0x1a2c...206030)

platform

Platform

The blockchain network enum (e.g. ETHEREUM, POLYGON)

#### Example Request

#### Example Response

### Response Fields

#### Transaction (top level)

identifier

The transaction hash

The blockchain network

fromAddress

Transaction sender address

toAddress

Transaction recipient / contract address

blockNumber

Block number the transaction was included in

timestamp

DateTime

Block timestamp (UTC)

Whether the transaction succeeded (reverted = false)

methodId

First 4 bytes of the input data (e.g. 0xa9059cbb). null for simple ETH transfers

decodedFunctionName

Human-readable function name (e.g. transfer, swap). Resolved from the contract ABI or a signature database. null if unknown

subTransactions

[SubTransaction]

Parsed value movements within the transaction

balanceChanges

[BalanceChange]

On-chain balance snapshots before and after the transaction

#### SubTransaction

Each sub-transaction represents a single value movement (native transfer, token transfer, or gas fee).

Identifier: basic (native transfer), gas, or log_N (Nth log event)

Address sending the value

recipient

Address receiving the value

assetIdentifier

native for the chain's native currency, or the token contract address

AssetInfo?

Enriched asset metadata (see below)

Transfer amount, adjusted by decimals (human-readable units)

One of: NATIVE_TRANSFER, TOKEN_TRANSFER, GAS

balanceFactor

-1 (outflow) or 1 (inflow), relative to the transaction sender

#### BalanceChange

Shows the on-chain balance of each account+asset pair immediately before and after the transaction.

Wallet address

native or token contract address

Enriched asset metadata

balanceBefore

Balance at blockNumber - 1 (raw, not decimal-adjusted)

balanceAfter

Balance at blockNumber (raw, not decimal-adjusted)

balanceAfter - balanceBefore

#### AssetInfo

Token symbol (e.g. USDT, ETH). null if not found in our database

Token name (e.g. Tether USD). null if not found

decimals

Token decimals (fetched from DB, or from RPC if unavailable)

### Supported Networks

All EVM-compatible blockchains are supported. Pass the network name as the platform variable.

Platform Value

Ethereum

ETHEREUM

Arbitrum

ARBITRUM

Optimism

OPTIMISM

Avalanche C-Chain

BNB Smart Chain

zkSync Era

ZKSYNC_ERA

Gnosis Chain

GNOSIS_CHAIN

Moonbeam

MOONBEAM

Manta Pacific

MANTA_PACIFIC

Polygon zkEVM

Berachain

BERACHAIN

Unichain

UNICHAIN

World Chain

WORLD_CHAIN

Immutable zkEVM

IMMUTABLE_ZKEVM

Abstract

ABSTRACT

Hyperliquid

HYPERLIQUID

The full list includes 100+ EVM networks. Any chain listed under the Platform enum with EVM support will work. If a network is missing, contact us.

### How It Works

Fetch — The transaction and its receipt are fetched from the chain's RPC node.

Parse — Native transfers, ERC-20 token transfers (from event logs), and gas fees are extracted into sub-transactions.

Balance snapshots — For each account+asset involved, the on-chain balance is queried at blockNumber - 1 (before) and blockNumber (after).

Asset enrichment — Each asset is enriched with symbol, name, and decimals from our database. If an asset is unknown, decimals are fetched directly from the token contract's RPC.

Function decoding — The method ID is resolved to a human-readable function name using the contract's ABI (if available) or a signature database.

### Limitations

Limitation

EVM only

Non-EVM chains (Solana, Bitcoin, Cosmos, Substrate, etc.) are not yet supported.

Read-only

The transaction is not persisted to the database. Each call fetches fresh data from the RPC.

No internal transactions

Internal (trace-level) calls are not parsed. Only top-level native transfers and ERC-20/ERC-721 Transfer events from logs are included.

Balance changes depend on the onchain service

If the onchain balance service is unavailable or the token is not indexed, balanceChanges may be empty.

Balance changes are raw values

balanceBefore, balanceAfter, and diff are returned as raw blockchain values (not divided by decimals). Use the asset.decimals field to convert to human-readable amounts.

Asset metadata may be partial

If a token is not in our database, symbol and name will be null. Decimals will still be fetched from the RPC.

decodedFunctionName may be null

Function decoding relies on known contract ABIs and a signature database. Uncommon or custom functions may not be decoded.

The query has a 100-second timeout. Complex transactions with many balance-change lookups may approach this limit.

Authentication required

A valid JWT Bearer token is required in the Authorization header.

### Error Handling

Scenario

Response

Invalid or non-existent tx hash

getStatelessTransaction returns null

Unsupported platform (non-EVM)

RPC unreachable or rate-limited

Timeout (>100s)

Missing auth token

HTTP 401 with {"errors": [{"message": "Authentication required"}]}

All errors are logged server-side. If you consistently get null for a valid transaction, contact support.

### Testing with cURL

### Testing with Postman

Set the request to POST https://<your-bff-host>/graphql

Under Headers, add:

Content-Type: application/json

Authorization: Bearer <your-jwt-token>

Under Body (raw JSON), paste the query and variables from the example above

Click Send

### Testing with GraphiQL

If you have access to the BFF's GraphiQL interface (/graphql in a browser), you can paste the query directly and provide the variables in the Variables panel. Note that GraphiQL requests from localhost may bypass authentication for introspection, but the actual query still requires a valid token in the Authorization header.
