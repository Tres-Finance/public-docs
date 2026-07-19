# Tres API — Workflows

Endpoints in the 'Workflows' section of the public Tres API collection (2 requests).

## Create Workflow

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateOrUpdateWorkflow($currency: String!, $name: String!, $type: String!, $trigger: JSONString, $action: JSONString, $description: String, $id: String) {
  createOrUpdateWorkflow(
    currency: $currency
    name: $name
    type: $type
    trigger: $trigger
    action: $action
    description: $description
    id: $id
  ) {
    status
    __typename
  }
}
```

**Variables:**
```json
{
  "name": "Create transaction roll-up",
  "type": "generateRollup",
  "action": "{\"name\":\"test solana\",\"frequency\":\"monthly\",\"activity\":\"STAKING REWARDS\"}",
  "trigger": "{\"assets\":\"Solana (SOL)\",\"internalAccounts\":\"SOL06 - IOM\",\"platforms\":\"solana\",\"direction\":\"inflow\",\"methodId\":null}",
  "description": "When Solana (SOL) on solana in wallet SOL06 - IOM , Create a monthly roll-up transaction, name it test solana and tag it as STAKING REWARDS",
  "currency": "usd",
  "id": null
}
```

## Get Workflows

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ListWorkflows {
  workflow {
    results {
      id
      description
      action
      currency
      name
      trigger
      type
      status
      __typename
    }
    __typename
  }
}
```
