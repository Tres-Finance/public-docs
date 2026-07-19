# Tres API — Reconciliation — general

Endpoints in the 'Reconciliation — general' section of the public Tres API collection (6 requests).

## Query Transactions vs Balances

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query TransactionsVsBalances(
  $belongsToIds: [ID], 
  $ assetNames: [String],
  $ endDate: DateTime,
  $ limit: Int
){
  reconciliation (
      belongsToId_In: $belongsToIds, 
      asset_Name_In: $assetNames, 
      endDate: $endDate,
      limit: $limit
      ) {
      results {
          pendingTransactionsCount
          pendingTransactionsTotalAmount
          gap (endDate: $endDate)
          plug (endDate: $endDate){
              date
              amount
              direction
              participatingWalletAddress
              hash
              }
          belongsTo {
              id
              name
              platforms
              identifier
          }
          asset {
              key
              name
              symbol
              identifier
              assetClass {
                  name
                  symbol
              }
          }
      }
}
}
```

**Variables:**
```json
{
  "limit": 10,
  "endDate": "2023-01-01T00:00:00Z",
  "belongsToIds": null,
  "assetNames": null
}
```

**Sample response (200):**
```json
{
    "data": {
        "reconciliation": {
            "results": [
                {
                    "gap": -160,
                    "plug": {
                        "date": "2023-09-19T12:00:31.737642+00:00",
                        "amount": 160,
                        "direction": "INFLOW",
                        "participatingWalletAddress": "native",
                        "hash": "5a45c4c9-d6d2-4a6d-b73a-ad0e9cabea0b"
                    },
                    "belongsTo": {
                        "id": "92764",
                        "name": "Staking Vault Wallet",
                        "platforms": [
                            "ethereum"
                        ],
                        "identifier": "0x1234567890abcdef01234567890abcdef1234567"
                    },
                    "asset": {
                        "name": "Ethereum",
                        "symbol": "ETH",
                        "assetClass": {
                            "name": "Ethereum",
                            "symbol": "ETH"
                        }
                    }
                }
            ]
        }
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "reconciliation": {
            "results": [
                {
                    "pendingTransactionsCount": 0,
                    "pendingTransactionsTotalAmount": 0,
                    "gap": -139.27,
                    "plug": {
                        "date": "2023-03-01T23:59:52+00:00",
                        "amount": 139.26632147035983,
                        "direction": "INFLOW",
                        "participatingWalletAddress": "native",
                        "hash": "837ea78e-f9f1-467e-a5bd-5b570b78ef97"
                    },
                    "belongsTo": {
                        "id": "9840",
                        "name": "Main revenue wallet - Polygon",
                        "platforms": [
                            "polygon"
                        ],
                        "identifier": "0x9276ee8dfa54e47b8ecd9049e0561f780939e7e2"
                    },
                    "asset": {
                        "id": "polygon_0x67eb41a14c0fe5cd701fc9d5a3d6597a72f641a6",
                        "name": "Giddy Token",
                        "symbol": "GIDDY",
                        "identifier": "0x67eb41a14c0fe5cd701fc9d5a3d6597a72f641a6",
                        "assetClass": {
                            "name": "Giddy",
                            "symbol": "GIDDY"
                        }
                    }
                },
                {
                    "pendingTransactionsCount": 0,
                    "pendingTransactionsTotalAmount": 0,
                    "gap": -36639.74,
                    "plug": {
                        "date": "2023-04-05T21:31:54+00:00",
                        "amount": 36639.7441828677,
                        "direction": "INFLOW",
                        "participatingWalletAddress": "native",
                        "hash": "c73030dd-75f0-4a59-ba78-51562c751c74"
                    },
                    "belongsTo": {
                        "id": "84514"
[TRUNCATED]
```

## Create Transaction Plug

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ManualSubTransaction($amount: Float!, $assetId: ID!, $assetIdentifier: String!, $belongsToId: ID!, $thirdPartyIdentifier: String!, $hash: String!, $direction: Direction, $platform: Platform!, $timestamp: DateTime!) {
  createPlug(
    amount: $amount
    assetId: $assetId
    assetIdentifier: $assetIdentifier
    belongsToId: $belongsToId
    thirdPartyIdentifier: $thirdPartyIdentifier
    direction: $direction
    hash: $hash
    platform: $platform
    timestamp: $timestamp
  ) {
    transaction {
      id
    }
  }
}
```

**Variables:**
```json
{
  "amount": 12,
  "platform": "ETHEREUM",
  "assetId": "bitcoin_native",
  "assetIdentifier": "native",
  "belongsToId": "757",
  "thirdPartyIdentifier": "0x5b34741c6320ce8608f06efd3b7489dcc62da2a7",
  "direction": "INFLOW",
  "hash": "0101010xa",
  "timestamp": "2023-09-19T12:00:31.737642+00:00"
}
```

**Sample response (200):**
```json
{
    "data": {
        "createPlug": {
            "transaction": {
                "id": "1624"
            }
        }
    },
    "debugToolbar": {
        "panels": {
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "42 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "3 calls in 2.54ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "subtitle": "6 queries in 36.31ms"
            },
            "RequestPanel": {
                "title": "Request",
                "subtitle": "view"
            },
            "HeadersPanel": {
                "title": "Headers",
                "subtitle": ""
            },
            "SettingsPanel": {
                "title": "Settings from configuration.settings",
                "subtitle": ""
            },
            "TimerPanel": {
                "title": "Time",
                "subtitle": "CPU: 1433.47ms (5768.95ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.2.4"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "595a6649c2164ab58dd1cc4cccd4ddf1"
    }
}
```

## Query Counter Transfers

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query CounterTransfers (
  $ startDate: Date
  $ endDate: Date,
  $ currency: Currency!
){
    counterTransfers {
        counterTransfersStatus (currency: $currency, startDate: $startDate, endDate: $endDate,) {
            matchedTransfersCount
            unmatchedTransfersCount
            totalFiatValueMatched
            totalFiatValueUnmatched
        }
    }
}
```

**Variables:**
```json
{
  "limit": 10,
  "belongsToIds": null,
  "assetNames": null,
  "currency": "USD"
}
```

**Sample response (200):**
```json
{
    "data": {
        "counterTransfers": {
            "counterTransfersStatus": {
                "matchedTransfersCount": 994,
                "unmatchedTransfersCount": 566,
                "totalFiatValueMatched": 1247776.0994845773,
                "totalFiatValueUnmatched": 2177.680381360559
            }
        }
    }
}
```

## Query Counter organizations

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query CounterTransfers (
  $ startDate: Date
  $ endDate: Date,
  $ currency: Currency!
){
    counterTransfers {
        counterTransfersStatus (currency: $currency, startDate: $startDate, endDate: $endDate,) {
            matchedTransfersCount
            unmatchedTransfersCount
            totalFiatValueMatched
            totalFiatValueUnmatched
        }
    }
}
```

**Variables:**
```json
{
  "limit": 10,
  "belongsToIds": null,
  "assetNames": null,
  "currency": "USD"
}
```

## Create Gap Filler Automation

`POST {{backend}}/graphql`

**Auth:** oauth2

**GraphQL query:**
```graphql
mutation CreateReconciliationGapFillRule {
    createReconciliationGapFillRule(assetId: null)
}
```

## Asset Balances

`POST {{backend}}/graphql`

**Auth:** oauth2

**GraphQL query:**
```graphql
mutation CreateReconciliationGapFillRule {
    createReconciliationGapFillRule(assetId: null)
}
```
