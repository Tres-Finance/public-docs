# Tres API — Transaction — SubTransactions

Endpoints in the 'Transaction — SubTransactions' section of the public Tres API collection (16 requests).

## Get Sub Transactions by Internal Account Identifier

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTransactionsData(
    $limit: Int,
    $offset: Int,
    $timestamp_Gte: DateTime,
    $timestamp_Lte: DateTime,
    $platform: String,
    $belongsTo_Identifier_In: [String],
    $asset_Identifier: String) {
    subTransaction(
        limit: $limit,
        offset: $offset,
        timestamp_Gte: $timestamp_Gte,
        platform: $platform,
        timestamp_Lte: $timestamp_Lte,
        belongsTo_Identifier_In: $belongsTo_Identifier_In,
        asset_Identifier: $asset_Identifier
    ) {
        totalCount
        results {
            asset {
                symbol
            }
            type
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                success
            }
            timestamp
            belongsTo {
                id
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            originalSender {
                originalIdentifier
            }
            originalRecipient {
                originalIdentifier
            }
            amount
            balanceFactor
        }
    }
}
```

**Variables:**
```json
{
    "limit": 500,
    "offset": 0,
    "timestamp_Gte": "2021-01-01T00:00:00",
    "timestamp_Lte": "2025-10-20T23:59:59",
    "platform": "substrate_polkadot",
    "asset_Identifier": "native",
    "belongsTo_Identifier_In": ["1NZP4EFFsNzZkAEL8Fgnje2aNJyB8UcCUU65GmqyJYGfUFB"]
}
```

**Sample response (200):**
```json
{
    "data": {
        "subTransaction": {
            "totalCount": 1778,
            "results": [
                {
                    "platform": "ethereum",
                    "asset": {
                        "name": "Ethereum",
                        "identifier": "native",
                        "symbol": "ETH",
                        "assetClass": {
                            "id": "3",
                            "name": "Ethereum",
                            "symbol": "ETH"
                        }
                    },
                    "amount": 0.01928725,
                    "tx": {
                        "decodedFunctionName": "beaconWithdrawal",
                        "methodId": "beaconWithdrawal",
                        "blockNumber": 0,
                        "identifier": "withdrawal_1147233_1513",
                        "classification": {
                            "action": "claim consensus layer rewards",
                            "activity": "STAKING REWARDS"
                        }
                    },
                    "balanceFactor": 1,
                    "timestamp": "2025-01-22T23:59:59+00:00",
                    "belongsTo": {
                        "tags": [
                            "BITPANDA"
                        ],
                        "identifier": "0xb10edd6fa6067dba8d4326f1c8f0d1c791594f13",
                        "name": "ETH 1983"
                    },
                    "sender": {
                        "identifier": "0x96f076d26fa6ac33469f0eb839cc7bbf9d59ba31730b6af92ee0da2af747e8192d455d2b76a12086508b5f972b3524f1"
                    },
                    "recipient": {
                        "identifier": "0xb10edd6fa6067dba8d4326f1c8f0d1c791594f13"
                    },
                    "createdAt": "2025-02-21T17:47:02.737355+00:00",
                    "updatedAt": "2025-02-21T17:47:02.737360+00:00",
                    "deleted": false
                },
               
[TRUNCATED]
```

## Get Sub Transactions by Internal Account ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_In: [ID],  
    $balanceFactor: Float,
    $tag: [String]
    $tx_Identifier_In: [String]) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_In: $belongsTo_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
            type
        }
    }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "timestamp_Lt": "2025-04-20T17:25:25.805453+00:00",
    "timestamp_Gt": "2025-04-19T17:25:25.805453+00:00",
    "belongsTo_In": ["628066"]
}
```

## Get Sub Transactions by Internal Account ID and Asset

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier1(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_In: [ID],  
    $balanceFactor: Float,
    $tag: [String]
    $asset_In: [ID],
    $tx_Identifier_In: [String]) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_In: $belongsTo_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    asset_In: $asset_In
    ) {
        results {
            platform
            amount
            balanceFactor
            type
            asset {
                symbol
                identifier
            }
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
            }
            timestamp
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
        }
    }
}
```

**Variables:**
```json
{
    "limit": 100,
    "offset": 0,
    "timestamp_Lt": "2025-04-20T17:25:25.805453+00:00",
    "timestamp_Gt": "2025-04-13T17:25:25.805453+00:00",
    "belongsTo_In": ["628066"],
    "asset_In": ["ethereum_native"]
}
```

## Get Sub Transactions by Internal Account Identifier and Asset

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String]
    $asset_In: [ID],
    $tx_Identifier_In: [String]) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    asset_In: $asset_In
    ) {
        results {
            platform
            amount
            balanceFactor
            type
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
            }
            timestamp
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
        }
    }
}
```

**Variables:**
```json
{
    "limit": 100,
    "offset": 0,
    "timestamp_Lt": "2025-04-20T17:25:25.805453+00:00",
    "timestamp_Gt": "2025-04-01T17:25:25.805453+00:00",
    "belongsTo_Identifier_In": ["75NPzpxoh8sXGuSENFMREidq6FMzEx4g2AfcBEB6qjCV"],
    "asset_In": ["solana_native"]
}
```

**Sample response (200):**
```json
{
    "data": {
        "subTransaction": {
            "totalCount": 2,
            "results": [
                {
                    "amount": 8228177,
                    "balanceFactor": -1,
                    "id": "223273820",
                    "type": "TOKEN_TRANSFER",
                    "timestamp": "2023-01-04T21:07:11+00:00",
                    "belongsTo": {
                        "identifier": "0xd809d6d80bf33944f91acc6db85f7f50cf23e281"
                    },
                    "asset": {
                        "symbol": "MATIC"
                    },
                    "tx": {
                        "identifier": "0x19082884c7f7b3be4d4e2610864b8717ccc8abbf353c6df9a580bdbb66814911",
                        "blockNumber": 16336008,
                        "methodId": "0x6ab15071",
                        "classification": {
                            "action": "deposit into proof of stake",
                            "activity": "STAKING LOCKUP"
                        }
                    },
                    "recipient": {
                        "identifier": "0x5e3ef299fddf15eaa0432e6e66473ace8c13d908"
                    },
                    "sender": {
                        "identifier": "0xd809d6d80bf33944f91acc6db85f7f50cf23e281"
                    }
                },
                {
                    "amount": 8228177,
                    "balanceFactor": 1,
                    "id": "223273818",
                    "type": "TOKEN_TRANSFER",
                    "timestamp": "2022-12-12T20:40:23+00:00",
                    "belongsTo": {
                        "identifier": "0xd809d6d80bf33944f91acc6db85f7f50cf23e281"
                    },
                    "asset": {
                        "symbol": "MATIC"
                    },
                    "tx": {
                        "identifier": "0x50d1e23fc378d0e47a34bbbd3cf6a68a4b1e20d543e3e482be7e57ddfc108dac",
                        "blockNumber": 16171068,
   
[TRUNCATED]
```

## Get Sub Transactions by Method ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String],
    $tx_MethodId: String,
    $tx_Identifier_In: [String],
    $asset_Identifier: String) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    tx_MethodId: $tx_MethodId
    asset_Identifier: $asset_Identifier
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
        }
    }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "timestamp_Gt": "2024-01-20T17:25:25.805453+00:00",
    "balanceFactor": 1,
    "tx_MethodId": "withdrawPendingVestingTokens"
}
```

## Get Sub Transactions by Transaction Identifier

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $asset_Symbol_Icontains: String,
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String]
    $tx_Identifier_In: [String]) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    asset_Symbol_Icontains: $asset_Symbol_Icontains,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    ) {
        totalCount
        results {
            id
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
        }
    }
}
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "tx_Identifier_In": ["0x46bea5bc5a495f60bca33a493640f2b1b26f22ee0943bc1cc10b832b98d3af22"],
    "asset_Symbol_Icontains": "MATIC"
}
```

