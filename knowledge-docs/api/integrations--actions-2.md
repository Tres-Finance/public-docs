# Tres API — Integrations — Actions (part 2)

Endpoints in the 'Integrations — Actions (part 2)' section of the public Tres API collection (2 requests).

## Unexclude SubTransactions From Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UnexcludeSubTransactionsFromRule($ruleId: Int!, $stxIds: [BigInt]!) {
    unexcludeSubTransactionsFromRule(ruleId: $ruleId, stxIds: $stxIds) {
        status
    }
}
```

**Variables:**
```json
{
  "ruleId": 245351,
  "stxIds": [4728688431, 4728689218]
}
```

## exclude SubTransactions From Rule Copy

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UnexcludeSubTransactionsFromRule($ruleId: Int!, $stxIds: [BigInt]!) {
    unexcludeSubTransactionsFromRule(ruleId: $ruleId, stxIds: $stxIds) {
        status
    }
}
```

**Variables:**
```json
{
  "ruleId": 245351,
  "stxIds": [4728688431, 4728689218]
}
```
