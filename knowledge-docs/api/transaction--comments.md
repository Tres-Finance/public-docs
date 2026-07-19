# Tres API — Transaction — Comments

Endpoints in the 'Transaction — Comments' section of the public Tres API collection (6 requests).

## Get Transaction Comments

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query getLedgerTxComments($limit: Int, $offset: Int, $currency: String, $children_Asset_AssetClass_In: [String], $children_BelongsTo_In: [String], $applications_In: [String], $protocols_In: [String], $classification_Action_In: [String], $success: Boolean, $excludeSpam: Boolean, $onlyStarred: Boolean, $platform_In: [String], $children_Sender_Identifier_In: [String], $children_Recipient_Identifier_In: [String], $decodedFunctionName_In: [String], $classification_Activity_In: [String], $identifier_In: [String], $id_In: [String], $timestamp_Gte: DateTime, $timestamp_Lt: DateTime, $exportName: String, $exportFormat: String, $thirdPartyAccounts_In: [String], $id: String) {
  transaction(
    id: $id
    thirdPartyAccounts_In: $thirdPartyAccounts_In
    limit: $limit
    offset: $offset
    currency: $currency
    children_Asset_AssetClass_In: $children_Asset_AssetClass_In
    children_BelongsTo_In: $children_BelongsTo_In
    applications_In: $applications_In
    protocols_In: $protocols_In
    classification_Action_In: $classification_Action_In
    children_Sender_Identifier_In: $children_Sender_Identifier_In
    children_Recipient_Identifier_In: $children_Recipient_Identifier_In
    success: $success
    excludeSpam: $excludeSpam
    onlyStarred: $onlyStarred
    platform_In: $platform_In
    decodedFunctionName_In: $decodedFunctionName_In
    classification_Activity_In: $classification_Activity_In
    identifier_In: $identifier_In
    id_In: $id_In
    timestamp_Gte: $timestamp_Gte
    timestamp_Lt: $timestamp_Lt
    exportName: $exportName
    exportFormat: $exportFormat
  ) {
    results {
      comments {
        results {
          id
          comment
          createdAt
          updatedAt
          fileLink
          user {
            displayName
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
  "id": "1709626719.000000023726879155313657540000"
}
```

## Delete Transaction Comments

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($comment: String!, $id: Float!,) {
  deleteTransactionComment(comment: $comment, id: $id) {
    status
  }
}
```

**Variables:**
```json
{
 "id": 4,
 "comment": "mymy"
}
```

## Update Transaction Comments

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($comment: String!, $id: Float!, $fileKey: String) {
  updateTransactionComment(comment: $comment, id: $id, fileKey: $fileKey) {
    comment {
      comment
      identifier
      platform
      id
    }
  }
}
```

**Variables:**
```json
{
 "id": 1,
 "comment": "111",
 "fileKey": "1"
}
```

## Create Transaction Comments

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($comment: String!, $identifier: String!, $platform: String!, $fileKey: String) {
  createTransactionComment(comment: $comment, identifier: $identifier, platform: $platform, fileKey: $fileKey) {
    comment {
      comment
      identifier
      platform
      id
    }
  }
}
```

**Variables:**
```json
{
 "identifier": "E6FC795D25F588B19891D517367E4C24144B58D9BA9FAC6D6FBD236758860DC6",
 "comment": "111",
 "platform": "axelar",
 "fileKey": "1"
}
```

## Generate Upload File Url

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation MyMutation ($key: String!, $identifier: String!, $bucket: BucketNames) {
  generateUploadFileUrl(key: $key, identifier: $identifier, bucket: $bucket) {
    url
  }
}
```

**Variables:**
```json
{

 "key": "ghrb_Aviv.jped",
 "identifier": "0x123456"
}
```

## Upload file

`POST https://tres-upload-files.s3.amazonaws.com`

**Auth:** noauth
