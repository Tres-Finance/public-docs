# Tres API — Integrations — Queries

Endpoints in the 'Integrations — Queries' section of the public Tres API collection (18 requests).

## Get transaction with subtxs + erp rules

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($id: Float, $currency: String) {
  transaction(id: $id, currency: $currency) {
    results {
        children {
            ignoreRuleId
            flowRule {
                integrationAccount {
                    value
                    name
                }
                ruleId
                extraData
            }
            inventoryRule {
                integrationAccount {
                    value
                    name
                }
                extraData
            }
            gainRule {
                integrationAccount {
                    value
                    name
                }
                extraData
            }
            
            lossRule{
                integrationAccount {
                    value
                    name
                }
                extraData
            }
            unrealizedGainLossRule{
                integrationAccount{
                    value
                    name
                }
                extraData
            }
        }
    }
  }
}
```

**Variables:**
```json
{
  "id": 90692073,
  "currency": "usd"
}
```

## Get Rules - Custom Rules & Default & netsuite data

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query rulesData {
  erp {
    results {
      customRules
      wallets
      assetClassNames
      contacts
      platforms
      tags
      actions
      contracts
      __typename
    }
    __typename
  }
}
```

## Get Rules - Internal Transfer Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetRules {
  erp {
      results {
        internalTransferAccount
      }
  }
}
```

## Get APAR

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query APAR {
  erp {
    results {
    currency
      erpBills{
          id
          billId
          dateCreated
          origAmount
          balance
          vendorName
      }
      erpInvoices {
          invoiceId
          dateCreated
          customerName
          customerId
          balance
          origAmount
      }
      erpCustomers {
          customerId
          name
      }
      erpVendors {
          name
          vendorId
      }
    }
  }
}
```

## Get Invoices

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAPARDataInvoices($limit: Int, $offset: Int, $dateCreated_Gte: DateTime, $dateCreated_Lte: DateTime, $customerId: String, $dueDate_Gte: DateTime, $dueDate_Lte: DateTime, $status: String) {
      erpInvoices (limit: $limit, offset: $offset, customerId: $customerId, dateCreated_Gte: $dateCreated_Gte, dateCreated_Lte: $dateCreated_Lte, dueDate_Lte: $dueDate_Lte, dueDate_Gte: $dueDate_Gte, status: $status) {
       results {
         id
        invoiceId
        dateCreated
        origAmount
        balance
        customerName
        subTx {
          tx {
            identifier
          }
        }
        status
        publicInvoiceId
        paymentToInternalAccounts {
            id
            internalAccount {
                name
                identifier
                parentPlatform
            }
            assets {
                name
                symbol
                identifier
                platform
            }
        }
      }
       }
}
```

**Variables:**
```json
{
    "limit": 1,
    "status": "paid"
}
```

## Get Bills

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAPARDataBills($limit: Int, $offset: Int) {
      erpBills (limit: $limit, offset: $offset) {
       results {
        
          id
          billId
          dateCreated
          origAmount
          balance
          vendorName
      
      }
       }
}
```

**Variables:**
```json
{
    "limit": 50,
    "ordering": "dateCreated"
}
```

## Get ERP Chart of Accounts

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AllIntegrationAccounts {
  erp {
    results {
      accountsByCategory
    }
  }
}
```

## Get related organizations

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AllIntegrationAccounts {
  erp {
    results {
      accountsByCategory
    }
  }
}
```

