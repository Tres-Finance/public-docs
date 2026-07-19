# Tres API — Commit / Data Collection Managment

Endpoints in the 'Commit / Data Collection Managment' section of the public Tres API collection (14 requests).

## Get Last Success Commit

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetLastSuccessCommit($status: String, $offset: Int, $limit: Int) {
  collectAudit(status: $status, offset: $offset, limit: $limit) {
    results {
        commitId
        createdAt
        updatedAt
        status
        progress
        numOfTransactionsCreated
    }
  }
}
```

**Variables:**
```json
{
    "status": "completed",
    "limit": 1
}
```

**Sample response (200):**
```json
{
    "data": {
        "collectAudit": {
            "results": [
                {
                    "commitId": "39943afb-1378-4ae0-8135-f8e8176d1444",
                    "createdAt": "2023-07-06T08:30:21.691091+00:00",
                    "updatedAt": "2023-07-06T08:52:46.185593+00:00",
                    "status": "COMPLETED",
                    "progress": {
                        "succeeded": 526
                    },
                    "numOfTransactionsCreated": 0
                }
            ]
        }
    }
}
```

## Get Last Success or Running Commit

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetLastSuccessCommit($status_In: [String], $offset: Int, $limit: Int) {
  collectAudit(status_In: $status_In, offset: $offset, limit: $limit) {
    results {
        commitId
        createdAt
        updatedAt
        status
        progress
        numOfTransactionsCreated
    }
  }
}
```

**Variables:**
```json
{
    "status_In": ["completed", "in_progress"],
    "limit": 1
}
```

## Get Commit Status by Commit ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetCommit($commitId: UUID) {
  collectAudit(commitId: $commitId) {
    results {
        commitId
        createdAt
        updatedAt
        status
        progress
        numOfTransactionsCreated
        requestMetadata
        failureReasons {
            errorType
        }
    }
  }
}
```

**Variables:**
```json
{
    "commitId": "7ad8a762-5249-4dcf-9aa4-e43c8932d4ae"
}
```

## Get Last Commit

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetLastSuccessCommit($status: String, $offset: Int, $limit: Int) {
  collectAudit(status: $status, offset: $offset, limit: $limit) {
    results {
        commitId
        createdAt
        status
        updatedAt
        progress
        numOfTransactionsCreated
    }
  }
}
```

**Sample response (200):**
```json
{
    "data": {
        "collectAudit": {
            "results": [
                {
                    "commitId": "39943afb-1378-4ae0-8135-f8e8176d1444",
                    "createdAt": "2023-07-06T08:30:21.691091+00:00",
                    "status": "COMPLETED",
                    "updatedAt": "2023-07-06T08:52:46.185593+00:00",
                    "progress": {
                        "succeeded": 526
                    },
                    "numOfTransactionsCreated": 0
                }
            ]
        }
    }
}
```

## Trigger Commit

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TriggerCommit {
  triggerCommit {
    status
    message   
    commitId
  }
}
```

## Trigger Commit By Internal Account

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TriggerCommit($internalAccountIds: [ID]) {
  triggerCommit(internalAccountIds: $internalAccountIds) {
    status
    message   
    commitId
  }
}
```

**Variables:**
```json
{
    "internalAccountIds": ["628141"]
}
```

## Trigger Commit By Internal Account + Time

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TriggerCommit($internalAccountIds: [ID], $fromDate: DateTime, $toDate: DateTime) {
  triggerCommit(internalAccountIds: $internalAccountIds, fromDate: $fromDate, toDate: $toDate) {
    status
    message   
    commitId      
  }
}
```

**Variables:**
```json
{
    "internalAccountIds": ["628493"],
    "fromDate": "2025-04-01T07:51:40.529501+00:00",
    "toDate": "2025-04-30T07:51:40.529501+00:00"
}
```

## Trigger Commit By Internal Account + Time + Commit ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TriggerCommit($internalAccountIds: [ID], $fromDate: DateTime, $toDate: DateTime, $commitId: UUID) {
  triggerCommit(internalAccountIds: $internalAccountIds, fromDate: $fromDate, toDate: $toDate, commitId: $commitId) {
    status
    message   
    commitId      
  }
}
```

