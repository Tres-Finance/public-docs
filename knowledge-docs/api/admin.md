# Tres API — Admin

Endpoints in the 'Admin' section of the public Tres API collection (15 requests).

## Get Locked Period History

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query LockedPeriod {
    lockedPeriod {
        totalCount
        results {
            updatedAt
            lockDate
            note
            isCurrentLock
            lockedBy
        }
    }
}
```

## Create Locked Period

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateLockedPeriod($lockDate: DateTime!, $note: String) {
    createLockedPeriod(lockDate: $lockDate, note: $note) {
        success
    }
}
```

**Variables:**
```json
{
  "lockDate": "2025-03-02T00:00:00.009000+00:00",
  "note": "nlknvc"
}
```

## Update Locked Period

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateLockedPeriod($lockedPeriodId: Int!, $note: String!) {
    updateLockedPeriod(lockedPeriodId: $lockedPeriodId, note: $note) {
        success
    }
}
```

**Variables:**
```json
{
  "lockedPeriodId": 13,
  "note": "khgdjh"
}
```

## Delete Locked Period

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteLockedPeriod($lockedPeriodId: Int!) {
    deleteLockedPeriod(lockedPeriodId: $lockedPeriodId) {
        success
    }
}
```

**Variables:**
```json
{
  "lockedPeriodId": 6
}
```

## Invite Users

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation InviteUser($emails: [String]!, $userType: UserType, $connectionId: Auth0ConnectionId) {
  inviteUser(emails: $emails, userType: $userType, connectionId: $connectionId) {
    success
  }
}
```

**Variables:**
```json
{
    "emails": [
        "user@org.com"
    ],
    "userType": "ADMIN"
}
```

## Get Users List

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetUsersList {
  admin {
    orgName
    users {
      userId
      email
      userType
      name
      picture
      invitationExpired
      invitationUrl
    }
  }
}
```

## Delete Invite

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($userId: String!) {
  deleteInvite(userId: $userId) {
    success
  }
}
```

**Variables:**
```json
{
    "userId": "uinv_vO4rCsHEjaR4qlCg"
}
```

## Delete User

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($userId: String!) {
  deleteUser(userId: $userId) {
    success
  }
}
```

**Variables:**
```json
{
    "userId": "auth0|635ad83da396f641a508b177"
}
```

## Get Admin Page / Settings

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery {
  admin {
    orgName
    users {
        userId
        email
        userType
        name
        picture
        invitationExpired
        invitationUrl
    }
    organizationSettings {
        useNewCostBasis
        costBasisStrategy
        calculateCostBasisByInternalAccount
        peggedStableCoinsToFiat {
            assetName
        }
        proofOfFunds {
            dashboardUrl
        }
    }
    
  }
}
```

## Set User Type

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($userId: String!, $userType: UserType!) {
  setUserType(userId: $userId, userType: $userType) {
    success
  }
}
```

**Variables:**
```json
{
    "userId": "auth0|6304c2999143722cfce47efa",
    "userType": "VIEWER"
}
```

