# Tres API — Use cases / Examples — Stateless Positions

Endpoints in the 'Use cases / Examples — Stateless Positions' section of the public Tres API collection (20 requests).

## Stateless DeFi / Staking Positions [Near]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["chorusone.near"],
    "platform": "NEAR",
    "timestamp": "2023-05-31T18:37:00"
}
```

## Stateless DeFi / Staking Positions [Celo]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0xdadbd6cfb29b054adc9c4c2ef0f21f0bbdb44871"],
    "platform": "CELO"
}
```

## Stateless DeFi / Staking Positions [eth-harbour]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0xce44359c9fffd743f721e54e3b605ce333b38fa6"],
    "platform": "ETHEREUM",
    "application": "eth-harbour",
    "timestamp": "2023-07-31T00:00:00"
}
```

## Stateless DeFi / Staking Positions [eth-staking]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0x2324b024aac834cbe050718848ac56f607587dc8"],
    "platform": "ETHEREUM",
    "application": "ethereum-staking"
}
```

## Stateless DeFi / Staking Positions [Ethereum2]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0xa86ab2d8c2d43ae5f83573f924b3b8b4e0f8594f5823e0245fa150155840d91265c60e549a34492363132e8eb96b5519"],
    "platform": "ETHEREUM2"
}
```

## Stateless DeFi / Staking Positions [Polkadot]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["1155dDdp1X4F3rh35hAMoK8r4iDVdzprtRpVrScP35YPC2b", "124YFXA3XoRs9Epcx3aRUSk3EKYaznocqMWfrMKtGjx8TJ2W", "126brtAJ2VMLcDNZHNQ6cfaUSdgZikP7EbddVxoQzj8hEovX", "12ECDEb18Wiy4MoLn3NTM5zhJfDfpS4mLNvjHpcEr8ogGrMZ", "12GTt3pfM3SjTU6UL6dQ3SMgMSvdw94PnRoF6osU6hPvxbUZ", "12HFymxpDmi4XXPHaEMp74CNpRhkqwG5qxnrgikkhon1XMrj", "12WmM98h4Ar6y7ZyyMKPXwSyuP5GSZvXTbEkDXm1tirbZFW4", "12Yz9HPcF66pAGpwEW5cyFZ59TFeXFGVnkuxTphC3Lrap29z"],
    "platform": "OLD_POLKADOT"
}
```

## Stateless DeFi / Staking Positions [Flow]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0x02aef436ae96cec3", "0xf5224874d6729085"],
    "platform": "FLOW"
}
```

## Stateless DeFi / Staking Positions [Sui]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0xa62197444b71ba63354ab65518c692ad4777179285a7150e4dc62f7b34415e1c"],
    "platform": "SUI"
}
```

## Stateless DeFi / Staking Positions [Evmos]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["evmos1h62qm8qcctvcdd8t3jwm9jcc9cwleqjg77uwze"],
    "platform": "EVMOS"
}
```

## Stateless DeFi / Staking Positions [Cardano]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["pool1dqzprrl8305mlysnh85znqpe22lg0q2d9zest7jjhugajuf46kv"],
    "platform": "CARDANO"
}
```

## Stateless DeFi / Staking Positions [Livepeer]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0xda43d85b8d419a9c51bbf0089c9bd5169c23f2f9"],
    "platform": "ARBITRUM",
    "application": "livepeer"
}
```

## Stateless DeFi / Staking Positions [Polygon]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0xbd6528e430c0be4203fb80d3a80828a76711e669"],
    "platform": "ETHEREUM",
    "application": "polygon-staking",
    "timestamp": "2023-05-15T18:37:00"
}
```

## Stateless DeFi / Staking Positions [Aptos]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0xee49776eff9fd395eb90d601449542080645e63704f518b31c6f72b6a95d7868"],
    "platform": "APTOS"
}
```

## Stateless DeFi / Staking Positions [Solana]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["8mHUDJjzPo2AwJp8SHKmG9rk9ftWTp7UysqYz36cMpJe"],
    "platform": "SOLANA",
    "timestamp": "2023-05-15T18:37:00"
}
```

## Stateless DeFi / Staking Positions [Flow]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0xe59d0db8816bed59"],
    "platform": "FLOW"
}
```

## Stateless DeFi / Staking Positions [Cosmos]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["cosmos15urq2dtp9qce4fyc85m6upwm9xul3049um7trd"],
    "platform": "COSMOS",
    "timestamp": "2023-04-01T00:00:00"
}
```

## Stateless DeFi / Staking Positions [Injective]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["inj1zaw6duj85ntnue9jmyxte2mlahl3ysw57yrcpx"],
    "platform": "INJECTIVE",
    "timestamp": "2023-04-01T00:00:00"
}
```

## Stateless DeFi / Staking Positions [dYdX]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    extras {
        validatorData
    }
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["dydx12xvq20j56kz6vzhwphxm97mupga40fmvj54306"],
    "platform": "DYDX",
    "timestamp": "2023-12-20T00:13:00+00:00"
}
```

## Stateless DeFi / Staking Positions [Curve-Stablepool]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0x7257555e96417cbc663e8bfd09bf8aebaeb53483"],
    "platform": "ETHEREUM",
    "application": "curve-stablepool"
}
```

## Stateless DeFi / Staking Positions [Tron]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessWalletPositions($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application) {
    walletIdentifier
    displayName
    blockNumber
    platform
    positionType
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
    }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["TBfJhtGydsNkGt3VVN1mwcXLec9RExMRav"],
    "platform": "TRON",
    "application": "tron"
}
```
