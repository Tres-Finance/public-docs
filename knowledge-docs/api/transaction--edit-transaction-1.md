# Tres API — Transaction — Edit Transaction (part 1)

Endpoints in the 'Transaction — Edit Transaction (part 1)' section of the public Tres API collection (20 requests).

## Set Batch Non Taxable

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SetNonTaxable($ids: [String]!, $isNonTaxable: Boolean) {
  setNonTaxable(ids: $ids, isNonTaxable: $isNonTaxable ) {
    success
  }
}
```

**Variables:**
```json
{
  "ids": ["33628", "33627"],
  "isNonTaxable": false
}
```

## Set Batch Unit Fiat Value by Sub Transaction ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SetBatchManualFiatValue($ids: [String]!, $newUnitValue: Float!, $currency: String) {
  setBatchManualFiatValue(ids: $ids, newUnitValue: $newUnitValue, currency: $currency) {
    success
  }
}
```

**Variables:**
```json
{
  "ids": ["33628", "33627"],
  "newUnitValue": 0,
  "currency": "usd"
}
```

## Set Batch Unit Fiat Value by Asset Class Id

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation bulkFiatEdit($assetClassId: Int!, $currency: Currency!, $startDate: DateTime!, $endDate: DateTime!, $updateExistingFiat: Boolean, $unitPrice: Float!) {
  bulkFiatEdit(
    assetClassId: $assetClassId
    currency: $currency
    startDate: $startDate
    endDate: $endDate
    updateExistingFiat: $updateExistingFiat
    unitPrice: $unitPrice
  ) {
    success
    __typename
  }
}
```

**Variables:**
```json
{
  "assetClassId": 333,
  "currency": "USD",
  "startDate": "2025-03-11T18:32:00.000Z",
  "endDate": "2025-03-13T18:32:00.000Z",
  "unitPrice": 1,
  "updateExistingFiat": true
}
```

## Set Batch Bookmark

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SetBatchBookmark($bookmarks: [TransactionBookmarkInput]!) {
  setBatchTransactionBookmark(
    bookmarks: $bookmarks
  ) {
    success
  }
}
```

**Variables:**
```json
{
  "bookmarks": [
      {
          "identifier": "3YYZauVCTidLHmy2F8Y5GydC4RDXnFNpWhgArNs8cXV1KoyUcyJRf4hQboTagmPf2gdhSS3zu1poTMXS3CVzQbg2",
          "platform": "SOLANA",
          "active": true,
          "bookmarkValue": "STAR"
      },
      {
          "identifier": "4KVdHfTs7K9spHbLBtmCGDc576cvo1tMNfmcDJxcVhpWW8cevrsvdQVnxUhQ4z4FHFazmrHVbXEZ98V2mJgxk4bg",
          "platform": "SOLANA",
          "active": true,
          "bookmarkValue": "STAR"
      }
  ]
}
```

## Calculate Batch Transactions Fiat Value

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CalculateBatchTransactionsFiatValues($transactionsIds: [ID]!) {
  calculateBatchTransactionsFiatValues(transactionsIds: $transactionsIds) {
    workflowId
  }
}
```

**Variables:**
```json
{
  "transactionsIds": ["1633715696.000000044410227653554710900000"]
}
```

## Classify Batch Transactions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ClassifyBatchTransactions($transactionsIds: [ID]!) {
  classifyBatchTransactions(transactionsIds: $transactionsIds) {
    workflowId
  }
}
```

**Variables:**
```json
{
  "transactionsIds": ["1750636799.000000074650308361862872130000"]
}
```

## Set Batch Custom Activity

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SetBatchCustomActivity($customLabels: [CustomLabelInput]!) {
  setBatchCustomActivity(
    customLabels: $customLabels
  ) {
    labels {
      id
    }
  }
}
```

**Variables:**
```json
{
  "customLabels": [
      {
          "identifier": "3YYZauVCTidLHmy2F8Y5GydC4RDXnFNpWhgArNs8cXV1KoyUcyJRf4hQboTagmPf2gdhSS3zu1poTMXS3CVzQbg2",
          "platform": "SOLANA",
          "labelValue": "Bye"
      },
      {
          "identifier": "4KVdHfTs7K9spHbLBtmCGDc576cvo1tMNfmcDJxcVhpWW8cevrsvdQVnxUhQ4z4FHFazmrHVbXEZ98V2mJgxk4bg",
          "platform": "SOLANA",
          "labelValue": "Hi"
      }
  ]
}
```

## Delete Batch Custom Activity

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteBatchCustomActivity($customLabels: [CustomLabelInput]!) {
  deleteBatchCustomActivity(
    customLabels: $customLabels
  ) {
    status
  }
}
```

**Variables:**
```json
{
  "customLabels": [
      {
          "identifier": "3YYZauVCTidLHmy2F8Y5GydC4RDXnFNpWhgArNs8cXV1KoyUcyJRf4hQboTagmPf2gdhSS3zu1poTMXS3CVzQbg2",
          "platform": "SOLANA"
      },
      {
          "identifier": "4KVdHfTs7K9spHbLBtmCGDc576cvo1tMNfmcDJxcVhpWW8cevrsvdQVnxUhQ4z4FHFazmrHVbXEZ98V2mJgxk4bg",
          "platform": "SOLANA"
      }
  ]
}
```

