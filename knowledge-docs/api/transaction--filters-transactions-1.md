# Tres API — Transaction — Filters Transactions (part 1)

Endpoints in the 'Transaction — Filters Transactions (part 1)' section of the public Tres API collection (20 requests).

## Get Transactions - Filter by Only Pending Transactions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $onlyPending: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    onlyPending: $onlyPending
  ) {
    results {
      id
      isPending
    }
  }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "onlyPending": true
}
```

## Get Transactions - Show All

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $showAll: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    showAll: $showAll
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
    "limit": 20,
    "offset": 0,
    "showAll": true
}
```

## Get Transactions - Filter by Only Ready Transactions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int){
  transaction(
    limit: $limit
    offset: $offset
  ) {
    results {
      id
      isPending
    }
  }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
}
```

## Get Transactions - Filter by Only Deleted Transactions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $onlyDeleted: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    onlyDeleted: $onlyDeleted
  ) {
    results {
      id
      isPending
    }
  }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "onlyDeleted": true
}
```

## Get Transactions - Filter by fiat value

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $children_BalanceFactor: Float,
    $children_FiatValue_Between: String, $currency: String){
  transaction(
    limit: $limit
    offset: $offset
    children_FiatValue_Between: $children_FiatValue_Between
    children_BalanceFactor: $children_BalanceFactor
    currency: $currency
  ) {
    results {
      id
      identifier
      children {
          amount
          balanceFactor
          asset {
              symbol
          }
          fiat
      }
    }     
  }
}
```

**Variables:**
```json
{
    "limit": 10,
    "offset": 10,
    "children_BalanceFactor": 1,
    "children_FiatValue_Between": "1900,2000",
    "currency": "usd"
}
```

## Get Transactions - Filter by ERP Remote ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $erpRemoteId_In:[String], $currency: String){
  transaction(
    limit: $limit
    offset: $offset
    erpRemoteId_In: $erpRemoteId_In
    currency: $currency
  ) {
    results {
      id
      identifier
      children {
          amount
          balanceFactor
          asset {
              symbol
          }
          fiat
      }
    }     
  }
}
```

**Variables:**
```json
{
    "limit": 10,
    "offset": 0,
    "erpRemoteId_In": ["19db0529-47be-4ef7-9f0d-d1d7b41780f2"],
    "currency": "usd"
}
```

## Get Transactions - Filter by fiat value Copy

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $onlyReady: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    onlyReady: $onlyReady
  ) {
    results {
      id
      identifier
      children {
          amount
          balanceFactor
          asset {
              symbol
          }
          fiat
      }
    }     
  }
}
```

**Variables:**
```json
{
    "limit": 10,
    "offset": 10,
    "children_BalanceFactor": 1,
    "children_FiatValue_Between": "1900,2000",
    "currency": "usd",
    "isReady": true}
```

## Get Transactions - Filter by amount

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $children_BalanceFactor: Float,
    $children_Amount_Between: String){
  transaction(
    limit: $limit
    offset: $offset
    children_Amount_Between: $children_Amount_Between
    children_BalanceFactor: $children_BalanceFactor
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
    "limit": 20,
    "offset": 0,
    "children_Amount_Between": "100,200",
    "children_BalanceFactor": 1
}
```