**Variables:**
```json
{
    "internalAccountIds": ["655670"],
    "fromDate": "2024-03-14T00:00:00+00:00",
    "toDate": "2024-03-15T00:00:00+00:00",
    "commitId": "40a2268a-2006-4ef2-b056-0ce134febe8f"
}
```

## Trigger Parallel Commit

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TriggerParallelCommit($internalAccountIds: [ID], $internalAccountIdentifiers: [String], $fromDate: DateTime!, $toDate: DateTime!, $commitId: UUID, $assetsToCollect: [String], $fetchFullHistory: Boolean, $commitRequestCustomerMetadata: CommitRequestCustomerMetadataInput) {
  triggerParallelCommit(internalAccountIds: $internalAccountIds, fromDate: $fromDate, toDate: $toDate, commitId: $commitId, assetsToCollect: $assetsToCollect, internalAccountIdentifiers: $internalAccountIdentifiers, fetchFullHistory: $fetchFullHistory, commitRequestCustomerMetadata: $commitRequestCustomerMetadata) {
    status
    message   
    commitId      
  }
}
```

**Variables:**
```json
{
    "internalAccountIdentifiers": ["0x6897938af83502d348720679fe7d8e83e7dd5ff2a13c9cad189302babceb7be9"],
    "assetsToCollect": ["substrate_kusama_native"],
    "fetchFullHistory": false,
    "fromDate": "2025-01-01T00:00:00Z",
    "toDate": "2025-09-28T23:59:59Z",
    "commitRequestCustomerMetadata": {
        "env": "EXAMPLE",
        "userId": "user"
    }
}
```

## Trigger Parallel Commit + Max Transaction Limit

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TriggerParallelCommit($internalAccountIds: [ID], $internalAccountIdentifiers: [String], $fromDate: DateTime!, $toDate: DateTime!, $commitId: UUID, $assetsToCollect: [String]!, $maxTransactionLimit: Int) {
  triggerParallelCommit(internalAccountIds: $internalAccountIds, fromDate: $fromDate, toDate: $toDate, commitId: $commitId, assetsToCollect: $assetsToCollect, internalAccountIdentifiers: $internalAccountIdentifiers, maxTransactionLimit: $maxTransactionLimit) {
    status
    message   
    commitId      
  }
}
```

**Variables:**
```json
{"toDate": "2025-08-07T23:59:59+00:00", "fromDate": "2025-07-07T00:00:00+00:00", "assetsToCollect": ["arbitrum_0xff970a61a04b1ca14834a43f5de4533ebddb5cc8"], "internalAccountIds": [679191]}
```

## Update Parallel Commit Max Transaction Limit

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateCommitMaxTransactionLimit($commitId: UUID!, $maxTransactionLimit: Int!) {
  updateCommitMaxTransactionLimit(commitId: $commitId, maxTransactionLimit: $maxTransactionLimit) {
    success
  }
}
```

**Variables:**
```json
{
    "commitId": "6b16a105-422a-2f68-bafd-b4634eafc801",
    "maxTransactionLimit": 1000
}
```

## Check Parallel Commit Reconciliation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query CheckParallelCommitReconciliationStatus($commitId: UUID!) {
  checkParallelCommitReconciliationStatus(commitId: $commitId) {
    inflowAmount     
    outflowAmount
    feeAmount
    totalAmount
    openingBalance
    closingBalance
    balanceDiff
    closingUnbondingBalance
    openingUnbondingBalance
    reconciliationDiff
    internalAccountIdentifier
    assetKey
    reconciliationDiffUsd
    internalAccountName
    fromDate
    toDate
    isReconciled
    commitRequestCustomerMetadata {
        env
        userId
    }
  }
}
```

**Variables:**
```json
{
    "commitId":"1047cc60-dc1c-477a-8104-084ebdf5a74e"
}
```

## Kill Commits

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation KillCommits {
  killCommits {
    status
  }
}
```

## Kill Commit by ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation KillCommits ($commitIds: [String]) {
  killCommits(commitIds: $commitIds) {
    status
  }
}
```

**Variables:**
```json
{
    "commitIds": ["51f27092-f6e9-4fd8-a8d9-c36100ba7c05"]
}
```
