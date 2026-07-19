# Tres API — Use cases / Examples — Rewards Collection

Endpoints in the 'Use cases / Examples — Rewards Collection' section of the public Tres API collection (20 requests).

## [Ethereum2] Consesnsus Withdrawals in Ethereum2 Context

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime,  $timestamp_Lt: DateTime, $platform: String, $tx_DecodedFunctionName: String ,$belongsTo_Identifier_In: [String],  $balanceFactor: Float) {
 subTransaction(
     balanceFactor: $balanceFactor,
     limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_DecodedFunctionName: $tx_DecodedFunctionName) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     tx {
        identifier
        decodedFunctionName
     }
     belongsTo {
        identifier
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "limit": 10,
    "belongsTo_Identifier_In": [],
    "tx_DecodedFunctionName": "beaconWithdrawal",
    "timestamp_Gt":"2023-05-01T00:00:00+00:00",
    "timestamp_Lt":"2023-05-02T00:00:00+00:00"
}
```

## [Ethereum2] Consesnsus Withdrawals in Ethereum2 Context - Only Exited

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime,  $timestamp_Lt: DateTime, $platform: String, $tx_DecodedFunctionName: String ,$belongsTo_Identifier_In: [String],  $balanceFactor: Float) {
 subTransaction(
     balanceFactor: $balanceFactor,
     limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_DecodedFunctionName: $tx_DecodedFunctionName) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     tx {
        identifier
        decodedFunctionName
     }
     belongsTo {
        identifier
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "limit": 10,
    "belongsTo_Identifier_In": [],
    "tx_DecodedFunctionName": "beaconWithdrawal",
    "timestamp_Gt":"2023-05-01T00:00:00+00:00",
    "timestamp_Lt":"2023-05-02T00:00:00+00:00",
    "children_Amount_Between": "32,33"
}
```

## [Ethereum2] MEV Rewards in Ethereum2

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime,  $timestamp_Lt: DateTime, $platform: String, $tx_DecodedFunctionName: String ,$belongsTo_Identifier_In: [String],  $balanceFactor: Float) {
 subTransaction(
     balanceFactor: $balanceFactor,
     limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_DecodedFunctionName: $tx_DecodedFunctionName) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     tx {
         identifier
         methodId
         classification {
             action
             activity
         }
     }
     belongsTo {
        identifier
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "limit": 10,
    "belongsTo_Identifier_In": [],
    "tx_DecodedFunctionName": "mevRewards"

}
```

## [Ethereum2] Consensus Rewards in Ethereum2

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime,  $timestamp_Lt: DateTime, $platform: String, $tx_DecodedFunctionName: String ,$belongsTo_Identifier_In: [String],  $balanceFactor: Float) {
 subTransaction(
     balanceFactor: $balanceFactor,
     limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_DecodedFunctionName: $tx_DecodedFunctionName) {
   totalCount
   results {
    amount
    balanceFactor
    timestamp
    tx {
        identifier
        isPending
        methodId
        classification {
            action
            activity
        }
    }
    belongsTo {
        identifier
    }
    sender {
        identifier
    }
    recipient {
        identifier
    }
   }
 }
}
```

**Variables:**
```json
{
    "limit": 100,
    "balanceFactor": 1,
    "tx_DecodedFunctionName":"consensusRewards",
    "platform":"ethereum2",
    "timestamp_Gt":"2023-06-30T00:00:00+00:00",
    "timestamp_Lt":"2023-07-01T00:00:00+00:00"
}
```

## [Ethereum2] Execution Layer Rewards in Ethereum2

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime,  $timestamp_Lt: DateTime, $platform: String, $tx_DecodedFunctionName: String ,$belongsTo_Identifier_In: [String],  $balanceFactor: Float) {
 subTransaction(
     balanceFactor: $balanceFactor,
     limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_DecodedFunctionName: $tx_DecodedFunctionName) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     tx {
        identifier
        decodedFunctionName
     }
     belongsTo {
        identifier
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "limit": 10,
    "balanceFactor": -1,
    "belongsTo_Identifier_In": [],
    "tx_DecodedFunctionName": "executionLayerRewards",
    "timestamp_Gt":"2023-05-01T00:00:00+00:00",
    "timestamp_Lt":"2023-06-01T00:00:00+00:00"
}
```

## [Ethereum2] Producer Rewards in Ethereum2

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime,  $timestamp_Lt: DateTime, $platform: String, $tx_DecodedFunctionName: String ,$belongsTo_Identifier_In: [String],  $balanceFactor: Float) {
 subTransaction(
     balanceFactor: $balanceFactor,
     limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_DecodedFunctionName: $tx_DecodedFunctionName) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     tx {
         identifier
         decodedFunctionName
     }
     belongsTo {
        identifier
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "limit": 10,
    "balanceFactor": -1,
    "belongsTo_Identifier_In": [],
    "tx_DecodedFunctionName": "producerReward"

}
```

## [ETH-Staking] Consesnsus Withdrawals in Ethereum Context

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $platform: String, $tx_DecodedFunctionName: String ,$belongsTo_Identifier_In: [String],  $balanceFactor: Float, $tx_Classification_Action_In: [String]) {
 subTransaction(
     tx_Classification_Action_In: $tx_Classification_Action_In,
     balanceFactor: $balanceFactor,
     limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_DecodedFunctionName: $tx_DecodedFunctionName) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     tx {
        identifier
        decodedFunctionName
     }
     belongsTo {
        identifier
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "platform": "ethereum",
    "limit": 10,
    "belongsTo_Identifier_In": [],
    "tx_Classification_Action_In": [
        "claim consensus layer rewards"
    ],
    "timestamp_Gt":"2023-04-23T00:00:00+00:00",
    "timestamp_Lt":"2023-04-24T00:00:00+00:00"
}
```

## [ETH-Staking] MEV Rewards in Ethereum

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $platform: String, $tx_DecodedFunctionName: String ,$belongsTo_Identifier_In: [String],  $balanceFactor: Float, $tx_Classification_Action_In: [String]) {
 subTransaction(
     tx_Classification_Action_In: $tx_Classification_Action_In,
     balanceFactor: $balanceFactor,
     limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_DecodedFunctionName: $tx_DecodedFunctionName) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     tx {
        identifier
        decodedFunctionName
     }
     belongsTo {
        identifier
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "platform": "ethereum",
    "limit": 10,
    "belongsTo_Identifier_In": [],
    "tx_Classification_Action_In": [
        "claim mev rewards"
    ],
    "timestamp_Gt":"2023-04-23T00:00:00+00:00",
    "timestamp_Lt":"2023-04-24T00:00:00+00:00"
}
```

## [ETH-Staking] Execution Layer Rewards in Ethereum2

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $platform: String, $tx_DecodedFunctionName: String ,$belongsTo_Identifier_In: [String],  $balanceFactor: Float, $tx_Classification_Action_In: [String]) {
 subTransaction(
     tx_Classification_Action_In: $tx_Classification_Action_In,
     balanceFactor: $balanceFactor,
     limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_DecodedFunctionName: $tx_DecodedFunctionName) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     tx {
        identifier
        decodedFunctionName
     }
     belongsTo {
        identifier
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "platform": "ethereum",
    "limit": 10,
    "belongsTo_Identifier_In": [],
    "tx_Classification_Action_In": [
        "claim execution layer rewards"
    ],
    "timestamp_Gt":"2023-01-23T00:00:00+00:00",
    "timestamp_Lt":"2023-04-24T00:00:00+00:00"
}
```

## Get Near Pool Rewards / Commission

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxBy($limit: Int, $offset: Int, $belongsTo_Identifier_In: [String], $tx_Timestamp_Gt: DateTime, $tags_Overlap: [String], $tx_BlockNumber: Int, $tx_BlockNumber_Gte: Int, $tx_BlockNumber_Lte: Int, $tx_Classification_Activity_In: [String]) {
 subTransaction(limit: $limit, offset: $offset, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_Timestamp_Gt: $tx_Timestamp_Gt, tags_Overlap: $tags_Overlap, tx_BlockNumber_Lte: $tx_BlockNumber_Lte, tx_BlockNumber_Gte: $tx_BlockNumber_Gte, tx_BlockNumber: $tx_BlockNumber, tx_Classification_Activity_In: $tx_Classification_Activity_In) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     sender {
         identifier
     }
     tx {
         blockNumber
     }
     recipient {
         identifier
     }
     tx {
         commissionRate
         classification {
             action
             activity
         }
     }
     asset {
         symbol
     }
     type
   }
 }
}
```

**Variables:**
```json
{
  "limit": 10,
  "offset": 0,
  "currency": "usd",
  "belongsTo_Identifier_In": ["bisontrails.poolv1.near"],
  "tx_Classification_Activity_In": ["ACCRUED STAKING REWARDS"],
  "decodedFunctionName_In": [],
  "children_Recipient_Identifier_In": [],
  "success_In": [],
  "excludeSpam": true,
  "onlyStarred": false,
  "thirdPartyAccounts_In": []
}
```

## Get Polygon Checkpoints

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxBy($limit: Int, $offset: Int, $belongsTo_Identifier_In: [String], $tags_Overlap: [String], $tx_BlockNumber_Gte: Int, $tx_BlockNumber_Lte: Int, $tx_Classification_Activity: String, $tx_Classification_Action: String) {
 subTransaction(limit: $limit, offset: $offset,, tags_Overlap: $tags_Overlap, tx_BlockNumber_Lte: $tx_BlockNumber_Lte, tx_BlockNumber_Gte: $tx_BlockNumber_Gte,  tx_Classification_Activity: $tx_Classification_Activity, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_Classification_Action: $tx_Classification_Action) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     sender {
         identifier
     }
     tx {
         blockNumber
     }
     recipient {
         identifier
     }
     tx {
         commissionRate
         classification {
             action
             activity
         }
     }
     asset {
         symbol
     }
   }
 }
}
```

**Variables:**
```json
{
  "limit": 100,
  "offset": 0,
  "currency": "usd",
  "belongsTo_Identifier_In": ["0x666723873d83654b38542b1fa410e56eb755879d"],
  "tx_Classification_Activity": "STAKING REWARDS",
  "tx_Classification_Action": "Checkpoint signing reward"
}
```

## Get Asset Balances

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AssetBalanceQuery($limit: Int, $offset: Int, $currency: String, $internalAccount: Float, $parentBalance_Isnull: Boolean, $asset_Name_Icontains: String, $state: String) {
  assetBalance(limit: $limit, offset: $offset, currency: $currency, belongsTo_Id: $internalAccount, parentBalance_Isnull: $parentBalance_Isnull, state: $state
  asset_Name_Icontains: $asset_Name_Icontains) {
      totalCount
    results {
      name
      id
      updatedAt
      asset {
          symbol
      }
      amount   
      state
      belongsTo {
          identifier
      }
      childBalances {
          asset {
              symbol
          }
          state
          amount
      }
      fiatValue {
        value
        fiatCurrency
      }
    }
  }
}
```

