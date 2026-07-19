# Tres API — Integrations — Actions (part 1)

Endpoints in the 'Integrations — Actions (part 1)' section of the public Tres API collection (20 requests).

## Create or Update Netsuite AUth

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation($netsuiteAuth: NetsuiteAuthInputType!) {
  createOrUpdateNetsuiteAuth (netsuiteAuth: $netsuiteAuth) {
      netsuiteAuth {
          clientId
      }
  }
}
```

**Variables:**
```json
{
    "netsuiteAuth": {
        "clientId": "   ",
        "clientSecret": "bbb",
        "tokenId": "ccc",
        "tokenSecret": "eee",
        "subsidiaryId": "fff",
        "account": "kkk"
    }
}
```

**Sample response (200):**
```json
{
    "data": {
        "createOrUpdateNetsuiteAuth": {
            "netsuiteAuth": {
                "clientId": "aad"
            }
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
                "subtitle": "2 calls in 0.12ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (201 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "subtitle": "3 queries in 617.40ms"
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
                "subtitle": "CPU: 214.88ms (910.94ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.2.2"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "5163b093be2f4914a4f2552acc8ee32a"
    }
}
```

## Sync All

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation syncIntegration($integrationName: String, $startDate: Date, $endDate: Date) {
  syncIntegration(integrationName: $integrationName, startDate: $startDate, endDate: $endDate) {
    status
  }
}
```

**Variables:**
```json
{
    "integrationName": "xero",
    "startDate": "2025-04-07",
    "endDate": "2025-04-07"
}
```

## Sync Specific Txs

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation syncSpecificTransactions($transactionIds: [String]) {
    syncSpecificTransactions(transactionIds: $transactionIds) {
        status
    }
}
```

**Variables:**
```json
{
  "transactionIds": ["1763292299.000000078947617824919841610000",
  "1763292107.000000084550589336300822360000","1763291699.000000069611158107620520530000"

]
}
```

## Sync Specific Txs With Entity Source Type

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation syncSpecificTransactions($transactionIds: [String], $entitySourceType: String) {
    syncSpecificTransactions(transactionIds: $transactionIds, entitySourceType: $entitySourceType) {
        status
    }
}
```

**Variables:**
```json
{
  "transactionIds": ["1744059158.000000017839502720966608420000","1744058187.000000145157484321610494910000","1744020042.000000033357476989121834330000","1744016449.000000011978696238053247690000"],
  "entitySourceType": "invoice_payment"
}
```

## Ignore Tx

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ignoreTransaction($transactionIds: [String]) {
    ignoreTransaction(transactionIds: $transactionIds) {
        status
    }
}
```

**Variables:**
```json
{
  "transactionIds": [    
    1735689601.000000059057336727483529150000,
    1735689601.000000062342484530168467290000,
    1735689601.000000158857862261109840550000,
    1735689601.000000157644425704285257120000,
    1735689601.000000023673689812058800210000,
    1735689601.000000094446467654859456720000,
    1735689601.000000006488315250372030110000,
    1735689601.000000076850097898811715430000,
    1735689601.000000104148303476416985780000,
    1735689601.000000049497016993668073250000,
    1735689601.000000001037564133473921160000,
    1735689601.000000043752981599401830600000,
    1735689601.000000125933776451915528080000,
    1735689601.000000044495491830719363340000,
    1735689601.000000091091156536767909070000,
    1735689601.000000004392076641012937780000,
    1735689601.000000027521005954032790970000,
    1735689601.000000055765812745117245360000,
    1735689601.000000120142455234859727500000,
    1735689601.000000006936579668140761580000,
    1735689601.000000130902928056207396350000,
    1735689601.000000052559267340388604790000,
    1735689601.000000120998858472084376910000,
    1735689601.000000037857351354091430770000,
    1735689601.000000109855316920651779130000,
    1735689601.000000125372531495245229410000,
    1735689601.000000176398254301294812970000,
    1735689601.000000040718917213548477460000,
    1735689601.000000077465927854023154630000,
    1735689601.000000059165567192478202350000,
    1735689601.000000009444339697715622870000,
    1735689601.000000082377289289661795140000,
    1735689601.000000119264404321907667060000,
    1735689601.000000101680318487376096370000,
    1735689601.000000154601136003953826390000,
    1735689601.000000067673128302692967630000,
    1735689601.000000082447859665900371870000,
    1735689601.000000137494824556179719830000,
    1735689601.000000132919757229677079380000,
    1735689601.000000162420090191802893560000,
    1735689601.000000127219385060798430990000,
    1735689601.000000074100151723802797050000
[TRUNCATED]
```

## Undo Ignore Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation undoIgnoreTransaction($transactionIds: [Int]) {
    undoIgnoreTransaction(transactionIds: $transactionIds) {
        status
    }
}
```

**Variables:**
```json
{
  "transactionIds": [217]
}
```

## Unsync Specific Txs

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation unsyncSpecificTransactions($transactionIds: [String]) {
    unsyncSpecificTransactions(transactionIds: $transactionIds) {
        status
    }
}
```

**Variables:**
```json
{
  "transactionIds": ["1744059158.000000017839502720966608420000","1744058187.000000145157484321610494910000","1744020042.000000033357476989121834330000","1744016449.000000011978696238053247690000"]
}
```

**Sample response (200):**
```json
{
    "data": {
        "unsyncSpecificTransactions": {
            "status": "ok"
        }
    },
    "debugToolbar": {
        "panels": {
            "LoggingPanel": {
                "title": "Log messages",
                "subtitle": "0 messages"
            },
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "40 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "0 calls in 0.00ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (206 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "subtitle": "3 queries in 22.09ms"
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
                "subtitle": "CPU: 1160.97ms (1463.73ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.1.3"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "7f71766923d54bbea379154ca19999ae"
    }
}
```

## Unsync Specific Txs With Entity Source Type

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation unsyncSpecificTransactions($transactionIds: [String], $entitySourceType: String) {
    unsyncSpecificTransactions(transactionIds: $transactionIds, entitySourceType: $entitySourceType) {
        status
    }
}
```

**Variables:**
```json
{
  "transactionIds":["1744058187.000000145157484321610494910000"],
  "entitySourceType": "invoice_payment"
}
```

## Create or Update Rule - Custom Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation upsertRule($rule: GenericScalar) {
    upsertRule(rule: $rule) {
        status
    }
}
```

**Variables:**
```json
{
  "rule": {
    "type": "custom_rule",
    "name": "Rule 1fdfdss3",
    "identifier": null,
    "accounts": {
      "inventory": {
        "name": "Other Revenue",
        "value": "260"
      },
      "unrealized_gain_loss": {
        "name": "Other Revenue",
        "value": "260"
      },
      "income": null,
      "expense": null,
      "fee": null,
      "gain": null,
      "loss": null
    },
    "filters": {
      "wallets": [
        {
          "id": "0x157911fdsa2fdsad07895dc42b94223b04d3928447c738d8",
          "name": "",
          "address": "0x157911fds2d07895dc42b94223b04d3928447c7asdf38d8",
          "parentPlatform": "ethereum"
        }
      ],
      "assetClassNames": [],
      "senders": [],
      "recipients": [],
      "platforms": [],
      "tags": [],
      "actions": [],
      "contracts": [],
      "specificIds": [],
      "fromDate": "2023-07-03T00:00:00+00:00",
      "toDate": "2023-08-03T00:00:00+00:00"
    }
  }
}
```

## Create or Update Rule - Default

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation upsertRule($rule: GenericScalar) {
    upsertRule(rule: $rule) {
        status
    }
}
```

**Variables:**
```json
{
    "rule": {
        "name": "Default Rule",
        "type": "default",
        "identifier": null,
        "netsuite_class": "nsclass",
        "netsuite_department": "nsdepartment",
        "accounts": {
            "inventory": {
                "name": "Uncategorised Expense",
                "value": "2"
            },
            "incomes": {
                "name": "Uncategorised Income",
                "value": "1"
            },
            "expenses": {
                "name": "Sales",
                "value": "5"
            },
            "fees": {
                "name": "Uncategorised Expense",
                "value": "2"
            },
            "gains": {
                "name": "Uncategorised Expense",
                "value": "2"
            },
            "losses": {
                "name": "Sales",
                "value": "5"
            }
        },
        "filters": {
            "wallets": [],
            "assetClassNames": [],
            "senders": [],
            "recipients": [],
            "platforms": [],
            "tags": [],
            "actions": [],
            "contracts": [],
            "specific_ids": [],
            "isInternalTransfer": null
        }
    }
}
```

## Create or Update Rule - Internal Transfer

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation upsertRule($rule: GenericScalar) {
    upsertRule(rule: $rule) {
        status
    }
}
```

**Variables:**
```json
{
    "rule": {
        "type": "internal_transfer",
        "identifier": null,
        "accounts": {
            "inventory": {
                "name": "Retained Earnings",
                "value": "4",
                "type": "inventory"
        
            },
            "income": null,
            "expense": null,
            "fee":null,
            "gain": null,
            "loss": null
        },
        "filters": {
            "wallets": [],
            "asset_class_names": [],
            "senders": [],
            "recipients": [],
            "platforms": [],
            "tags": [],
            "actions": [],
            "contracts": [],
            "specificIds": [],
            "isInternalTransfer": true
        }
    }
}
```

## Create or Update Rule - Specific Sub Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation upsertRule($rule: GenericScalar) {
    upsertRule(rule: $rule) {
        status
    }
}
```

**Variables:**
```json
{
  "rule": {
    "type": "specific_sub_transaction",
    "identifier": null,
    "accounts": {
      "inventory": {
        "name": "Gnosis Safe",
        "value": "1085"
      },
      "expense": {
        "name": "Foundation Gringotts Deposits 1 Receive (1001)",
        "value": "1001"
      },
      "gain": {
        "name": "SEI Ecosystem Reserve 9 Receive (1045)",
        "value": "1045"
      },
      "loss": {
        "name": "SEI Ecosystem Reserve 10 Receive (1046)",
        "value": "1046"
      }
    },
    "filters": {
      "wallets": [],
      "assetClassNames": [],
      "senders": [],
      "recipients": [],
      "platforms": [],
      "tags": [],
      "actions": [],
      "contracts": [],
      "walletTagsSenders": [],
      "walletTagsRecipients": [],
      "financialActionGroups": [],
      "contactGroupsSenders": [],
      "contactGroupsRecipients": [],
      "specificIds": [
        {
          "id": 3864362542
        }
      ],
      "isInternalTransfer": null
    }
  }
}
```

## Create or Update Rule - Ignore Specific Sub Transaction

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation upsertRule($rule: GenericScalar) {
    upsertRule(rule: $rule) {
        status
    }
}
```

**Variables:**
```json
{
    "rule": {
        "type": "ignore_specific_sub_transaction",
        "identifier": null,
        "netsuite_class": "nsclass",
        "netsuite_department": "nsdepartment",
        "accounts": {
            "inventory": null,
            "income": null,
            "expense": null,
            "fee": null,
            "gain": null,
            "loss": null
        },
        "filters": {
            "wallets": [],
            "assetClassNames": [],
            "senders": [],
            "recipients": [],
            "platforms": [],
            "tags": [],
            "actions": [],
            "contracts": [],
            "specificIds": [
                {
                    "id": 1
                }
            ],
            "isInternalTransfer": null
        }
    }
}
```

## create Manual ERP

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateManualErp ($csvS3Key: String!, $currency: Currency!, $integrationName: String!) {
    createManualErp(csvS3Key: $csvS3Key, currency: $currency, integrationName: $integrationName

    ) {
        isSuccessful
        csvWithComments
    }
}
```

**Variables:**
```json
{       "csvS3Key": "org_J8rs7jN5zXbuDZBw/org_J8rs7jN5zXbuDZBw/wpyw_manual_erp_invalid_test.csv",
        "currency": "USD",
        "integrationName": "my_inter"
}
```

## Bulk Sync

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateManualErp ($csvS3Key: String!, $currency: Currency!, $integrationName: String!) {
    createManualErp(csvS3Key: $csvS3Key, currency: $currency, integrationName: $integrationName

    ) {
        isSuccessful
        csvWithComments
    }
}
```

**Variables:**
```json
{       "csvS3Key": "org_J8rs7jN5zXbuDZBw/org_J8rs7jN5zXbuDZBw/wpyw_manual_erp_invalid_test.csv",
        "currency": "USD",
        "integrationName": "my_inter"
}
```

## logout

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation CreateManualErp ($csvS3Key: String!, $currency: Currency!, $integrationName: String!) {
    createManualErp(csvS3Key: $csvS3Key, currency: $currency, integrationName: $integrationName

    ) {
        isSuccessful
        csvWithComments
    }
}
```

**Variables:**
```json
{       "csvS3Key": "org_J8rs7jN5zXbuDZBw/org_J8rs7jN5zXbuDZBw/wpyw_manual_erp_invalid_test.csv",
        "currency": "USD",
        "integrationName": "my_inter"
}
```

## Revoke Integration

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation RevokeIntegration ($integrationName: String!, $skipValidations: Boolean) {
    revokeIntegration(integrationName: $integrationName, skipValidations: $skipValidations) {
        success
        message
    }
}
```

**Variables:**
```json
{
        "integrationName": "quickbooks",
        "skipValidations": false
}
```

## Upsert Integration Account

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpsertIntegrationAccount($integrationId: Int!, $name: String!, $value: String!, $type: AccountType!, $integrationAccountId: Int ) {
    upsertIntegrationAccount(
        integrationAccountId: $integrationAccountId
        integrationId: $integrationId
        name: $name
        value: $value
        type:  $type
    ) {
        isSuccessful
        createdNew
        integrationAccountId
    }
}
```

**Variables:**
```json
{       "integrationId": 9878,
        "name": "account2",
        "value": "96845",
        "type": "EQUITY"
}
```

## Delete Integration Account

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation DeleteIntegrationAccount ($integrationAccountId: Int!,  $integrationId: Int!){
    deleteIntegrationAccount(integrationAccountId: $integrationAccountId, integrationId:  $integrationId) {
        deleted,
        message
    }
}
```

**Variables:**
```json
{       "integrationId": 10759,
        "integrationAccountId": 223614
}
```

## Delete Rule

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation deleteRule($identifier: String) {
    deleteRule(identifier: $identifier) {
        status
    }
}
```

**Variables:**
```json
{
"identifier": "05363d79-4ebb-4f48-b287-49781754b19a"
}
```

**Sample response (200):**
```json
{
    "data": {
        "deleteRule": {
            "status": "ok"
        }
    },
    "debugToolbar": {
        "panels": {
            "LoggingPanel": {
                "title": "Log messages",
                "subtitle": "0 messages"
            },
            "SignalsPanel": {
                "title": "Signals",
                "subtitle": "41 receivers of 15 signals"
            },
            "CachePanel": {
                "title": "Cache calls from 1 backend",
                "subtitle": "0 calls in 0.00ms"
            },
            "StaticFilesPanel": {
                "title": "Static files (206 found, 0 used)",
                "subtitle": "0 files used"
            },
            "SQLPanel": {
                "title": "SQL queries from 2 connections",
                "subtitle": "4 queries in 30.47ms"
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
                "subtitle": "CPU: 168.38ms (708.31ms)"
            },
            "VersionsPanel": {
                "title": "Versions",
                "subtitle": "Django 4.1.3"
            },
            "HistoryPanel": {
                "title": "History",
                "subtitle": "/graphql"
            }
        },
        "storeId": "f60a274f32eb4460849240f182c2d664"
    }
}
```
