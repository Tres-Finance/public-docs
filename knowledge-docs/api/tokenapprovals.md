# Tres API — TokenApprovals

Endpoints in the 'TokenApprovals' section of the public Tres API collection (2 requests).

## TriggerTokenApprovalsWorkflow

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation TriggerTokenApprovalScan {
    triggerTokenApprovalScan(platform: ETHEREUM) {
        scanId
        status
        startedAt
    }
}
```

## TokenApprovalsQuery

`GET {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query TokenApprovals {
    tokenApprovals {
        totalCount
        results {
            id
            createdAt
            updatedAt
            spenderAddress
            allowanceRaw
            valueAtRiskQuoteUsd
            spenderLabelExternal
            spenderLabelInternal
            lastModifiedBlock
            lastModifiedAt
            lastModifiedTxHash
            organization {
                id
            }
            internalAccount {
                id
            }
            asset {
                key
            }
            scan {
                id
            }
        }
    }
}
```
