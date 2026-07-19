# Tres API — Report

Endpoints in the 'Report' section of the public Tres API collection (16 requests).

## Get All Recurring Reports

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query RecurringReportQuery {
    recurringReportQuery {
        totalCount
        results {
            id
            createdAt
            updatedAt
            name
            description
            exportType
            when
            enable
        }
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "recurringReportQuery": {
            "totalCount": 2,
            "results": [
                {
                    "id": "3",
                    "createdAt": "2025-02-18T10:04:16.659698+00:00",
                    "updatedAt": "2025-02-18T10:04:16.664435+00:00",
                    "name": "draft_v1",
                    "description": "",
                    "exportType": "RAW_BALANCES",
                    "when": "{\"hour\": null, \"year\": null, \"month\": null, \"interval\": 86400, \"dayOfWeek\": null, \"dayOfMonth\": null}",
                    "enable": true
                },
                {
                    "id": "2",
                    "createdAt": "2025-02-17T15:39:31.366156+00:00",
                    "updatedAt": "2025-02-17T15:39:31.385675+00:00",
                    "name": "draft_v1",
                    "description": "",
                    "exportType": "RAW_BALANCES",
                    "when": "{\"hour\": null, \"year\": null, \"month\": null, \"interval\": 86400, \"dayOfWeek\": null, \"dayOfMonth\": null}",
                    "enable": true
                }
            ]
        }
    }
}
```

## Delete Recurring Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteRecurringReport($id: String) {
    deleteRecurringReport(id: $id) {
        status
    }
}
```

**Variables:**
```json
{
"id": "4"
}
```

**Sample response (200):**
```json
{
    "data": {
        "deleteRecurringReport": {
            "status": "ok"
        }
    }
}
```

## Create Recurring report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateRecurringReport($exportType: ReportGeneratorType! $name: String! $enable: Boolean $when: WhenInput!) {
    createRecurringReport(
        exportType: $exportType
        name: $name
        enable: $enable
        when: $when
    ) {
        status
        recurringReport {
            id
            when
        }
    }
}
```

**Variables:**
```json
{
    "exportType": "MT940",
    "name": "mt940-daily",
    "enable": true,
    "when": {
        "interval": 600,
        "year": "*",
        "month": "*",
        "dayOfMonth": "*",
        "dayOfWeek": "*",
        "hour": "*"
      }
}
```

**Sample response (200):**
```json
{
    "data": {
        "createOrUpdateRecurringReport": {
            "status": "ok",
            "recurringReport": {
                "id": "6",
                "when": "{\"interval\": null, \"year\": \"*\", \"month\": \"*\", \"dayOfMonth\": \"1\", \"dayOfWeek\": \"\", \"hour\": \"\"}"
            }
        }
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "createOrUpdateRecurringReport": {
            "status": "ok",
            "recurringReport": {
                "id": "7",
                "when": "{\"interval\": null, \"year\": \"*\", \"month\": \"\", \"dayOfMonth\": \"\", \"dayOfWeek\": \"0\", \"hour\": \"15\"}"
            }
        }
    }
}
```

## Update Recurring report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateRecurringReport($exportResource: Resource, $when: WhenInput $id: ID!) {
    updateRecurringReport(
        id: $id
        exportResource: $exportResource
        when: $when
    ) {
        status
        recurringReport {
            id
            when
        }
    }
}
```

**Variables:**
```json
{
    "id": 3467,
    "exportResource": "CUSTOMER_SFTP",
    "when": {
        "hour": "0",
        "year": "",
        "every": "DAY",
        "month": "",
        "interval": null,
        "dayOfWeek": "",
        "dayOfMonth": ""
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "updateRecurringReport": {
            "status": "ok",
            "recurringReport": {
                "id": "23",
                "when": {
                    "interval": null,
                    "year": "",
                    "month": "*",
                    "day_of_month": "1",
                    "day_of_week": "",
                    "hour": "",
                    "every": "month"
                }
            }
        }
    }
}
```

## Generate Historical Balance Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query PollReport($nameFilter: String!) {
    report(
      name_Icontains: $nameFilter
      ordering: "-created_at"
      limit: 1
    ) {
      results {
        id
        name
        status
        link
      }
    }
  }
```

**Variables:**
```json
{ "nameFilter": "Kinesis Historical Balance 2026-05-31" }
```

## Generate Audit Log Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AuditLog($exportName: String, $exportFormat: String, $currency: String, $timestamp_Lte: DateTime, $timestamp_Gte: DateTime, $outputFormat: ReportOutputFormat) {
    auditLog(
        exportName: $exportName
        exportFormat: $exportFormat
        currency: $currency
        timestamp_Lte: $timestamp_Lte
        timestamp_Gte: $timestamp_Gte
        outputFormat: $outputFormat
    ) {
        totalCount
    }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "exportName": "audit_log_report_test",
  "exportFormat": "audit_log",
  "timestamp_Gte": "2024-07-10T23:59:50+00:00",
  "timestamp_Lte": "2024-08-10T23:59:50+00:00",
  "outputFormat": "CSV"
}
```

