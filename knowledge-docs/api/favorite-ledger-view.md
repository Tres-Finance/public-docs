# Tres API — Favorite Ledger View

Endpoints in the 'Favorite Ledger View' section of the public Tres API collection (5 requests).

## Save favorite ledger view

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query SaveFavoriteLedgerView($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String,  $outputFormat: ReportOutputFormat, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxable: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean, $applyFilterToChildren: Boolean,$favoriteLedgerViewName: String, 
$queryParams: String) {
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
    success: $succes
[TRUNCATED]
```

**Variables:**
```json
{
  "timestamp_Gte": "2023-01-01T00:00:00+03:00",
  "timestamp_Lt": "2025-01-01T00:00:00.000000000+03:00",
  "limit": 60,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": [],
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
  "methodIds": [],
  "balanceDate": null,
  "applyFilterToChildren": false,
  "favoriteLedgerViewName": "second test2",
  "queryParams": "fromDate=2024-01-01&toDate=2024-12-31&dateType=2024&pageSize=100&internalAccounts=144"
}
```

## Get Favorite ledger views

`GET {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query FavoriteLedgerView {
    favoriteLedgerView {
        totalCount
        results {
            id
            name
            variables
            queryParams
        }
    }
}
```

## Get Favorite ledger view by name

`GET {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query FavoriteLedgerView {
    favoriteLedgerView(name: "second test") {
        totalCount
        results {
            id
            name
            variables
            queryParams
        }
    }
}
```

## Update name for favorite ledger view

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateFavoriteLedgerView {
    updateFavoriteLedgerView(favoriteLedgerViewId: 1, name: "name") {
        success
    }
}
```

## Delete favorite ledger view

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteFavoriteLedgerView {
    deleteFavoriteLedgerView(favoriteLedgerViewId: 4) {
        success
    }
}
```
