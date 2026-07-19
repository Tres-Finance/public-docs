# Tres API — Custodian Sync

Endpoints in the 'Custodian Sync' section of the public Tres API collection (2 requests).

## Integrate Anchorage Custodian [PoF + FinOS]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateCustodianIntegration($custodianName: String!, $credentials: JSONString!, $configuration: [CustodianDataTypeConfiguration]!) {
  createCustodianIntegration(
    custodianName: $custodianName
    credentials: $credentials
    configuration: $configuration
  ) {
    success
    validationResults {
      issueType
      errorMessage
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
  "custodianName": "anchorage",
  "credentials": "{\"api_key\":\"myApiKey\"}",
  "configuration": [
    {
      "dataType": "vault",
      "configuration": {
        "finOs": {
          "syncToObject": "INTERNAL_ACCOUNT",
          "templateName": "CUSTODIAN_WALLET_ASSET",
          "filters": [],
          "ignoreArchived": false
        },
        "proofOfFunds": {
          "isEnabled": true,
          "filters": []
        }
      }
    },
    {
      "dataType": "vault_address",
      "configuration": {
        "finOs": {
          "syncToObject": "INTERNAL_ACCOUNT",
          "templateName": "CUSTODIAN_WALLET_ASSET",
          "filters": [],
          "ignoreArchived": false
        },
        "proofOfFunds": {
          "isEnabled": true,
          "filters": []
        }
      }
    }
  ]
}
```

## Integrate Anchorage Custodian [Only PoF]

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateCustodianIntegration($custodianName: String!, $credentials: JSONString!, $configuration: [CustodianDataTypeConfiguration]!) {
  createCustodianIntegration(
    custodianName: $custodianName
    credentials: $credentials
    configuration: $configuration
  ) {
    success
    validationResults {
      issueType
      errorMessage
      __typename
    }
    __typename
  }
}
```

**Variables:**
```json
{
  "custodianName": "anchorage",
  "credentials": "{\"api_key\":\"myApiKey\"}",
  "configuration": [
    {
      "dataType": "vault",
      "configuration": {
        "finOs": {
          "syncToObject": "IGNORE",
          "templateName": "CUSTODIAN_WALLET_ASSET",
          "filters": [],
          "ignoreArchived": false
        },
        "proofOfFunds": {
          "isEnabled": true,
          "filters": []
        }
      }
    },
    {
      "dataType": "vault_address",
      "configuration": {
        "finOs": {
          "syncToObject": "IGNORE",
          "templateName": "CUSTODIAN_WALLET_ASSET",
          "filters": [],
          "ignoreArchived": false
        },
        "proofOfFunds": {
          "isEnabled": true,
          "filters": []
        }
      }
    }
  ]
}
```
