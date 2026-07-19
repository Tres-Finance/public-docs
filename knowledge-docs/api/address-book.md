# Tres API — Address Book

Endpoints in the 'Address Book' section of the public Tres API collection (8 requests).

## Set Custom Account Name

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SetCustomAccountName($labelValue: String, $identifier: String) {
    setCustomAccountName(labelValue: $labelValue, identifier: $identifier) {
      accountTxsSummary {
        customLabel {
          labelValue
          tags
          originalIdentifier
        }
        accountIdentifier
        inflowFiatValue
        outflowFiatValue
      }
    }
  }
```

**Variables:**
```json
{
    "identifier": "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270",
    "labelValue": "aaabbb"
}
```

## Set Tags to Custom Account Name

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SetCustomAccountNameTags($identifier: String!, $tags: [String]!) {
    setCustomAccountNameLabelTags(identifier: $identifier, tags: $tags) {
      accountTxsSummary {
        customLabel {
          labelValue
          tags
          originalIdentifier
        }
        accountIdentifier
      }
    }
  }
```

**Variables:**
```json
{
    "identifier": "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270",
    "tags": ["a5a"]
}
```

## Get Custom Account Name Tags

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ActivitiesNames {
  ledgerFilters {
    customNameLabelTags {
      displayName
      id
      __typename
    }
    
  }
}
```

## Delete Custom Account Name

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($labelValue: String, $identifier: String) {
  deleteCustomAccountNameLabel(labelValue: $labelValue, identifier: $identifier) {
    status
  }
}
```

**Variables:**
```json
{
    "identifier": "cosmos1sa0khzc3jn8v2sjflm9eyqkwyfx5deqvk7tmg8",
    "labelValue": "test"
}
```

## Get Account Tx Summary

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AddressBookWithCount($limit: Int, $offset: Int, $fiatCurrency: String) {
  accountTxsSummary(
    fiatCurrency: $fiatCurrency
    excludeInternalAccounts: true
    identificationState: "identified"
    offset: $offset
    limit: $limit
  ) {
    results {
        id
      customLabel {
        labelValue
        tags
        originalIdentifier
      }
      accountIdentifier
      inflowFiatValue
      outflowFiatValue
    }
  }
}
```

**Variables:**
```json
{
    "limit": 1000
}
```

## Get Address Book with Tx Summary

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AddressBookWithoutSummary($limit: Int, $offset: Int, $search: String) {
  customAccountNameLabel(
    search: $search
    offset: $offset
    limit: $limit
  ) {
    results {
        id
        labelValue
        tags
        originalIdentifier
        accountTxsSummary {
            outflowFiatValue
            inflowFiatValue
        }
    }
  }
}
```

**Variables:**
```json
{
    "limit": 1000
}
```

## Get Address Book without Tx Summary

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AddressBookWithoutSummary($limit: Int, $offset: Int, $search: String) {
  customAccountNameLabel(
    search: $search
    offset: $offset
    limit: $limit
  ) {
    results {
        id
        labelValue
        tags
        originalIdentifier
      
    }
  }
}
```

**Variables:**
```json
{
    "search": "TYeeEZCz5CUHYuExhXfCty2x3QatsMwQBo"
}
```

## Get Unidentified Addresses

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query UnidentifiedAddressesWithCount($limit: Int, $offset: Int, $fiatCurrency: String, $accountDirection: String) {
  accountTxsSummary(
    fiatCurrency: $fiatCurrency
    ordering: "-outflowTxCount,"
    excludeInternalAccounts: true
    accountDirection: $accountDirection
    identificationState: "unidentified"
    offset: $offset
    limit: $limit
  ) {
    totalCount
    results {
      accountIdentifier
      outflowFiatValue
      outflowTxCount
    }
  }
}
```

**Variables:**
```json
{
  "limit": 10,
  "offset": 0,
  "fiatCurrency": "usd",
  "accountDirection": "recipient"
}
```