## Get Transactions - Filter by Missing Cost Basis

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $bookmark_In: [String], $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxableState: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean, $applyFilterToChildren: Boolean, $children_InternalTransferSubTx_Isnull: Boolean) {
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
    success: $success
    syncingStatus_In: $syncingStatus_In
   
[TRUNCATED]
```

**Variables:**
```json
{
  "timestamp_Gte": "2024-10-19T00:00:00+03:00",
  "timestamp_Lt": "2024-11-18T23:59:59.999000000+02:00",
  "limit": 20,
  "offset": 0,
  "currency": "eur",
  "children_Asset_AssetClass_In": [],
  "children_BelongsTo_In": [],
  "platform_In": [],
  "classification_Activity_In": [],
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
  "createdByUser": false,
  "identifier_In": [],
  "tags_Overlap": [],
  "thirdPartyAccountsTags_Overlap": [],
  "children_FiatValues_Isnull": null,
  "children_BalanceFactor": null,
  "children_Amount_Between": "",
  "children_FiatValue_Between": "",
  "onlyRollup": false,
  "success": null,
  "children_NonTaxableState": null,
  "apar": false,
  "methodIds": [],
  "children_FifoCostBasis_Isnull": true,
  "children_InternalTransferSubTx_Isnull": null
}
```

## Get Transactions - Filter by TX Hash / Identifier

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [Boolean], $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $timestamp_Gte: DateTime, $timestamp_Lte: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean) {
  transaction(limit: $limit, offset: $offset, comments_Isnull: $comments_Isnull, comments_FileKey_Isnull: $comments_FileKey_Isnull, invoices_Isnull: $invoices_Isnull, currency: $currency, children_Asset_AssetClass_In: $children_Asset_AssetClass_In, children_BelongsTo_In: $children_BelongsTo_In, applications_In: $applications_In, protocols_In: $protocols_In, classification_Action_In: $classification_Action_In, thirdPartyAccounts_In: $thirdPartyAccounts_In, children_Recipient_Identifier_In: $children_Recipient_Identifier_In, success_In: $success_In, syncingStatus_In: $syncingStatus_In, children_FiatValues_Isnull: $children_FiatValues_Isnull, excludeSpam: $excludeSpam, onlyStarred: $onlyStarred, platform_In: $platform_In, decodedFunctionName_In: $decodedFunctionName_In, classification_Activity_In: $classification_Activity_In, identifier_In: $identifier_In, timestamp_Gte: $timestamp_Gte, timestamp_Lte: $timestamp_Lte, exportName: $exportName, exportForma
[TRUNCATED]
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "identifier_In": ["test"]
}
```

## Get Transactions - Filter by platform / network

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $children_BalanceFactor: Float,
    $children_Amount_Between: String){
  transaction(
    limit: $limit
    offset: $offset
    children_Amount_Between: $children_Amount_Between
    children_BalanceFactor: $children_BalanceFactor
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
    "limit": 20,
    "offset": 0,
    "children_Amount_Between": "100,200",
    "children_BalanceFactor": 1
}
```

## Get Transactions - Filter by 3rd party account

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $thirdPartyAccounts_In: [String]){
  transaction(
    limit: $limit
    offset: $offset
    thirdPartyAccounts_In: $thirdPartyAccounts_In
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
    "limit": 20,
    "offset": 0,
    "thirdPartyAccounts_In": ["0xf89d7b9c864f589bbf53a82105107622b35eaa40"]
}
```

## Get Transactions - Filter by 3rd party account & from/to

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $thirdPartyAccounts_In: [String], $searchByFrom: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    searchByFrom: $searchByFrom
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
    "limit": 20,
    "offset": 0,
    "searchByFrom": true,
    "thirdPartyAccounts_In": ["0xf89d7b9c864f589bbf53a82105107622b35eaa40"]
}
```

## Get Transactions - Filter by original & from/to

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $children_OriginalRecipient_Identifier_In: [String], $children_OriginalSender_Identifier_In: [String]){
  transaction(
    limit: $limit
    offset: $offset
    children_OriginalRecipient_Identifier_In: $children_OriginalRecipient_Identifier_In
    children_OriginalSender_Identifier_In: $children_OriginalSender_Identifier_In
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
    "limit": 20,
    "offset": 0,
    "children_OriginalRecipient_Identifier_In": ["CSg9j2h9ThgCtPP8EESAEfte6LDhCFfqk1taoEEgFNkP"]
}
```

