# Tres API — Asset Balances — Statefull

Endpoints in the 'Asset Balances — Statefull' section of the public Tres API collection (20 requests).

## Get Organization Positions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery($limit: Int, $offset: Int) {
  position(limit: $limit, offset: $offset) {
    results {
      application
      identifier
      currentBalance {
        name
        amount
        fiatValue {
          value
        }
        childBalances {
          amount
          name
          fiatValue {
            value
          }
        }
      }
      displayName
      walletName
      createdAt
    }
  }
}
```

**Variables:**
```json
{
    "currency": "eur"
}
```

**Sample response (200):**
```json
{
    "data": {
        "position": {
            "results": [
                {
                    "application": "audius",
                    "identifier": "audius_staking_position-0x6802374B0e9e2274f3B9863700cE2A4ecd00B93D",
                    "currentBalance": {
                        "name": "audius_virtual_vault",
                        "amount": "1.00000000000000000000000000000000",
                        "fiatValue": {
                            "value": "33931985302816063577.71359340000000000000000000000000"
                        },
                        "childBalances": [
                            {
                                "amount": "100328493725397864877.00000000000000000000000000000000",
                                "type": "LOCKED",
                                "name": "Audius",
                                "fiatValue": {
                                    "value": "33821242198745535772.76785007000000000000000000000000"
                                }
                            },
                            {
                                "amount": "328512145017640374.00000000000000000000000000000000",
                                "type": "CLAIMABLE",
                                "name": "Audius",
                                "fiatValue": {
                                    "value": "110743104070527804.94574333200000000000000000000000"
                                }
                            }
                        ]
                    },
                    "displayName": "Audius Staking",
                    "walletName": "Eilon",
                    "createdAt": "2022-06-30T15:43:36+00:00"
                }
            ]
        }
    }
}
```

## Get Organization Per Wallet

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query Position($currentBalanceBelongsToIdentifier: String) {
  position(currentBalance_BelongsTo_Identifier: $currentBalanceBelongsToIdentifier) {
    results {
      application
      contractAddress
      createdAt
      displayName
      extras
      id
      identifier
      platform
      type
      updatedAt
      walletAddress
      walletName
      currentBalance {
        asset {
          name
          platform
        }
      }
    }
    pageInfo {
      hasNextPage
      totalCount
    }
  }
}
```

**Variables:**
```json
{
}
```