## Set Organization Settings

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation (
    $calculateCostBasisByInternalAccount: Boolean!
    $calculateCostBasisForCurrencies: [Currency]!
    $costBasisStrategy: CostBasisStrategy!
    $peggedStableCoinsToFiat: [PeggingPairInputType]!
    $acceptableSwapFiatValueAlignmentRate: Float!
    $runErpInvalidate: Boolean!
    $skipCostBasisForAssetClassSymbol: [String]!
    $useCommentsForErpLineDescription: Boolean!
    $enableApAr: Boolean!
    $pricingApiSource: PricingSource!
    $pricingApiSourcePerAsset: [PricingSourcePairInputType]!
    $reevaluationInternalAccountId: ID,
    $dashboardDefaultLedgerTransactions: DashboardDefaultLedgerTransactions
    $auth0ConnectionId: Auth0ConnectionId
    $whitelistAssetClassNames: [String]
    ) {
  setOrganizationSettings(
      calculateCostBasisByInternalAccount: $calculateCostBasisByInternalAccount
      calculateCostBasisForCurrencies: $calculateCostBasisForCurrencies
      costBasisStrategy: $costBasisStrategy
      useCommentsForErpLineDescription: $useCommentsForErpLineDescription
      peggedStableCoinsToFiat: $peggedStableCoinsToFiat
      acceptableSwapFiatValueAlignmentRate: $acceptableSwapFiatValueAlignmentRate
      runErpInvalidate: $runErpInvalidate
      skipCostBasisForAssetClassSymbol: $skipCostBasisForAssetClassSymbol
      enableApAr: $enableApAr
      pricingApiSource: $pricingApiSource
      pricingApiSourcePerAsset: $pricingApiSourcePerAsset
      reevaluationInternalAccountId: $reevaluationInternalAccountId
      dashboardDefaultLedgerTransactions: $dashboardDefaultLedgerTransactions
      auth0ConnectionId: $auth0ConnectionId
      whitelistAssetClassNames: $whitelistAssetClassNames
      ) {
    organizationSettings {
        useCommentsForErpLineDescription
        filterAssetsDistributionWidgetGtZero
        calculateCostBasisByInternalAccount
        skipCostBasisForAssetClassSymbol
        calculateCostBasisForCurrencies
        acceptableSwapFiatValueAlignmentRate
        costBasisStrategy
        disabledCommit
[TRUNCATED]
```

**Variables:**
```json
{
    "calculateCostBasisByInternalAccount": false,
    "calculateCostBasisForCurrencies": ["USD"],
    "costBasisStrategy": "FIFO",
    "peggedStableCoinsToFiat": [
        {"currency": "USD", "assetName": "USD Coin"}
    ],
    "acceptableSwapFiatValueAlignmentRate": 0.1,
    "runErpInvalidate": false,
    "skipCostBasisForAssetClassSymbol": ["USD"],
    "useCommentsForErpLineDescription": false,
    "enableApAr": false,
    "pricingApiSource": "KRAKEN",
    "pricingApiSourcePerAsset": [
        {"pricingApiSource": "KRAKEN", "assetName": "Ethereum"}
    ],
    "reevaluationInternalAccountId": "560594",
    "dashboardDefaultLedgerTransactions": "ONLY_READY",
    "auth0ConnectionId": "APP",
    "whitelistAssetClassNames": ["USD Coin"]
}
```

## Get Platform Settings

`POST {{backend}}/graphql`

<p>Enable/Disable data collection for each platform</p>

**Auth:** bearer

**GraphQL query:**
```graphql
query GetPlatformSettings($platform: String, $internalAccountId: Int) {
  platformSettings(
    platform: $platform, internalAccountId: $internalAccountId
  ) {
    results {
        platformSettings {
            commitStrategy
        }
    }
  }
}
```

**Variables:**
```json
{
    
}
```

## Ledger Task Query

`POST {{backend}}/graphql`

<p>Enable/Disable data collection for each platform</p>

**Auth:** bearer

**GraphQL query:**
```graphql
query LedgerTaskQuery($workflowId: String) {
  ledgerTasks {
    listWorkflows(workflowId: $workflowId) {
      workflowId
      runId
      workflowType
      status
      progress
    }
  }
}
```

**Variables:**
```json
{
  "workflowId": "your-temporal-workflow-id-here"
}
```

## Set Platform Settings

`POST {{backend}}/graphql`

<p>Enable/Disable data collection for each platform</p>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SetPlatformSettings($platform: Platform!, $internalAccountId: Int!, $balanceRollupSettings: BalanceRollupSettingsInputType!, $maxToDate: DateTime, $minLastSyncedAt: DateTime, $forceReplace: Boolean, $calculateBalanceDiff: Boolean) {
  setPlatformSettings(
    balanceRollupSettings: $balanceRollupSettings
    internalAccountId: $internalAccountId
    platform: $platform,
    maxToDate: $maxToDate,
    minLastSyncedAt: $minLastSyncedAt,
    forceReplace: $forceReplace,
    calculateBalanceDiff: $calculateBalanceDiff
  ) {
    platformSettings {
        balanceRollupSettings {
            assetIdentifiers
            interval
        }
        minLastSyncedAt
        maxToDate
        calculateBalanceDiff
    }
  }
}
```

**Variables:**
```json
{
    "internalAccountId": 1,
    "platform": "ETHEREUM",
    "minLastSyncedAt": "2022-01-03T00:00:00Z", "balanceRollupSettings": {"interval": "DAILY", "assetIdentifiers": ["native"]
    },
    "maxToDate": "2024-01-03T00:00:00Z",
    "forceReplace": false,
    "calculateBalanceDiff": true
}
```

## Skip/Disable Data Collection for Platform

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation($platform: Platform!, $internalAccountId: Int!, $balanceRollupSettings: BalanceRollupSettingsInputType!) {
  setPlatformSettings(
    balanceRollupSettings: $balanceRollupSettings
    internalAccountId: $internalAccountId
    platform: $platform
  ) {
    platformSettings {
      balanceRollupSettings {
        assetIdentifiers
        interval
      }
    }
  }
}
```

**Variables:**
```json
{
    "commitStrategy": "SKIP_ALL",
    "platform": "ASTAR"
}
```
