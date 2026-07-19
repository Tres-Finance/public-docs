# Tres API — Payments

Endpoints in the 'Payments' section of the public Tres API collection (9 requests).

## Get Invoices

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAPARDataInvoices($limit: Int, $offset: Int) {
      erpInvoices (limit: $limit, offset: $offset) {
       results {
         id
        invoiceId
        dateCreated
        origAmount
        balance
        customerName
        subTx {
          tx {
            identifier
          }
        }
        status
        publicInvoiceId
        paymentToInternalAccounts {
            id
            internalAccount {
                name
                identifier
                parentPlatform
            }
            assets {
                name
                symbol
                identifier
                platform
            }
        }
      }
       }
}
```

**Variables:**
```json
{
    "limit": 10
}
```

## Get Invoices Overview

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAPARDataInvoices($limit: Int, $offset: Int) {
      erpInvoices (limit: $limit, offset: $offset) {
       results {
         id
        invoiceId
        dateCreated
        origAmount
        balance
        customerName
        subTx {
          tx {
            identifier
          }
        }
        status
        publicInvoiceId
        paymentToInternalAccounts {
            id
            internalAccount {
                name
                identifier
                parentPlatform
            }
            assets {
                name
                symbol
                identifier
                platform
            }
        }
      }
       }
}
```

**Variables:**
```json
{
    "limit": 10
}
```

## Get Invoice Activity Log by ID

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetAPARDataInvoices($id: Float) {
      erpInvoices (id: $id) {
       results {
         activityLog {
            timestamp
            rawData
            type
         }
       }
      }
    }
```

**Variables:**
```json
{
    "id": 9294411
}
```

## Get Public Invoice Details

`POST {{backend}}/graphql`

**Auth:** noauth

**GraphQL query:**
```graphql
query PublicErpInvoice($publicInvoiceId: UUID!) {
  publicErpInvoice(publicInvoiceId: $publicInvoiceId) {
    invoiceId
    balance
    customerDetails {
        name
        address
    }
    receivingAddresses {
        identifier
        parentPlatform
        assets {
            name
            symbol
            identifier
            platform
        }
    }
    invoiceDetails {
        createdAt
        updatedAt
        dueAt
        docNumber
    }
    companyDetails {
        name
        address
        phone
        companyNumber
        email
    }
    lines {
        quantity
        unitPrice
        totalPrice
        description
        lineNum
    }
  }
}
```

**Variables:**
```json
{
  "publicInvoiceId": "004a7566-d0a2-4a34-bebf-2a69d7d8e9f3"
}
```

## Public Invoice Actions

`POST {{backend}}/graphql`

**Auth:** noauth

**GraphQL query:**
```graphql
query PublicErpInvoice($publicInvoiceId: UUID!) {
  publicErpInvoice(publicInvoiceId: $publicInvoiceId) {
    invoiceId
    balance
    customerDetails {
        name
        address
    }
    receivingAddresses {
        identifier
        parentPlatform
        assets {
            name
            symbol
            identifier
            platform
        }
    }
    invoiceDetails {
        createdAt
        updatedAt
        dueAt
        docNumber
    }
    companyDetails {
        name
        address
        phone
        companyNumber
        email
    }
    lines {
        quantity
        unitPrice
        totalPrice
        description
        lineNum
    }
  }
}
```

**Variables:**
```json
{
  "publicInvoiceId": "004a7566-d0a2-4a34-bebf-2a69d7d8e9f3"
}
```

## Get Public Invoice PDF

`POST {{backend}}/graphql`

**Auth:** noauth

**GraphQL query:**
```graphql
query PublicErpInvoice($publicInvoiceId: UUID!) {
  publicErpInvoice(publicInvoiceId: $publicInvoiceId) {
    invoiceId
    balance
    customerDetails {
        name
        address
    }
    receivingAddresses {
        identifier
    }
    invoiceDetails {
        createdAt
        updatedAt
        dueAt
    }
    lines {
        quantity
        unitPrice
        totalPrice
        description
        lineNum
    }
  }
}
```

**Variables:**
```json
{
  "publicInvoiceId": "004a7566-d0a2-4a34-bebf-2a69d7d8e9f3"
}
```

## Set Receiving Accounts

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation ConfigureInvoicePaymentDetails($paymentToInternalAccountsConfig: [PaymentToInternalAccountsConfigInput]) {
  configureInvoicePaymentDetails(paymentToInternalAccountsConfig: $paymentToInternalAccountsConfig) {
    invoice {
        id
        publicInvoiceId
        paymentToInternalAccounts {
            internalAccount {
                identifier
            }
            assets {
                symbol
            }
        }
    }
  }
}
```

**Variables:**
```json
{
  "paymentToInternalAccountsConfig": [
    {
        "internalAccountId": "523397",
        "assetKeys": ["ethereum_native"]
    }
  ]
}
```

## Get Default Receiving Accounts For Organization

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query OrganizationDefaultPaymentToInternalAccounts {
    organizationDefaultPaymentToInternalAccounts {
        defaultPaymentConfigs {
            internalAccountId
            assetKeys
        }
    }
}
```

## Update Default Receiving Accounts For Organization

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation UpdateDefaultPaymentDetailsForOrg($paymentConfigs: [DefaultPaymentConfigInput!]!) {
  updateDefaultPaymentDetailsForOrg(paymentConfigs: $paymentConfigs) {
    success
    message
  }
}
```

**Variables:**
```json
{
    "paymentConfigs": [
        {
            "internalAccountId": "627963",
            "assetKeys": [
                    "ethereum_0x01d3bbb8c419d2dc1732f5c8a757e5347defe6b0",
                    "ethereum_0x0d42c1eea7dd1fe94614f4a767c72a5b6e9abcc7",
                    "ethereum_0x0f516957532b8dd51f7e5de338d898b560ec8fc8"
                ]
        },
        {
            "internalAccountId": "599148",
            "assetKeys": ["litecoin_native"]
        },
                {
            "internalAccountId": "628035",
            "assetKeys": ["kava_hard", "kava_uatom","kava_ukava"]
        }
    ]
}
```