## Delete Batch Txs by Identifiers

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation BulkDeleteTransactions($identifiers: [String]!) {
    bulkDeleteTransactions(identifiers: $identifiers) {
        deletedCount
        skippedCount
    }
}
```

**Variables:**
```json
{
  "identifiers": [
      "81d3c0ef9918e8669871fdfaadbb4685078c6b80255c696a9dcce8b4a06ea978"
  ]
}
```

## Delete Batch Txs by Ids

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation BulkDeleteTransactionsByIds($ids: [String]!) {
    bulkDeleteTransactionsByIds(ids: $ids) {
        deletedCount
        skippedCount
    }
}
```

**Variables:**
```json
{
  "ids": [
      "1"
  ]
}
```

## Delete Batch Txs by Timerange

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation BulkDeleteTransactionsByTimestamp(
    $internalAccountId: Int,
    $startTimestamp: DateTime!
    $endTimestamp: DateTime!
) {
    bulkDeleteTransactionsByTimestamp(
        internalAccountId: $internalAccountId
        startTimestamp: $startTimestamp
        endTimestamp: $endTimestamp
    ) {
        deletedCount
        skippedCount
    }
}
```

**Variables:**
```json
{
  "internalAccountId": 3276317,
  "startTimestamp": "2025-01-01T00:00:00+00:00",
  "endTimestamp": "2026-01-01T00:00:00+00:00"
}
```

## Restore Batch Txs by Identifiers

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation BulkRestoreTransactions($identifiers: [String]!) {
    bulkRestoreTransactions(identifiers: $identifiers) {
        restoredCount
    }
}
```

**Variables:**
```json
{
  "identifiers": [
      "81d3c0ef9918e8669871fdfaadbb4685078c6b80255c696a9dcce8b4a06ea978"
  ]
}
```

## Restore Batch Txs by Timerange

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation BulkRestoreTransactionsByTimestamp(
    $internalAccountId: Int,
    $startTimestamp: DateTime!
    $endTimestamp: DateTime!
) {
    bulkRestoreTransactionsByTimestamp(
        internalAccountId: $internalAccountId
        startTimestamp: $startTimestamp
        endTimestamp: $endTimestamp
    ) {
        restoredCount
    }
}
```

**Variables:**
```json
{
    "internalAccountId": 3276317,
    "startTimestamp": "2025-01-01T00:00:00+00:00",
    "endTimestamp": "2026-01-01T00:00:00+00:00"
}
```

## Restore Batch Txs by Ids

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation BulkDeleteTransactionsByIds($ids: [String]!) {
    bulkDeleteTransactionsByIds(ids: $ids) {
        deletedCount
        skippedCount
    }
}
```

**Variables:**
```json
{
  "ids": ["0"]
}
```

## Set Total Fiat Value

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation setManualFiatValue($id: String!, $newFiatValue: String!, $currency: String) {
  setManualFiatValue(id: $id, newFiatValue: $newFiatValue, currency: $currency) {
    success
  }
}
```

**Variables:**
```json
{
  "id": "9574836",
  "newFiatValue": "0",
  "currency": "usd"
}
```

## Edit Sub Transaction 3rd Party

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation EditSubTransactionThirdParty($id: ID!, $thirdPartyIdentifier: String!) {
  editSubTransactionThirdParty(id: $id, thirdPartyIdentifier: $thirdPartyIdentifier) {
    success
  }
}
```

**Variables:**
```json
{
  "id": 1192684658,
  "thirdPartyIdentifier": "juno1qanwkm62vetdgan6kpyq7n3kufrwce2suv483v"
}
```

## Delete Custom Activity

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($labelValue: String, $identifier: String, $platform: Platform) {
  setCustomActivity(labelValue: $labelValue, identifier: $identifier, platform: $platform) {
    label {
      labelValue
      identifier
      platform
      id
    }
  }
}
```

**Variables:**
```json
{
    "identifier": "0x46781e59bfbafb7330f19f9f806ad16db2448d1d04ee5c7cc30c549d3f13c68e",
    "platform": "ETHEREUM",
    "labelValue": "test"
}
```

## Set Custom Activity

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation setCustomActivity($identifier: String!, $platform: Platform!, $labelValue: String!) {
  setCustomActivity(
    identifier: $identifier
    labelValue: $labelValue
    platform: $platform
  ) {
    label {
      id
    }
  }
}
```

**Variables:**
```json
{
  "identifier": "HsVrsx7CZmRX5a49yxAqqsvoWGjhGGk112KBXxDSG3qZ",
  "labelValue": "APY FUNDER",
  "platform": "NEAR"
}
```

**Sample response (200):**
```json
{
    "data": {
        "setCustomActivity": {
            "label": {
                "id": "59368"
            }
        }
    }
}
```

## Set Bookmark

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation setTransactionBookmark($identifier: String!, $platform: String!, $active: Boolean!, $bookmark_value: String!) {
  setTransactionBookmark(
    identifier: $identifier
    platform: $platform
    active: $active
    bookmarkValue: $bookmark_value
  ) {
    active
  }
}
```

**Variables:**
```json
{
  "identifier": "6031B417803304D7040946D59D86148D78C879873532330D8FBC4A6A9EC96D07",
  "platform": "ripple",
  "active": true,
  "bookmark_value": "star"
}
```

**Sample response (200):**
```json
{
    "data": {
        "setCustomActivity": {
            "label": {
                "id": "59368"
            }
        }
    }
}
```

## Delete Sub Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($id: String!) {
  deleteSubTransaction(id: $id) {
      success
  }
}
```

**Variables:**
```json
{
    "id": "477320141"
}
```