## Generate Staking Rewards Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AuditLog($exportName: String, $exportFormat: String, $currency: String, $startDate_Gte: Date, $endDate_Lte: Date, $outputFormat: ReportOutputFormat) {
    stakingYieldRecord(
        exportName: $exportName
        exportFormat: $exportFormat
        currency: $currency
        startDate_Gte: $startDate_Gte
        endDate_Lte: $endDate_Lte
    ) {
        totalCount
    }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "exportName": "staking_data",
  "exportFormat": "staking_data",
  "startDate_e": "2024-01-01",
  "endDate": "2024-08-01"
}
```

## Generate Balance Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetOrgBalance($balanceName: String, $assetClass_Assets_Type: String, $assetClass_Assets_Identifier_Icontains: String, $assetClass_Assets_Platform_In: [String], $showZeros: Boolean, $currency: String, $exportName: String, $exportFormat: String, $state: String, $position_Type: String, $internalAccountIds: [String], $position_Isnull: Boolean, $balanceDate: DateTime, $assetClass_In: [ID], $applyFilterToChildren: Boolean) {
  organizationBalance(
    limit: $limit
    offset: $offset
    balanceName: $balanceName
    assetClass_Assets_Type: $assetClass_Assets_Type
    assetClass_Assets_Platform_In: $assetClass_Assets_Platform_In
    assetClass_Assets_Identifier_Icontains: $assetClass_Assets_Identifier_Icontains
    currency: $currency
    exportName: $exportName
    exportFormat: $exportFormat
    state: $state
    position_Type: $position_Type
    internalAccountIds: $internalAccountIds
    position_Isnull: $position_Isnull
    excludeUnderDelegation: true
    balanceDate: $balanceDate
    showZeros: $showZeros
    assetClass_In: $assetClass_In
    applyFilterToChildren: $applyFilterToChildren
  ) {
    __typename
  }
}
```

**Variables:**
```json
{
  "currency": "eur",
  "assetClass_Assets_Platform_In": [],
  "assetClass_In": [],
  "internalAccountIds": [],
  "showZeros": false,
  "exportName": "Now",
  "exportFormat": "RAW_BALANCES",
  "applyFilterToChildren": false
}
```

## Generate Archived Balance Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetOrgBalance($balanceName: String, $assetClass_Assets_Type: String, $assetClass_Assets_Identifier_Icontains: String, $assetClass_Assets_Platform_In: [String], $showZeros: Boolean, $currency: String, $exportName: String, $exportFormat: String, $state: String, $position_Type: String, $internalAccountIds: [String], $position_Isnull: Boolean, $calculatedAssetBalances_GroupTime_Lt: DateTime, $calculatedAssetBalances_GroupTime_Gte: DateTime,
    $assetClass_In: [ID], $applyFilterToChildren: Boolean) {
  organizationBalance(
    balanceName: $balanceName
    assetClass_Assets_Type: $assetClass_Assets_Type
    assetClass_Assets_Platform_In: $assetClass_Assets_Platform_In
    assetClass_Assets_Identifier_Icontains: $assetClass_Assets_Identifier_Icontains
    currency: $currency
    exportName: $exportName
    exportFormat: $exportFormat
    state: $state
    position_Type: $position_Type
    internalAccountIds: $internalAccountIds
    position_Isnull: $position_Isnull
    excludeUnderDelegation: true
    calculatedAssetBalances_GroupTime_Gte: $calculatedAssetBalances_GroupTime_Gte
    calculatedAssetBalances_GroupTime_Lt: $calculatedAssetBalances_GroupTime_Lt
    showZeros: $showZeros
    assetClass_In: $assetClass_In
    applyFilterToChildren: $applyFilterToChildren
  ) {
    __typename
  }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "assetClass_Assets_Platform_In": [],
  "assetClass_In": [],
  "internalAccountIds": [],
  "showZeros": false,
  "exportName": "March 2025 Balances",
  "exportFormat": "ARCHIVED_BALANCES",
  "applyFilterToChildren": true,
  "calculatedAssetBalances_GroupTime_Gte": "2025-02-28T00:00:14.645833+00:00",
  "calculatedAssetBalances_GroupTime_Lt": "2025-04-01T00:50:14.645833+00:00"
}
```

## Generate Ledger Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GenerateLedgerReport($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String,  $outputFormat: ReportOutputFormat, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxable: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean, $applyFilterToChildren: Boolean) {
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
    children_Fi
[TRUNCATED]
```

**Variables:**
```json
{
  "timestamp_Gte": "2024-05-16T00:00:00+03:00",
  "timestamp_Lt": "2024-06-16T00:00:00.000000000+03:00",
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
  "exportName": "myreport1234",
  "exportFormat": "BASIC_RAW_TRANSACTIONS",
  "outputFormat": "CSV",
  "balanceDate": null,
  "applyFilterToChildren": false
}
```

