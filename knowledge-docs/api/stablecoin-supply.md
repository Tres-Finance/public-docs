# Tres API — Stablecoin Supply

Endpoints in the 'Stablecoin Supply' section of the public Tres API collection (2 requests).

## stablecoinSupplyReport

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StablecoinSupplyReport($fromDate: DateTime!, $toDate: DateTime!, $blockchain: String!, $token: String!) {
    stablecoinSupplyReport(fromDate: $fromDate, toDate: $toDate, blockchain: $blockchain, token: $token) {
        metadata {
            fromDate
            toDate
            fromBlock
            toBlock
            blockchain
            token
            version
        }
        aggregatedData {
            openingTotalSupply
            mint
            burn
            computedTotalSupply
            closingTotalSupply
            reconciliationDiff
            restrictedBalance
            treasuryBalance
            netCirculatingSupply
        }
        treasuryWallets {
            account
            balance
        }
        restrictedAccounts {
            account
            balance
        }
    }
}
```

**Variables:**
```json
{
    "fromDate": "2026-01-01T00:00:00",
    "toDate": "2026-04-01T00:00:00",
    "blockchain": "ethereum",
    "token": "USDT"
}
```

## stablecoinSupplyEvents

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StablecoinSupplyEvents(
    $iaIdentifier: [String!]
    $eventTypes: [String!]
    $txHash: String
    $fromBlock: Int
    $toBlock: Int
    $fromDate: DateTime
    $toDate: DateTime
    $minAmount: Float
    $maxAmount: Float
    $limit: Int!
    $offset: Int!
) {
    stablecoinSupplyEvents: subTransaction(
        platform: "token_supply_tracking"
        belongsTo_Identifier_In: $iaIdentifier
        tx_DecodedFunctionName_In: $eventTypes
        tx_Identifier: $txHash
        tx_BlockNumber_Gte: $fromBlock
        tx_BlockNumber_Lte: $toBlock
        timestamp_Gte: $fromDate
        timestamp_Lte: $toDate
        amount_Gte: $minAmount
        amount_Lte: $maxAmount
        ordering: "timestamp,desc"
        limit: $limit
        offset: $offset
    ) {
        totalCount
        events: results {
            timestamp
            tx { blockNumber, transactionId: identifier, eventType: methodId }
            sender: originalSender { identifier }
            recipient: originalRecipient { identifier }
            amount
            balanceFactor
        }
    }
}
```

**Variables:**
```json
{
    "iaIdentifier": ["solana_es9vmfrzacermjfrf4h2fyd4kconky11mcce8benwnyb"],
    "eventTypes": ["issue"],
    "txHash": null,
    "fromBlock": 0,
    "toBlock": null,
    "fromDate": "2020-01-01T00:00:00+00:00",
    "toDate": "2026-01-01T00:00:00+00:00",
    "minAmount": 1000000,
    "maxAmount": null,
    "limit": 3,
    "offset": 0
}
```
