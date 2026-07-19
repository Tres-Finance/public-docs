# Tres API — Asset Balances — Stateless

Endpoints in the 'Asset Balances — Stateless' section of the public Tres API collection (3 requests).

## Stateless DeFi / Staking Positions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $application: String, $blockNumber: Int) {
  getStatelessWalletsPositions(walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, application: $application, blockNumber: $blockNumber) {      
    walletIdentifier
    displayName
    blockNumber
    fiatValue
    platform
    positionType
    extras {
        validatorAddress
        contracts {
            address
            type
        }
    }
    children {
        amount
        originalAmount
        walletIdentifier
        assetIdentifier
        state
        symbol
        fiatValue
    }
  }
}
```

**Variables:**
```json
{"walletIdentifiers":["TNPdqto8HiuMzoG7Vv9wyyYhWzCojLeHAF"],"platform":"TRON","application":"tron",
"timestamp": "2024-05-16T00"}
```

**Sample response (200):**
```json
{
    "data": {
        "getStatelessWalletsPositions": [
            {
                "walletIdentifier": "cosmos13nvnv6q8d3yg7tjeahjzljkqu0y27s8yqd2guk",
                "displayName": "Cosmos - Staking",
                "blockHeight": null,
                "platform": "COSMOS",
                "positionType": "STAKING",
                "children": [
                    {
                        "amount": "2.0",
                        "originalAmount": "2000000",
                        "walletIdentifier": "cosmos13nvnv6q8d3yg7tjeahjzljkqu0y27s8yqd2guk",
                        "assetIdentifier": "native",
                        "state": "LOCKED",
                        "symbol": "Atom"
                    },
                    {
                        "amount": "5886.034823",
                        "originalAmount": "5886034823",
                        "walletIdentifier": "cosmos13nvnv6q8d3yg7tjeahjzljkqu0y27s8yqd2guk",
                        "assetIdentifier": "native",
                        "state": "CLAIMABLE",
                        "symbol": "Atom"
                    }
                ]
            },
            {
                "walletIdentifier": "cosmos13nvnv6q8d3yg7tjeahjzljkqu0y27s8yqd2guk",
                "displayName": "Cosmos - Under Delegation",
                "blockHeight": 13482774,
                "platform": "COSMOS",
                "positionType": "DELEGATED_TO_ACCOUNT",
                "children": [
                    {
                        "amount": "576409.979213",
                        "originalAmount": "576409979213",
                        "walletIdentifier": "cosmos13nvnv6q8d3yg7tjeahjzljkqu0y27s8yqd2guk",
                        "assetIdentifier": "native",
                        "state": "UNDER_DELEGATION",
                        "symbol": "Atom"
                    }
                ]
            },
            {
                "walletIdentifier": "cosmos1c4k24jzduc365kywrsvf5ujz4ya6mwymy8vq4q",
           
[TRUNCATED]
```

**Sample response (200):**
```json
{
    "data": {
        "getStatelessWalletsPositions": [
            {
                "walletIdentifier": "0xce44359c9fffd743f721e54e3b605ce333b38fa6",
                "displayName": "ETH Harbour Liquid Staking",
                "blockHeight": null,
                "platform": "ETHEREUM",
                "positionType": "STAKING",
                "children": [
                    {
                        "amount": "2004.0",
                        "originalAmount": "2004000000000000000000",
                        "walletIdentifier": "0xce44359c9fffd743f721e54e3b605ce333b38fa6",
                        "assetIdentifier": "native",
                        "state": "LOCKED",
                        "symbol": "ETH"
                    },
                    {
                        "amount": "23.717244739650972",
                        "originalAmount": "23717244739650974988",
                        "walletIdentifier": "0xce44359c9fffd743f721e54e3b605ce333b38fa6",
                        "assetIdentifier": "0xCBE26dbC91B05C160050167107154780F36CeAAB",
                        "state": "CLAIMABLE",
                        "symbol": "rETH-h"
                    }
                ]
            }
        ]
    }
}
```

## Stateless Token Balance

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessTokenBalance($walletIdentifiers: [String]!, $platform: Platform!, $timestamp: DateTime, $assetIdentifier: String!, $includeSubAccounts: Boolean) {
  getStatelessTokenBalance (walletIdentifiers: $walletIdentifiers, platform: $platform, timestamp: $timestamp, assetIdentifier: $assetIdentifier, includeSubAccounts: $includeSubAccounts) {
        amount
        originalAmount
        walletIdentifier
        state
        errorCode
        blockNumber
        fiatValue
        blockTimestamp
    }
}
```

**Variables:**
```json
{
    "walletIdentifiers": ["TKNviXKbnZPANFnZBHGCen7U7xSxwjM2Xn"],
    "platform": "TRON",
    "assetIdentifier": "native",
    "includeSubAccounts": false,
    "timestamp":"2025-12-29T23:59:59"
}
```

**Sample response (200):**
```json
{
    "data": {
        "getStatelessTokenBalance": [
            {
                "amount": "1.0",
                "originalAmount": "1000000000",
                "walletIdentifier": "5MCJvLEPNtMDbThMeMt5dbBKqQMdBpE745Ve1jR8iMxx",
                "state": "WALLET"
            }
        ]
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "getStatelessTokenBalance": [
            {
                "amount": "44000000.0",
                "originalAmount": "44000000000000",
                "walletIdentifier": "addr1z8jd97ct35n4s5ss8lt4sq0zclw0dmf7yak8fj46m0jm3dswtf6nj8t35qph4n6m04gawl49yvsxytfjpjpcfhehpcvqwwrrlu",
                "state": "WALLET"
            }
        ]
    }
}
```

## Supported Stateless Balances & Positions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query StatelessSupportedAPI {
  getSupportedStatelessApi {
        applications {
            name
            platforms
        }
        balances
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "getSupportedStatelessApi": {
            "applications": [
                {
                    "name": "band",
                    "platforms": [
                        "BAND"
                    ]
                },
                {
                    "name": "emoney",
                    "platforms": [
                        "EMONEY"
                    ]
                },
                {
                    "name": "akash",
                    "platforms": [
                        "AKASH"
                    ]
                },
                {
                    "name": "secret",
                    "platforms": [
                        "SECRET"
                    ]
                },
                {
                    "name": "sentinel",
                    "platforms": [
                        "SENTINEL"
                    ]
                },
                {
                    "name": "kava",
                    "platforms": [
                        "KAVA"
                    ]
                },
                {
                    "name": "persistence",
                    "platforms": [
                        "PERSISTENCE"
                    ]
                },
                {
                    "name": "osmosis",
                    "platforms": [
                        "OSMOSIS"
                    ]
                },
                {
                    "name": "provenance",
                    "platforms": [
                        "PROVENANCE"
                    ]
                },
                {
                    "name": "injective",
                    "platforms": [
                        "INJECTIVE"
                    ]
                },
                {
                    "name": "juno",
                    "platforms": [
                        "JUNO"
                    ]
                },
                {
                    "name": "gravity",
                    "platfor
[TRUNCATED]
```
