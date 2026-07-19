# Tres API — Roll forward

Endpoints in the 'Roll forward' section of the public Tres API collection (13 requests).

## Get all Roll forward views

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query RollForwardView {
    rollForwardView {
        results {
            id
            createdAt
            updatedAt
            name
            startDate
            endDate
            assetClasses
            fields
            status
            lastSyncAt
            totalOpenCostBasis
            totalCloseCostBasis
            numberOfAssets
            numberOfWallets
            progress
        }
        totalCount
    }
}
```

## Get all Roll forward views Copy

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query RollForwardView {
    rollForwardView {
        results {
            id
            createdAt
            updatedAt
            name
            startDate
            endDate
            assetClasses
            fields
            status
            lastSyncAt
            totalOpenCostBasis
            totalCloseCostBasis
            numberOfAssets
            numberOfWallets
            progress
        }
        totalCount
    }
}
```

## Get progress of roll forward view

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query RollForwardView {
    rollForwardView(id: 43) {
        results {
            
            progress
        }
    }
}
```

## Create and generate Roll forward data

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation GenerateRollForwardView {
    generateRollForwardView(
        endDate: "2025-08-01T00:00:00.166865+00:00"
        name: "staging-test9"
        startDate: "2025-01-02T00:00:00.166865+00:00"
        fields: []
        assetClasses: ["6"]
    ) {
        success
        viewId
    }
}
```

## Duplicate and generate Roll forward data

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation GenerateRollForwardView {
    generateRollForwardView(
        duplicatedViewId: "43"
        name: "bla"
    ) {
        success
        viewId
    }
}
```

## Regenerate Roll forward data Copy

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation GenerateRollForwardView {
    generateRollForwardView(
        viewId: "43"
    ) {
        success
        viewId
    }
}
```

## Update Roll forward view name by id

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateRollForwardViewName {
    updateRollForwardViewName(id: "32", name: "name") {
        status
    }
}
```

## Delete Roll forward view by id

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteRollForwardView {
    deleteRollForwardView(id: "40") {
        status
    }
}
```

## Get Roll forward data by view Id

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query RollForwardData {
    rollForwardData(rollForwardViewId: 35) {
        totalCount
        results {
            id
            createdAt
            updatedAt
            status
            openRunningBalance
            openRunningBalanceFiatValue
            openReversedBalance
            openReversedBalanceFiatValue
            openDiff
            openDiffFiatValue
            openUnitPrice
            openOrgCostBasis
            openTotalInventory
            openHistoricalBalance
            openHistoricalBalanceFiatValue
            openUnrealizedGains
            closeRunningBalance
            closeRunningBalanceFiatValue
            closeReversedBalance
            closeReversedBalanceFiatValue
            closeDiff
            closeDiffFiatValue
            closeUnitPrice
            closeOrgCostBasis
            closeTotalInventory
            closeHistoricalBalance
            closeHistoricalBalanceFiatValue
            closeUnrealizedGains
            inflow
            inflowFiatValue
            outflow
            outflowFiatValue
            fees
            feesFiatValue
            realizedGains
            internalAccount {
                id
                parentPlatform
                identifier
                platformKeys
                name
                description
                lastSynced
                lastSyncedAt
                lastSyncedParams
                externalId
                tags
                createdAt
                updatedAt
                status
                displayName
                platforms
                totalFiatValue
                reconciliationMissing
                balancesCount
                isExchange
            }
            asset {
                key
                identifier
                platform
                createdAt
                updatedAt
                decimals
                symbol
                name
                type
                nonFungibleId
    
[TRUNCATED]
```

## Get RollForwardData - Summary rows

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query RollForwardData($rollForwardViewId: String, $rollForwardViewDataType: String,$walletsRelatedRows: [String]) {
  rollForwardData(rollForwardViewId: $rollForwardViewId, rollForwardViewDataType: $rollForwardViewDataType, walletsRelatedRows: $walletsRelatedRows) {
    totalCount
    results {
      id
      status
      openRunningBalance
      openRunningBalanceFiatValue
      openReversedBalance
      openReversedBalanceFiatValue
      openDiff
      openDiffFiatValue
      openUnitPrice
      openOrgCostBasis
      openTotalInventory
      openHistoricalBalance
      openHistoricalBalanceFiatValue
      openUnrealizedGains
      closeRunningBalance
      closeRunningBalanceFiatValue
      closeReversedBalance
      closeReversedBalanceFiatValue
      closeDiff
      closeDiffFiatValue
      closeUnitPrice
      closeOrgCostBasis
      closeTotalInventory
      closeHistoricalBalance
      closeHistoricalBalanceFiatValue
      closeUnrealizedGains
      inflow
      inflowFiatValue
      outflow
      outflowFiatValue
      fees
      feesFiatValue
      realizedGains
      rollForwardViewDataType
      internalAccount {
        id
        identifier
        name
        description
        tags
        status
        displayName
      }
      assetClass{
        id
        verificationStatus
      }
    }
  }
}
```

**Variables:**
```json
{
  "rollForwardViewId": "607",
  "rollForwardViewDataType": "basic_row",
  "walletsRelatedRows": ["718789"]
  "summaryRowId": 25309
}
```

## Get RollForwardData - Get Basic Rows By Summary Row ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query RollForwardData($summaryRow_Id: Float) {
  rollForwardData(summaryRow_Id: $summaryRow_Id) {
    totalCount
    results {
      id
      status
      openRunningBalance
      openRunningBalanceFiatValue
      openReversedBalance
      openReversedBalanceFiatValue
      openDiff
      openDiffFiatValue
      openUnitPrice
      openOrgCostBasis
      openTotalInventory
      openHistoricalBalance
      openHistoricalBalanceFiatValue
      openUnrealizedGains
      closeRunningBalance
      closeRunningBalanceFiatValue
      closeReversedBalance
      closeReversedBalanceFiatValue
      closeDiff
      closeDiffFiatValue
      closeUnitPrice
      closeOrgCostBasis
      closeTotalInventory
      closeHistoricalBalance
      closeHistoricalBalanceFiatValue
      closeUnrealizedGains
      inflow
      inflowFiatValue
      outflow
      outflowFiatValue
      fees
      feesFiatValue
      realizedGains
      internalAccount {
        id
        parentPlatform
        identifier
        name
        description
        externalId
        tags
        status
        displayName
      }
      asset {
        key
        identifier
        platform
        createdAt
        updatedAt
        decimals
        symbol
        name
        type
        nonFungibleId
        bookmark
        parentPlatform
      }
    }
  }
}
```

**Variables:**
```json
{
  "summaryRow_Id": 23376
}
```

## Get RollForwardData - Get Wallet Related Rows

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query RollForwardData($walletsRelatedRows: [String], $rollForwardViewId: String) {
  rollForwardData(
    walletsRelatedRows: $walletsRelatedRows,
    rollForwardViewId: $rollForwardViewId
  ) {
    totalCount
    results {
      id
      asset {
        key
      }
      assetClass {
        id
        symbol
      }
      rollForwardViewDataType
      openRunningBalance
      openReversedBalance
      openRunningBalanceFiatValue
      openTotalInventory
      openUnrealizedGains
      closeReversedBalance
      closeRunningBalanceFiatValue
      closeDiff
      closeReversedBalanceFiatValue
      closeTotalInventory
      closeUnitPrice
      closeUnrealizedGains
    }
  }
}
```

**Variables:**
```json
{
  "walletsRelatedRows": ["718789"],
  "rollForwardViewId": "607"
}
```

## Get Roll forward view Fields

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query RollForwardViewFields {
    rollForwardViewFields {
        fields
    }
}
```
