# Tres API — Notification Center

Endpoints in the 'Notification Center' section of the public Tres API collection (9 requests).

## Query Notification Rules

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetNotificationRules($limit: Int, $offset: Int,) {
  notificationRule(limit: $limit, offset: $offset) {
    results {
      id
      createdAt
      deliveryMethod
      rule
      side
      threshold
      updatedAt
      asset {
        id
      }
      internalAccount {
        identifier
      }
    }
  }
}
```

**Variables:**
```json
{
    "limit": 1,
    "offset": 0
}
```

**Sample response (200):**
```json
{
    "data": {
        "notificationRule": {
            "results": [
                {
                    "id": "1",
                    "createdAt": "2024-04-14T18:06:32.022366+00:00",
                    "deliveryMethod": [
                        "slack"
                    ],
                    "rule": "EXPOSURE_TO_ASSET",
                    "side": "OVER",
                    "threshold": 70,
                    "updatedAt": "2024-04-15T07:35:21.562108+00:00",
                    "asset": {
                        "identifier": "native",
                        "key": "tezos_native",
                        "name": "Tezos"
                    },
                    "internalAccount": {
                        "identifier": "tz1dyuSBjph2CEDygixhJEu9N8JwQt49Vnxu"
                    }
                },
                {
                    "id": "2",
                    "createdAt": "2024-04-14T18:07:44.345941+00:00",
                    "deliveryMethod": [
                        "slack",
                        "discord"
                    ],
                    "rule": "TX_FIAT_VALUE",
                    "side": "OVER",
                    "threshold": 970,
                    "updatedAt": "2024-04-15T08:53:27.731884+00:00",
                    "asset": null,
                    "internalAccount": {
                        "identifier": "tz1dyuSBjph2CEDygixhJEu9N8JwQt49Vnxu"
                    }
                }
            ]
        }
    },
    "debugToolbar": {
        "panels": {
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "43 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "0 calls in 0.00ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
            
[TRUNCATED]
```

## Query Notification Rules Templates

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query MyQuery {
  notificationsRuleTemplate {
    name
    optionalFields
    requiredFields
    excludeFields
  }
}
```

**Sample response (200):**
```json
{
    "data": {
        "notificationsRuleTemplate": [
            {
                "name": "TX_AMOUNT",
                "optionalFields": [
                    "belongs_to",
                    "asset_key",
                    "fiat_currency"
                ],
                "requiredFields": [
                    "side",
                    "threshold"
                ],
                "excludeFields": null
            },
            {
                "name": "FIRST_TX_WITH_ASSET",
                "optionalFields": [
                    "belongs_to"
                ],
                "requiredFields": [
                    "asset_key"
                ],
                "excludeFields": null
            },
            {
                "name": "RECONCILIATION",
                "optionalFields": [
                    "asset_key"
                ],
                "requiredFields": [
                    "internal_account_id"
                ],
                "excludeFields": null
            },
            {
                "name": "NET_WORTH",
                "optionalFields": [
                    "fiat_currency",
                    "internal_account_id",
                    "asset_key"
                ],
                "requiredFields": [
                    "side",
                    "threshold"
                ],
                "excludeFields": null
            }
        ]
    },
    "debugToolbar": {
        "panels": {
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "42 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "4 calls in 0.09ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "sub
[TRUNCATED]
```

## Query Notification Records

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetNotificationRecord {
  notificationRecord {
    results {
      id
      commitId
      createdAt
      error
      extra
      id
      status
      updatedAt
      notificationRule {
        rule
      }
    }
  }
}
```

**Sample response (200):**
```json
{
    "data": {
        "notificationRecord": {
            "results": [
                {
                    "commitId": "a37778b3-e516-4bcb-9014-327fe35e4d95",
                    "createdAt": "2024-05-28T09:16:29.970243+00:00",
                    "error": null,
                    "extra": "{\"ratio\": {\"ratio__gt\": 30}, \"filter\": {\"fiat_currency\": \"usd\", \"updated_at__gte\": \"2024-05-27T03:36:40.480Z\", \"updated_at__lte\": \"2024-05-28T09:16:29.944\"}}",
                    "id": "463",
                    "status": "SENT",
                    "updatedAt": "2024-05-28T09:31:23.415984+00:00",
                    "notificationRule": {
                        "rule": "EXPOSURE_TO_ASSET"
                    }
                },
                {
                    "commitId": "fbda7ef3-7ab4-4ef7-9d2a-aa6e6252e6c4",
                    "createdAt": "2024-05-27T03:36:42.081633+00:00",
                    "error": null,
                    "extra": "{\"ratio\": {\"ratio__gt\": 30}, \"filter\": {\"fiat_currency\": \"usd\", \"updated_at__gte\": \"2024-05-25T22:24:33.718Z\", \"updated_at__lte\": \"2024-05-27T03:36:42.058\"}}",
                    "id": "430",
                    "status": "SENT",
                    "updatedAt": "2024-05-27T04:01:23.637642+00:00",
                    "notificationRule": {
                        "rule": "EXPOSURE_TO_ASSET"
                    }
                },
                {
                    "commitId": "ded5d1cd-0222-4e2d-83f3-61de75d83d14",
                    "createdAt": "2024-05-25T22:24:34.750112+00:00",
                    "error": null,
                    "extra": "{\"ratio\": {\"ratio__gt\": 30}, \"filter\": {\"fiat_currency\": \"usd\", \"updated_at__gte\": \"2024-05-24T16:14:24.029Z\", \"updated_at__lte\": \"2024-05-25T22:24:34.722\"}}",
                    "id": "397",
                    "status": "SENT",
                    "updatedAt": "2024-05-25T22:31:28.074827+00:00",
                    "notificati
[TRUNCATED]
```

## Query Notification Records w\ Sub Transactions

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetNotificationRecord($id: Float, $limit: Int, $offset: Int) {
  notificationRecord(id: $id) {
    results {
      subTransactions (limit: $limit, offset: $offset){
        totalCount
        results {
            id
            timestamp
            platform
            type
            balanceFactor
            amount
            fiat
            asset {
                symbol
            }
            belongsTo {
                identifier
            }
            sender {
                identifier
                originalIdentifier
                name
                customAccountName
                isInternal
            }
            recipient {
                identifier
                originalIdentifier
                name
                customAccountName
                isInternal
            }
            tx {
                identifier
            }
        }
      }
    }
  }
}
```

**Variables:**
```json
{
  "id": 4126,
  "limit":1
}
```

**Sample response (200):**
```json
{
    "data": {
        "notificationRecord": {
            "results": [
                {
                    "commitId": "a37778b3-e516-4bcb-9014-327fe35e4d95",
                    "createdAt": "2024-05-28T09:16:29.970243+00:00",
                    "error": null,
                    "extra": "{\"ratio\": {\"ratio__gt\": 30}, \"filter\": {\"fiat_currency\": \"usd\", \"updated_at__gte\": \"2024-05-27T03:36:40.480Z\", \"updated_at__lte\": \"2024-05-28T09:16:29.944\"}}",
                    "id": "463",
                    "status": "SENT",
                    "updatedAt": "2024-05-28T09:31:23.415984+00:00",
                    "notificationRule": {
                        "rule": "EXPOSURE_TO_ASSET"
                    }
                },
                {
                    "commitId": "fbda7ef3-7ab4-4ef7-9d2a-aa6e6252e6c4",
                    "createdAt": "2024-05-27T03:36:42.081633+00:00",
                    "error": null,
                    "extra": "{\"ratio\": {\"ratio__gt\": 30}, \"filter\": {\"fiat_currency\": \"usd\", \"updated_at__gte\": \"2024-05-25T22:24:33.718Z\", \"updated_at__lte\": \"2024-05-27T03:36:42.058\"}}",
                    "id": "430",
                    "status": "SENT",
                    "updatedAt": "2024-05-27T04:01:23.637642+00:00",
                    "notificationRule": {
                        "rule": "EXPOSURE_TO_ASSET"
                    }
                },
                {
                    "commitId": "ded5d1cd-0222-4e2d-83f3-61de75d83d14",
                    "createdAt": "2024-05-25T22:24:34.750112+00:00",
                    "error": null,
                    "extra": "{\"ratio\": {\"ratio__gt\": 30}, \"filter\": {\"fiat_currency\": \"usd\", \"updated_at__gte\": \"2024-05-24T16:14:24.029Z\", \"updated_at__lte\": \"2024-05-25T22:24:34.722\"}}",
                    "id": "397",
                    "status": "SENT",
                    "updatedAt": "2024-05-25T22:31:28.074827+00:00",
                    "notificati
[TRUNCATED]
```

## Create Notification Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation($createdBy: String!, $currency: Currency!, $deliveryMethod: [DeliveryMethod]!, $side: UnderOver!, $rule: Rule!, $threshold: Float!, $enable: Boolean!) {
  createNotificationRule(
    deliveryMethod: $deliveryMethod
    side: $side
    threshold: $threshold
    enable: $enable
    createdBy: $createdBy
    currency: $currency
    rule: $rule
  ) {
    id
    success
  }
}
```

**Variables:**
```json
{
    "deliveryMethod": ["SLACK"],
    "rule": "TX_AMOUNT",
    "side": "OVER",
    "threshold": 1,
    "createdBy": "user",
    "currency": "USD",
    "enable": true
  }
```

**Sample response (200):**
```json
{
    "data": {
        "createNotificationRule": {
            "id": 11,
            "success": true
        }
    },
    "debugToolbar": {
        "panels": {
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "43 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "2 calls in 0.09ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 1 connection",
                "subtitle": "1 query in 7.25ms"
            },
            "RequestPanel": {
                "title": "Request",
                "subtitle": "CustomGraphQLView"
            },
            "HeadersPanel": {
                "title": "Headers",
                "subtitle": ""
            },
            "SettingsPanel": {
                "title": "Settings from configuration.settings",
                "subtitle": ""
            },
            "TimerPanel": {
                "title": "Time",
                "subtitle": "CPU: 61.30ms (72.10ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.2.13"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "bf5d9ba0c66a451bb876bba3232c7ca3"
    }
}
```

## Delete Notification Rule

`POST {{backend}}/graphql`

**Auth:** oauth2

**GraphQL query:**
```graphql
mutation DeleteNotificationRule($id: ID!) {
  deleteNotificationRule(id: $id) {
    status
  }
}
```

**Variables:**
```json
{"id": 8}
```

**Sample response (200):**
```json
{
    "data": {
        "deleteNotificationRule": {
            "status": true
        }
    },
    "debugToolbar": {
        "panels": {
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "43 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "0 calls in 0.00ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "subtitle": "4 queries in 15.10ms"
            },
            "RequestPanel": {
                "title": "Request",
                "subtitle": "view"
            },
            "HeadersPanel": {
                "title": "Headers",
                "subtitle": ""
            },
            "SettingsPanel": {
                "title": "Settings from configuration.settings",
                "subtitle": ""
            },
            "TimerPanel": {
                "title": "Time",
                "subtitle": "CPU: 47.56ms (73.53ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.2.7"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "6a6d3a2fe3124cf5a6d76c1630923782"
    }
}
```

## Update Notification Rule State

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation(
    $key: Int!,
    $enable: Boolean!
) {
  updateNotificationRule(enable: $enable, key: $key) {
    success
  }
}
```

**Variables:**
```json
{
    "key": 1,
    "enable": false
  }
```

**Sample response (200):**
```json
{
    "data": {
        "updateNotificationRule": {
            "success": true
        }
    },
    "debugToolbar": {
        "panels": {
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "43 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "2 calls in 0.09ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "subtitle": "2 queries in 4.33ms"
            },
            "RequestPanel": {
                "title": "Request",
                "subtitle": "CustomGraphQLView"
            },
            "HeadersPanel": {
                "title": "Headers",
                "subtitle": ""
            },
            "SettingsPanel": {
                "title": "Settings from configuration.settings",
                "subtitle": ""
            },
            "TimerPanel": {
                "title": "Time",
                "subtitle": "CPU: 18.90ms (29.12ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.2.13"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "8b7ad5ed21a74552b7275c0a6938f29b"
    }
}
```

## Query Get Operation Notification Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OperationNotificationRule {
  operationNotificationRule {
    totalCount
    results {
      id
      createdAt
      updatedAt
      deliveryMethod
      deliveryConfig
      rule
      createdBy
      enable
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
        "updateNotificationRule": {
            "success": true
        }
    },
    "debugToolbar": {
        "panels": {
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "43 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "2 calls in 0.09ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "subtitle": "2 queries in 4.33ms"
            },
            "RequestPanel": {
                "title": "Request",
                "subtitle": "CustomGraphQLView"
            },
            "HeadersPanel": {
                "title": "Headers",
                "subtitle": ""
            },
            "SettingsPanel": {
                "title": "Settings from configuration.settings",
                "subtitle": ""
            },
            "TimerPanel": {
                "title": "Time",
                "subtitle": "CPU: 18.90ms (29.12ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.2.13"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "8b7ad5ed21a74552b7275c0a6938f29b"
    }
}
```

## Update Notification Rule V2

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation updateNotificationRule(
    $id: Int!,
    $enable: Boolean!
    $ruleType: Rule,
    $deliveryConfig: DeliveryConfigInput,
    $deliveryMethods: [DeliveryMethod]
) {
  updateNotificationRuleV2(enable: $enable, id: $id, ruleType: $ruleType,
  deliveryConfig: $deliveryConfig, deliveryMethods: $deliveryMethods) {
    success
  }
}
```

**Variables:**
```json
{
  "enable": true,
  "ruleType": "RECURRING_REPORT_READY",
  "id": 3103,
  "deliveryConfig": {
        "method": "EMAIL",
        "target": [
            "1@gmail.com",
            "2@gmail.com",
            "3@gmail.com",
            "4@gmail.com",
            "5@gmail.com",
            "6@gmail.com"
        ]
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "updateNotificationRule": {
            "success": true
        }
    },
    "debugToolbar": {
        "panels": {
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "43 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "2 calls in 0.09ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "subtitle": "2 queries in 4.33ms"
            },
            "RequestPanel": {
                "title": "Request",
                "subtitle": "CustomGraphQLView"
            },
            "HeadersPanel": {
                "title": "Headers",
                "subtitle": ""
            },
            "SettingsPanel": {
                "title": "Settings from configuration.settings",
                "subtitle": ""
            },
            "TimerPanel": {
                "title": "Time",
                "subtitle": "CPU: 18.90ms (29.12ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.2.13"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "8b7ad5ed21a74552b7275c0a6938f29b"
    }
}
```
