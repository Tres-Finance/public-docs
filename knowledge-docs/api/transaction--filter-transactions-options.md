# Tres API — Transaction — Filter Transactions Options

Endpoints in the 'Transaction — Filter Transactions Options' section of the public Tres API collection (6 requests).

## Asset Classes Filters

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAssetsNames {
  filterOptions {
    assetsClass {
      name
      displayName
      id
      verificationStatus
      __typename
    }
    __typename
  }
}
```

## Get Assets Filters

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAssetsNames {
  filterOptions {
    assets {
      displayName: name
      id
      bookmark
      __typename
    }
    __typename
  }
}
```

## External Accounts Names

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query ExternalSenderAccountsNames {
  ledgerFilters {
    thirdPartyAccounts {
      displayName
      id
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
  "limit": 10,
  "offset": 0
}
```

## General Filters

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query FilterOptions {
  filterOptions {
    platforms {
      displayName
      id
    }
    transactionsTags {
        displayName
        id
    }
    actions {
        displayName
        id
    }
  }
}
```

## All Platforms

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query getAllPlatforms {
    ledgerFilters {
      allPlatforms
    }
  }
```

## All Onchain Parent Platforms

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query getAllPlatforms {
    ledgerFilters {
      allPlatforms
    }
  }
```
