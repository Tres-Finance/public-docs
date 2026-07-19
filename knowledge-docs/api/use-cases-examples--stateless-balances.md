# Tres API — Use cases / Examples — Stateless Balances

Endpoints in the 'Use cases / Examples — Stateless Balances' section of the public Tres API collection (6 requests).

## Stateless Token Balance [Near]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $assetIdentifier: String!) {
  getStatelessTokenBalance(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, assetIdentifier: $assetIdentifier) {
      results {
        amount
        originalAmount
        walletIdentifier
        state
      }
  }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["cryptium.near"],
    "platform": "NEAR",
    "assetIdentifier": "native",
    "timestamp": "2023-01-31T00:00:00"
}
```

## Stateless Token Balance [Solana]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessTokenBalance($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $assetIdentifier: String!) {
  getStatelessTokenBalance (walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, assetIdentifier: $assetIdentifier) {
        amount
        originalAmount
        walletIdentifier
        state
    }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["5MCJvLEPNtMDbThMeMt5dbBKqQMdBpE745Ve1jR8iMxx"],
    "platform": "SOLANA",
    "assetIdentifier": "native",
    "timestamp": "2022-05-14T00:00:00"
}
```

## Stateless Token Balance [Ethereum]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessTokenBalance($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $assetIdentifier: String!) {
  getStatelessTokenBalance (walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, assetIdentifier: $assetIdentifier) {
        amount
        originalAmount
        walletIdentifier
        state
    }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["0x5D8D732a1B0D9c024E9cD6EcA5B8c4a4ad8840d4"],
    "platform": "MOONBEAM",
    "assetIdentifier": "native"
}
```

## Stateless Token Balance [Cosmos]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessTokenBalance($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $assetIdentifier: String!) {
  getStatelessTokenBalance (walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, assetIdentifier: $assetIdentifier) {
        amount
        originalAmount
        walletIdentifier
        state
    }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["cosmos1lvkuedmc4vtz28zxeumk0d3st92z8t2ccksmqu", "cosmos1g6uycr7d3ky6t5f5sjh2nfzd26p49hskyc4a2h"],
    "platform": "COSMOS",
    "timestamp": "2023-04-01T00:00:00",
    "assetIdentifier": "native"
}
```

## Stateless Token Balance [Cardano]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessTokenBalance($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $assetIdentifier: String!) {
  getStatelessTokenBalance (walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, assetIdentifier: $assetIdentifier) {
        amount
        originalAmount
        walletIdentifier
        state
    }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["addr1z8jd97ct35n4s5ss8lt4sq0zclw0dmf7yak8fj46m0jm3dswtf6nj8t35qph4n6m04gawl49yvsxytfjpjpcfhehpcvqwwrrlu"],
    "platform": "CARDANO",
    "assetIdentifier": "native"
}
```

## Stateless Token Balance [Polkadot]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessTokenBalance($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $assetIdentifier: String!) {
  getStatelessTokenBalance (walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, assetIdentifier: $assetIdentifier) {
        amount
        originalAmount
        walletIdentifier
        state
    }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["addr1z8jd97ct35n4s5ss8lt4sq0zclw0dmf7yak8fj46m0jm3dswtf6nj8t35qph4n6m04gawl49yvsxytfjpjpcfhehpcvqwwrrlu"],
    "platform": "CARDANO",
    "assetIdentifier": "native"
}
```
