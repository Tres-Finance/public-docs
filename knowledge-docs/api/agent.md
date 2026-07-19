# Tres API — Agent

Endpoints in the 'Agent' section of the public Tres API collection (3 requests).

## Get Agent History

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
query GetTresAgentHistory($sessionId: String!) {
    tresAgentHistory(sessionId: $sessionId)
}
```

**Variables:**
```json
{
    "sessionId": "1"
}
```

## Start Agent Session

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation StartTresAgentSession($sessionId: String!) {
    startTresAgentChat(sessionId: $sessionId) {
        success
    }
}
```

**Variables:**
```json
{
    "sessionId": "1"
}
```

## Send Message To Agent

`POST {{backend}}/graphql`

**Auth:** bearer

**GraphQL query:**
```graphql
mutation SendTresAgentMessage($message: String!, $sessionId: String!) {
    sendTresAgentMessage(message: $message, sessionId: $sessionId) {
        success
    }
}
```

**Variables:**
```json
{
    "message":  "Hi",
    "sessionId": "1"
}
```
