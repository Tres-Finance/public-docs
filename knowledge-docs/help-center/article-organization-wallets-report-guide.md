# Organization Wallets | TRES Finance Help Center

Source: https://help.tres.finance/article/organization-wallets-report-guide

# Organization Wallets

Complete inventory of all wallets and accounts in your organization: name, address, platform, status, and total fiat value.

### Why use this report?

Your single source of truth for all wallets onboarded into TRES. Lists every wallet with its name, address, parent platform, active platform(s), status, total balance, and creation date. Use this for audit preparation, compliance documentation, and verifying your wallet registry is complete.

### Excel Tabs (1)

What It Shows

raw_data

One per wallet

11 columns (see Key Columns below)

Every wallet/account in your organization.

### Key Columns

#### ALL COLUMNS

What It Contains

Wallet name as set in TRES.

Identifier

Blockchain address or exchange account identifier.

Description

User-provided description.

Tags assigned to this wallet.

Parent Platform

Primary platform (ethereum, manual, exchange name, etc.).

Active Platforms

Comma-separated list of all chains this wallet is monitored on.

Total Fiat Value

Current total fiat value across all assets in this wallet.

Created At

When this wallet was onboarded to TRES.

"ready", "syncing", "error", etc.

Internal Account ID

TRES internal wallet ID.

Custodian

Custodian name if applicable.

### Use Cases

Use Case

Alternative Report

Audit preparation

Provide to auditors as evidence of all monitored addresses.

Wallet registry review

Verify all wallets are accounted for. Check for missing wallets or stale entries.

Compliance documentation

Export as evidence that all organizational wallets are tracked and monitored.

Onboarding verification

After adding new wallets, export to confirm they appear with correct names, addresses, and platforms.

### Related Reports

Extra Columns vs. This Report

Best For

Organization Wallets

This report: wallet registry

Audit, compliance, onboarding check

Asset Balances

Current holdings per wallet

Token balances each wallet holds

Wallet Balances

Per-wallet balance breakdown with states

Detailed wallet-level balances

Note: Total Fiat Value is the sum of all assets in the wallet at the time of export. It may differ from Asset Balances if data collection cycles are not aligned.

Tip: Active Platforms shows all chains TRES monitors for this wallet. If a chain is missing, add it in the wallet settings to start collecting data.
