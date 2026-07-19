# Tres API — Form Filler

Endpoints in the 'Form Filler' section of the public Tres API collection (2 requests).

## FormFiler - Fill Form(s) with AI

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query FormFillerQuery($formsInputs: [FormFillerUserInputObjectType]!) {
    formFiller(
        formsInputs: $formsInputs
    ) {
        userIntent
        filledForm {
            formId
            aiReasoning
            fields {
                fieldName
                fieldValue
                fieldType
                aiReasoning
            }
        }
        
    }
}
```

**Variables:**
```json
{
    "formsInputs": [
        {
            "userIntent": "swaps between assets",
            "form":{
  "form_id": 1,
  "form_name": "TransactionLedgerFilters",
  "description": "Filter your transactions ledger by dozens of attributes to pinpoint exactly what you need. Note that since this is a filter form, if the user mentions \"any\" related to a select/radio field, it means that this field is irrelevant.",
  "fields": [
    {
      "field_name": "transaction_date",
      "description": "Select the start and end dates for the transactions you want to include.",
      "field_type": "date_range"
    },
    {
      "field_name": "wallets",
      "description": "Choose one or more wallets whose transactions should be shown.",
      "field_type": "select",
      "batch_size": 50,
      "options": [
        {
          "option_value": "main_wallet",
          "option_name": "Your primary wallet.",
          "description": "Your primary wallet."
        },
        {
          "option_value": "savings_wallet",
          "option_name": "Long-term savings wallet.",
          "description": "Long-term savings wallet."
        },
        {
          "option_value": "trading_wallet",
          "option_name": "Wallet used for active trading.",
          "description": "Wallet used for active trading."
        },
        {
          "option_value": "cold_storage",
          "option_name": "Offline cold storage.",
          "description": "Offline cold storage."
        }
      ]
    },
    {
      "field_name": "assets",
      "description": "Filter by asset type or token symbol.",
      "field_type": "select",
      "batch_size": 50,
      "options": [
        {
          "option_value": "BTC",
          "option_name": "Bitcoin",
          "description": "Bitcoin"
        },
        {
          "option_value": "ETH",
          "option_name": "Ethereum",
          "description": "Ethereum"
        },
        {
          "option_value": "USDC",
          "option_name": "USD Coi
[TRUNCATED]
```

**Sample response (200):**
```json
{
    "data": {
        "aiStartProcessingTxsCsvMutation": {
            "ok": true
        }
    }
}
```

## FormFiler - Send Feedback

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation FormFillerSendFeedbackMutation($requestId: String!, $feedbackScore: Int!, $feedbackText: String!) {
    aiPlatformSendFeedback(
        requestId: $requestId, feedbackScore: $feedbackScore, feedbackText: $feedbackText
    ) {
        success
        message
    }
}
```

**Variables:**
```json
{
    "requestId": "blabla",
    "feedbackScore": 0,
    "feedbackText": "EFES AGOL!"
}
```

**Sample response (200):**
```json
{
    "data": {
        "aiStartProcessingTxsCsvMutation": {
            "ok": true
        }
    }
}
```