## Get Sub Transactions by Internal Account Name

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String],
    $belongsTo_Name_In: [String],
    $tx_Identifier_In: [String]) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    belongsTo_Name_In: $belongsTo_Name_In,
    tx_Identifier_In: $tx_Identifier_In 
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
        }
    }
}
```

**Variables:**
```json
{
    "limit": 2,
    "offset": 0,
    "timestamp_Gt": "2024-01-20T17:25:25.805453+00:00",
    "belongsTo_Name_In": ["Solana Wallet"]
}
```

## Get Sub Transactions without Cost Basis

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String],
    $belongsTo_Name_In: [String],
    $tx_Identifier_In: [String]) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    belongsTo_Name_In: $belongsTo_Name_In,
    tx_Identifier_In: $tx_Identifier_In 
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
        }
    }
}
```

**Variables:**
```json
{
    "limit": 2,
    "offset": 0,
    "timestamp_Gt": "2024-01-20T17:25:25.805453+00:00",
    "belongsTo_Name_In": ["Solana Wallet"]
}
```

## Get Sub Transactions by Asset Symbol

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $asset_Symbol_Icontains: String,
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String]
    $tx_Identifier_In: [String]) {
    subTransaction(
    asset_Symbol_Icontains: $asset_Symbol_Icontains,
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            balanceImpact
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
        }
    }
}
```

**Variables:**
```json
{
    "limit": 2,
    "offset": 0,
    "asset_Symbol_Icontains": "USDC"
}
```

## Get Sub Transactions by Platform

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $asset_Symbol_Icontains: String,
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String]
    $tx_Identifier_In: [String]) {
    subTransaction(
    asset_Symbol_Icontains: $asset_Symbol_Icontains,
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    ) {
        totalCount
        results {
            platform
            type
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
        }
    }
}
```

