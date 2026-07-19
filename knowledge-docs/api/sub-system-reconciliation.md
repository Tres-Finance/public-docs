# Tres API — Sub System Reconciliation

Endpoints in the 'Sub System Reconciliation' section of the public Tres API collection (1 requests).

## Total Reconciliation Status

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query CounterTransfers($startDate: Date, $endDate: Date, $currency: Currency!, $assetClass: Int, $platform: Platform) {
  counterTransfers {
    counterTransfersStatus(
      currency: $currency
      startDate: $startDate
      endDate: $endDate
      assetClass: $assetClass
      platform: $platform
    ) {
      matchedTransfersCount
      unmatchedTransfersCount
      totalFiatValueMatched
      totalFiatValueUnmatched
    }
    counterTransfersAssetClassBreakdown(
      currency: $currency
      startDate: $startDate
      endDate: $endDate
      assetClass: $assetClass
      platform: $platform
    ) {
        date
        assetClassId
        assetClassName
        assetClassSymbol
        matchedTransfersCount
        unmatchedTransfersCount
        totalFiatValueMatched
        totalFiatValueUnmatched
    }

  }
  
}
```

**Variables:**
```json
{
  "currency": "USD",
  "startDate": "2026-04-14",
  "endDate": "2026-05-14"
}
```