**Variables:**
```json
{
    "currency": "usd",
    "limit": 20,
    "parentBalance_Isnull": false,
    "asset_Name_Icontains": ""
}
```

## Get Asset Balance (only Accured Rewards)

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AssetBalanceQuery($limit: Int, $offset: Int, $currency: String, $internalAccount: Float, $parentBalance_Isnull: Boolean, $asset_Name_Icontains: String, $state: String) {
  assetBalance(limit: $limit, offset: $offset, currency: $currency, belongsTo_Id: $internalAccount, parentBalance_Isnull: $parentBalance_Isnull, state: $state
  asset_Name_Icontains: $asset_Name_Icontains) {
      totalCount
    results {
      name
      id
      updatedAt
      asset {
          symbol
      }
      amount   
      state
      belongsTo {
          identifier
      }
      childBalances {
          asset {
              symbol
          }
          state
          amount
      }
      fiatValue {
        value
        fiatCurrency
      }
    }
  }
}
```

**Variables:**
```json
{
    "currency": "usd",
    "limit": 10,
    "parentBalance_Isnull": false,
    "asset_Name_Icontains": "",
    "state": "claimable"
}
```

## Get Collected Rewards Between Dates from Validator and Wallet Tag

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $belongsTo_Identifier_In: [String], $tx_Timestamp_Gt: DateTime, $tags_Overlap: [String], $platform_In: [String], $sender_Identifier_In: [String]) {
 subTransaction(limit: $limit, offset: $offset, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_Timestamp_Gt: $tx_Timestamp_Gt, tags_Overlap: $tags_Overlap,
    platform_In: $platform_In, sender_Identifier_In: $sender_Identifier_In
 ) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     belongsTo {
         tags
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
     tx {
         commissionRate
         classification {
             action
             activity
         }
     }
     asset {
         symbol
     }
   }
 }
}
```

