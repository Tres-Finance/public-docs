# Tres API — Internal Account / Wallets

Endpoints in the 'Internal Account / Wallets' section of the public Tres API collection (14 requests).

## Get Internal accounts by Identifier

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetInternalAccountsInit($offset: Int, $limit: Int, $currency: String, $balanceType: [String], $id_In: [String], $platform_In: [String], $assetClass_In: [String], $tags_Overlap: [String], $isSynced: Boolean, $identifier_In: [String]) {
  internalAccount(
    offset: $offset
    limit: $limit
    currency: $currency
    balanceType: $balanceType
    id_In: $id_In
    platform_In: $platform_In
    assetClass_In: $assetClass_In
    tags_Overlap: $tags_Overlap
    isSynced: $isSynced
    orderByFiatValue: true
    identifier_In: $identifier_In
  ) {
    results {
      id
      identifier
      createdAt
      updatedAt
      platforms
      name
      description
      parentPlatform
      reconciliationMissing
      totalFiatValue
      balancesCount
      tags
      status
    }
    totalCount
  }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "limit": 20,
  "offset": 0,
  "id_In": [],
  "platform_In": [],
  "assetClass_In": [],
  "tags_Overlap": [],
  "isSynced": true,
  "identifier_In": ["0x12"]
}
```

## Get Internal accounts by Statuses

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query InternalAccount($status_In: [String]!) {
    internalAccount(status_In: $status_In) {
        totalCount
    }
}
```

**Variables:**
```json
{
  "status_In": ["deleting"]
}
```

## Get Internal Account Full List and Status

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAccountById($limit: Int, $offset: Int, $tags_Overlap: [String], $isSynced: Boolean, $id_In: [String], $identifier_In: [String]) {
  internalAccount(
    limit: $limit
    offset: $offset
    tags_Overlap: $tags_Overlap
    isSynced: $isSynced
    id_In: $id_In
    identifier_In: $identifier_In
  ) {
    totalCount
    results {
      name
      identifier
      tags
      parentPlatform
      createdAt
      totalFiatValue

    }
  }
}
```

**Variables:**
```json
{
    "limit": 40,
    "identifier_In": ["75NPzpxoh8sXGuSENFMREidq6FMzEx4g2AfcBEB6qjCV"]
}
```

## Get Internal Accounts by Asset Class

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAccountById($limit: Int, $offset: Int, $tags_Overlap: [String], $isSynced: Boolean, $id_In: [String]) {
  internalAccount(
    limit: $limit
    offset: $offset
    tags_Overlap: $tags_Overlap
    isSynced: $isSynced
    id_In: $id_In
  ) {
    totalCount
    results {
      name
      identifier
      tags
    }
  }
}
```

**Variables:**
```json
{
    "limit": 40
}
```

## Create / Update Batch Internal Accounts

`POST {{backend}}/graphql`

<p>Create a batch of Internal Accounts / Wallets:</p>
<ul>
<li>In case of EVM network like Polygon, Arbitrum, Binance Smart Chain, use "ethereum" as ethereum.</li>
<li>To add off chain wallets and exchanges - contract TRES support team.</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateBatchInternalAccount ($internalAccounts: [InternalAccountInput]){
    updateBatchInternalAccounts(
        internalAccounts: $internalAccounts
    ) {
    internalAccounts {
            name
            identifier
            parentPlatform
            id
        }
        validationResults {
            validationResult {
                issueType
                errorMessage
            }
        }
    }
    
}
```

**Variables:**
```json
{
    "internalAccounts":[
        {
            "parentPlatform":"SEI",
            "identifier":"0x1887FA9EdADeaB7562B01CC3F4FA246AcE2c3Cdd",
            "name":"Test",
            "tags": ["A", "B"]
        }
    ]
}
```

**Sample response (200):**
```json
{
    "data": {
        "updateBatchInternalAccounts": {
            "internalAccounts": [
                {
                    "name": "Ton Wallet",
                    "identifier": "uqbcps6zovog6kbkkvvlufgoen5s56ewbrukxrbcdhsjnfuc",
                    "parentPlatform": "ton"
                },
                {
                    "name": "Ethereum Walelt",
                    "identifier": "0x53b55b4b540aed4b2b10575d83dda28bbc170194",
                    "parentPlatform": "ethereum"
                },
                {
                    "name": "Celestia Wallet",
                    "identifier": "celestia1lzg8m9f976gzcdvx3tcpcm5wkcefwn3nu3nm0l",
                    "parentPlatform": "celestia"
                },
                {
                    "name": "Ethereum Wallet 2",
                    "identifier": "0xffee087852cb4898e6c3532e776e68bc68b1143b",
                    "parentPlatform": "ethereum"
                }
            ]
        }
    }
}
```

## Create / Update Batch Internal Accounts (Exchange / Offchain)

`POST {{backend}}/graphql`

<p>Create a batch of Internal Accounts / Wallets:</p>
<ul>
<li>In case of EVM network like Polygon, Arbitrum, Binance Smart Chain, use "ethereum" as ethereum.</li>
<li>To add off chain wallets and exchanges - contract TRES support team.</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateBatchInternalAccount ($internalAccounts: [InternalAccountInput]){
    updateBatchInternalAccounts(
        internalAccounts: $internalAccounts
    ) {
    internalAccounts {
            name
            identifier
            parentPlatform
            id
            
        }           
    }
}
```