## Get Transactions - Filter by 3rd party account tags + time

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $thirdPartyAccountsTags_Overlap: [String], $thirdPartyAccounts_In: [String], $searchByFrom: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    thirdPartyAccountsTags_Overlap: $thirdPartyAccountsTags_Overlap
    searchByFrom: $searchByFrom
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
  "timestamp_Gte": "2024-04-01T00:00:00+02:00",
  "timestamp_Lt": "2024-05-01T00:00:00.000000000+02:00",
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": [],
  "children_BelongsTo_In": [],
  "platform_In": [],
  "classification_Activity_In": [],
  "protocols_In": [],
  "syncingStatus_In": [],
  "applications_In": [],
  "classification_Action_In": [],
  "decodedFunctionName_In": [],
  "thirdPartyAccounts_In": [],
  "excludeSpam": true,
  "onlyStarred": false,
  "createdByUser": false,
  "identifier_In": [],
  "tags_Overlap": [],
  "thirdPartyAccountsTags_Overlap": [
    "LABS"
  ],
  "children_FiatValues_Isnull": null,
  "children_BalanceFactor": null,
  "children_Amount_Between": "",
  "children_FiatValue_Between": "",
  "onlyRollup": false,
  "success": null,
  "children_NonTaxable": null
}
```

## Get Transactions - Filter by missing fiat values

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $timestamp_Gte: DateTime, $timestamp_Lte: DateTime, $children_FiatValues_Isnull: Boolean){
  transaction(
    timestamp_Lte: $timestamp_Lte
    timestamp_Gte: $timestamp_Gte
    limit: $limit
    offset: $offset
    children_FiatValues_Isnull: $children_FiatValues_Isnull
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
    "limit": 20,
    "offset": 0,
    "currency": "usd",
    "timestamp_Gte": "2023-07-10T00:00:00+03:00",
    "timestamp_Lte": "2023-07-11T23:59:59+03:00",
    "children_FiatValues_Isnull": true
}
```

## Get Transactions - Filter by missing fiat values and Asset Class

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $bookmark_In: [String], $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxableState: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean, $applyFilterToChildren: Boolean, $children_InternalTransferSubTx_Isnull: Boolean) {
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
    success: $success
    syncingStatus_In: $syncingStatus_In
   
[TRUNCATED]
```

**Variables:**
```json
{
  "limit": 20,
  "offset": 0,
  "currency": "brl",
  "children_Asset_AssetClass_In": [
    "3"
  ],
  "children_BelongsTo_In": [],
  "platform_In": [],
  "classification_Activity_In": [],
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
  "createdByUser": false,
  "identifier_In": [],
  "tags_Overlap": [],
  "thirdPartyAccountsTags_Overlap": [],
  "children_FiatValues_Isnull": true,
  "children_BalanceFactor": null,
  "children_Amount_Between": "",
  "children_FiatValue_Between": "",
  "onlyRollup": false,
  "success": null,
  "children_NonTaxableState": null,
  "apar": false,
  "methodIds": [],
  "children_FifoCostBasis_Isnull": null,
  "children_InternalTransferSubTx_Isnull": null
}
```

## Get Transactions - Filter by ID gt/lt

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $id_Gte: Float, $id_Lte: Float){
  transaction(
    id_Gte: $id_Gte
    id_Lte: $id_Lte
    limit: $limit
    offset: $offset
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
    "limit": 20,
    "offset": 0,
    "id_Gte": 5
}
```

## Get Transactions - Filter by Ready Transactions & Created by User

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [ID], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [String], $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $timestamp_Gte: DateTime, $timestamp_Lte: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $onlyPending: Boolean, $createdByUser: Boolean) {
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
    timestamp_Gte: $timestamp_Gte

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
  "syncingStatus_In": [],
  "applications_In": [],
  "classification_Action_In": [],
  "decodedFunctionName_In": [],
  "thirdPartyAccounts_In": [],
  "excludeSpam": true,
  "onlyStarred": false,
  "onlyPending": false,
  "createdByUser": true,
  "identifier_In": [],
  "tags_Overlap": [],
  "thirdPartyAccountsTags_Overlap": [],
  "children_FiatValues_Isnull": null,
  "children_BalanceFactor": null,
  "children_Amount_Between": "",
  "children_FiatValue_Between": "",
  "identifier_Contains": ""
}
```

**Sample response (200):**
```json
{
    "data": {
        "transaction": {
            "results": [
                {
                    "id": "90122601",
                    "createdBy": "USER"
                },
                {
                    "id": "90122600",
                    "createdBy": "USER"
                }
            ]
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
                "subtitle": "4 calls in 0.50ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "subtitle": "4 queries in 823.87ms"
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
                "subtitle": "CPU: 1018.69ms (3290.12ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.2.2"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "fc7e14adc44a4cbfa9f695e5fe84fb82"
    }
}
```

## Get Transactions - Filter by Failed

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $success: Boolean){
  transaction(
    limit: $limit
    offset: $offset
    success: $success
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
    "offset": 0
}
```
