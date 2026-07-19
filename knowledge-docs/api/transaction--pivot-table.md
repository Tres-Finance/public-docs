# Tres API — Transaction — Pivot Table

Endpoints in the 'Transaction — Pivot Table' section of the public Tres API collection (3 requests).

## Get Transactions Pivot by Activity

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
    statsByActivity
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
  "children_Recipient_Id_In": [],
  "children_Sender_Id_In": [],
  "success_In": [],
  "identifier_In": [],
  "excludeSpam": true
}
```

## Get Transactions Pivot by Activity without Direction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQueryPivot($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $bookmark_In: [String], $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxable: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean) {
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
    children_FiatValues_Isnull: $children_FiatValues_Isnull
    excludeSpam: $excludeS
[TRUNCATED]
```

**Variables:**
```json
{
  "timestamp_Gte": "2024-06-07T00:00:00+03:00",
  "timestamp_Lt": "2024-07-07T23:59:59.999000000+03:00",
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
  "children_NonTaxable": null,
  "apar": false,
  "missing_Account_Data": false,
  "integrationAccount_In": [],
  "methodIds": [],
  "children_FifoCostBasis_Isnull": null
}
```

## Get Transactions Pivot by Asset

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQueryPivot($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $bookmark_In: [String], $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxableState: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean) {
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
    children_FiatValues_Isnull: $children_FiatValues_Isnull
    excludeSpam: $exc
[TRUNCATED]
```

**Variables:**
```json
{
  "timestamp_Gte": "2024-06-08T00:00:00+03:00",
  "timestamp_Lt": "2024-07-08T23:59:59.999000000+03:00",
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": ["5478102"],
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
  "missing_Account_Data": false,
  "integrationAccount_In": [],
  "methodIds": [],
  "children_FifoCostBasis_Isnull": null
}
```
