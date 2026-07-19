# Setup Okta Login | TRES Finance Help Center

Source: https://help.tres.finance/article/setup-okta-login

# Setup Okta Login

Login into your Okta Admin DashboardUse the following settings when you set up your Okta OIDC app integration:

1. Select OIDC as the Sign-in method.

2. Select Web application as the Application type, and set the following parameters:

Sign-in Redirect URIs

https://tres-finance.us.auth0.com/login/callback

Sign-out redirect URIs

https://tres-finance.us.auth0.com/logout/callback

Trusted Origins

https://*.tres.finance

3. Record the Client ID and Client Secret that Okta generates for your app integration.

4. Send to TRES team the following details:

Okta Domain - Okta's domain name for your organization.

Client ID - Unique identifier for your registered Okta application.

Client Secret - String used to gain access to your registered Okta application.

5. Tres team will send you your login URL
