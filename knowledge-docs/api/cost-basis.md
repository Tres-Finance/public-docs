# Tres API — Cost Basis

Endpoints in the 'Cost Basis' section of the public Tres API collection (15 requests).

## create reevaluation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateReevaluation($reevaluations: [ReevaluationObjectType]!) {
    createReevaluation(reevaluations: $reevaluations) {
      reevaluationIds
    }
  }
```

**Variables:**
```json
{
    "reevaluations": [
        {
            "unitPrice": 1,
            "timestamp": "",
            "assetClassId": 3,
            "isImpairment": false
}
    ]
}
```

## update reevaluation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateReevaluationMutation($reevaluationId: Int!, $unitPrice: Decimal!, $timestamp: DateTime!, $assetClassId: Int!) {
    updateReevaluation(reevaluationId: $reevaluationId, unitPrice: $unitPrice, timestamp: $timestamp, assetClassId: $assetClassId) {
        status
    }
}
```

**Variables:**
```json
{
    "reevaluationId": 1,
    "unitPrice": 1,
    "timestamp": "",
    "assetClassId": 3
}
```

## delete reevaluation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteReevaluationMutation($reevaluationId: Int!) {
    deleteReevaluation(reevaluationId: $reevaluationId) {
        status
    }
}
```

**Variables:**
```json
{
    "reevaluationId": 1
}
```

## get reevaluations

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetReevaluations{
  reevaluation {
    results {
     id
     appliedCostBasis {
        id
        totalCost
        totalCostBeforeReevaluation
     }
    }
  }
}
```

**Variables:**
```json
{

}
```

## set reevaluation internal account

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation (
    $reevaluationInternalAccountId: ID
    ) {
  setOrganizationSettings(
      reevaluationInternalAccountId: $reevaluationInternalAccountId
      ) {
    organizationSettings {
        reevaluationInternalAccountId
    }
  }
}
```

**Variables:**
```json
{
    "reevaluationInternalAccountId": "560594"
}
```

## Set Spec ID Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SetSpecIdRules($subTransactionId: ID!, $specIdRules: [SpecIdRuleInput!]!) {
  setSpecIdRules(
    subTransactionId: $subTransactionId,
    specIdRules: $specIdRules
  ) {
    success
  }
}
```

**Variables:**
```json
{
    "subTransactionId": "1297190029",
    "specIdRules": [
        {"disposedLotSubTransactionId": 1297190028, "amount": 100.50, "priority": 1},
        {"disposedLotSubTransactionId": 1297190027, "amount": 200.75, "priority": 2}
    ]
}
```

## Delete Spec ID Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteSpecIdRules($specIdRuleIds: [ID!]!) {
  deleteSpecIdRules(
    specIdRuleIds: $specIdRuleIds,
  ) {
    success
  }
}
```

**Variables:**
```json
{
    "specIdRuleIds": ["40"]
}
```

## Get Spec ID Rules

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSpecIdRules {
  costBasisSpecIdRule {
    results {
        outflowSubTransaction {
            tx {
                identifier
            }
        }
    }
    
  }
}
```

## Get Spec ID Rules By SubTx ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSpecIdRules($outflowSubTransaction_In: [ID]) {
  costBasisSpecIdRule (outflowSubTransaction_In: $outflowSubTransaction_In){
    results {
        id
        priority
        disposedLotSubTransaction {
            id
        }
        outflowSubTransaction {
            tx {
                identifier
            }
        }
    }
    
  }
}
```

**Variables:**
```json
{
    "outflowSubTransaction_In": "3893035629"
}
```

## Get Spec ID Rules By Rule ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSpecIdRules($id: Float) {
  costBasisSpecIdRule (id: $id){
    results {
        disposedLotSubTransaction {
            id
        }
        outflowSubTransaction {
            tx {
                identifier
            }
        }
    }
    
  }
}
```

**Variables:**
```json
{
    "id": 50
}
```

## Trigger Cost Basis

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($assetClassIds: [Int]) {
    triggerCostBasis(assetClassIds: $assetClassIds) {
        success
    }
}
```

**Variables:**
```json
{
    "assetClassIds" : [1825,1827,2503,2565,2620,2686,2713,2805,2892,3257,3263,3273,3304,3308,3309,3312,3321,3324,3326,3327,3334,3335,3336,3338,3498,3506,3517,3523,3525,3529,3542]
}
```

## Set Full Cost Basis Inventory Configuration

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SetFullCostBasisInventoryConfiguration ($subTransactionId: ID, $enableFullInventory: Boolean) {
    setFullCostBasisInventoryConfiguration(subTransactionId: $subTransactionId, enableFullInventory: $enableFullInventory) {
        success
    }
}
```

**Variables:**
```json
{
    "subTransactionId" : "4048133089",
    "enableFullInventory": false
}
```

## Update Cost Basis Strategy By Date

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateCostBasisStrategyByDate(
    $defaultStrategy: CostBasisStrategy!,
    $strategyPeriods: [CBStrategyPeriodInput!]!
) {
    updateCostBasisStrategyByDate(
        defaultStrategy: $defaultStrategy,
        strategyPeriods: $strategyPeriods
    ) {
        success
        message
    }
}
```

**Variables:**
```json
{
    "defaultStrategy": "FIFO",
    "strategyPeriods": [
        {
            "strategy": "MAX_LOSSES",
            "startDate": "2020-12-31T23:59:59+00:00",
            "endDate": "2021-12-31T23:59:59+00:00"
        },
        {
            "strategy": "MAX_GAINS",
            "startDate":"2021-12-31T23:59:59+00:00",
            "endDate": "2022-12-31T23:59:59+00:00"
        },
        {
            "strategy": "FIFO",
            "startDate":"2022-12-31T23:59:59+00:00",
            "endDate": "2023-12-31T23:59:59+00:00"
        }
    ]
}
```

## Get Cost Basis Strategy By Date

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetCostBasisStrategyByDate{
    getCostBasisStrategyByDate{
        response {
            defaultStrategy
            strategyPeriods {
                startDate
                endDate
                strategy
            }
        }
}
}
```

## Get Cost Basis Status

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query myQuery {
  costBasisGetStatus{
      status
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "readinessScore": {
            "reconciliation": 80,
            "fiat": 70
        }
    },
    "debugToolbar": {
        "panels": {
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "43 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "0 calls in 0.00ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 0 connections",
                "subtitle": "0 queries in 0.00ms"
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
                "subtitle": "CPU: 260.85ms (2760.31ms)"
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
        "storeId": "1f58811eb23d4b68bb936792735239c4"
    }
}
```