## Get ERP Integration

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query getIntegrationStatus($integratedApp: String) {
  erp(integratedApp: $integratedApp) {
    results {
      integratedApp
      lastMappedAt
      syncingStatus
      internalTransferRuleId
      companyDetails {
        companyName
        companyEmail
        isConnected
        __typename
      }
      totalTransactions
      syncedTransactions
      lastSync
      syncingStatus
      customRules
      defaultRule
      isConfigured
      internalTransferAccount
      pendingCount
      requiresAttentionCount
      completedCount
      isErp
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
  "integratedApp": "quickbooks"
}
```

**Sample response (200):**
```json
{
    "data": {
        "integration": {
            "totalCount": 1,
            "results": [
                {
                    "integratedApp": "QUICKBOOKS",
                    "companyDetails": {
                        "is_connected": true,
                        "company_name": "Sandbox Company_US_1",
                        "company_mail": "noreply@quickbooks.com"
                    },
                    "connectionStatus": "ACTIVE",
                    "totalTransactions": 1428,
                    "syncedTransactions": 4,
                    "accountsByCategory": {
                        "inventory": {
                            "options": [
                                {
                                    "name": "Account 1",
                                    "value": "334",
                                    "type": "asset"
                                },
                                {
                                    "name": "Account 10",
                                    "value": "343",
                                    "type": "asset"
                                },
                                {
                                    "name": "Account 11",
                                    "value": "344",
                                    "type": "asset"
                                },
                                {
                                    "name": "Account 12",
                                    "value": "345",
                                    "type": "asset"
                                },
                                {
                                    "name": "Account 13",
                                    "value": "346",
                                    "type": "asset"
                                },
                                {
                                    "name": "Account 14",
                                    "value": "347",
                                  
[TRUNCATED]
```

**Sample response (200):**
```json
{
    "data": {
        "integration": {
            "totalCount": 1,
            "results": [
                {
                    "customRules": [
                        {
                            "ruleFilters": {
                                "wallets": [],
                                "assetClassNames": [],
                                "senders": [
                                    {
                                        "name": "Tomerico",
                                        "id": "None",
                                        "address": "0x237343c10705ae7605850977503e25a8c12851e6"
                                    }
                                ],
                                "recipients": []
                            },
                            "accounts": {
                                "inventory": {
                                    "name": "Cost of Goods Sold",
                                    "value": "80",
                                    "type": "expense"
                                },
                                "income": {
                                    "name": "Cost of Goods Sold",
                                    "value": "80",
                                    "type": "expense"
                                },
                                "expense": null,
                                "fee": {
                                    "name": "Cost of Goods Sold",
                                    "value": "80",
                                    "type": "expense"
                                },
                                "gain": null,
                                "loss": null
                            },
                            "updatedAt": "2023-03-07T13:52:49.782112+00:00",
                            "identifier": "654d1d18-15df-409d-884c-23bc7b415b84",
                            "name": "Custom Rule"
                        },
                        {
      
[TRUNCATED]
```

## Get ERP TX Syncing Status

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
  "offset": 20,
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
  "isPending": null,
  "createdByUser": false,
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

## Get QBO Link

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation {
  getIntegrationOauthLink(integrationName: "quickbooks") {
    url
  }
}
```

## Get Slack Link

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation {
  getIntegrationOauthLink(integrationName: "slack") {
    url
  }
}
```

**Variables:**
```json
{
    "integrationName": "slack"
}
```

## Get Slack Status

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query getIntegrationStatusSlack($integratedApp: String) {
  integration(integratedApp: $integratedApp) {
    results {
      integratedApp
      connectionStatus
      isErp
      credentials
      channelName
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
    "integratedApp": "slack"
}
```

## Get Deel Link

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation {
  getIntegrationOauthLink(integrationName: "deel") {
    url
  }
}
```

## Get txs status

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ErpStatusQuery {
    erpStatus {
        statuses(txIds: [147977009, 147978747, 147977016, 147977011, 147977012, 147977013, 147978753, 147977008, 147977010, 147977014, 129321141, 129321414, 129321245, 129321142, 129321143, 121480469, 121477658, 121477503, 121477663, 121477662, 121480471, 121477502, 121477665, 121477657, 121477659, 121477500, 121480470, 121477666, 121477660, 121477501, 121480468, 121477664, 121477661, 121477656]) {
            txId
            syncingType
            syncingErrorType
            syncingStatus
            lastSynced
            aparSyncId
            aparSyncingStatus
            aparLastSynced
        }
    }
}
```

## Get stxs erp accounts

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ErpStatusQuery {
    transaction (id: 5432) {
        results {
            erpAccounts {
                flowAccount {
                    id
                    name
                }
                assetAccount {
                    id
                    name
                }
                gainLossAccount {
                    id
                    name
                }
                classes {
                    id
                    name
                }
                departments {
                    id
                    name
                }
            }
        }
    }
}
```

## get related organizations

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ErpStatusQuery {
    transaction (id: 5432) {
        results {
            erpAccounts {
                flowAccount {
                    id
                    name
                }
                assetAccount {
                    id
                    name
                }
                gainLossAccount {
                    id
                    name
                }
                classes {
                    id
                    name
                }
                departments {
                    id
                    name
                }
            }
        }
    }
}
```

## get transaction journal

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($identifier: String) {
  transaction(identifier: $identifier) {
    results {
      journal
      journalMemo
    }
  }
}
```

**Variables:**
```json
{
    "identifier": ""
}
```
