# Tres API — Reconciliation — Reconciliation Engine

Endpoints in the 'Reconciliation — Reconciliation Engine' section of the public Tres API collection (17 requests).

## Change Reconciliation Gap Fill Rule Name

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ChangeReconciliationGapFillRuleName(
    $ruleId: String!
    $name: String!
    
) {
    changeReconciliationGapFillRuleName(
        ruleId: $ruleId
        name: $name
    ) {
        success
    }
}
```

**Variables:**
```json
{
    "ruleId":"5",
    "name": "ChangedRuleName"
}
```

## Change Reconciliation Gap Fill Rule Name  - DELETE

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $ordering: String, $currency: String, $children_Asset_In: [String], $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $description_Icontains: String, $comments_Isnull: Boolean, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $bookmark_In: [String], $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $classification_In: [ID], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $timestamp_Lte: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $createdByUser: Boolean, $children_NonTaxableState: Boolean, $onlyRollup: Boolean, $onlyPlug: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean, $applyFilterToChildren: Boolean, $children_InternalTransferSubTx_Isnull: Boolean, $missingCounterMatchedTransfers: Boolean, $ignoreFee: Boolean, $outputFormat: ReportOutputFormat, $comment_Contains: String, $onlyDeleted: Boolean, $onlyPending: Boolean, $onlyReady: Boolean, $showAll: Boolean, $globalSearch: String) {
  transaction(
    limit: $limit
    offset: $offset
    ordering: $ordering
    description_Icontains: $description_Icontains
    comments_Isnull: $comments_Isnull
    comments_FileKey_Isnull: $comments_FileKey_Isnull
    invoices_Isnull: $i
[TRUNCATED]
```

**Variables:**
```json
{
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "ignoreFee": false,
  "children_Asset_AssetClass_In": [],
  "children_Asset_In": [],
  "children_BelongsTo_In": [
    "665058"
  ],
  "platform_In": [
    "fireblocks"
  ],
  "classification_Activity_In": [],
  "classification_In": [],
  "protocols_In": [],
  "syncingStatus_In": [],
  "missing_Account_Data": false,
  "integrationAccount_In": [],
  "applications_In": [],
  "classification_Action_In": [],
  "decodedFunctionName_In": [],
  "thirdPartyAccounts_In": [],
  "excludeSpam": true,
  "bookmark_In": [],
  "createdByUser": null,
  "identifier_In": [],
  "tags_Overlap": [],
  "thirdPartyAccountsTags_Overlap": [],
  "children_FiatValues_Isnull": null,
  "children_BalanceFactor": null,
  "onlyRollup": true,
  "onlyPlug": false,
  "success": null,
  "children_NonTaxableState": null,
  "apar": false,
  "methodIds": [
    "SOL Fees_rollup"
  ],
  "children_FifoCostBasis_Isnull": null,
  "children_InternalTransferSubTx_Isnull": null,
  "onlyReady": true
}
```

## Delete Reconciliation Gap Fill Rule

`POST {{backend}}/graphql`

<p>Generated from cURL: curl --location '{{backend}}/graphql' --request POST --header 'Content-Type: application/json' --data '{"query":"mutation DeleteReconciliationGapFillRule($ruleIds: [String!]!) { deleteReconciliationGapFillRule(ruleIds: $ruleIds) }","variables":{"ruleIds":{{ruleIds}}}}'</p>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteReconciliationGapFillRule(
    $ruleIds: [String]!
) {
    deleteReconciliationGapFillRule(
        ruleIds: $ruleIds
    ) {
        success
        message
    }
}
```

**Variables:**
```json
{
    "ruleIds": ["5"]
}
```

## Create Reconciliation Gap Fill Rule - all options

`POST {{backend}}/graphql`

<p>Generated from cURL: curl --location '{{backend}}/graphql' --request POST --header 'Content-Type: application/json' --data '{"query":"mutation CreateReconciliationGapFillRule($input: CreateReconciliationGapFillRuleInput!) { createReconciliationGapFillRule(input: $input) }","variables":{{variablesJson}}'</p>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateReconciliationGapFillRule(
    $internalAccountId: Int!
    $assetId: String!
    $interval: Interval!
    $name: String!
    $methodId: String
    $startDate: Date
    $endDate: Date
) {
    createReconciliationGapFillRule(
        internalAccountId: $internalAccountId
        assetId: $assetId
        interval: $interval
        name: $name
        methodId: $methodId
        startDate: $startDate
        endDate: $endDate
    ) {
        success
        message
        ruleId
    }
}
```

**Variables:**
```json
{
            "internalAccountId": 627782,
            "assetId": "ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "interval": "DAY",
            "methodId": "test_method",
            "name": "Test Rule",
            "startDate": "2024-01-01",
            "endDate": "2030-01-01"
}
```

## Batch Create Reconciliation Gap Fill Rules