## Generate Inventory Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GenerateLedgerReport($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String,  $outputFormat: ReportOutputFormat, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxable: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean, $applyFilterToChildren: Boolean) {
  transaction(
    limit: $limit
    offset: $offset
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
    excludeSpam: $e
[TRUNCATED]
```

**Variables:**
```json
{
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": [
    "7399291"
  ],
  "thirdPartyAccounts_In": [],
  "excludeSpam": true,
  "createdByUser": null,
  "children_FiatValues_Isnull": null,
  "missingCounterMatchedTransfers": null,
  "children_BalanceFactor": null,
  "children_Amount_Between": "",
  "children_FiatValue_Between": "",
  "success": null,
  "children_NonTaxableState": null,
  "children_FifoCostBasis_Isnull": null,
  "children_InternalTransferSubTx_Isnull": null,
  "exportFormat": "INVENTORY_ERROR",
  "exportName": "Inventory Report",
  "balanceDate": ""
}
```

## Generate Pre Sync Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery($limit: Int, $offset: Int, $currency: String, $children_Asset_In: [String], $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $bookmark_In: [String], $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxableState: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean, $applyFilterToChildren: Boolean, $children_InternalTransferSubTx_Isnull: Boolean) {
  transaction(
    limit: $limit
    offset: $offset
    comments_Isnull: $comments_Isnull
    comments_FileKey_Isnull: $comments_FileKey_Isnull
    invoices_Isnull: $invoices_Isnull
    currency: $currency
    children_Asset_In: $children_Asset_In
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    children_BelongsTo_In: $children_BelongsTo_In
    applications_In: $applications_In
    protocols_In: $protocols_In
    classification_Action_In: $classification_Action_In
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    children_Recipient_Identifier_In: $children_Recipient_Identifi
[TRUNCATED]
```

**Variables:**
```json
{
  "timestamp_Gte": "2025-04-23T00:00:00Z",
  "timestamp_Lt": "2025-05-24T00:00:00.000000000+00:00",
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": [],
  "children_Asset_In": [],
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
  "children_FifoCostBasis_Isnull": null,
  "children_InternalTransferSubTx_Isnull": null,
  "exportName": "pre_sync_journal_ledger_2025-05-22",
  "exportFormat": "PRE_SYNC_JOURNAL",
  "balanceDate": null,
  "applyFilterToChildren": false
}
```

## Generate Post Sync Report

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery($limit: Int, $offset: Int, $currency: String, $children_Asset_In: [String], $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $bookmark_In: [String], $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxableState: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean, $applyFilterToChildren: Boolean, $children_InternalTransferSubTx_Isnull: Boolean) {
  transaction(
    limit: $limit
    offset: $offset
    comments_FileKey_Isnull: $comments_FileKey_Isnull
    invoices_Isnull: $invoices_Isnull
    currency: $currency
    children_Asset_In: $children_Asset_In
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    children_BelongsTo_In: $children_BelongsTo_In
    applications_In: $applications_In
    protocols_In: $protocols_In
    classification_Action_In: $classification_Action_In
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    children_Recipient_Identifier_In: $children_Recipient_Identifier_In
    success: $success
    syncingStatus_In: $syncingStatus
[TRUNCATED]
```

**Variables:**
```json
{
  "timestamp_Gte": "2025-10-24T00:00:00Z",
  "timestamp_Lt": "2025-10-30T00:00:00.000000000+00:00",
  "limit": 20,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": [],
  "children_Asset_In": [],
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
  "children_FifoCostBasis_Isnull": null,
  "children_InternalTransferSubTx_Isnull": null,
  "exportName": "pre_sync_journal_ledger_2025-05-22",
  "exportFormat": "POST_SYNC_JOURNAL",
  "balanceDate": null,
  "applyFilterToChildren": false
}
```

## Get Available Reports

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetReports($limit: Int, $offset: Int) {
  report(ordering: "-id,", limit: $limit, offset: $offset) {
    totalCount
    results {
      id
      name
      status
      reportType
      createdAt
      exportFormat
      reportTypeName
      link
      variables
      progress
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

## Get Available Report Types

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AvailableReportTypes {
  availableReportTypes {
    name
    entitiesType
    exportType
    description
    exampleReport
  }
}
```

## Sync Report to Snowflake

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SyncReportToExternal($id: Int! $resource: Resource) {
    syncReportToExternal(id: $id, resource: $resource) {
        status
    }
}
```

**Variables:**
```json
{
    "id": 165370,
    "resource": "SNOWFLAKE"
}
```

**Sample response (200):**
```json
{
    "data": {
        "syncReportToExternal": {
            "status": "ok"
        }
    }
}
```
