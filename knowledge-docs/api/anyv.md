# Tres API — AnyV

Endpoints in the 'AnyV' section of the public Tres API collection (10 requests).

## DismissCsvNotification

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DismissCsvNotification($csvId: ID, $status: String! ) {
    aiDismissCsvNotificationMutation(csvId:$csvId, status: $status) {
        success
    }
}
```

**Variables:**
```json
{
    "csvId": 1,
    "status": "banana"
}
```

**Sample response (200):**
```json
{
    "data": {
        "aiDismissCsvNotificationMutation": {
            "success": true
        }
    }
}
```

## CancelCsvWorkflowMutation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation AiCancelCsvWorkflowMutation($csvKey: String!) {
    aiCancelCsvWorkflowMutation(csvKey:$csvKey) {
        ok
    }
}
```

**Variables:**
```json
{
    "csvKey": "org_DuLAbXtQDM9GQHtr/input_files/tx_1740394277.26561_ssaz.csv"
}
```

**Sample response (200):**
```json
{
    "data": {
        "aiCancelCsvWorkflowMutation": {
            "ok": true
        }
    }
}
```

## AiDismissTxsCsv

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation AiDismissTxsCsvMutation($csvId: ID, $status: String) {
    aiDismissTxsCsvMutation(csvId: $csvId, status: $status) {
        ok
    }
}
```

**Variables:**
```json
{
    "csvId": 1,
    "status": "banana"
}
```

**Sample response (200):**
```json
{
    "data": {
        "aiDismissTxsCsvMutation": {
            "ok": true
        }
    }
}
```

## AiGenerateUploadTXCSVUrlMutation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation AiGenerateUploadTXCSVUrlMutation($fileName: String!) {
    aiGenerateUploadTxCsvUrlMutation(fileName:$fileName) {
        url
    }
}
```

**Variables:**
```json
{
    "fileName": "test.csv"
}
```

## AiGetCSVMappingErrorsMutation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation AiGetCSVMappingErrorsMutation($csvKey: String!) {
    aiGetCsvMappingErrorsMutation(csvKey:$csvKey) {
        errorsMapping
    }
}
```

**Variables:**
```json
{
    "csvKey": "org_DuLAbXtQDM9GQHtr/input_files/tx_1733399009.395956_zcat.csv"
}
```

**Sample response (200):**
```json
{
    "data": {
        "aiGetCsvMappingErrorsMutation": {
            "errorsMapping": [
                {
                    "Block Timestamp": "Thursday, February 8, 2024",
                    "Destination Domain Name": null,
                    "Destination Native Token": "XRP",
                    "Expense in Token": "0.000067",
                    "Expense in USD": "0.0022"
                },
                {
                    "Block Timestamp": "Tuesday, February 27, 2024",
                    "Destination Domain Name": "native",
                    "Destination Native Token": "",
                    "Expense in Token": "0.000019",
                    "Expense in USD": "0.00068072"
                },
                {
                    "Block Timestamp": "Wednesday, September 18, 2024",
                    "Destination Domain Name": "native",
                    "Destination Native Token": "USDC",
                    "Expense in Token": "0.000116475",
                    "Expense in USD": null
                }
            ]
        }
    }
}
```

## AiGetCSVInsightsMutation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ReportMessageMutation($prompt: String!, $reportId: String!, $sessionId: String) {
    queryReportMutation(prompt: $prompt, reportId: $reportId, sessionId: $sessionId) {
      response
      sessionId
    }
  }
```

**Variables:**
```json
{
    "csvKey": "org_DuLAbXtQDM9GQHtr/input_files/tx_1733399913.377263_gmyw.csv"
}
```

**Sample response (200):**
```json
{
    "data": {
        "aiGetCsvInsightsMutation": {
            "insights": [
                {
                    "assetName": "ethereum",
                    "assetSymbol": "ETH",
                    "endBalance": 10,
                    "subTxsCount": 2,
                    "txsCount": 1
                },
                {
                    "assetName": "bitcoin",
                    "assetSymbol": "BTC",
                    "endBalance": 8,
                    "subTxsCount": 8,
                    "txsCount": 8
                },
                {
                    "assetName": "solana",
                    "assetSymbol": "SOL",
                    "endBalance": 200,
                    "subTxsCount": 200,
                    "txsCount": 1
                }
            ]
        }
    }
}
```