## Get Organization Balance

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetOrgBalance($limit: Int, $offset: Int, $balanceName: String, $assetClass_Assets_Type: String, $assetClass_Assets_Identifier_Icontains: String, $assetClass_Assets_Platform_In: [String], $showZeros: Boolean, $currency: String, $exportName: String, $exportFormat: String, $state: String, $position_Type: String, $internalAccountIds: [String], $position_Isnull: Boolean, $assetClass_In: [ID]) {
  organizationBalance(
    limit: $limit
    offset: $offset
    balanceName: $balanceName
    assetClass_Assets_Type: $assetClass_Assets_Type
    assetClass_Assets_Platform_In: $assetClass_Assets_Platform_In
    assetClass_Assets_Identifier_Icontains: $assetClass_Assets_Identifier_Icontains
    showZeros: $showZeros
    currency: $currency
    exportName: $exportName
    exportFormat: $exportFormat
    state: $state
    position_Type: $position_Type
    internalAccountIds: $internalAccountIds
    position_Isnull: $position_Isnull
    excludeUnderDelegation: true
    assetClass_In: $assetClass_In
  ) {
    totalCount
    results {
      id
      reconciliationMissing
      amount
      name
      state
      updatedAt
      balances {
          position {
              id
          }
        id
        asset {
          platform
          symbol
        }
        belongsTo {
          identifier
        }
        childBalances {
          amount
          asset {
            symbol
            contract {
                applications
            }
          }
        }
      }
      position {
        application
        type
      }
      assetClass {
        symbol
        id
        verificationStatus
      }
      fiatValue {
        value
      }
    }
  }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "limit": 1,
  "offset": 0,
  "balanceName": "",
  "position_Isnull": true,
  "assetClass_Assets_Identifier_Icontains": "",
  "assetClass_Assets_Type": "token",
  "assetClass_Assets_Platform_In": [],
  "internalAccountIds": [],
  "showZeros": false,
  "assetClass_In": []
}
```

## Get Organization Balance of DeFi Assets

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetOrgBalance($limit: Int, $offset: Int, $balanceName: String, $assetClass_Assets_Type: String, $assetClass_Assets_Identifier_Icontains: String, $assetClass_Assets_Platform_In: [String], $showZeros: Boolean, $currency: String, $exportName: String, $exportFormat: String, $state: String, $position_Type: String, $internalAccountIds: [String], $position_Isnull: Boolean, $assetClass_In: [ID]) {
  organizationBalance(
    limit: $limit
    offset: $offset
    balanceName: $balanceName
    assetClass_Assets_Type: $assetClass_Assets_Type
    assetClass_Assets_Platform_In: $assetClass_Assets_Platform_In
    assetClass_Assets_Identifier_Icontains: $assetClass_Assets_Identifier_Icontains
    showZeros: $showZeros
    currency: $currency
    exportName: $exportName
    exportFormat: $exportFormat
    state: $state
    position_Type: $position_Type
    internalAccountIds: $internalAccountIds
    position_Isnull: $position_Isnull
    excludeUnderDelegation: true
    assetClass_In: $assetClass_In
  ) {
    totalCount
    results {
      id
      reconciliationMissing
      amount
      name
      state
      updatedAt
      balances {
          position {
              id
          }
        id
        asset {
          platform
          symbol
        }
        belongsTo {
          identifier
        }
        childBalances {
          amount
          asset {
            symbol
            contract {
                applications
            }
          }
        }
      }
      position {
        application
        type
      }
      assetClass {
        symbol
        id
        verificationStatus
      }
      fiatValue {
        value
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
  "offset": 0,
  "balanceName": "",
  "position_Isnull": true,
  "assetClass_Assets_Identifier_Icontains": "",
  "assetClass_Assets_Type": "token",
  "assetClass_Assets_Platform_In": [],
  "internalAccountIds": [],
  "showZeros": false,
  "assetClass_In": ["1"]
}
```

## Get Organization Balance + Cost Basis

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetOrgBalance($id_In: [String], $limit: Int, $offset: Int, $balanceName: String, $showZeros: Boolean, $currency: String, $state: String, $timestamp: DateTime) {
  organizationBalance(
    id_In: $id_In
    limit: $limit
    offset: $offset
    balanceName: $balanceName
    showZeros: $showZeros
    currency: $currency
    state: $state
    timestamp: $timestamp
  ) {
    totalCount
    results {
      id
      costBasis {
        totalRealizedGains
        totalCost
        totalRunningInventoryQuantity
    }
      assetClass {
        name
        symbol
        id
        verificationStatus
      }
      fiatValue {
        value
      }
      financialIssues {
        type
        tx {
          identifier
        }
      }
      balances {
        id
        amount
        costBasis {
            totalRealizedGains
            totalCost
            totalRunningInventoryQuantity
        }
        reconciliation
        financialIssues {
          type
          tx {
            identifier
          }
        }
        belongsTo {
          id
          name
          identifier
        }
        fiatValue {
          value
        }
      }
    }
  }
}
```

**Variables:**
```json
{
  "offset": 1,
  "limit": 1,
  "balanceName": "",
  "currency": "usd",
  "state": "wallet",
  "showZeros": false,
  "id_In": [],
  "timestamp": "2024-12-31T00"
}
```

## Get Organization Balance + Counter Transfers State

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetOrgBalance($id_In: [String], $limit: Int, $offset: Int, $balanceName: String, $showZeros: Boolean, $currency: String, $state: String, $timestamp: DateTime) {
  organizationBalance(
    id_In: $id_In
    limit: $limit
    offset: $offset
    balanceName: $balanceName
    showZeros: $showZeros
    currency: $currency
    state: $state
    timestamp: $timestamp
  ) {
    totalCount
    results {
      id
      costBasis {
        runningBalance
        totalCost
        totalRunningInventoryQuantity
    }
      assetClass {
        name
        symbol
        id
        verificationStatus
      }
      counterTransfersStatus {
        matchedTransfersCount
        unmatchedTransfersCount
        totalFiatValueMatched
        totalFiatValueUnmatched
      }
      counterBalanceStatus {
        counterTotalCost
        counterRunningBalance
        counterTotalRunningInventoryQuantity
      }
    }
  }
}
```

