# Tres API — Use cases / Examples — Staked Assets

Endpoints in the 'Use cases / Examples — Staked Assets' section of the public Tres API collection (2 requests).

## Get Asset Balance (only staked assets)

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query AssetBalanceQuery($limit: Int, $offset: Int, $currency: String, $internalAccount: Float, $parentBalance_Isnull: Boolean, $asset_Name_Icontains: String, $state: String, $includePending: Boolean) {
  assetBalance(limit: $limit, offset: $offset, currency: $currency, belongsTo_Id: $internalAccount, parentBalance_Isnull: $parentBalance_Isnull, state: $state, includePending: $includePending
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
          name
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
    "state": "locked",
    "includePending": true
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
    "state": "locked"
}
```
