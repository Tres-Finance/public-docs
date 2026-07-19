# Tres API — Classification

Endpoints in the 'Classification' section of the public Tres API collection (5 requests).

## Get Classification Rules

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTransactionClassificationQuery {
  transactionClassification {
    results {
      id
      activity
      balanceFactor
      methodId
      parentPlatform
      recipientIdentifier
      senderIdentifier
      senderInternalAccountTag
      recipientInternalAccountTag
      senderContactTag
      recipientContactTag
      status
      priority
      organization {
        id
      }
    }
  }
}
```

## Get All Workflows / Tasks

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query LedgerTasks {
    ledgerTasks {
        listWorkflows {
            progress
            workflowId
            runId
            workflowType
        }
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "ledgerTasks": {
            "listWorkflows": [
                {
                    "progress": {
                        "total": 636,
                        "completed": 169
                    },
                    "workflowId": "ReportWorkflow-153703",
                    "runId": "0196105e-6191-773b-9809-508bc0b79144"
                }
            ]
        }
    }
}
```

## Create Classification Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateTransactionClassificationRule($activity: String!, $parentPlatform: ParentPlatform, $methodId: String,
    $recipientIdentifier: String, $senderIdentifier: String,
    $senderInternalAccountTag: String, $recipientInternalAccountTag: String,
    $senderContactTag: String, $recipientContactTag: String, $priority: Int) {
  createTransactionClassificationRule(
    activity: $activity,
    parentPlatform: $parentPlatform,
    methodId: $methodId,
    recipientIdentifier: $recipientIdentifier,
    senderIdentifier: $senderIdentifier
    senderInternalAccountTag: $senderInternalAccountTag
    recipientInternalAccountTag: $recipientInternalAccountTag
    senderContactTag: $senderContactTag
    recipientContactTag: $recipientContactTag
    priority: $priority
  ) {
    success
  }
}
```

**Variables:**
```json
{
    "parentPlatform": "ETHEREUM",
    "activity": "hi",
    "senderContactTag": "bye",
    "priority": 0
}
```

## Update Classification Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateTransactionClassificationRule($id: ID!, $activity: String!, $priority: Int) {
  updateTransactionClassificationRule(
    activity: $activity
    id: $id
    priority: $priority
  ) {
    success
  }
}
```

**Variables:**
```json
{
    "activity": "DONE",
    "id": "13075"
}
```

## Delete Classification Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteTransactionClassificationRule($key: String!) {
  deleteTransactionClassificationRule(
    key: $key
  ) {
    success
  }
}
```

**Variables:**
```json
{
    "key": "substrate_None_None_org_ItnSDQBl32kHjo2F_None_None_None_None_None_None"
}
```
