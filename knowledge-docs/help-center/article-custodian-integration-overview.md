# Custodian Integration - Overview | TRES Finance Help Center

Source: https://help.tres.finance/article/custodian-integration-overview

# Custodian Integration - Overview

### What is the custodian integration?

Tres connects to your qualified crypto custodian to automatically import the data you need for accounting, reporting, and reconciliation: vault accounts and addresses. Once connected, your custodial holdings appear in your Tres dashboard, ledger, and reports without manual exports or spreadsheets.

The connection is read-only. Tres can see your data, but cannot move, withdraw, or otherwise act on your assets.

### Supported custodians

Tres supports the following qualified custodians out of the box:

Anchorage

Coinbase Prime

Fireblocks

Kraken Custody

LayerOne

Ledger Enterprise

### What we fetch

The primary thing Tres imports from your custodian is on-chain wallet addresses - the addresses associated with the vaults and accounts in your custody setup.

Once imported, each address is saved into Tres in one of three places, depending on how you intend to use it:

Wallets in Tres - addresses you own (vault addresses) become wallets in Tres. They appear in your dashboard, ledger, and reports, and on-chain activity is automatically attributed to the right account.

Contacts - addresses belonging to counterparties (the parties you send funds to or receive from) are saved as contacts so that future activity with them is automatically labeled.

Proof of Funds - addresses can be designated for Proof of Funds, where Tres tracks them for compliance and attestation reporting.

This routing is customizable - you can configure how addresses from each custodian, vault, or account are classified (Wallet, Contact, or Proof of Funds) to match how your team actually uses them.

The exact data points depend on what each custodian’s API exposes. We do not collect anything beyond what is required to produce accurate accounting and reporting outputs.

### How it works

The integration runs in three stages:

Connect. You generate a read-only API key in your custodian’s portal and paste it into Tres. Tres validates the key by performing a test read.

Sync. Tres calls your custodian’s API on a recurring schedule, pulling the latest vaults and addresses. The raw data is transformed into Tres’s unified data model.

Use. Your custodial holdings appear automatically across the Tres dashboard, ledger, reports, and reconciliation views.

The integration is continuous - any changes in your custodian (new vaults, new addresses, updated metadata) are picked up on the next sync and reflected in Tres automatically, with no manual intervention required.

### Need help?

For onboarding assistance, contact your Tres account manager or support@tresfinance.com.
