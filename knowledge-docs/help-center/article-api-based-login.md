# API-Based Login | TRES Finance Help Center

Source: https://help.tres.finance/article/api-based-login

# API-Based Login

API Call: https://api-docs.tres.finance/#e3d2d882-8ed7-4d71-a964-7b9379cbd841

Use the Login call with the clientId and clientSecret you got from TRES team

The login endpoint allows users to authenticate and obtain an access token for accessing protected resources in the Tres Finance API.

This endpoint is GraphQL-based.

The clientId and clientSecret parameters should be provided as variables.

As a response, you will get an access token.

Include the access token obtained from the login endpoint in the Authorization header (as Bearer Token) of subsequent requests to authenticate and access protected resources in the API.

### Working with Multiple Entities

If your account includes multiple entities, each API request (after the initial login) must include an x-org-name key-value pair in the request headers. The org name is found in your entity's URL — for example, if your entity URL is https://demo-tres.tres.finance, the x-org-name value would be demo-tres.

This is required because the same API credentials are shared across all your entities. Once you have an access token, the x-org-name header tells the API which specific entity you want to query.
