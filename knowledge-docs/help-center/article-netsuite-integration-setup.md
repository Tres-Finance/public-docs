# Netsuite Integration Setup | TRES Finance Help Center

Source: https://help.tres.finance/article/netsuite-integration-setup

# Netsuite Integration Setup

Creating a Netsuite User for Tres Finance Integration

Introduction

Integrating your Netsuite account with Tres Finance can streamline your financial data management and boost productivity. To make this integration work seamlessly, you need to set up a dedicated Netsuite user with the right permissions and access.

Prerequisites

Before you start, ensure you have administrator access to your Netsuite account.

Step 1: Enable SOAP Web Services

Log in to your Netsuite account.

Go to 'Setup' and select 'Company.'

Under 'Company,' choose 'Enable Features.'

In the 'SuiteCloud' tab, find 'SOAP Web Services' and enable it. Click 'Save.'

Step 2: Create a Role for the Integration

Make sure the WEB SERVICES ONLY ROLE is checked

1. ‘permissions -> setup ’ add SOAP Web Services and Log in using Access Tokens

2. ‘permissions -> transactions’ add Make Journal Entry

3. ‘permissions -> lists’ add Accounts, Departments, Subsidiaries, Classes, and 4. Currencies in a read/full level

Step 3: Create User

Go to 'Employees' -> new

Choose the create role - this must be the only role chosen for the integration user

on ‘Global permissions’ add SOAP web services

Step 4: add the created role and user to the SOAP services configuration -got to Setup -> Integration -> SOAP Web Services Preferences.add the new Tres Integration user and role to the allowed users configuration

​Step 5: Create an integration

Go to ‘setup -> integration -> manage integration -> new’

check TOKEN-BASED AUTHENTICATION

Copy the created client id and Client secret and fill in in Tres configuration window (See below)

Step 6: Create an access token

go to ‘setup -> user/roles -> access tokens -> new’

choose the created user and role

Copy the created token ID and token secret - and fill in in Tres configuration window (See below)

Step 7: Fill in the user info inside Tres integration page1. Log in to Tres finance2. Move to the Integration page3. Choose Netsuite integration4. Fill in the required parameters​
