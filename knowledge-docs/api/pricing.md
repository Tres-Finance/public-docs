# Tres API — Pricing

Endpoints in the 'Pricing' section of the public Tres API collection (3 requests).

## Stateless Pricing

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessPricing($assetIdentifier: String!, $platform: Platform!, $timestamp: DateTime, $currencies: [Currency]!) {
  getStatelessPricing (assetIdentifier: $assetIdentifier, platform: $platform, timestamp: $timestamp, currencies: $currencies) {
      prices
    }
}
```

**Variables:**
```json
{
    "assetIdentifier": "0x5c647ce0ae10658ec44fa4e11a51c96e94efd1dd",
    "platform": "ETHEREUM",
    "currencies": ["USD"],
    "timestamp": "2026-03-11T11:10:22Z"
}
```

**Sample response (200):**
```json
{
    "data": {
        "getStatelessPricing": {
            "prices": {
                "usd": 17.93975377975985
            }
        }
    }
}
```

## Batch Stateless Pricing

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessPricing($requests: [GetBatchPricesRequest]!) {
  getBatchStatelessPricing (requests: $requests) {
      prices
    }
}
```

**Variables:**
```json
{
    "requests": [
        {
        "currencies": ["USD"],
        "timestamp": "2023-11-11T11:10:22Z",
        "assetIdentifier": "native",
        "platform": "ETHEREUM"
        },
        {
        "currencies": ["USD"],
        "timestamp": "2023-11-11T11:10:22Z",
        "assetIdentifier": "native",
        "platform": "SOLANA"
        }
    ]
}
```

## Batch Stateless Pricing By Asset Class

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessPricingByAssetClass($requests: [GetBatchPricesByAssetClassRequest]!) {
  getBatchStatelessPricingByAssetClass (requests: $requests) {
      prices
      assetClassId
      symbol
    }
}
```

**Variables:**
```json
{
    "requests": [
        {
        "currencies": ["USD"],
        "timestamp": "2023-11-11T11:10:22Z",
        "assetClass": "3"
        },
        {
        "currencies": ["USD"],
        "timestamp": "2023-11-11T11:10:22Z",
        "assetClass": "5"
        },
        {
        "currencies": ["USD"],
        "timestamp": "2023-11-11T11:10:22Z",
        "assetClass": "1"
        },
         {
        "currencies": ["USD"],
        "timestamp": "2023-11-11T11:10:22Z",
        "assetClass": "1000000"
        }
    ]
}
```
