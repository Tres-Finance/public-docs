# Tres API — Transaction — Custom Price Feed / Manual Fiat Value Configs

Endpoints in the 'Transaction — Custom Price Feed / Manual Fiat Value Configs' section of the public Tres API collection (4 requests).

## Upsert Configuration

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateManualFiatValueConfiguration($assetClassId: Int!, $currency: Currency!, $startTimestamp: DateTime!, $endTimestamp: DateTime!, $unitPrice: Float!) {
  createManualFiatValueConfiguration(
    assetClassId: $assetClassId
    currency: $currency
    startTimestamp: $startTimestamp
    endTimestamp: $endTimestamp
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
  "assetClassId": 3,
  "currency": "USD",
  "startTimestamp": "2020-03-11T18:32:00.000Z",
  "endTimestamp": "2026-03-13T18:32:00.000Z",
  "unitPrice": 1
}
```

## Get Configurations

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ManualFiatValueConfiguration($offset: Int, $limit: Int, $assetClass_In: [ID]) {
  manualFiatValueConfiguration (
    offset: $offset
    limit: $limit
    assetClass_In: $assetClass_In
  ){
    totalCount
    results { 
     assetClass {
        name
        symbol
        id
    }
    id
    startTimestamp
    endTimestamp
    unitPrice
    currency
   }
  }
}
```

**Variables:**
```json
{
    "offset": 0,
    "limit": 2,
    "assetClass_In": ["2"]
}
```

## Delete Configuration

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteManualFiatValueConfiguration($configurationId: ID!) {
  deleteManualFiatValueConfiguration(
    configurationId: $configurationId
  ) {
    success
    __typename
  }
}
```

**Variables:**
```json
{
  "configurationId": 1
}
```

## Available Asset Classes

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query PaginatedAssets($limit: Int, $offset: Int, $assetType: String, $verificationStatus: String, $showRelated: Boolean) {
  assetClass(
    limit: $limit
    offset: $offset
    assetType: $assetType
    verificationStatus: $verificationStatus
    showRelated: $showRelated
  ) {
    totalCount
    results {
      id
      symbol
      displayName: name
      verificationStatus
    }
  }
}
```

**Variables:**
```json
{
  "verificationStatus": "verified"
}
```
