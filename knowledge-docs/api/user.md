# Tres API — User

Endpoints in the 'User' section of the public Tres API collection (5 requests).

## Login

`POST {{backend}}/graphql`

<h3 id="how-to-use">How to use?</h3>
<ul>
<li><p>The login endpoint allows users to authenticate and obtain an access token for accessing protected resources in the Tres Finance API.</p>
</li>
<li><p>This endpoint is GraphQL-based.</p>
</li>
<li><p>The <code>clientId</code> and <code>clientSecret</code> parameters should be provided as variables.</p>
</li>
<li><p>Include the access token obtained from the login endpoint in the Authorization header of subsequent requests to authenticate and access protected resources in the API.</p>
</li>
</ul>

**Auth:** noauth

**GraphQL query:**
```graphql
mutation Login($clientId: String!, $clientSecret: String!) {
    getApiKey(clientId: $clientId, clientSecret: $clientSecret) {
        token
    }
}
```

**Variables:**
```json
{
    "clientId": "{{client_id}}",
    "clientSecret": "{{client_secret}}"
}
```

**Sample response (200):**
```json
{
    "data": {
        "getApiKey": {
            "token": {
                "access_token": "{{access_token}}",
                "scope": "read:* write:* admin:*",
                "expires_in": 86400,
                "token_type": "Bearer"
            }
        }
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "getApiKey": {
            "token": {
                "error": "access_denied",
                "error_description": "Unauthorized"
            }
        }
    }
}
```

## Logout

`POST {{backend}}/graphql`

<h3 id="how-to-use">How to use?</h3>
<ul>
<li><p>The login endpoint allows users to authenticate and obtain an access token for accessing protected resources in the Tres Finance API.</p>
</li>
<li><p>This endpoint is GraphQL-based.</p>
</li>
<li><p>The <code>clientId</code> and <code>clientSecret</code> parameters should be provided as variables.</p>
</li>
<li><p>Include the access token obtained from the login endpoint in the Authorization header of subsequent requests to authenticate and access protected resources in the API.</p>
</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation LogoutMutation {
  logout {
    success
  }
}
```

## Viewer

`POST {{backend}}/graphql`

<p>Get details about the connected user, the associated organizations and it's settings.</p>

**Auth:** bearer

**GraphQL query:**
```graphql
query Viewer {
  viewer {
    firstName
    displayName
    id
    orgName
    isDemoUser
    isTresUser
    relatedOrganizations
    plainTicketingUserSignature
    organizationSettings {
      costBasisReallocationPerWallet
      showSyncingStatusWidget
      costBasisStrategy
      calculateCostBasisForCurrencies
      calculateCostBasisByInternalAccount
      pricingApiSourcePerAsset {
        assetName
        pricingApiSource
        __typename
      }
      peggedStableCoinsToFiat {
        assetName
        currency
        __typename
      }
      proofOfFunds {
        dashboardUrl
        __typename
      }
      acceptableSwapFiatValueAlignmentRate
      skipCostBasisForAssetClassSymbol
      runErpInvalidate
      useCommentsForErpLineDescription
      enableClasses
      storeArchivedBalances
      defaultDatetimeFilterEnabled
      updateOrgStakingData
      allowInternalAccountCreation
      disableAutoCommit
      autoScheduledCommitHours
      enableCoaMapping
      allowRealtimeNotifications
      fetchXeroDepartmentAndEntityTrackingCategories
      enableReevaluation
      pricingApiSource
      allowShort
      minimumErpLineValueToSync
      organizationIdsToReconcileWith
      counterTransferAmountDeltaRate
      enableCapitalizeFee
      reconciliationShortNames
      enableMultiEntity
      reevaluationInternalAccountId
      whitelistAssetClassIds
      isPivotTableEnabled
      isCryptoPaymentEnabled
      isVestingEnabled
      is1099Enabled
      paymentNotifyDate
      __typename
    }
    __typename
  }
}
```

**Sample response (200):**
```json
{
    "data": {
        "viewer": {
            "id": "3",
            "username": "auth0.62113f1acab39c006b79b0c0",
            "orgName": "live",
            "settings": {
                "calculateCostBasisByInternalAccount": false
            },
            "displayName": "My Demo Account"
        }
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "viewer": {
            "organizationSettings": {
                "calculateCostBasisByInternalAccount": false,
                "calculateCostBasisForCurrencies": [
                    "USD"
                ],
                "costBasisStrategy": "FIFO"
            }
        }
    }
}
```

## Platforms Status

`POST {{backend}}/graphql`

<p>Get details about the connected user, the associated organizations and it's settings.</p>

**Auth:** bearer

**GraphQL query:**
```graphql
query Viewer {
  viewer {
    firstName
    displayName
    id
    orgName
    isDemoUser
    isTresUser
    relatedOrganizations
    plainTicketingUserSignature
    organizationSettings {
      costBasisReallocationPerWallet
      showSyncingStatusWidget
      costBasisStrategy
      calculateCostBasisForCurrencies
      calculateCostBasisByInternalAccount
      pricingApiSourcePerAsset {
        assetName
        pricingApiSource
        __typename
      }
      peggedStableCoinsToFiat {
        assetName
        currency
        __typename
      }
      proofOfFunds {
        dashboardUrl
        __typename
      }
      acceptableSwapFiatValueAlignmentRate
      skipCostBasisForAssetClassSymbol
      runErpInvalidate
      useCommentsForErpLineDescription
      enableClasses
      storeArchivedBalances
      defaultDatetimeFilterEnabled
      updateOrgStakingData
      allowInternalAccountCreation
      disableAutoCommit
      autoScheduledCommitHours
      enableCoaMapping
      allowRealtimeNotifications
      fetchXeroDepartmentAndEntityTrackingCategories
      enableReevaluation
      pricingApiSource
      allowShort
      minimumErpLineValueToSync
      organizationIdsToReconcileWith
      counterTransferAmountDeltaRate
      enableCapitalizeFee
      reconciliationShortNames
      enableMultiEntity
      reevaluationInternalAccountId
      whitelistAssetClassIds
      isPivotTableEnabled
      isCryptoPaymentEnabled
      isVestingEnabled
      is1099Enabled
      paymentNotifyDate
      __typename
    }
    __typename
  }
}
```

## Rotate API Key

`POST {{backend}}/graphql`

<h3 id="general-notes">General Notes</h3>
<ul>
<li><p>The rotate API keys endpoint allows users to rotate their API keys for enhanced security.</p>
</li>
<li><p>Rotating API keys regularly helps mitigate the risk of unauthorized access to the Tres Finance API.</p>
</li>
</ul>

**Auth:** bearer

**GraphQL query:**
```graphql
mutation RotateAPIKey {
    rotateApiKey {
        clientSecret
    }
}
```
