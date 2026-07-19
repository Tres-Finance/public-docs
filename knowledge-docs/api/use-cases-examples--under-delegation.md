# Tres API — Use cases / Examples — Under Delegation

Endpoints in the 'Use cases / Examples — Under Delegation' section of the public Tres API collection (2 requests).

## Get Asset Balance (only under delegation assets)

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AssetBalanceQuery($limit: Int, $offset: Int, $currency: String, $internalAccount: Float, $parentBalance_Isnull: Boolean, $asset_Name_Icontains: String, $state: String) {
  assetBalance(limit: $limit, offset: $offset, currency: $currency, belongsTo_Id: $internalAccount, parentBalance_Isnull: $parentBalance_Isnull, state: $state
  asset_Name_Icontains: $asset_Name_Icontains) {
      totalCount
    results {
      name
      id
      updatedAt
      asset {
          symbol
      }
      amount   
      state
      parentBalance {
          position {
            displayName
        }
      }
      belongsTo {
          identifier
      }
      childBalances {
          asset {
              symbol
          }
          state
          amount
      }
      fiatValue {
        value
        fiatCurrency
      }
    }
  }
}
```

**Variables:**
```json
{
    "currency": "usd",
    "limit": 10,
    "parentBalance_Isnull": false,
    "asset_Name_Icontains": "",
    "state": "delegated_to_account"
}
```

## Get Asset Balance (only staked assets) by Platform

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AssetBalanceQuery($limit: Int, $offset: Int, $currency: String, $internalAccount: Float, $parentBalance_Isnull: Boolean, $asset_Name_Icontains: String, $state: String, $asset_Platform_In: [String]) {
  assetBalance(limit: $limit, offset: $offset, currency: $currency, belongsTo_Id: $internalAccount, parentBalance_Isnull: $parentBalance_Isnull, state: $state
  asset_Name_Icontains: $asset_Name_Icontains asset_Platform_In: $asset_Platform_In) {
      totalCount
    results {
      name
      id
      updatedAt
      asset {
          symbol
          platform
      }
      amount   
      state
      parentBalance {
          position {
            displayName
        }
      }
      belongsTo {
          identifier
          name
      }
      childBalances {
          asset {
              symbol
          }
          state
          amount
      }
      blockHeight
      fiatValue {
        value
        fiatCurrency
      }
    }
  }
}
```

**Variables:**
```json
{
    "currency": "usd",
    "limit": 10,
    "parentBalance_Isnull": false,
    "asset_Platform_In": ["flow"],
    "state": "delegated_to_account"
}
```
