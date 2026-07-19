# Tres API — Trial Balance

Endpoints in the 'Trial Balance' section of the public Tres API collection (3 requests).

## Trigger Trial Balance

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TriggerTrialBalance($sources: [String!]!) {
    triggerTrialBalance(sources: $sources) {
        success
        workflowId
        message
    }
}
```

**Variables:**
```json
{
    "sources" : ["PRE_SYNC"]
}
```

## Trial Balance Status

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TrialBalanceStatus {
    trialBalanceStatus {
        success
        message
        status {
            status
            lastUpdatedAt
            progressTotal
            progressCompleted
        }
    }
}
```

**Variables:**
```json
{
  "integrationId": 1234
}
```

## Trial Balance Data

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TrialBalanceStatus {
    trialBalanceStatus {
        success
        message
        status {
            status
            lastUpdatedAt
        }
    }
}
```
