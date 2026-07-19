# Tres API — Asset Balances — Archived / Portfolio Tracking

Endpoints in the 'Asset Balances — Archived / Portfolio Tracking' section of the public Tres API collection (4 requests).

## Get Daily Total Networth

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query DailyNetworth($currency: Currency!, $startDate: Date!, $endDate: Date!) {
  portfolio {  
    dailyNetworth (currency: $currency, startDate: $startDate, endDate: $endDate) {
        date
        totalValue
        totalAmount
    }
  }
}
```

**Variables:**
```json
{
    "currency": "USD",
    "startDate": "2025-11-10",
    "endDate": "2025-11-15"
}
```

**Sample response (200):**
```json
{
    "data": {
        "portfolio": {
            "dailyNetworthPerInternalAccount": [
                {
                    "internalAccountName": "Admin SOL P2P",
                    "internalAccountIdentifier": "gedl6ckju5hg4jdj2yvcapajpxt4z17pcanvyqzzcltq",
                    "date": "2023-12-19",
                    "totalValue": 34.15634227462335,
                    "totalAmount": 0.45993
                },
                {
                    "internalAccountName": "Admin SOL P2P",
                    "internalAccountIdentifier": "gedl6ckju5hg4jdj2yvcapajpxt4z17pcanvyqzzcltq",
                    "date": "2023-12-20",
                    "totalValue": 35.69664770676992,
                    "totalAmount": 0.45993
                },
                {
                    "internalAccountName": "Admin SOL P2P",
                    "internalAccountIdentifier": "gedl6ckju5hg4jdj2yvcapajpxt4z17pcanvyqzzcltq",
                    "date": "2023-12-21",
                    "totalValue": 42.62174562444272,
                    "totalAmount": 0.45993
                },
                {
                    "internalAccountName": "Admin SOL P2P",
                    "internalAccountIdentifier": "gedl6ckju5hg4jdj2yvcapajpxt4z17pcanvyqzzcltq",
                    "date": "2023-12-22",
                    "totalValue": 44.60821683407349,
                    "totalAmount": 0.45993
                },
                {
                    "internalAccountName": "Agoric P2P",
                    "internalAccountIdentifier": "agoric1r343yx754h82cjmeghjjekfz4v5decgh3z84ve",
                    "date": "2023-12-19",
                    "totalValue": 203416.18280402513,
                    "totalAmount": 1102681.192499
                },
                {
                    "internalAccountName": "Agoric P2P",
                    "internalAccountIdentifier": "agoric1r343yx754h82cjmeghjjekfz4v5decgh3z84ve",
                    "date": "2023-12-20",
                    "totalValue
[TRUNCATED]
```

**Sample response (200):**
```json
{
    "data": {
        "portfolio": {
            "dailyNetworth": [
                {
                    "date": "2024-06-20",
                    "totalValue": 317479165.8804863
                }
            ]
        }
    }
}
```

## Get Daily Networth Per Asset Class / Underlying Assets

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query DailyNetworthPerAssetClass($currency: Currency!, $startDate: Date!, $endDate: Date!, $assetClassNames: [String], $assetClassSymbols: [String], $limit : Int) {
  portfolio {  
    dailyNetworthPerAssetClass (currency: $currency, startDate: $startDate, endDate: $endDate, assetClassNames: $assetClassNames, assetClassSymbols: $assetClassSymbols, limit: $limit) {
        assetClassName
        assetClassSymbol
        date
        totalValue
        totalAmount
    }
  }
}
```

**Variables:**
```json
{
    "currency": "USD",
    "startDate": "2024-08-01",
    "endDate": "2024-08-03",
    "assetClassNames": ["Bitcoin", "Ethereum"],
    "assetClassSymbols": [],
    "limit": null
}
```

**Sample response (200):**
```json
{
    "data": {
        "portfolio": {
            "dailyNetworthPerAssetClass": [
                {
                    "assetClassName": "Ethereum",
                    "assetClassSymbol": "ETH",
                    "date": "2024-08-01",
                    "totalValue": 4307133.679878451,
                    "totalAmount": 1353.5517338458178
                },
                {
                    "assetClassName": "Ethereum",
                    "assetClassSymbol": "ETH",
                    "date": "2024-08-02",
                    "totalValue": 4151739.7267574626,
                    "totalAmount": 1353.5840235229061
                },
                {
                    "assetClassName": "Ethereum",
                    "assetClassSymbol": "ETH",
                    "date": "2024-08-03",
                    "totalValue": 3940995.0298762694,
                    "totalAmount": 1353.8707787801068
                },
                {
                    "assetClassName": "Geist ETH",
                    "assetClassSymbol": "gETH",
                    "date": "2024-08-01",
                    "totalValue": 13.320085200408101,
                    "totalAmount": 0.004181388493420134
                },
                {
                    "assetClassName": "Geist ETH",
                    "assetClassSymbol": "gETH",
                    "date": "2024-08-02",
                    "totalValue": 12.585645652338927,
                    "totalAmount": 0.004181388758617813
                },
                {
                    "assetClassName": "Geist ETH",
                    "assetClassSymbol": "gETH",
                    "date": "2024-08-03",
                    "totalValue": 12.198885051411436,
                    "totalAmount": 0.004181389050638317
                },
                {
                    "assetClassName": "Lido Staked Ether 2.0",
                    "assetClassSymbol": "stETH",
                    "date": "2024-08-01",
                    "totalValu
[TRUNCATED]
```

**Sample response (200):**
```json
{
    "data": {
        "portfolio": {
            "dailyNetworthPerAssetClass": [
                {
                    "assetClassName": "Ethereum",
                    "assetClassSymbol": "ETH",
                    "date": "2024-08-01",
                    "totalValue": 4307133.679878451,
                    "totalAmount": 1353.5517338458178
                },
                {
                    "assetClassName": "Ethereum",
                    "assetClassSymbol": "ETH",
                    "date": "2024-08-02",
                    "totalValue": 4151739.7267574626,
                    "totalAmount": 1353.5840235229061
                },
                {
                    "assetClassName": "Ethereum",
                    "assetClassSymbol": "ETH",
                    "date": "2024-08-03",
                    "totalValue": 3940995.0298762694,
                    "totalAmount": 1353.8707787801068
                }
            ]
        }
    }
}
```

## Get Daily Networth Per Internal Account

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query DailyNetworthPerInternalAccount($currency: Currency!, $startDate: Date!, $endDate: Date!) {
  portfolio {
    dailyNetworthPerInternalAccount(
      currency: $currency
      startDate: $startDate
      endDate: $endDate
    ) {
      internalAccountName
      internalAccountIdentifier
      date
      totalValue
      totalAmount
    }
  }
}
```

**Variables:**
```json
{
    "currency": "USD",
    "startDate": "2024-06-20",
    "endDate": "2024-06-28"
}
```

**Sample response (200):**
```json
{
    "data": {
        "portfolio": {
            "dailyNetworthPerInternalAccount": [
                {
                    "internalAccountName": "BTC Oracle",
                    "internalAccountIdentifier": "0x0fca2761538f4a28aa38e2cada1469f0",
                    "date": "2024-06-20",
                    "totalValue": -0.03451839644326209,
                    "totalAmount": -1
                },
                {
                    "internalAccountName": "BTC Oracle",
                    "internalAccountIdentifier": "0x0fca2761538f4a28aa38e2cada1469f0",
                    "date": "2024-06-21",
                    "totalValue": -0.030015452170235192,
                    "totalAmount": -1
                },
                {
                    "internalAccountName": "BTC Oracle",
                    "internalAccountIdentifier": "0x0fca2761538f4a28aa38e2cada1469f0",
                    "date": "2024-06-22",
                    "totalValue": -0.02530629659604822,
                    "totalAmount": -1
                },
                {
                    "internalAccountName": "BTC Oracle",
                    "internalAccountIdentifier": "0x0fca2761538f4a28aa38e2cada1469f0",
                    "date": "2024-06-23",
                    "totalValue": -0.024510160825590887,
                    "totalAmount": -1
                },
                {
                    "internalAccountName": "BTC Oracle",
                    "internalAccountIdentifier": "0x0fca2761538f4a28aa38e2cada1469f0",
                    "date": "2024-06-24",
                    "totalValue": -0.02597411654181659,
                    "totalAmount": -1
                },
                {
                    "internalAccountName": "BTC Oracle",
                    "internalAccountIdentifier": "0x0fca2761538f4a28aa38e2cada1469f0",
                    "date": "2024-06-25",
                    "totalValue": -0.03480650864437856,
                    "totalAmount": -1
                },
        
[TRUNCATED]
```

**Sample response (200):**
```json
{
    "data": {
        "portfolio": {
            "dailyNetworthPerInternalAccount": [
                {
                    "internalAccountName": "Dydx Chain Wallet",
                    "internalAccountIdentifier": "dydx16pj5gljqnqs0ajxakccfjhu05yczp9870tkh0z",
                    "date": "2024-06-20",
                    "totalValue": 53771.69908790571,
                    "totalAmount": 53299.08021555063
                },
                {
                    "internalAccountName": "Dydx Chain Wallet",
                    "internalAccountIdentifier": "dydx16pj5gljqnqs0ajxakccfjhu05yczp9870tkh0z",
                    "date": "2024-06-21",
                    "totalValue": 53867.20807981631,
                    "totalAmount": 53398.738597307216
                },
                {
                    "internalAccountName": "Dydx Chain Wallet",
                    "internalAccountIdentifier": "dydx16pj5gljqnqs0ajxakccfjhu05yczp9870tkh0z",
                    "date": "2024-06-22",
                    "totalValue": 53970.42423981065,
                    "totalAmount": 53534.74610433279
                },
                {
                    "internalAccountName": "Dydx Chain Wallet",
                    "internalAccountIdentifier": "dydx16pj5gljqnqs0ajxakccfjhu05yczp9870tkh0z",
                    "date": "2024-06-23",
                    "totalValue": 54005.95264130729,
                    "totalAmount": 53575.26434828454
                },
                {
                    "internalAccountName": "Dydx Chain Wallet",
                    "internalAccountIdentifier": "dydx16pj5gljqnqs0ajxakccfjhu05yczp9870tkh0z",
                    "date": "2024-06-24",
                    "totalValue": 23183.646873526195,
                    "totalAmount": 23159.680986355157
                },
                {
                    "internalAccountName": "Dydx Chain Wallet",
                    "internalAccountIdentifier": "dydx16pj5gljqnqs0ajxakccfjhu05yczp9870tkh0z",
      
[TRUNCATED]
```

## Get Daily Networth Per Balance

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query DailyNetworthPerBalanceName($currency: Currency!, $startDate: Date!, $endDate: Date!) {
  portfolio {
    dailyNetworthPerBalanceName(
      currency: $currency
      startDate: $startDate
      endDate: $endDate
    ) {
        state
        balanceName
        assetClassName
        date
        totalValue
        totalAmount
    }
  }
}
```

**Variables:**
```json
{
    "currency": "USD",
    "startDate": "2024-06-26",
    "endDate": "2024-06-28"
}
```