**Variables:**
```json
{
    "limit": 100,
    "offset": 0,
    "tx_Classification_Activity": "STAKING REWARDS",
    "tx_Timestamp_Gt": "2023-01-01T00:00:00",
    "tx_Timestamp_Lt": "2023-01-31T00:00:00",
    "tags_Overlap": [
        "POLADOT 1"
    ],
    "sender_Identifier_In": [
        "14wFkAiTSxhUUdpkN37QMhZv6dYcURJVgSGwqDRd4TK2qhrL"
    ]
}
```

## Get Collected Rewards Transactions In Org Context

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery($limit: Int, $offset: Int,
    $classification_Activity: String, $identifier_In: [String],
    $timestamp_Gt: DateTime, $timestamp_Lt: DateTime,
    $children_Recipient_Identifier_In: [String]) {
  transaction(
    limit: $limit
    offset: $offset
    classification_Activity: $classification_Activity
    identifier_In: $identifier_In
    timestamp_Gt: $timestamp_Gt
    timestamp_Lt: $timestamp_Lt
    children_Recipient_Identifier_In: $children_Recipient_Identifier_In
    
  ) {
    results {
      id
      success
      timestamp
      children {
          asset {
              symbol
          }
          amount
          balanceFactor
      }
      identifier
      platform
      commissionRate
      classification {
        action
        activity
        action
      }
    }
  }
}
```

**Variables:**
```json
{
  "limit": 20,
  "offset": 100,
  "classification_Activity": "STAKING REWARDS"
}
```

## Get Collected Rewards Transactions Stats In Org Context

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $classification_Activity: String, $identifier_In: [String], $timestamp_Gt: DateTime, $timestamp_Lt: DateTime) {
  transaction(
    limit: $limit
    offset: $offset
    classification_Activity: $classification_Activity
    identifier_In: $identifier_In
    timestamp_Gt: $timestamp_Gt
    timestamp_Lt: $timestamp_Lt
  ) {
    stats
  }
}
```

