# Tres API — Transaction — Edit Transaction (part 2)

Endpoints in the 'Transaction — Edit Transaction (part 2)' section of the public Tres API collection (5 requests).

## Split Sub Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SplitSubTransaction(
  $splitDataList: [SplitDataInputObjectType!]!
  $originalSubTxId: ID!
) {
  splitSubTransaction(
    splitDataList: $splitDataList
    originalSubTxId: $originalSubTxId
  ) {
    createdTxIds
  }
}
```

**Variables:**
```json
{
    "splitDataList": [
        {"balance": "3000.0", "direction": "INFLOW", "thirdPartyAddress": "p-avaxValidator", "methodId": "claimRewards"},
        {"balance": "38000.0", "direction": "INFLOW", "thirdPartyAddress": "native", "methodId": "withdrawStake"},
        {"balance": "1993.53887", "direction": "OUTFLOW", "thirdPartyAddress": "p-avaxValidator", "methodId": "feesToValidator"}
    ],
    "originalSubTxId": "4106904287"
}
```

## Undo Split Sub Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation undoSplitSubTransactio($subTxId: ID!) {
  undoSplitSubTransaction(
    subTxId: $subTxId
  ) {
        success
        message
        restoredSubTxId
        restoredTxId
    }
}
```

**Variables:**
```json
{
    "subTxId": "3940036805"
}
```

## Delete Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($id: String!) {
  deleteTransaction(id: $id) {
      success
  }
}
```

**Variables:**
```json
{
    "id": "87698197"
}
```

## Restore Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation RestoreTx($transactionId: String!) {
    restoreTx(transactionId: $transactionId) {
        success
        message
    }
}
```

**Variables:**
```json
{
    "transactionId": "1722950616.000000126706387778075873990000"
}
```

## Restore SubTransaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation RestoreSubTx($subTxId: String!) {
    restoreSubTx(subTxId: $subTxId) {
        success
        message
    }
}
```

**Variables:**
```json
{
    "subTxId": "1295983140"
}
```
