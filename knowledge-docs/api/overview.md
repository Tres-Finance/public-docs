# Tres API — Overview

Endpoints in the 'Overview' section of the public Tres API collection (16 requests).

## Get Overview

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OverviewNetworkExposure($currency: String) {
  overviewQuery {
    netWorthWidget(currency: $currency)
  }
}
```

**Variables:**
```json
{
    "currency": "eur"
}
```

## Get Overview - Net Worth

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OverviewNetworkExposure($currency: String) {
  overviewQuery {
    netWorthWidget(currency: $currency)
  }
}
```

**Variables:**
```json
{
    "currency": "usd"
}
```

## Get Overview - Under Delegation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OverviewNetworkExposure($currency: String) {
  overviewQuery {
    netWorthWidget(currency: $currency)
  }
}
```

**Variables:**
```json
{
    "currency": "usd"
}
```

## Get Overview - Top Assets

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query TopAssets($platform: String, $currency: String, $limit: Int) {
  organizationBalance(
    calculatedAssetBalances_Asset_Platform: $platform
    currency: $currency
    haveValue: true
    excludeUnderDelegation: true
    limit: $limit
  ) {
    results {
      filteredAmount
      name  
      amount
      assetClass {
        id
        symbol
        verificationStatus
        __typename
      }
      filteredFiatValue
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
  "platform": null,
  "currency": "usd",
  "limit": 10
}
```

## Get Overview - dApp Applications Summary

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OverviewNetworkExposure($currency: String, $currentBalance_BelongsTo_In: [ID], $assetClass_In: [ID]) {
  overviewQuery {
    applicationSummaryWidget(currency: $currency, currentBalance_BelongsTo_In: $currentBalance_BelongsTo_In, assetClass_In: $assetClass_In) {
        application
        platform
        totalFiatValue
    }
  }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "currentBalance_BelongsTo_In": [
    "555839"
  ],
  "assetClass_In": [
    "3"
  ]
}
```

## Get Overview - Asset Breakdown

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OverviewAssetByPlatform($platform: String, $currency: String,) {
  organizationBalance(calculatedAssetBalances_Platform: $platform, currency: $currency) {
    results {
      amount
      name
      balances {
          asset {
              platform
          }
      }
      assetClass {
        id
        symbol
        __typename
      }
      fiatValue {
        value
        __typename
      }
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
  "platform": "solana",
  "currency": "usd"
}
```

