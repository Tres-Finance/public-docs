# Tres API — Transaction — Filters Transactions (part 2)

Endpoints in the 'Transaction — Filters Transactions (part 2)' section of the public Tres API collection (18 requests).

## Get Transactions - Filter by Comments

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $comment_Contains: String){
  transaction(
    limit: $limit
    offset: $offset
    comment_Contains: $comment_Contains
  ) {
    results {
      id
      success
      comments {
        results {
            comment
        }
            
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
    "comment_Contains": "test"
}
```

## Get Transactions - Filter by Has Comments

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $comments_Isnull: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    comments_Isnull: $comments_Isnull
  ) {
    results {
      id
      success
      comments {
        results {
            comment
        }
            
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
    "comments_Isnull": false
}
```

## Get Transactions - Filter by Bookmark

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $bookmark_In: [String]){
  transaction(
    limit: $limit
    offset: $offset
    bookmark_In: $bookmark_In
  ) {
    results {
      id
      success
    }
  }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "bookmark_In": ["empty_bookmark"]
}
```

## Get Transactions - Filter by Asset Class + Ignore Fees

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery2($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $ignoreFee: Boolean) {
  transaction(
    limit: $limit
    offset: $offset
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    ignoreFee: $ignoreFee
    currency: $currency
  ) {
    results {
      id
      identifier
      bookmarks
      children {
        asset {
            symbol
        }
        type
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
  "children_Asset_AssetClass_In": [
    "3"
  ],
  "ignoreFee": true
}
```

## Get Transactions - Filter by without Counter Match

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $missingCounterMatchedTransfers: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    missingCounterMatchedTransfers: $missingCounterMatchedTransfers
  ) {
    totalCount
    results {
      id
      success
    }
  }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "missingCounterMatchedTransfers": true
}
```

## Get Transactions - Filter by Non Taxable

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $children_NonTaxable: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    children_NonTaxable: $children_NonTaxable
  ) {
    results {
      id
      success
    }
  }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "children_NonTaxable": true
}
```

## Get Transactions - Filter by deleted

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $childrenDeleted: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    childrenDeleted: $childrenDeleted
  ) {
    results {
      id
      identifier
      success
      deleted
      children {
        deleted
        derivedFrom {
            id
            tx {
                identifier
            }
        }
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
    "childrenDeleted": true
}
```

## Get Transactions - Filter by deleted By Rollup

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $childrenDeletedByRollup: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    childrenDeletedByRollup: $childrenDeletedByRollup
  ) {
        results {
            id
            children {
                id
                derivedFrom {
                    id
                    tx {
                        id
                    }
                }
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
    "childrenDeletedByRollup": true
}
```

## Get Transactions - Filter by Transaction Activity [Tag]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $children_NonTaxable: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    children_NonTaxable: $children_NonTaxable
  ) {
    results {
      id
      success
    }
  }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "children_NonTaxable": true
}
```

## Get Transaction by Symbol

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery2($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [Boolean], $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $timestamp_Gte: DateTime, $timestamp_Lte: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_Asset_Symbol_Icontains: String) {
  transaction(
    limit: $limit
    offset: $offset
    comments_Isnull: $comments_Isnull
    comments_FileKey_Isnull: $comments_FileKey_Isnull
    invoices_Isnull: $invoices_Isnull
    currency: $currency
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    children_Asset_Symbol_Icontains: $children_Asset_Symbol_Icontains
    children_BelongsTo_In: $children_BelongsTo_In
    applications_In: $applications_In
    protocols_In: $protocols_In
    classification_Action_In: $classification_Action_In
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    children_Recipient_Identifier_In: $children_Recipient_Identifier_In
    success_In: $success_In
    syncingStatus_In: $syncingStatus_In
    children_FiatValues_Isnull: $children_FiatValues_Isnull
    excludeSpam: $excludeSpam
    onlyStarred: $onlyStarred
    platform_In: $platform_In
    decodedFunctionName_In: $decodedFunctionName_In
    classific
[TRUNCATED]
```

**Variables:**
```json
{
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": [],
  "children_BelongsTo_In": [],
  "children_Asset_Symbol_Icontains": "ASTR",
  "platform_In": [],
  "classification_Activity_In": [],
  "protocols_In": [],
  "applications_In": [],
  "classification_Action_In": [],
  "decodedFunctionName_In": [],
  "children_Recipient_Identifier_In": [],
  "success_In": [],
  "identifier_In": [],
  "excludeSpam": true,
  "onlyStarred": false,
  "thirdPartyAccounts_In": []
}
```