**Variables:**
```json
{
  "offset": 1,
  "limit": 1,
  "balanceName": "",
  "currency": "usd",
  "state": "wallet",
  "showZeros": false,
  "id_In": []
}
```

## Get Asset Balances (Root Balances)

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAssetBalances($limit: Int, $offset: Int, $currency: String, $state: String, $internalAccount: Float, $parentBalance_Isnull: Boolean, $assetNameIcontains: String $belongsTo_Identifier: String, $asset_Platform: String, $status: String, $groupTime_Lte: DateTime, $groupTime_Gte: DateTime, $includeArchived: Boolean,  $asset_Identifier: String, $groupId: UUID) {
  assetBalance(
    groupId: $groupId
    state: $state
    limit: $limit
    offset: $offset
    currency: $currency
    belongsTo_Id: $internalAccount
    parentBalance_Isnull: $parentBalance_Isnull
    asset_Name_Icontains: $assetNameIcontains
    excludeUnderDelegation: false
    includeArchived: $includeArchived
    belongsTo_Identifier: $belongsTo_Identifier
    asset_Platform: $asset_Platform
    status: $status
    groupTime_Gte: $groupTime_Gte,
    groupTime_Lte: $groupTime_Lte,
    asset_Identifier: $asset_Identifier

  ) {
    totalCount
    results {
      id
      rollingId
      name
      state
      amount
      position {
        displayName
        application
        extras 
        identifier
      }
      belongsTo {
        name
        identifier
        description
        tags
        parentPlatform
      }
      updatedAt
      asset {
        identifier
        platform
        symbol
        assetClass {
          id
          verificationStatus
        }
        contract {
          applications
          contractName
        }
      }
      fiatValue {
        value
      }
      childBalances {
        asset {
          symbol
        }
        state
        amount
      }
    }
  }
}
```

**Variables:**
```json
{
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "parentBalance_Isnull": true
}
```

**Sample response (200):**
```json
{
    "data": {
        "assetBalance": {
            "totalCount": 277,
            "results": [
                {
                    "name": "Wrapped Ether",
                    "state": "CLAIMABLE",
                    "asset": {
                        "identifier": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                        "platform": "ETHEREUM",
                        "symbol": "WETH",
                        "assetClass": {
                            "id": "3"
                        },
                        "contract": {
                            "applications": [
                                "wrapped-ethereum"
                            ]
                        }
                    },
                    "fiatValue": {
                        "value": 2219927.7704984616
                    },
                    "amount": 1047.2380871749801,
                    "childBalances": []
                },
                {
                    "name": "Wrapped Ether",
                    "state": "LOCKED",
                    "asset": {
                        "identifier": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                        "platform": "ETHEREUM",
                        "symbol": "WETH",
                        "assetClass": {
                            "id": "3"
                        },
                        "contract": {
                            "applications": [
                                "wrapped-ethereum"
                            ]
                        }
                    },
                    "fiatValue": {
                        "value": 828386.1691297204
                    },
                    "amount": 390.7863844627819,
                    "childBalances": []
                },
                {
                    "name": "Wrapped Ether",
                    "state": "LOCKED",
                    "asset": {
                        "identifier": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756
[TRUNCATED]
```

**Sample response (200):**
```json
{
    "data": {
        "assetBalance": {
            "totalCount": 24,
            "results": [
                {
                    "name": "BUSD Token",
                    "status": "READY",
                    "amount": 1462.8089968109994,
                    "fiatValue": {
                        "value": 1462.89942914117
                    },
                    "asset": {
                        "name": "BUSD Token",
                        "type": "STABLE",
                        "platform": "BINANCE"
                    },
                    "belongsTo": {
                        "name": "Eilon",
                        "identifier": "0x6802374b0e9e2274f3b9863700ce2a4ecd00b93d"
                    }
                },
                {
                    "name": "USD Coin (Arb1)",
                    "status": "READY",
                    "amount": 991.517561,
                    "fiatValue": {
                        "value": 990.5965474425409
                    },
                    "asset": {
                        "name": "USD Coin (Arb1)",
                        "type": "STABLE",
                        "platform": "ARBITRUM"
                    },
                    "belongsTo": {
                        "name": "tres-demo-1",
                        "identifier": "0x613700baf1481f3781a6b3ec9e44a4585f89dfbc"
                    }
                },
                {
                    "name": "Dai Stablecoin",
                    "status": "READY",
                    "amount": 46.50245030833976,
                    "fiatValue": {
                        "value": 46.49454702547141
                    },
                    "asset": {
                        "name": "Dai Stablecoin",
                        "type": "STABLE",
                        "platform": "ETHEREUM"
                    },
                    "belongsTo": {
                        "name": "tres-demo-ribbon",
                        "identifier": "0x2acf58b4c80dbe20c8d2c
[TRUNCATED]
```

## Get Asset Balances (Underlying Balances)

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAssetBalances($limit: Int, $offset: Int, $currency: String, $state: String, $internalAccount: Float, $parentBalance_Isnull: Boolean, $assetNameIcontains: String $belongsTo_Identifier: String, $asset_Platform: String, $status: String, $groupTime_Lte: DateTime, $groupTime_Gte: DateTime, $includeArchived: Boolean,  $asset_Identifier: String, $groupId: UUID) {
  assetBalance(
    groupId: $groupId
    state: $state
    limit: $limit
    offset: $offset
    currency: $currency
    belongsTo_Id: $internalAccount
    parentBalance_Isnull: $parentBalance_Isnull
    asset_Name_Icontains: $assetNameIcontains
    excludeUnderDelegation: false
    includeArchived: $includeArchived
    belongsTo_Identifier: $belongsTo_Identifier
    asset_Platform: $asset_Platform
    status: $status
    groupTime_Gte: $groupTime_Gte,
    groupTime_Lte: $groupTime_Lte,
    asset_Identifier: $asset_Identifier

  ) {
    totalCount
    results {
      id
      rollingId
      name
      state
      amount
      belongsTo {
        name
        identifier
        description
        tags
        parentPlatform
      }
      updatedAt
      asset {
        identifier
        platform
        symbol
        assetClass {
          id
          verificationStatus
        }
        contract {
          applications
          contractName
        }
      }
      parentBalance {
        id
        position {
          displayName
          application
          extras 
          identifier
        }
      }
      fiatValue {
        value
      }
    }
  }
}
```

**Variables:**
```json
{
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "childBalances_Isnull": true
}
```

## Get Asset Balances with Realtime (Stateless) Data

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetBalancesByAccountId($limit: Int, $offset: Int, $currency: String, $state: String, $internalAccount: Float, $parentBalance_Isnull: Boolean, $assetNameIcontains: String $belongsTo_Identifier: String, $asset_Platform: String, $status: String, $groupTime_Lte: DateTime, $groupTime_Gte: DateTime, $includeArchived: Boolean,
$asset_Identifier: String, $position_Isnull: Boolean) {
  assetBalance(
    position_Isnull: $position_Isnull
    state: $state
    limit: $limit
    offset: $offset
    currency: $currency
    belongsTo_Id: $internalAccount
    parentBalance_Isnull: $parentBalance_Isnull
    asset_Name_Icontains: $assetNameIcontains
    excludeUnderDelegation: false
    includeArchived: $includeArchived
    belongsTo_Identifier: $belongsTo_Identifier
    asset_Platform: $asset_Platform
    status: $status
    groupTime_Gte: $groupTime_Gte,
    groupTime_Lte: $groupTime_Lte
    asset_Identifier: $asset_Identifier
  ) {
    totalCount
    results {
      id
      rollingId
      name
      state
      amount
      statelessBalance
      statelessChildBalances {
        asset {
            symbol
            identifier
        }
        amount
        fiatValue
      }
      position {
        displayName
        application
        extras 
        identifier
      }
      belongsTo {
        name
        identifier
        description
        tags
        parentPlatform
      }
      updatedAt
      asset {
        identifier
        platform
        symbol
        assetClass {
          id
          verificationStatus
        }
        contract {
          applications
          contractName
        }
      }
      statelessFiatValue
      fiatValue {
        value
      }
      childBalances {
        asset {
          symbol
        }
        state
        amount
    
      }
    }
  }
}
```

**Variables:**
```json
{
  "limit": 500,
  "offset": 0,
  "currency": "usd",
   "belongsTo_Identifier": "0xcaC19662Ec88d23Fa1c81aC0e8570B0cf2FF26b3",
   "asset_Platform": "hyperliquid",
   "parentBalance_Isnull": true,
   "position_Isnull": true
}
```

## Get Asset Balances by Activity Time

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetOrgBalance($limit: Int, $offset: Int, $balanceName: String, $assetClass_Assets_Type: String, $assetClass_Assets_Identifier_Icontains: String, $assetClass_Assets_Platform_In: [String], $showZeros: Boolean, $currency: String, $exportName: String, $exportFormat: String, $state: String, $position_Type: String, $internalAccountIds: [String], $position_Isnull: Boolean, $assetClass_In: [ID]) {
  organizationBalance(
    limit: $limit
    offset: $offset
    balanceName: $balanceName
    assetClass_Assets_Type: $assetClass_Assets_Type
    assetClass_Assets_Platform_In: $assetClass_Assets_Platform_In
    assetClass_Assets_Identifier_Icontains: $assetClass_Assets_Identifier_Icontains
    showZeros: $showZeros
    currency: $currency
    exportName: $exportName
    exportFormat: $exportFormat
    state: $state
    position_Type: $position_Type
    internalAccountIds: $internalAccountIds
    position_Isnull: $position_Isnull
    excludeUnderDelegation: true
    assetClass_In: $assetClass_In
  ) {
    totalCount
    results {
      id
      reconciliationMissing
      amount
      name
      state
      updatedAt
      balances {
          position {
              id
          }
        id
        asset {
          platform
          symbol
        }
        belongsTo {
          identifier
        }
        childBalances {
          amount
          asset {
            symbol
            contract {
                applications
            }
          }
        }
      }
      position {
        application
        type
      }
      assetClass {
        symbol
        id
        verificationStatus
      }
      fiatValue {
        value
      }
    }
  }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "limit": 1,
  "offset": 0,
  "balanceName": "",
  "position_Isnull": true,
  "assetClass_Assets_Identifier_Icontains": "",
  "assetClass_Assets_Type": "token",
  "assetClass_Assets_Platform_In": [],
  "internalAccountIds": [],
  "showZeros": false,
  "assetClass_In": []
}
```

## Get Organization Balance Fiat Value

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery($limit: Int, $offset: Int, $currency: String) {
  organizationBalance(limit: $limit, offset: $offset, currency: $currency) {
    results {
      id
      calculatedBalance
      amount
      reconciliationMissing
      balancesCount
      assetClass {
          name
      }
      balances{
          reconciliation
          childBalances {
              amount
              name
          }
          fiatValue {
              value
          }
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
    "currency": "eur",
    "limit": 10
}
```

## Get Claimables

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery($limit: Int, $offset: Int, $state: String) {
          assetBalance(
            limit: $limit
            offset: $offset
            state: $state
          ) {
            results {
              amount
              state
              asset {
                name
                platform
                symbol
                identifier
              }
              fiatValue {
                value
              }
            }
          }
        }
```

**Variables:**
```json
{
    "state": "claimable"
}
```

## Get Positions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetPositions($currency: String, $currentBalance_BelongsTo_In: [ID], $assetClass_In: [String], $application_In: [String],
$application: String, $platform: String) {
  position(
    currency: $currency
    currentBalance_BelongsTo_In: $currentBalance_BelongsTo_In
    assetClass_In: $assetClass_In
    limit: 1000
    excludeUnderDelegation: true
    application_In: $application_In
    application: $application
    platform: $platform
  ) {
    totalCount
    results {
      id
      application
      identifier
      type
      platform
      extras
      currentBalance {
        id
        name
        amount
        asset {
          symbol
          assetClass {
            verificationStatus
          }
        }
        fiatValue {
          value
          __typename
        }
        state
        screenshot
        childBalances {
          id
          amount
          asset {
            symbol
            identifier
            assetClass {
              verificationStatus
            }
          }
          name
          fiatValue {
            value
            __typename
          }
          state
          screenshot
          childBalances {
            id
            amount
            asset {
              symbol
              assetClass {
                verificationStatus
              }
            }
            name
            state
            screenshot
            childBalances {
              id
              amount
              asset {
                symbol
                assetClass {
                  verificationStatus
                }
              }
              name
              fiatValue {
                value
                __typename
              }
              state
              screenshot
            }
            fiatValue {
              value
              __typename
            }
          }
        }
      }
      displayName
      walletName
      walletAddress
      createdAt
      extras
    }
  }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "currentBalance_BelongsTo_In": [],
  "application": "jito",
  "platform": "solana"
}
```

**Sample response (200):**
```json
{
    "data": {
        "position": {
            "totalCount": 253,
            "results": [
                {
                    "id": "6549048",
                    "application": "bittensor",
                    "identifier": "bittensor-5FRqwexkxqXLg4frDhGKM6rCw2y32JWojQ6JV6zBgzhnhq7r",
                    "type": "STAKING",
                    "platform": "bittensor",
                    "extras": {},
                    "currentBalance": {
                        "id": "85393724",
                        "name": "Bittensor (TAO) - Staking",
                        "amount": 1e-9,
                        "asset": {
                            "symbol": "virtual",
                            "assetClass": {
                                "verificationStatus": "VERIFIED"
                            }
                        },
                        "fiatValue": {
                            "value": 50341380.09738138,
                            "__typename": "AssetBalanceFiatValueQuery"
                        },
                        "state": "VIRTUAL",
                        "screenshot": null,
                        "childBalances": [
                            {
                                "id": "85393725",
                                "amount": 200011.588181185,
                                "asset": {
                                    "symbol": "TAO",
                                    "identifier": "native",
                                    "assetClass": {
                                        "verificationStatus": "VERIFIED"
                                    }
                                },
                                "name": "Bittensor",
                                "fiatValue": {
                                    "value": 50341380.09738138,
                                    "__typename": "AssetBalanceFiatValueQuery"
                                },
                                "state": "LOCKED",
         
[TRUNCATED]
```

## Get Asset Metadata

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAssetMetadata($identifier: String, $platform: String, $offset: Int, $limit: Int) {
  asset(
    offset: $offset,
    limit: $limit,
    identifier: $identifier,
    platform: $platform
  ) {
    results {
      symbol
      name
      platform
      identifier
      assetClass {
        name
        symbol
      }
    }
  }
}
```

**Variables:**
```json
{
  "limit": 10,
  "platform": "ethereum"
}
```

## Get All Possible Asset Class Stablecoins

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AssetClasses($limit: Int, $offset: Int, $assetType: String, $verificationStatus: String) {
  assetClass(limit: $limit, offset: $offset, assetType: $assetType, verificationStatus: $verificationStatus ) {
    totalCount
    results {
        id
        symbol
        name
        verificationStatus
    }
  }
}
```

**Variables:**
```json
{
  "assetType": "stable",
  "verificationStatus": "verified"
}
```

## Get Asset Balance by Internal Account Tag

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery($limit: Int, $offset: Int, $currency: String, $parentBalance_Isnull: Boolean, $tags_Overlap: [String]) {
  assetBalance(limit: $limit, offset: $offset, currency: $currency, parentBalance_Isnull: $parentBalance_Isnull, tags_Overlap: $tags_Overlap) {
      totalCount
    results {
      id
      asset {
          name
      }
      childBalances {
          state
          asset {
              symbol
          }
          amount
      }
      amount
      state
      belongsTo {
          id
      }
      fiatValue {
        value
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
    "parentBalance_Isnull": true,
    "tags_Overlap": ["MY-TAG"]
}
```

## Generate Historical Balance Report

`POST {{backend}}/graphql`

<p>This endpoint makes an HTTP POST request to {{backend}}/graphql. The request payload contains a request body of undefined type.</p>
<h3 id="response">Response</h3>
<p>The response of this request is documented as a JSON schema.</p>

**Auth:** bearer

**GraphQL query:**
```graphql
query GetOrgBalance($limit: Int, $offset: Int, $assetClass_Assets_Type: String, $name_Icontains: String, $assetClass_Assets_Identifier_Icontains: String, $assetClass_Assets_Platform_In: [String], $showZeros: Boolean, $currency: String, $exportName: String, $exportFormat: String, $state: String, $position_Type: String, $internalAccountIds: [String], $position_Isnull: Boolean, $balanceDate: DateTime, $commitId: UUID) {
  organizationBalance(
    limit: $limit
    offset: $offset
    assetClass_Assets_Type: $assetClass_Assets_Type
    assetClass_Assets_Name_Icontains: $name_Icontains
    assetClass_Assets_Platform_In: $assetClass_Assets_Platform_In
    assetClass_Assets_Identifier_Icontains: $assetClass_Assets_Identifier_Icontains
    showZeros: $showZeros
    currency: $currency
    exportName: $exportName
    exportFormat: $exportFormat
    state: $state
    position_Type: $position_Type
    internalAccountIds: $internalAccountIds
    position_Isnull: $position_Isnull
    excludeUnderDelegation: true
    balanceDate: $balanceDate
    commitId: $commitId
  ) {
    totalCount    
  }
}
```

**Variables:**
```json
{
    "currency":"usd",
    "offset":0,
    "assetClass_Assets_Platform_In":[],
    "internalAccountIds":[],
    "showZeros":false,
    "excludeSpam":true,
    "exportName":"Jan 1st 2025",
    "exportFormat": "RAW_BALANCES",
    "balanceDate": "2025-01-01T00:00:00.000Z",
    "commitId": "47f26d11-67be-4386-8abd-f960b3c69a49"
}
```

## Get Group Times [=Commits]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetGroupTimes($timestamp_Gte: DateTime, $timestamp_Lte: DateTime) {
    groupTimes(timestamp_Gte: $timestamp_Gte, timestamp_Lte: $timestamp_Lte) {
        groupId
        groupTimestamp
    }
}
```

**Variables:**
```json
{
    "timestamp_Lte": "2025-08-29T15:42:10.179109+00:00",
    "timestamp_Gte": "2025-08-18T15:42:10.179109+00:00"
}
```

## Get Archived Asset Balances

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetArchivedBalances($limit: Int, $offset: Int, $currency: String, $internalAccount: Float, $parentBalance_Isnull: Boolean, $assetNameIcontains: String $belongsTo_Identifier: String, $asset_Platform: String, $status: String, $groupId: UUID, $includeArchived: Boolean) {
  assetBalance(
    limit: $limit
    offset: $offset
    currency: $currency
    belongsTo_Id: $internalAccount
    parentBalance_Isnull: $parentBalance_Isnull
    asset_Name_Icontains: $assetNameIcontains
    excludeUnderDelegation: false
    includeArchived: $includeArchived
    belongsTo_Identifier: $belongsTo_Identifier
    asset_Platform: $asset_Platform
    status: $status
    groupId: $groupId,

  ) {
    totalCount
    results {
      name
      state
      groupTime
      groupId
      amount
      updatedAt
      position {
        displayName
        application
        extras 
      }
      belongsTo {
        name
        identifier
        description
        tags
        parentPlatform
      }
      updatedAt
      asset {
        identifier
        platform
        symbol
        assetClass {
          id
          verificationStatus
        }
      }
      fiatValue {
        value
      }
      childBalances {
        asset {
          symbol
        }
        state
        amount
    
      }
    }
  }
}
```

**Variables:**
```json
{
  "limit": 9,
  "offset": 0,
  "currency": "usd",
  "parentBalance_Isnull": true,
  "groupId": "d803a20e-d723-40a0-bd41-09e7d2923e14",
  "includeArchived": true
}
```

## Update manual wallet balance

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateManualBalance(
        $belongsToId: Int!,
        $assetIdentifier: String!,
        $platform: Platform!,
        $state: BalanceState!,
        $amount: Decimal!,
        $methodId: String
    ) {
        updateManualBalance(
            belongsToId: $belongsToId,
            assetIdentifier: $assetIdentifier,
            platform: $platform,
            state: $state,
            amount: $amount,
            methodId: $methodId
        ) {
            success
        }
    }
```

**Variables:**
```json
{
  "belongsToId": 480405,
  "assetIdentifier": "TOKEN1",
  "platform": "MANUAL",
  "state": "WALLET",
  "amount": "1000",
  "methodId": "fee"
}
```