## Get Overview - Asset Allocation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OverviewAssetByPlatform($platform: String, $currency: String,) {
  organizationBalance(calculatedAssetBalances_Platform: $platform, currency: $currency) {
    results {
      amount
      name
      balances {
          asset {
              platform
          }
      }
      assetClass {
        id
        symbol
        __typename
      }
      fiatValue {
        value
        __typename
      }
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
  "platform": "solana",
  "currency": "usd"
}
```

## Get Overview - Underlying Assets

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery {
  overviewQuery {
    underlyingAssetsWidget(currency: "usd")
  }
}
```

**Variables:**
```json
{
  "currency": "usd"
}
```

## Get Overview - Daily Inflow Outflow

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OverviewInflowOutflow($startDate: DateTime!, $endDate: DateTime!, $currency: String) {
  overviewQuery {
    dailyInflowOutflowWidget(
      startDate: $startDate
      endDate: $endDate
      currency: $currency
    )
  }
}
```

**Variables:**
```json
{
  "startDate": "2023-06-10T11:10:21+03:00",
  "endDate": "2023-07-09T11:10:21Z",
  "currency": "usd"
}
```

**Sample response (200):**
```json
{
    "data": {
        "overviewQuery": {
            "dailyInflowOutflowWidget": {
                "fees": [
                    [
                        "1686355200",
                        0.8620979195718178
                    ],
                    [
                        "1686441600",
                        2.5419282165557897
                    ],
                    [
                        "1686614400",
                        0.7115620677709712
                    ],
                    [
                        "1686700800",
                        48.13037080709682
                    ],
                    [
                        "1686873600",
                        0.7194979453096553
                    ],
                    [
                        "1686960000",
                        9.952068601197436
                    ],
                    [
                        "1687046400",
                        1.185950156625399
                    ],
                    [
                        "1687132800",
                        0.6726740271601042
                    ],
                    [
                        "1687219200",
                        3.4154386871287197
                    ],
                    [
                        "1687305600",
                        23.13732464978166
                    ],
                    [
                        "1687392000",
                        0.7711990953471346
                    ],
                    [
                        "1687478400",
                        0.723010497863901
                    ],
                    [
                        "1687564800",
                        0.820943473456018
                    ],
                    [
                        "1687651200",
                        19.778818177261385
                    ],
                    [
                        "1687737600",
                        1.33292758140026
                    ],
       
[TRUNCATED]
```

## Get Overview - Daily Claimed Rewards

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OverviewInflowOutflow($startDate: DateTime!, $endDate: DateTime!, $currency: String) {
  overviewQuery {
    dailyClaimedRewardsWidget(
      startDate: $startDate
      endDate: $endDate
      currency: $currency
    )
    __typename
  }
}
```

**Variables:**
```json
{
  "offset": 0,
  "startDate": "1970-01-01T00:00:00+02:00",
  "endDate": "2023-02-13T15:29:12Z",
  "currency": "usd"
}
```

## Get Overview - What to do?

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query WhatToDo($limit: Int, $offset: Int, $currency: String) {
  report(ordering: "-id,", limit: $limit, offset: $offset) {
    totalCount
    results {
      name
      link
    }
  }
  integration {
    results {
      pendingCount
      requiresAttentionCount
      completedCount
    }
  }
  overviewQuery {
    missingFiatValues (currency: $currency, limit: $limit)
  }

}
```

**Variables:**
```json
{
  "offset": 0,
  "limit": 3,
  "currency": "usd"
}
```

## Get Overview - Metrics

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query Metrics($currency: String) {
  internalAccount{
        totalCount
    }
    overviewQuery {
        netWorthWidget(currency: $currency)
    }
    organizationBalance {
        totalCount
    }
}
```

**Variables:**
```json
{
  "currency": "usd"
}
```

## Get Overview - Cost Basis

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query getCostBasis($id_In: [String], $limit: Int, $offset: Int, $balanceName: String, $showZeros: Boolean, $currency: String, $state: String, $timestamp: DateTime) {
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
        __typename
      }
      assetClass {
        name
        symbol
        id
        verificationStatus
        __typename
      }
      fiatValue {
        value
        __typename
      }
      financialIssues {
        type
        tx {
          identifier
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
  "offset": 0,
  "limit": 20,
  "balanceName": "Sol",
  "currency": "usd",
  "state": "wallet",
  "showZeros": false
}
```

## Get Overview - Cost Basis Per Wallet

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
  "offset": 0,
  "limit": 20,
  "balanceName": "",
  "currency": "usd",
  "state": "wallet",
  "showZeros": false
}
```

## Get Overview - Missing Fiat Value by Org Balance

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetOrgBalance($limit: Int, $offset: Int, $name_Icontains: String, $showZeros: Boolean, $excludeSpam: Boolean, $currency: String, $id_In: [String] ) {
  organizationBalance(
    id_In: $id_In,
    limit: $limit
    offset: $offset
    assetClass_Assets_Name_Icontains: $name_Icontains
    showZeros: $showZeros
    excludeSpam: $excludeSpam
    currency: $currency
  ) {
    totalCount
    results {
        id
      totalMissingFiatValues
    }
  }
}
```

**Variables:**
```json
{
  "id_In": ["9965560"],
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": [],
  "children_BelongsTo_In": [],
  "platform_In": [],
  "classification_Activity_In": [],
  "protocols_In": [],
  "applications_In": [],
  "classification_Action_In": [],
  "decodedFunctionName_In": [],
  "children_Recipient_Identifier_In": [],
  "success_In": [],
  "excludeSpam": true,
  "onlyStarred": false,
  "thirdPartyAccounts_In": []
}
```

## Get Overview - Tags Breakdown

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery($limit: Int, $offset: Int, $currency: String) {
  transaction(
    limit: $limit
    offset: $offset
    currency: $currency
    
  ) {
    statsByActivityNoDirection
  }
}
```

**Variables:**
```json
{
  "limit": 20,
  "offset": 0,
  "currency": "usd"
}
```