**Variables:**
```json
{
  "internalAccounts": [{"identifier":"coinbase-1", "name": "Coinbase #1", "parentPlatform": "COINBASE", "platformKeys":	"{\"api_key\":\"api_key\", \"secret_key\":\"secret_key\"}"}
]
}
```

## Update Internal Account Name / Description

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateWallet($identifier: String!, $parentPlatform: ParentPlatform!, $description: String!, $name: String!) {
  updateInternalAccount(
    identifier: $identifier
    parentPlatform: $parentPlatform
    description: $description
    name: $name
  ) {
    internalAccount {
      identifier
      id
      name
    }

  }
}
```

**Variables:**
```json
{
  "description": "",
  "name": "asd",
  "identifier": "0xd25a22aa81265c01b91bdcda78abef77a13abab2",
  "parentPlatform": "ETHEREUM"
}
```

## Update Internal Account Status

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateInternalAccountsStatuses($internalAccounts: [InternalAccountStatusUpdateInput!]!) {
  updateInternalAccountsStatuses(
    internalAccounts: $internalAccounts
  ) {
    errors
  }
}
```

**Variables:**
```json
{
    "internalAccounts": [
{ "id": 56061, "status": "DISABLED" },
{ "id": 66506, "status": "DISABLED" },
{ "id": 50348, "status": "DISABLED" }
            ]

}
```