## Get Transaction Syncing Status

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query getTxSyncingStatus($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [ID], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [String], $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $timestamp_Gte: DateTime, $timestamp_Lte: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean) {
  transaction(
    limit: $limit
    offset: $offset
    comments_Isnull: $comments_Isnull
    comments_FileKey_Isnull: $comments_FileKey_Isnull
    invoices_Isnull: $invoices_Isnull
    currency: $currency
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    children_BelongsTo_In: $children_BelongsTo_In
    applications_In: $applications_In
    protocols_In: $protocols_In
    classification_Action_In: $classification_Action_In
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    children_Recipient_Identifier_In: $children_Recipient_Identifier_In
    success_In: $success_In
    syncingStatus_In: $syncingStatus_In
    children_FiatValues_Isnull: $children_FiatValues_Isnull
    excludeSpam: $excludeSpam
    onlyStarred: $onlyStarred
    platform_In: $platform_In
    decodedFunctionName_In: $decodedFunctionName_In
    classification_Activity_In: $classification_Activity_In
    identifier_In: $identifier_In
    timestamp_Gte: $timestamp_G
[TRUNCATED]
```

**Variables:**
```json
{
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

## Get Transaction by Tag

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery2($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [String], $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $timestamp_Gte: DateTime, $timestamp_Lte: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $classification_MethodId_In: String) {
  transaction(
    limit: $limit
    offset: $offset
    comments_Isnull: $comments_Isnull
    comments_FileKey_Isnull: $comments_FileKey_Isnull
    invoices_Isnull: $invoices_Isnull
    currency: $currency
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    children_BelongsTo_In: $children_BelongsTo_In
    applications_In: $applications_In
    protocols_In: $protocols_In
    classification_Action_In: $classification_Action_In
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    children_Recipient_Identifier_In: $children_Recipient_Identifier_In
    success_In: $success_In
    syncingStatus_In: $syncingStatus_In
    children_FiatValues_Isnull: $children_FiatValues_Isnull
    excludeSpam: $excludeSpam
    onlyStarred: $onlyStarred
    platform_In: $platform_In
    decodedFunctionName_In: $decodedFunctionName_In
    classification_Activity_In: $classification_Activity_In
    identifier_In: $identifie
[TRUNCATED]
```

**Variables:**
```json
{
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": [],
  "children_BelongsTo_In": [],
  "classification_MethodId_In": "0xe19c2253",
  "platform_In": [],
  "classification_Activity_In": [],
  "protocols_In": [],
  "applications_In": [],
  "classification_Action_In": [],
  "decodedFunctionName_In": [],
  "children_Recipient_Identifier_In": [],
  "success_In": [],
  "identifier_In": [],
  "excludeSpam": false,
  "onlyStarred": false,
  "thirdPartyAccounts_In": []
}
```

## Get Transaction without Fiat Value

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [ID], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [String], $excludeSpam: Boolean, $onlyStarred: Boolean, $platform_In: [String], $children_Sender_Id_In: [Int], $children_Recipient_Id_In: [Int], $children_Sender_Identifier_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $classificationActivityIsnull: String, $identifier_In: [String], $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $thirdPartyAccounts_In: [String]) {
  transaction(
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    limit: $limit
    offset: $offset
    currency: $currency
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    children_BelongsTo_In: $children_BelongsTo_In
    applications_In: $applications_In
    protocols_In: $protocols_In
    classification_Action_In: $classification_Action_In
    children_Sender_Identifier_In: $children_Sender_Identifier_In
    children_Recipient_Identifier_In: $children_Recipient_Identifier_In
    success_In: $success_In
    excludeSpam: $excludeSpam
    onlyStarred: $onlyStarred
    platform_In: $platform_In
    children_Sender_Id_In: $children_Sender_Id_In
    children_Recipient_Id_In: $children_Recipient_Id_In
    decodedFunctionName_In: $decodedFunctionName_In
    classification_Activity_In: $classification_Activity_In
    classificationActivityIsnull: $classificationActivityIsnull
    identifier_In: $identifier_In
    timestamp_Gt: $timestamp_Gt
    timestamp_Lt: $timestamp_Lt
    exportName: $exportName
    exportFormat: $exportFormat
  ) {
    results {
      id
      applications
      protocols
      customActivity
      bookmarks
      syncingStatus
      syncId
      lastSynced
      comments {
          totalCount
      }
[TRUNCATED]
```

**Variables:**
```json
{
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

## Get Unlabled Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [ID], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [String], $excludeSpam: Boolean, $onlyStarred: Boolean, $platform_In: [String],  $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String) {
  transaction(
    limit: $limit
    offset: $offset
    currency: $currency
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    children_BelongsTo_In: $children_BelongsTo_In
    applications_In: $applications_In
    protocols_In: $protocols_In
    classification_Action_In: $classification_Action_In
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    children_Recipient_Identifier_In: $children_Recipient_Identifier_In
    success_In: $success_In
    excludeSpam: $excludeSpam
    onlyStarred: $onlyStarred
    platform_In: $platform_In
    decodedFunctionName_In: $decodedFunctionName_In
    classification_Activity_In: $classification_Activity_In
    identifier_In: $identifier_In
    timestamp_Gt: $timestamp_Gt
    timestamp_Lt: $timestamp_Lt
    exportName: $exportName
    exportFormat: $exportFormat
  ) {
    results {
      id
      success
      identifier
      ledgerSummary
    }
  }
}
```

**Variables:**
```json
{
  "timestamp_Gt": "1970-01-01T00:00:00+01:00",
  "timestamp_Lt": "2023-01-12T23:59:59+01:00",
  "limit": 20,
  "offset": 40,
  "currency": "usd",
  "children_Asset_AssetClass_In": [],
  "children_BelongsTo_In": [],
  "platform_In": [],
  "classification_Activity_In": [],
  "classificationActivityIsnull": "true",
  "protocols_In": [],
  "applications_In": [],
  "classification_Action_In": [],
  "decodedFunctionName_In": [],
  "thirdPartyAccounts_In": [],
  "success_In": [],
  "excludeSpam": true,
  "onlyStarred": false,
  "identifier_In": []
}
```

## Get Transaction by Integration Accounts

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQueryX($integrationAccount_In: [Int]) {
  transaction(
    integrationAccount_In: $integrationAccount_In
  ) {
    results {
      id
    }
  }
}
```

**Variables:**
```json
{
  "integrationAccount_In": ["193889", "203614"]
}
```

## Get Transaction by Missing Account Data

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation (
    $assetClassIds: [Int]
    ) {
    triggerCostBasis(
      assetClassIds: $assetClassIds
    ) {
        null
    }
  }
```

**Variables:**
```json
{
  "missing_Account_Data": true
}
```

## Get Transaction - only rollups

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $currency: String, $onlyRollup: Boolean) {
  transaction(
    limit: $limit
    offset: $offset
    currency: $currency
    onlyRollup: $onlyRollup
  ) {
    results {
      id
      success
      timestamp
      ledgerSummary
      decodedFunctionName
      identifier
      platform
      classification {
        activity
        action
        functionName
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
  "children_Asset_AssetClass_In": [],
  "children_BelongsTo_In": [],
  "platform_In": [],
  "classification_Activity_In": [],
  "protocols_In": [],
  "applications_In": [],
  "classification_Action_In": [],
  "decodedFunctionName_In": [],
  "thirdPartyAccounts_In": [],
  "success_In": [],
  "excludeSpam": false,
  "onlyStarred": false,
  "identifier_In": [],
  "tags_Overlap": [],
  "onlyRollup": true
}
```

## Get Transaction - only balance diff

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $currency: String, $onlyBalanceDiff: Boolean) {
  transaction(
    limit: $limit
    offset: $offset
    currency: $currency
    onlyBalanceDiff: $onlyBalanceDiff
  ) {
    results {
      id
      success
      timestamp
      isBalanceDiff
      ledgerSummary
      decodedFunctionName
      identifier
      platform
      classification {
        activity
        action
        functionName
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
  "children_Asset_AssetClass_In": [],
  "children_BelongsTo_In": [],
  "platform_In": [],
  "classification_Activity_In": [],
  "protocols_In": [],
  "applications_In": [],
  "classification_Action_In": [],
  "decodedFunctionName_In": [],
  "thirdPartyAccounts_In": [],
  "success_In": [],
  "excludeSpam": false,
  "onlyStarred": false,
  "identifier_In": [],
  "tags_Overlap": [],
  "onlyBalanceDiff": true
}
```
