# Tres API — Use cases / Examples — Staking Deposit / Withdrawals

Endpoints in the 'Use cases / Examples — Staking Deposit / Withdrawals' section of the public Tres API collection (1 requests).

## Ethereum2 Withdrawals

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTxBy($limit: Int, $offset: Int, $belongsTo_Identifier_In: [String], $timestamp_Gt: DateTime, $timestamp_Lt: DateTime, $platform: String, $tx_Classification_Activity: String) {
 subTransaction(limit: $limit, offset: $offset, belongsTo_Identifier_In: $belongsTo_Identifier_In, timestamp_Gt: $timestamp_Gt, timestamp_Lt: $timestamp_Lt, platform: $platform, tx_Classification_Activity: $tx_Classification_Activity) {
   totalCount
   results {
     amount
     balanceFactor
     timestamp
     sender {
         identifier
     }
     tx {
         blockNumber
     }
     recipient {
         identifier
     }
     tx {
         commissionRate
         classification {
             action
             activity
         }
     }
     asset {
         symbol
     }
   }
 }
}
```

**Variables:**
```json
{
  "limit": 10,
  "offset": 0,
  "tx_Classification_Activity": "STAKING RETURN",
  "platform": "ethereum2",
  "belongsTo_Identifier_In": ["0x800f96e79f4e105578c04f267776f6173047b43fdea9c12f1c7406661729f6131eaf9421d30c2b47b01d29be769bd1bb"],
  "timestamp_Gt": "2020-05-01T12:00:23.000002+00:00",
  "timestamp_Lt": "2023-05-01T12:00:23.000002+00:00"

}
```