## Get Internal Account By ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetWalletById($id: Float!) {
  internalAccount(id: $id) {
    results {
      id
      parentPlatform
      identifier
      name
      description
      externalId
      tags
      createdAt
      updatedAt
      status
      displayName
      platforms
      totalFiatValue
      reconciliationMissing
      balancesCount
      isExchange
      networthPerPlatform {
        networth
        platform
        __typename
      }
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
  "id": 714128
}
```

## Set Internal Account Tags

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation(
    $tags: [String]!,
    $parentPlatform: String!,
    $identifier: String!,
) {
  setInternalAccountTags(
      parentPlatform: $parentPlatform,
      identifier: $identifier,
      tags: $tags
    ) {
    internalAccount {
      identifier
      tags
    }
  }
}
```

**Variables:**
```json
{
    "parentPlatform": "ethereum",
    "identifier": "0xe7dae0ced7a64d50136d466945257b600e718aca",
    "tags": ["12", "23"]
}
```

## Delete Internal Account

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation(
    $identifier: String!
    $parentPlatform: ParentPlatform!
    $deleteInternalAccount: Boolean!
) {
  deleteInternalAccount(
        deleteInternalAccount: $deleteInternalAccount
        identifier: $identifier
        parentPlatform: $parentPlatform
    ) {
      errors
  }
}
```

**Variables:**
```json
{
    "identifier": "0xa2e1685f62b2a1a996a2a1ba10ac6836c2b72174cab1bd1c6907454e6365fb70",
    "parentPlatform": "ETHEREUM",
    "deleteInternalAccount": true
}
```

## Clean Internal Account

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation(
    $identifier: String!
    $parentPlatform: ParentPlatform!
    $deleteInternalAccount: Boolean!
) {
  deleteInternalAccount(
        deleteInternalAccount: $deleteInternalAccount
        identifier: $identifier
        parentPlatform: $parentPlatform
    ) {
      errors
  }
}
```

**Variables:**
```json
{
    "identifier": "kava1djqecw6nn5tydxq0shan7srv8j65clsfnnpvns",
    "parentPlatform": "KAVA",
    "deleteInternalAccount": false
}
```

## Get Internal accounts

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetInternalAccountsInit($offset: Int, $limit: Int, $currency: String, $balanceType: [String], $id_In: [String], $platform_In: [String], $assetClass_In: [String], $tags_Overlap: [String], $isSynced: Boolean) {
  internalAccount(
    offset: $offset
    limit: $limit
    currency: $currency
    balanceType: $balanceType
    id_In: $id_In
    platform_In: $platform_In
    assetClass_In: $assetClass_In
    tags_Overlap: $tags_Overlap
    isSynced: $isSynced
    orderByFiatValue: true
  ) {
    results {
      id
      identifier
      createdAt
      updatedAt
      platforms
      name
      description
      parentPlatform
      reconciliationMissing
      totalFiatValue
      balancesCount
      tags
      status
    }
    totalCount
  }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "limit": 20,
  "offset": 0,
  "id_In": [],
  "platform_In": [],
  "assetClass_In": [],
  "tags_Overlap": [],
  "isSynced": true
}
```

**Sample response (200):**
```json
{
    "data": {
        "internalAccount": {
            "results": [
                {
                    "id": "536089",
                    "identifier": "0xecdd548c83457ab43caf7867e2bef91ef783025db9659afd89794ec1220acf29",
                    "createdAt": "2024-06-26T11:41:48.695417+00:00",
                    "updatedAt": "2024-08-07T05:13:24.857125+00:00",
                    "platforms": [
                        "substrate_polkadot"
                    ],
                    "name": "16Ma3suDhT8TkTWffpPaS8sMFn2K6rEqddVJY4QCCUSj2J5J",
                    "description": "",
                    "parentPlatform": "substrate",
                    "reconciliationMissing": 1,
                    "totalFiatValue": 1848.0885750277787,
                    "balancesCount": 2,
                    "tags": [],
                    "status": "READY"
                }
            ],
            "totalCount": 1
        }
    }
}
```

## Get Internal accounts with Archived Fiat Value

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetInternalAccountsInit($offset: Int, $limit: Int, $currency: String, $balanceType: [String], $id_In: [String], $platform_In: [String], $assetClass_In: [String], $tags_Overlap: [String], $isSynced: Boolean, $groupId: UUID) {
  internalAccount(
    offset: $offset
    limit: $limit
    currency: $currency
    balanceType: $balanceType
    id_In: $id_In
    platform_In: $platform_In
    assetClass_In: $assetClass_In
    tags_Overlap: $tags_Overlap
    isSynced: $isSynced
    orderByFiatValue: true
    groupId: $groupId

  ) {
    results {
      id
      identifier
      createdAt
      updatedAt
      platforms
      name
      description
      parentPlatform
      reconciliationMissing
      totalFiatValue
      balancesCount
      tags
      status
    }
    totalCount
  }
}
```

**Variables:**
```json
{
  "currency": "usd",
  "limit": 20,
  "offset": 0,
  "platform_In": [],
  "assetClass_In": [],
  "tags_Overlap": [],
  "isSynced": true,
  "groupId": "cd15751a-d651-489a-ba27-fd8ff1dd0176"
}
```

**Sample response (200):**
```json
{
    "data": {
        "internalAccount": {
            "results": [
                {
                    "id": "536089",
                    "identifier": "0xecdd548c83457ab43caf7867e2bef91ef783025db9659afd89794ec1220acf29",
                    "createdAt": "2024-06-26T11:41:48.695417+00:00",
                    "updatedAt": "2024-08-07T05:13:24.857125+00:00",
                    "platforms": [
                        "substrate_polkadot"
                    ],
                    "name": "16Ma3suDhT8TkTWffpPaS8sMFn2K6rEqddVJY4QCCUSj2J5J",
                    "description": "",
                    "parentPlatform": "substrate",
                    "reconciliationMissing": 1,
                    "totalFiatValue": 1848.0885750277787,
                    "balancesCount": 2,
                    "tags": [],
                    "status": "READY"
                }
            ],
            "totalCount": 1
        }
    }
}
```
