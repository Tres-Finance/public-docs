# Tres API — Sub Transaction Rollup Rules

Endpoints in the 'Sub Transaction Rollup Rules' section of the public Tres API collection (7 requests).

## Create Sub Transaction Rollup Rules

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateSubTransactionRollupRules(
    $rules: [RollupRuleCreationRequest]!
  ) {
    createSubTransactionRollupRules(rules: $rules) {
      results {
        rollupRuleId
        validationIssues {
          blocking
          type
          message
        }
      }
    }
  }
```

**Variables:**
```json
{
    "rules": [
      {
        "name": "Daily ETH Outflow - 0x84E0",
        "interval": "DAY",
        "rule": {
          "internalAccountId": 715416,
          "assetId": "ethereum_native",
          "platform": "ETHEREUM",
          "balanceFactor": "OUTFLOW",
          "fees": "INCLUDE"
        }
      },
      {
        "name": "Daily ETH Inflow - 0x84E0",
        "interval": "DAY",
        "startDate": "2025-01-01",
        "endDate": "2026-12-31",
        "rule": {
          "internalAccountId": 715416,
          "assetId": "ethereum_native",
          "platform": "ETHEREUM",
          "balanceFactor": "INFLOW",
          "fees": "INCLUDE"
        }
      },
      {
        "name": "Bad Date Rule",
        "interval": "DAY",
        "startDate": "2026-12-31",
        "endDate": "2025-01-01",
        "rule": {
          "internalAccountId": 715416,
          "assetId": "ethereum_native",
          "platform": "ETHEREUM",
          "balanceFactor": "OUTFLOW",
          "fees": "EXCLUDE"
        }
      }
    ]
  }
```

## undo SubTransaction Rollup Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UndoRollup(
  $ruleId: Int!
  $dryRun: Boolean
  $startDate: Date
  $endDate: Date
) {
  undoSubTransactionRollupRule(
    ruleId: $ruleId
    dryRun: $dryRun
    startDate: $startDate
    endDate: $endDate
  ) {
    success
    workflowId
    preview {
      syncedRollupCount
      unsyncedRollupCount
      sourceSubTxsToRestore
      sourceParentTxsToRestore
      rollupStxsToDelete
      rollupTxsToDelete
      rollupTxsPartial
    }
  }
}
```

**Variables:**
```json
{
  "ruleId": 39899,
  "dryRun": true,
  "startDate": null,
  "endDate": null
}
```

## SubTransaction Rollup Rule Preview

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query SubTransactionRollupRulePreview(
  $rule: RollupRuleInputType!
  $startDate: Date
  $endDate: Date
  $interval: Interval
) {
  subTransactionRollupRulePreview(
    rule: $rule
    startDate: $startDate
    endDate: $endDate
    interval: $interval
  ) {
    subTransactionCount
    transactionCount
  }
}
```

**Variables:**
```json
{
  "rule": {
    "internalAccountId": 715416,
    "assetId": "ethereum_native",
    "platform": "ETHEREUM",
    "balanceFactor": "OUTFLOW",
    "fees": "INCLUDE"
  },
  "interval": "DAY"
  }
```

## Create Sub Transaction Rollup Rules - Edit

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateSubTransactionRollupRules(
    $rules: [RollupRuleCreationRequest]!
  ) {
    createSubTransactionRollupRules(rules: $rules) {
      results {
        rollupRuleId
        validationIssues {
          blocking
          type
          message
        }
      }
    }
  }
```

**Variables:**
```json
{
    "rules": [
      {
        "ruleId": 39802,
        "name": "Daily ETH Outflow - 0x84E0",
        "interval": "DAY",
        "rule": {
          "internalAccountId": 715416,
          "assetId": "ethereum_native",
          "platform": "ETHEREUM",
          "balanceFactor": "OUTFLOW",
          "fees": "INCLUDE"
        }
      }
    ]
  }
```

## Reactivate DisabledRollup Rules

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ReactivateDisabledRollupRules($ruleIds: [Int]!) {
  reactivateDisabledRollupRules(ruleIds: $ruleIds) {
    results {
      rules {
        ruleId
        success
        reason
      }
    }
  }
}
```

**Variables:**
```json
{
    "ruleIds": [
        39899,
        39910
    ]
}
```

## Activate Pending Rollup Rules

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ReactivateDisabledRollupRules($ruleIds: [Int]!) {
  reactivateDisabledRollupRules(ruleIds: $ruleIds) {
    results {
      rules {
        ruleId
        success
        reason
      }
    }
  }
}
```

**Variables:**
```json
{
    "ruleIds": [
        123,
        456
    ]
}
```

## Delete Sub Transaction Rollup Rules

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteSubTransactionRollupRules(
    $ruleIds: [Int]!
  ) {
    deleteSubTransactionRollupRules(ruleIds: $ruleIds) {
      results {
        deletedIds
        failures {
          ruleId
          reason
        }
      }
    }
  }
```

**Variables:**
```json
{
    "ruleIds": [33535,
33603,
38743,
38744
]
  }
```