**Variables:**
```json
{
  "timestamp_Gt": "2023-01-01T00:00:00",
  "limit": 1
}
```

## Get Collected Rewards In Account Context By Identifier

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $belongsTo_Identifier_In: [String], $tx_Timestamp_Gt: DateTime, $tags_Overlap: [String]) {
 subTransaction(limit: $limit, offset: $offset, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_Timestamp_Gt: $tx_Timestamp_Gt, tags_Overlap: $tags_Overlap) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     sender {
         identifier
     }
     tx {
         blockNumber
     }
     recipient {
         identifier
     }
     tx {
         commissionRate
         classification {
             action
             activity
         }
     }
     asset {
         symbol
     }
   }
 }
}
```

**Variables:**
```json
{
   "offset": 0,
   "limit": 60,
   "belongsTo_Identifier_In":[],
   "tx_Timestamp_Gt": "2023-01-01T06:00:23+00:00"
  
}
```

## Get Collected Rewards In Account Context By Tag

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $belongsTo_Identifier_In: [String], $tx_Timestamp_Gt: DateTime, $tags_Overlap: [String]) {
 subTransaction(limit: $limit, offset: $offset, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_Timestamp_Gt: $tx_Timestamp_Gt, tags_Overlap: $tags_Overlap) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     belongsTo {
         tags
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
     tx {
         commissionRate
         classification {
             action
             activity
         }
     }
     asset {
         symbol
     }
   }
 }
}
```

**Variables:**
```json
{
  "classification_Activity": "STAKING REWARDS",
  "timestamp_Gt": "2022-11-01T00:00:00+02:00",
  "tags_Overlap": ["test"]
}
```

## Get Collected Rewards In Account Context By Platform

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime,  $timestamp_Lt: DateTime, $platform: String, $belongsTo_Identifier_In: [String], $tx_Classification_Action: String) {
 subTransaction(limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, belongsTo_Identifier_In: $belongsTo_Identifier_In, tx_Classification_Action: $tx_Classification_Action) {
   totalCount
   results {
       id
     amount
     balanceFactor
     timestamp
     tx {
         classification {
             action
             activity
         }
     }
     belongsTo {
        identifier
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "offset": 10,
    "limit": 10,
    "tx_Classification_Action": "Claim Consensus Rewards",
    "timestamp_Gt": "2022-11-01T00:00:00+02:00",
    "timestamp_Lt": "2023-11-01T00:00:00+02:00",
    "platform": "ethereum2",
    "belongsTo_Identifier_In": ["0x80488ac78e8621d11de736ab8ba308d0ca4d73217eea7944ec41f10cafd03fd9346d5dc6433be2e37faf19ae2b77828d"]

}
```

## Get Collected Rewards In Account Context By Platform And Tag

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($limit: Int, $offset: Int, $timestamp_Gt: DateTime,  $timestamp_Lt: DateTime, $platform: String, $tx_Classification_Action: String, $tags_Overlap: [String]) {
 subTransaction(limit: $limit, offset: $offset, timestamp_Gt: $timestamp_Gt, platform: $platform, timestamp_Lt: $timestamp_Lt, tx_Classification_Action: $tx_Classification_Action, tags_Overlap: $tags_Overlap) {
   totalCount
   results {
       id
     amount
     balanceFactor
     timestamp
     tx {
         identifier
         classification {
             action
             activity
         }
     }
     belongsTo {
        identifier
        tags
     }
     sender {
         identifier
     }
     recipient {
         identifier
     }
   }
 }
}
```

**Variables:**
```json
{
    "offset": 10,
    "limit": 10,
    "tx_Classification_Action": "Claim Execution Layer Reward",
    "timestamp_Gt": "2023-04-01T00:00:00+02:00",
    "timestamp_Lt": "2023-05-01T00:00:00+02:00",
    "platform": "ethereum2"
}
```