**Variables:**
```json
{
    "limit": 2,
    "offset": 0,
    "platform": "ethereum"
}
```

## Get Sub Transactions by Date

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactions(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String]
    $tx_Identifier_In: [String]) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
        }
    }
}
```

**Variables:**
```json
{
    "limit": 2,
    "offset": 0,
    "timestamp_Gt": "2024-06-20T17:25:25.805453+00:00"
}
```

**Sample response (200):**
```json
{
    "data": {
        "subTransaction": {
            "totalCount": 6566,
            "results": [
                {
                    "amount": 0.000014691867884389401,
                    "balanceFactor": 1,
                    "timestamp": "2023-07-06T02:28:08+00:00",
                    "sender": {
                        "identifier": "pinger.near"
                    },
                    "recipient": {
                        "identifier": "kiln.poolv1.near"
                    },
                    "tx": {
                        "classification": {
                            "action": "ping validator",
                            "activity": "OPERATIONS"
                        }
                    },
                    "asset": {
                        "symbol": "NEAR"
                    }
                },
                {
                    "amount": 0.00013103560885806512,
                    "balanceFactor": -1,
                    "timestamp": "2023-07-06T00:00:22+00:00",
                    "sender": {
                        "identifier": "kiln.poolv1.near"
                    },
                    "recipient": {
                        "identifier": "kiln.poolv1.near"
                    },
                    "tx": {
                        "classification": {
                            "action": "ping validator",
                            "activity": "OPERATIONS"
                        }
                    },
                    "asset": {
                        "symbol": "NEAR"
                    }
                },
                {
                    "amount": 0.00011800782103598911,
                    "balanceFactor": 1,
                    "timestamp": "2023-07-06T00:00:22+00:00",
                    "sender": {
                        "identifier": "kiln_validator.near"
                    },
                    "recipient": {
                        "identifier": "kiln.poolv1.near"
                    },
          
[TRUNCATED]
```

## Get Sub Transactions by Creation Date

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactions(
    $limit: Int, 
    $offset: Int, 
    $createdAt_Gt: DateTime,  
    $createdAt_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String]
    $tx_Identifier_In: [String]) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    createdAt_Gt: $createdAt_Gt, 
    platform: $platform, 
    createdAt_Lt: $createdAt_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
        }
    }
}
```

**Variables:**
```json
{
    "limit": 2,
    "offset": 0,
    "createdAt_Gt": "2024-06-20T17:25:25.805453+00:00"
}
```

## Get Sub Transactions by Update Date

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactions(
    $limit: Int, 
    $offset: Int, 
    $updatedAt_Gt: DateTime,  
    $updatedAt_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String]
    $tx_Identifier_In: [String]) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    updatedAt_Gt: $updatedAt_Gt, 
    platform: $platform, 
    updatedAt_Lt: $updatedAt_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
        }
    }
}
```

**Variables:**
```json
{
    "limit": 2,
    "offset": 0,
    "updatedAt_Gt": "2024-06-20T17:25:25.805453+00:00"
}
```

## Get Sub Transactions by Internal Account Identifier and Sender Identifier

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetSubTransactionByInternalAccountIdentifier(
    $limit: Int, 
    $offset: Int, 
    $timestamp_Gt: DateTime,  
    $timestamp_Lt: DateTime, 
    $platform: String, 
    $tx_Id: String
    $tx_DecodedFunctionName: String ,
    $tx_DecodedFunctionNameIn: [String],
    $belongsTo_Identifier_In: [String],  
    $balanceFactor: Float,
    $tag: [String],
    $sender_Identifier_In: [String],
    $tx_Identifier_In: [String],
    $tx_BlockNumber_Lte: Int,
    $tx_BlockNumber_Gte: Int
    ) {
    subTransaction(
    balanceFactor: $balanceFactor,    
    limit: $limit, 
    offset: $offset, 
    tx_Id: $tx_Id,
    timestamp_Gt: $timestamp_Gt, 
    platform: $platform, 
    timestamp_Lt: $timestamp_Lt, 
    tx_DecodedFunctionName_In: $tx_DecodedFunctionNameIn,
    belongsTo_Identifier_In: $belongsTo_Identifier_In, 
    tx_DecodedFunctionName: $tx_DecodedFunctionName,
    tags_Overlap: $tag,
    tx_Identifier_In: $tx_Identifier_In 
    sender_Identifier_In: $sender_Identifier_In
    tx_BlockNumber_Lte: $tx_BlockNumber_Lte
    tx_BlockNumber_Gte: $tx_BlockNumber_Gte
    ) {
        totalCount
        results {
            platform
            asset {
                name
                identifier
                symbol
                assetClass {
                    id
                    name
                    symbol
                }
            }
            amount
            tx {
                decodedFunctionName
                methodId
                blockNumber
                identifier
                classification {
                    action
                    activity
                }
            }
            balanceFactor
            timestamp
            belongsTo {
                tags
                identifier
                name
            }
            sender {
                identifier
            }
            recipient {
                identifier
            }
            createdAt
            updatedAt
            deleted
        
[TRUNCATED]
```

**Variables:**
```json
{
    "limit": 20,
    "offset": 0,
    "tx_BlockNumber_Lte":99999999,
    "tx_BlockNumber_Gte":0,
    "belongsTo_Identifier_In": ["0xa0e3b43036050caec738e32aba3247927a5fe5c6"],
    "sender_Identifier_In": ["0x5e3ef299fddf15eaa0432e6e66473ace8c13d908"]
}
```

## Get Sub Transactions Cost Basis by ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query SubTxQuery($id: Float, $currency: String) {
  subTransaction(id: $id, currency: $currency) {
    results {
      fifoCostBasisQueue
      financialAttrs {
        saveFullInventory
        nonTaxableState
      }
    }
  }
}
```

**Variables:**
```json
{
  "id": 4048133089,
  "currency": "usd"
}
```

## Get Sub Transactions Aggregation

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query SubTransactionAggregation(
    $timestamp_Gt: DateTime
    $aggregations: [AggregationInput]
) {
    subTransaction(
        timestamp_Gt: $timestamp_Gt
        aggregations: $aggregations
    ) {
        aggregations {
            alias
            field
            function
            value
        }
    }
}
```

**Variables:**
```json
{
    "aggregations": [
        {"field": "amount", "function": "MIN", "alias": "totalAmount"}
    ],
    "groupBy": ["year"],
    "timestamp_Gt": "2025-12-19T00"
    
}
```
