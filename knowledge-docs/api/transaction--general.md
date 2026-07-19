# Tres API — Transaction — general

Endpoints in the 'Transaction — general' section of the public Tres API collection (16 requests).

## Get Transaction #1

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQueryX($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean
    $onlyRollup:Boolean,
    $apar:Boolean
    ) {
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
    excludeSpam: $excludeSpam
    onlyStarred: $onlyStarred
    platform_In: $platform_In
    decodedFunctionName_In: $decodedFunctionName_In
    classification_Activity_In: $classification_Activity_In
    identif
[TRUNCATED]
```

**Variables:**
```json
{
  "limit": 10,
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
  "thirdPartyAccountsTags_Overlap": [],
  "children_FiatValues_Isnull": null,
  "children_BalanceFactor": null,
  "children_Amount_Between": "",
  "children_FiatValue_Between": "",
  "identifier_Contains": "",
  "apar": false
}
```

**Sample response (200):**
```json
{
    "data": {
        "transaction": {
            "results": [
                {
                    "id": "87467778",
                    "success": true,
                    "timestamp": "2023-07-03T00:00:00+00:00",
                    "ledgerSummary": {
                        "inflow": [],
                        "outflow": [],
                        "fee": []
                    },
                    "decodedFunctionName": "ACCRUED STAKING REWARDS",
                    "identifier": "c6a4b47bfbdd4c01a7ee6e3537b73b36",
                    "platform": "acala",
                    "children": [],
                    "classification": null
                },
                {
                    "id": "84936381",
                    "success": true,
                    "timestamp": "2023-07-02T03:27:15+00:00",
                    "ledgerSummary": {
                        "inflow": [
                            {
                                "symbol": "cryp-Fl",
                                "amount": 1,
                                "fiat": 0,
                                "type": "token_transfer",
                                "balance_factor": 1
                            }
                        ],
                        "outflow": [],
                        "fee": []
                    },
                    "decodedFunctionName": "followFor",
                    "identifier": "0x5e53018ea943d9d8fdd004d7aa34ba57fa8f73e3e4e6f9620b0d6320368acda8",
                    "platform": "polygon",
                    "children": [
                        {
                            "id": "470014570",
                            "asset": {
                                "name": "cryptogirls.lens-Follower"
                            },
                            "amount": 1
                        }
                    ],
                    "classification": null
                },
                {
                    "id": "84932874",
        
[TRUNCATED]
```

## Get Transaction #2

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery2($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [Boolean], $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $timestamp_Gte: DateTime, $timestamp_Lte: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean) {
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
  "identifier_In": [""],
  "excludeSpam": true,
  "onlyStarred": false,
  "thirdPartyAccounts_In": []
}
```

## Get Transaction - Full

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery2($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [Boolean], $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: Boolean, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $timestamp_Gte: DateTime, $timestamp_Lte: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean) {
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
    timestamp_Gte: $timestamp_
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
  "identifier_In": [],
  "excludeSpam": true,
  "onlyStarred": false,
  "thirdPartyAccounts_In": []
}
```

## Get Transaction - Journal Entries

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetJournalEntry($id: String) {
  transaction(id: $id) {
    results {
      journal
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
  "children_Recipient_Identifier_In": [],
  "success_In": [],
  "identifier_In": [],
  "excludeSpam": true,
  "onlyStarred": false,
  "thirdPartyAccounts_In": []
}
```

## Get Transaction Classification Rules

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQueryX($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $onlyStarred: Boolean, $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean
    $onlyRollup:Boolean
    ) {
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
    excludeSpam: $excludeSpam
    onlyStarred: $onlyStarred
    platform_In: $platform_In
    decodedFunctionName_In: $decodedFunctionName_In
    classification_Activity_In: $classification_Activity_In
    identifier_In: $identifier
[TRUNCATED]
```

**Variables:**
```json
{
  "limit": 10,
  "offset": 30,
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
  "thirdPartyAccountsTags_Overlap": [],
  "children_FiatValues_Isnull": null,
  "children_BalanceFactor": null,
  "children_Amount_Between": "",
  "children_FiatValue_Between": "",
  "identifier_Contains": ""
}
```

## Get Transaction Total Count

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query readTxsQuery1($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success_In: [Boolean], $excludeSpam: Boolean, $onlyStarred: Boolean, $platform_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $thirdPartyAccounts_In: [String], $thirdPartyAccountsTags_Overlap: [String]) {
  transaction(
    thirdPartyAccountsTags_Overlap: $thirdPartyAccountsTags_Overlap
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    limit: $limit
    offset: $offset
    currency: $currency
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    children_BelongsTo_In: $children_BelongsTo_In
    applications_In: $applications_In
    protocols_In: $protocols_In
    classification_Action_In: $classification_Action_In
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
    totalCount
  }
}
```

**Variables:**
```json
{
  "thirdPartyAccountsTags_Overlap": [],
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

**Sample response (200):**
```json
{
    "data": {
        "transaction": {
            "totalCount": 21335
        }
    }
}
```

## Get Sub Transactions by Transaction ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByTxID($limit: Int, $offset: Int, $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $platform: String, $id: String, $id_In: [String], $tx_DecodedFunctionName: String, $tx_DecodedFunctionNameIn: [String], $belongsTo_Identifier_In: [String], $balanceFactor: Float, $tag: [String], $currency: String) {
  subTransaction(
    balanceFactor: $balanceFactor
    limit: $limit
    offset: $offset
    tx_Id: $id
    id_In: $id_In
    timestamp_Gt: $timestamp_Gt
    platform: $platform
    timestamp_Lt: $timestamp_Lt
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn
    belongsTo_Identifier_In: $belongsTo_Identifier_In
    tx_DecodedFunctionName: $tx_DecodedFunctionName
    tags_Overlap: $tag
    currency: $currency
  ) {
    totalCount
    results {
      isManualFiatValue
      id
      createdBy
      fiat
      recipient {
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
      sender {
        identifier
        customAccountName
        name
        isInternal
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
        __typename
      }
      internalTransferSubTx {
        id
        __typename
      }
      createdBy
      amount
      fiat
      asset {
        symbol
        name
        type
        identifier
        assetClass {
          verificationStatus
          id
          __typename
        }
        __typename
      }
      balanceFactor
      type
      recipient {
        identifier
        __typename
      }
      sender {
        identifier
        __typename
      }
      createdBy
      timestamp
      recipient {
        identifier
        __typename
      }
      sender {
        identifier
        __typename
      }
      balanceFactor
      nonTaxableType
      amount
      ignoreRuleId
      bala
[TRUNCATED]
```

**Variables:**
```json
{
  "id": "1742428960.000000048974233793124759260000",
  "currency": "usd",
  "isPending": false,
  "limit": 5,
  "offset": 0,
  "id_In": null
}
```

## Get Sub Transactions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByTxID(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String]
    $tx_Identifier_In: [String],
    $asset_Identifier: String) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    asset_Identifier: $asset_Identifier
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
                customAccountName
                
            }
            recipient {
                identifier
                customAccountName
            }
            balanceImpact
            createdAt
            updatedAt
            deleted
        }
    }
}
```

**Variables:**
```json
{
    "limit": 2,
    "offset": 0,
    "tx_Identifier_In": []
}
```

## Get Internal Transfer of Sub Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($id: String, $currency: String, $isPending: Boolean) {
  transaction(id: $id, currency: $currency, isPending: $isPending) {
    results {
      children {
        internalTransferSubTx {
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
  "id": "191100264",
  "currency": "usd",
  "isPending": false
}
```

## Get Counter Transfer of Sub Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxById($id: String, $currency: String, $isPending: Boolean) {
  transaction(id: $id, currency: $currency, isPending: $isPending) {
    results {
      children {
        counterTransferSubTxs {
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
  "id": "191100264",
  "currency": "usd",
  "isPending": false
}
```

## Mark Internal Transfer

`POST {{backend}}/graphql`

<p>This endpoint makes an HTTP POST request to {{backend}}/graphql to retrieve sub-transaction data. The request payload should include the necessary parameters for querying sub-transaction information.</p>
<h3 id="request-body">Request Body</h3>
<p>The request body for this endpoint should be in JSON format, containing the parameters required to specify the sub-transaction query.</p>
<h3 id="response">Response</h3>
<p>The response for this request is a JSON object with the following schema:</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code class="language-json">{
  "data": {
    "subTransaction": {
      "totalCount": 0,
      "results": [
        {
          "amount": 0,
          "balanceFactor": 0,
          "timestamp": "",
          "sender": {
            "identifier": ""
          },
          "recipient": {
            "identifier": ""
          },
          "tx": {
            "classification": {
              "action": "",
              "activity": ""
            }
          },
          "asset": {
            "symbol": ""
          }
        }
      ]
    }
  }
}

</code></pre>
<p>The "data" object contains the "subTransaction" field, which in turn includes "totalCount" and "results" fields. The "results" field is an array of objects, each representing a sub-transaction with "amount", "balanceFactor", "timestamp", "sender", "recipient", "tx", and "asset" properties.</p>
<p>The "sender" and "recipient" objects contain an "identifier" property, while the "tx" object contains a "classification" object with "action" and "activity" properties. The "asset" object includes a "symbol" property.</p>
<p>The response may include multiple sub-transaction objects based on the query parameters provided in the request body.</p>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MarkInternalTransfer ($stxId1: Int!, $stxId2: Int!) {
    markInternalTransfer(stxId1: $stxId1, stxId2: $stxId2) {
        success
        message
    }
}
```

**Variables:**
```json
{
  "stxId1": 1234700389,
  "stxId2": 1234700386
}
```

## Disconnect Internal Transfer

`POST {{backend}}/graphql`

<p>This endpoint makes an HTTP POST request to {{backend}}/graphql to retrieve sub-transaction data. The request payload should include the necessary parameters for querying sub-transaction information.</p>
<h3 id="request-body">Request Body</h3>
<p>The request body for this endpoint should be in JSON format, containing the parameters required to specify the sub-transaction query.</p>
<h3 id="response">Response</h3>
<p>The response for this request is a JSON object with the following schema:</p>
<pre class="click-to-expand-wrapper is-snippet-wrapper"><code class="language-json">{
  "data": {
    "subTransaction": {
      "totalCount": 0,
      "results": [
        {
          "amount": 0,
          "balanceFactor": 0,
          "timestamp": "",
          "sender": {
            "identifier": ""
          },
          "recipient": {
            "identifier": ""
          },
          "tx": {
            "classification": {
              "action": "",
              "activity": ""
            }
          },
          "asset": {
            "symbol": ""
          }
        }
      ]
    }
  }
}

</code></pre>
<p>The "data" object contains the "subTransaction" field, which in turn includes "totalCount" and "results" fields. The "results" field is an array of objects, each representing a sub-transaction with "amount", "balanceFactor", "timestamp", "sender", "recipient", "tx", and "asset" properties.</p>
<p>The "sender" and "recipient" objects contain an "identifier" property, while the "tx" object contains a "classification" object with "action" and "activity" properties. The "asset" object includes a "symbol" property.</p>
<p>The response may include multiple sub-transaction objects based on the query parameters provided in the request body.</p>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MarkInternalTransfer ($stxId1: Int!, $stxId2: Int!) {
    markInternalTransfer(stxId1: $stxId1, stxId2: $stxId2) {
        success
        message
    }
}
```

**Variables:**
```json
{
  "stxId1": 1234700389,
  "stxId2": 1234700386
}
```

## Get Internal Transfer Suggestions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query getInternalTransactionSuggestions($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $children_FiatValues_Isnull: Boolean, $syncingStatus_In: [String], $excludeSpam: Boolean, $comments_Isnull: String, $comments_FileKey_Isnull: String, $invoices_Isnull: String, $bookmark_In: [String], $platform_In: [String], $thirdPartyAccounts_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_Multiple: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $tags_Overlap: [String], $thirdPartyAccountsTags_Overlap: [String], $identifier_Contains: String, $classification_Activity: String, $children_BalanceFactor: Float, $children_Amount_Between: String, $children_FiatValue_Between: String, $isPending: Boolean, $createdByUser: Boolean, $children_NonTaxableState: Boolean, $onlyRollup: Boolean, $methodIds: [String], $apar: Boolean, $missing_Account_Data: Boolean, $integrationAccount_In: [String], $children_FifoCostBasis_Isnull: Boolean, $applyFilterToChildren: Boolean, $children_InternalTransferSubTx_Isnull: Boolean) {
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
    syncingStatus_In: $
[TRUNCATED]
```

**Variables:**
```json
{
  "timestamp_Gte": "2024-12-12T00:00:00+02:00",
  "timestamp_Lt": "2025-01-11T23:59:59.999000000+02:00",
  "limit": 10,
  "offset": 0,
  "currency": "usd",
  "children_Asset_AssetClass_In": [
    "199"
  ],
  "children_BelongsTo_In": [],
  "platform_In": [],
  "thirdPartyAccounts_In": [],
  "excludeSpam": true,
  "identifier_In": [],
  "tags_Overlap": [],
  "thirdPartyAccountsTags_Overlap": [],
  "children_FiatValues_Isnull": null,
  "children_BalanceFactor": -1,
  "children_Amount_Between": "31965.831,39069.349",
  "children_FiatValue_Between": "",
  "success": null,
  "children_NonTaxableState": null,
  "children_FifoCostBasis_Isnull": null,
  "children_InternalTransferSubTx_Isnull": null
}
```

## Get FifoCostBasis

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query SubTxQuery($id: Float, $currency: String) {
  subTransaction(id: $id, currency: $currency) {
    results {
      fifoCostBasisQueue
    }
  }
}
```

**Variables:**
```json
{
  "id": 254198211,
  "currency": "usd"
}
```

## Get Financial Issue

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query SubTxQuery($id: Float, $currency: String) {
  subTransaction(id: $id, currency: $currency) {
    results {
      fifoCostBasisQueue
    }
  }
}
```

**Variables:**
```json
{
  "id": 254198211,
  "currency": "usd"
}
```

## Get Stateless Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query($identifier: String!, $platform: Platform!) {
  getStatelessTransaction(txHash: $identifier, platform: $platform) {
    identifier
    platform
    fromAddress
    toAddress
    blockNumber
    timestamp
    success
    methodId
    subTransactions {
      typeId
      sender
      recipient
      assetIdentifier
      asset {
        symbol
        name
        decimals
      }
      amount
      type
      balanceFactor
    }
    balanceChanges {
      account
      assetIdentifier
      asset {
        symbol
        name
        decimals
      }
      balanceBefore
      balanceAfter
      diff
    }
  }
}
```

**Variables:**
```json
{
    "identifier": "0x1a2c1d615f1812def157f57cbe2a050ea0b610d60b27bad0ea60e3e47d206030",
    "platform": "ETHEREUM"
}
```