`POST {{backend}}/graphql`

<p>Generated from cURL: curl --location '{{backend}}/graphql' --request POST --header 'Content-Type: application/json' --data '{"query":"mutation CreateReconciliationGapFillRule($input: CreateReconciliationGapFillRuleInput!) { createReconciliationGapFillRule(input: $input) }","variables":{{variablesJson}}'</p>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation BatchCreateReconciliationGapFillRules($rulesData: [GapFillRuleData]!) {
    batchCreateReconciliationGapFillRules(rulesData: $rulesData) {
        ruleIds
        skippedRulesCount
        ruleNameToIssue {
            ruleName
            issue
        }
    }
}
```

**Variables:**
```json
{
    "rulesData":
    [
        {
            "internalAccountId": 715416,
            "assetId": "avax_0x184047c49b286a4ccd946b0c5eb1f66abfdb455c",
            "interval": "DAY",
            "name": "Rule 1",
            "methodId": "method_1",
            "startDate": "2024-01-01",
            "endDate": "2024-12-31"
        },
        {
            "internalAccountId": 715417,
            "assetId": "dogecoin_native",
            "interval": "MONTH",
            "name": "Rule 2",
            "methodId": "method_2",
            "startDate": "2024-01-01",
            "endDate": "2024-12-31"
        },
        {
            "internalAccountId": 794788,
            "assetId": "base_0x05af170b1c3674b843b7b50b5544758632673aaf",
            "interval": "DAY",
            "name": "Rule 3"
        }
    ]
}
```

## Create Reconciliation Gap Fill Rule - default

`POST {{backend}}/graphql`

<p>Generated from cURL: curl --location '{{backend}}/graphql' --request POST --header 'Content-Type: application/json' --data '{"query":"mutation CreateReconciliationGapFillRule($input: CreateReconciliationGapFillRuleInput!) { createReconciliationGapFillRule(input: $input) }","variables":{{variablesJson}}'</p>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateReconciliationGapFillRule(
    $internalAccountId: Int!
    $assetId: String!
    $interval: Interval!
    $name: String!
) {
    createReconciliationGapFillRule(
        internalAccountId: $internalAccountId
        assetId: $assetId
        interval: $interval
        name: $name

    ) {
        success
        message
        ruleId
        workflowIdentifiers {
            workflowId
            runId
        }
    }
}
```

**Variables:**
```json
{
            "internalAccountId": 794788,
            "assetId": "ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "interval": "DAY",
            "name": "Test Rule"
}
```

## Get Reconciliation Gap Fill Rules - with filters

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ReconciliationGapFillRule($asset_Key: String, $internalAccount_Id: Float) {
    reconciliationGapFillRule(asset_Key: $asset_Key, internalAccount_Id: $internalAccount_Id) {
        totalCount
        results {
            id
            status
            name
            internalAccount {
                id
            }
        }
    }
}
```

**Variables:**
```json
{
    "asset_Key": "ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "internalAccount_Id": 794788
}
```

## Get Reconciliation Gap Fill Rules - all rules for org

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSplitTransaction($identifier: String, $childrenDeleted: Boolean) {
  transaction(identifier: $identifier, childrenDeleted: $childrenDeleted) {
    results {
      id
      identifier
      platform
      timestamp
      classification {
        action
        functionName
        __typename
      }
      decodedFunctionName
      methodId
      children {
        id
        belongsTo {
          tags
          identifier
          name
          __typename
        }
        recipient {
          identifier
          customAccountName
          name
          isInternal
          __typename
        }
        sender {
          identifier
          customAccountName
          name
          isInternal
          __typename
        }
        originalRecipient {
          identifier
          __typename
        }
        originalSender {
          identifier
          __typename
        }
        type
        asset {
          symbol
          name
          type
          identifier
          __typename
        }
        amount
        fiat
        balanceFactor
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
  "identifier": "24TM1vvmdwvZFUdm8TH6gaZb9unPZKivYtZP3NkKL2Wt",
  "childrenDeleted": true
}
```

## Create Reconciliation Checkpoints And Fillers

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateReconciliationCheckpointsAndFillers(
    $assets: [String!]!
    $internalAccountIds: [Int!]!
    $interval: Interval!
    $balanceSource: BalanceSource!
) {
    createReconciliationCheckpointsAndFillers(
        assets: $assets
        internalAccountIds: $internalAccountIds
        interval: $interval
        balanceSource: $balanceSource
    ) {
        success
        message
        workflowIdentifiers{
            workflowId
            runId
        }
    }
}
```

**Variables:**
```json
{
    "internalAccountIds": [794788],
    "assets": [
        "ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
    ],
    "interval": "DAY",
    "balanceSource": "ON_CHAIN"
}
```

## Reconciliation Checkpoints And Fillers Workflow Status Query

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ReconciliationCheckpointsAndFillersWorkflowStatusQuery($runId: String!$workflowId: String!) {
    reconciliationCheckpointsAndFillersWorkflowStatusQuery {
        progress(runId: $runId,workflowId: $workflowId)
    }
}
```

