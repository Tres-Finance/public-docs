# Tres API — Transaction — Manual Transaction

Endpoints in the 'Transaction — Manual Transaction' section of the public Tres API collection (9 requests).

## Create Manual Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ManualTransaction($identifier: String!, $platform: Platform!, $timestamp: DateTime!, $methodId: String) {
  createOrUpdateManualTransaction(identifier: $identifier, platform: $platform, timestamp: $timestamp, methodId: $methodId),  {
      transaction {
        identifier
        platform
        timestamp
        id
        methodId
      }
  }

}
```

**Variables:**
```json
{
    "identifier": "my_tx_80",
    "platform": "ETHEREUM",
    "timestamp": "2023-06-06T18:55:11+00:00",
    "methodId": "method_id"
}
```

## Create Manual Sub Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ManualSubTransaction($amount: Decimal!, $fiatValue: Decimal, $assetId: ID!, $belongsToId: ID!, $thirdPartyIdentifier: String!, $transactionId: ID!, $direction: Direction, $typeId: ID!, $action: FinancialAction!, $platform: Platform!, $fiatCurrency: Currency!) {
  createOrUpdateManualSubTransaction(
    amount: $amount
    assetId: $assetId
    belongsToId: $belongsToId
    thirdPartyIdentifier: $thirdPartyIdentifier
    transactionId: $transactionId
    direction: $direction
    typeId: $typeId
    financialAction: $action
    platform: $platform
    fiatValue: $fiatValue
    fiatCurrency: $fiatCurrency
  ) {
    subTransaction {
      id
    }
  }
}
```

**Variables:**
```json
{
  "amount": 12,
  "platform": "BITCOIN",
  "fiatCurrency": "USD",
  "fiatValue": 12,
  "assetId": "bitcoin_native",
  "belongsToId": "29371",
  "thirdPartyIdentifier": "0x5b34741c6320ce8608f06efd3b7489dcc62da2a7",
  "transactionId": "89961053",
  "direction": "INFLOW",
  "action": "TOKEN_TRANSFER",
  "typeId": "cdaf6206853d49ca944c5e4c84833e95"
}
```

## Group Sub Transactions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation GroupSubTransactions($assetId: ID!, $belongsToId: ID!, $transactionId: ID!) {
  groupSubTransactions(
    assetId: $assetId
    belongsToId: $belongsToId
    transactionId: $transactionId
  ) {
    subTransaction {
      id
    }
  }
}
```

**Variables:**
```json
{
  "assetId": "ethereum_0xdac17f958d2ee523a2206206994597c13d831ec7",
  "belongsToId": "627738",
  "transactionId": "1739128679.000000119100258739293061760000"
}
```

## Get Internal Accounts

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAccountById($limit: Int, $offset: Int, $tags_Overlap: [String], $isSynced: Boolean) {
  internalAccount(
    limit: $limit
    offset: $offset
    tags_Overlap: $tags_Overlap
    isSynced: $isSynced
  ) {
    totalCount
    results {
      name
      identifier
      tags
    }
  }
}
```

**Variables:**
```json
{
    "limit": 40,
    "isSynced": true
}
```

## Get Verified Assets

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery($assetClass_VerificationStatus: String, $platform: String) {
  asset(
    assetClass_VerificationStatus: $assetClass_VerificationStatus
    platform: $platform
  ) {
      results {
          key
          name
          symbol
          identifier
      }
  }
}
```

**Variables:**
```json
{
    "platform": "manual",
    "assetClass_VerificationStatus": "verified"
}
```

## Dismiss csv notification

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation {
  dismissTxsCsv(status: "all") {
    ok
  }
}
```

**Sample response (200):**
```json
{
    "errors": [
        {
            "message": "ManualCSV matching query does not exist."
        }
    ],
    "data": {
        "dismissTxsCsv": null
    }
}
```

**Sample response (400):**
```json
{
    "errors": [
        {
            "message": "Unknown argument 'status' on field 'Mutation.dismissTxsCsv'.",
            "locations": [
                {
                    "line": 2,
                    "column": 17
                }
            ],
            "path": null
        },
        {
            "message": "Field 'dismissTxsCsv' argument 'csvId' of type 'String!' is required, but it was not provided.",
            "locations": [
                {
                    "line": 2,
                    "column": 3
                }
            ],
            "path": null
        }
    ]
}
```

## Generate upload txs csv url

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation GenerateCSVUrlMutation {
  aiGenerateUploadTxCsvUrlMutation(
    fileName: {
        value: "Aaa",

    }
    ){
    url
  }
}
```

## Start processing txs csv url

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation StartProcessingCsvMutation($s3Key: String!, $file_name: String!) {
  startProcessingTxsCsvUrl(s3Key: $s3Key, file_name: $file_name) {
    ok
  }
}
```

## Get manual CSV

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery {
  manualCsv {
    results {
      id
      key
      status
      commentedCsv 
    }
  }
}
```

**Sample response (200):**
```json
{
    "data": {
        "manualCsv": {
            "results": [
                {
                    "id": "1",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688298304.649044_izaa.csv",
                    "status": "PENDING"
                },
                {
                    "id": "2",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688298308.401494_zasj.csv",
                    "status": "PENDING"
                },
                {
                    "id": "3",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688299399.001236_xrda.csv",
                    "status": "PENDING"
                },
                {
                    "id": "6",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688304673.316002_jnkw_with_comments.csv",
                    "status": "PENDING"
                },
                {
                    "id": "5",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688304673.316002_jnkw.csv",
                    "status": "INVALID"
                },
                {
                    "id": "67",
                    "key": "org_DuLAbXtQDM9GQHtr/tx_1688369968.238407_lgwd_with_comments.csv",
                    "status": "PENDING"
                },
                {
                    "id": "34",
                    "key": "org_DuLAbXtQDM9GQHtr/tx_1688369968.238407_lgwd.csv",
                    "status": "COMPLETED"
                }
            ]
        }
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "manualCsv": {
            "results": [
                {
                    "id": "1",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688298304.649044_izaa.csv",
                    "status": "PENDING",
                    "commentedCsv": null
                },
                {
                    "id": "2",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688298308.401494_zasj.csv",
                    "status": "PENDING",
                    "commentedCsv": null
                },
                {
                    "id": "3",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688299399.001236_xrda.csv",
                    "status": "PENDING",
                    "commentedCsv": null
                },
                {
                    "id": "6",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688304673.316002_jnkw_with_comments.csv",
                    "status": "PENDING",
                    "commentedCsv": null
                },
                {
                    "id": "5",
                    "key": "org_J49Kxn6pUKjiGim4/tx_1688304673.316002_jnkw.csv",
                    "status": "INVALID",
                    "commentedCsv": {
                        "key": "org_J49Kxn6pUKjiGim4/tx_1688304673.316002_jnkw_with_comments.csv"
                    }
                },
                {
                    "id": "67",
                    "key": "org_DuLAbXtQDM9GQHtr/tx_1688369968.238407_lgwd_with_comments.csv",
                    "status": "PENDING",
                    "commentedCsv": null
                },
                {
                    "id": "34",
                    "key": "org_DuLAbXtQDM9GQHtr/tx_1688369968.238407_lgwd.csv",
                    "status": "COMPLETED",
                    "commentedCsv": {
                        "key": "org_DuLAbXtQDM9GQHtr/tx_1688369968.238407_lgwd_with_comments.csv"
                    }
                }
            ]
        }
    }
}
```