## AiGetCSVUniqueExamplesMutation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation AiGetCSVUniqueExamplesMutation($csvKey: String!) {
    aiGetCsvUniqueExamplesMutation(csvKey:$csvKey) {
        examples
    }
}
```

**Variables:**
```json
{
    "csvKey": "org_DuLAbXtQDM9GQHtr/input_files/tx_1733399913.377263_gmyw.csv"
}
```

**Sample response (200):**
```json
{
    "data": {
        "aiGetCsvUniqueExamplesMutation": {
            "examples": [
                {
                    "Block Timestamp": "Thursday, February 8, 2024",
                    "Destination Domain Name": "native",
                    "Destination Native Token": "XRP",
                    "Expense in Token": "0.000067",
                    "Expense in USD": "0.0022"
                },
                {
                    "Block Timestamp": "Tuesday, February 27, 2024",
                    "Destination Domain Name": "native",
                    "Destination Native Token": "XRP",
                    "Expense in Token": "0.000019",
                    "Expense in USD": "0.00068072"
                },
                {
                    "Block Timestamp": "Wednesday, September 18, 2024",
                    "Destination Domain Name": "native",
                    "Destination Native Token": "USDC",
                    "Expense in Token": "0.000116475",
                    "Expense in USD": null
                }
            ]
        }
    }
}
```

## AiStartProcessingTXSCSVMutation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation AiStartProcessingTXSCSVMutation($csvKey: String!) {
    aiStartProcessingTxsCsvMutation(
        csvKey: $csvKey
    ){
        ok
    }
}
```

**Variables:**
```json
{
    "csvKey": "org_DuLAbXtQDM9GQHtr/input_files/tx_1733399913.377263_gmyw.csv"
}
```

**Sample response (200):**
```json
{
    "data": {
        "aiStartProcessingTxsCsvMutation": {
            "ok": true
        }
    }
}
```

## AiContinueCsvToProcessingMutation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation AiContinueCsvToProcessingMutation($csvKey: String!) {
    aiContinueCsvToProcessingMutation(
        csvKey: $csvKey
    ){
        ok
    }
}
```

**Variables:**
```json
{
    "csvKey": "org_DuLAbXtQDM9GQHtr/input_files/tx_1740503520.234883_yzxs.csv"
}
```

**Sample response (200):**
```json
{
    "data": {
        "aiStartProcessingTxsCsvMutation": {
            "ok": true
        }
    }
}
```

## AiUploadCsvMappingMutation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation AiStartProcessingTXSCSVMutation($csvKey: String!, $mapping: [GenericScalar]!) {
    aiUploadCsvMappingMutation(
        csvKey: $csvKey,
        mapping: $mapping
    ){
        ok
    }
}
```

**Variables:**
```json
{
    "csvKey": "org_DuLAbXtQDM9GQHtr/input_files/tx_1733399913.377263_gmyw.csv",
    "mapping": [
    {
        "input":
        {
            "Destination Domain Name": "native",
            "Destination Native Token": "USDC",
            "Block Timestamp": "Tuesday, May 21, 2024",
            "Expense in Token": "0.01041",
            "Expense in USD": "0.017638559422931"
        },
        "output":
        {
            "Year": "2024",
            "Month": "5",
            "Day": "21",
            "Time": "00:00:00",
            "Organizational Wallet": "empty",
            "Participating Wallet": "native",
            "Network": "btc_markets",
            "Direction": "sender",
            "Financial Action": "token_transfer",
            "Asset Identifier": "USDC",
            "Amount": "0.01041",
            "Fiat Value (optional)": "0.017638559422931",
            "Fiat Currency": "USD",
            "Transaction Hash": "btc-markets-usdc-2024-05-21T00:00:00.000",
            "Transfer ID": "1",
            "Function Name": "token transfer",
            "Method ID": "token transfer"
        }
    },
    {
        "input":
        {
            "Destination Domain Name": "native",
            "Destination Native Token": "USDC",
            "Block Timestamp": "Thursday, September 19, 2024",
            "Expense in Token": "0.001590502",
            "Expense in USD": "0.000002848127058"
        },
        "output":
        {
            "Year": "2024",
            "Month": "9",
            "Day": "19",
            "Time": "00:00:00",
            "Organizational Wallet": "empty",
            "Participating Wallet": "native",
            "Network": "btc_markets",
            "Direction": "sender",
            "Financial Action": "token_transfer",
            "Asset Identifier": "USDC",
            "Amount": "0.001590502",
            "Fiat Value (optional)": "0.000002848127058",
            "Fiat Currency": "USD",
            "Transaction Hash": "btc-markets-usdc-
[TRUNCATED]
```

**Sample response (200):**
```json
{
    "data": {
        "aiUploadCsvMappingMutation": {
            "ok": true
        }
    }
}
```