**Variables:**
```json
{
                    "workflowId": "ReconciliationCheckpointsAndFillersWorkflow-None-demo-aviv2-794788-ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                    "runId": "019d9551-8a05-7961-be00-c6b37e5820a5"
                }
```

## Create Reconciliation Checkpoints And Fillers - With Timerange

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSplitTransaction($identifier: String, $childrenDeleted: Boolean, $showAll: Boolean) {
  transaction(identifier: $identifier, childrenDeleted: $childrenDeleted,showAll: $showAll) {
    results {
      id
      identifier
      platform
      timestamp
      classification {
        action
        functionName
        __typename
      }
      decodedFunctionName
      methodId
      children {
        id
        belongsTo {
          tags
          identifier
          name
          __typename
        }
        recipient {
          identifier
          customAccountName
          name
          isInternal
          __typename
        }
        sender {
          identifier
          customAccountName
          name
          isInternal
          __typename
        }
        originalRecipient {
          identifier
          __typename
        }
        originalSender {
          identifier
          __typename
        }
        type
        asset {
          symbol
          name
          type
          identifier
          __typename
        }
        amount
        fiat
        balanceFactor
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
  "identifier": "4dufWqhe9DMiNHym2GuQsPNhQMDJ8JVMQn4W7Yb4pdr1TVh89vC1QCzo3ZeZ33hiMSrPLc1rJzqECsN6HP99BkQw",
  "childrenDeleted": true,
  "showAll": true
}
```

## Create Manual Sub Transactions From Fillers

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateManualSubTransactionsFromFillers(
    $internalAccountId: Int!
    $asset: String!
    $methodId: String
)  {
    createManualSubTransactionsFromFillers(
        asset: $asset
        internalAccountId: $internalAccountId
        methodId: $methodId
    ) {
        success
        message
    }
}
```

**Variables:**
```json
{
    "internalAccountId": 794788,
    "asset": "ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "methodId": "plug"
    
}
```

## Query Reconciliation Fillers

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ReconciliationFillerQuery(
    $internalAccountId: Float!
    $assetId: String!
    $subTxIsnull: Boolean
) {
    reconciliationFiller(
        internalAccountId: $internalAccountId
        assetId: $assetId
        subTxIsnull: $subTxIsnull
    ) {
        results {
            id
            amount
            balanceFactor
            balanceImpact
            timestamp
        }
    }
}
```

**Variables:**
```json
{
    "internalAccountId": 627782,
    "asset": "ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "methodId": "plug"
    
}
```

## Create Manual Sub Transactions From Fillers With Filler Ids

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateManualSubTransactionsFromFillers(
    $internalAccountId: Int!
    $asset: String!
    $methodId: String
    $fillerIds: [ID]

)  {
    createManualSubTransactionsFromFillers(
        asset: $asset
        internalAccountId: $internalAccountId
        methodId: $methodId
        fillerIds: $fillerIds
    ) {
        success
        message
        workflowIdentifiers{
            workflowId
            runId
        }
    }
}
```

**Variables:**
```json
{
    "internalAccountId": 794788,
    "asset": "ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "methodId": "plug",
    "fillerIds": [13203, 13204]
}
```

## Delete Plug Transactions - by (internal_account_id, asset_id)

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeletePlugTransactions(
    $internalAccountId: Int
    $assetId: String
) {
    deletePlugTransactions(
        internalAccountId: $internalAccountId
        assetId: $assetId
    ) {
        success
        message
        deletedCount
        syncedTxNotDeletedCount
    }
}
```

**Variables:**
```json
{
    "internalAccountId": 794788,
    "assetId": "ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
}
```

## Delete Plug Transactions - by (internal_account_id, asset_id) w. start date end date

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeletePlugTransactions(
    $internalAccountId: Int
    $assetId: String
    $startDate: DateTime
    $endDate: DateTime
) {
    deletePlugTransactions(
        internalAccountId: $internalAccountId
        assetId: $assetId
        startDate: $startDate
        endDate: $endDate
    ) {
        success
        message
        deletedCount
        syncedTxNotDeletedCount
    }
}
```

**Variables:**
```json
{
    "internalAccountId": 794788,
    "assetId": "ethereum_0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "startDate": "2024-01-01T00:00:00Z",
    "endDate": "2025-01-01T00:00:00Z"
}
```

## Delete Plug Transactions - by rule id

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeletePlugTransactions(
    $ruleId: String
) {
    deletePlugTransactions(
        ruleId: $ruleId
    ) {
        success
        message
        deletedCount
        syncedTxNotDeletedCount
    }
}
```

**Variables:**
```json
{
    "ruleId": "2"
}
```
