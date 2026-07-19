# TRES Custodian Integration: Complete Knowledge Base

This comprehensive guide explains custodian integration in TRES, including supported custodians, credential requirements, configuration steps, user flows, and troubleshooting. This document serves as the primary knowledge base for the TRES-agent AI.

---

## What are Custodians?

A **custodian** is a qualified financial institution that specializes in safeguarding and managing digital assets on behalf of clients. In TRES, custodian integration allows you to:

- **Automatically Sync Holdings**: Import your custodial assets and balances
- **Track Transactions**: Monitor all custodian transactions and movements
- **Unified Portfolio View**: See all assets (custodial and non-custodial) in one place
- **Compliance Reporting**: Generate reports that include custodial holdings
- **Proof of Funds**: Provide evidence of custodial assets for compliance

**Purpose:** Helps organizations maintain real-time visibility of their digital asset holdings across multiple custodial platforms without manual data entry or file uploads.

### Custodial vs Non-Custodial Assets

| Type | Description | Examples | TRES Integration |
|------|-------------|----------|------------------|
| **Custodial** | Assets held by third-party custodian | Fireblocks, Coinbase Prime, Anchorage | Automatic sync via API |
| **Non-Custodial** | Assets in your own wallets | MetaMask, Ledger, Exchange accounts | Manual entry or wallet connection |

---

## Supported Custodians

TRES currently supports integration with the following custodians:

### 1. **Fireblocks**
**Type**: Enterprise-grade digital asset custody platform
**Specialization**: Institutional custody, DeFi, and trading infrastructure

**Data Types Available:**
- **Vaults**: Custodial vault information and balances
- **External Wallets**: Connected external wallet addresses
- **Internal Wallets**: Internal wallet configurations
- **Transaction Metadata**: Transaction details and metadata

**Use Cases:**
- Large institutional clients
- DeFi protocol integrations
- Multi-signature wallet management
- Compliance and audit requirements

### 2. **Coinbase Prime**
**Type**: Institutional trading and custody platform
**Specialization**: Professional trading, custody, and prime services

**Data Types Available:**
- **Vaults**: Prime custody vault balances and information

**Use Cases:**
- Institutional trading firms
- Asset managers
- Family offices
- Professional traders

### 3. **Anchorage Digital**
**Type**: Digital asset custody and financial services
**Specialization**: Institutional custody and staking services

**Data Types Available:**
- **Vaults**: Custodial vault information
- **Vault Addresses**: Associated wallet addresses

**Use Cases:**
- Institutional custody
- Staking services
- Compliance-focused organizations
- Long-term asset holding

### 4. **Copper**
**Type**: Digital asset custody and settlement
**Specialization**: Institutional custody and settlement services

**Data Types Available:**
- **Wallets**: Custodial wallet information and balances

**Use Cases:**
- Trading firms
- Asset managers
- Settlement services
- Multi-party custody

### 5. **BitGo**
**Type**: Digital asset custody and security
**Specialization**: Multi-signature security and institutional custody

**Data Types Available:**
- **Wallets**: BitGo wallet information and balances

**Use Cases:**
- Security-focused organizations
- Multi-signature requirements
- Institutional custody
- Compliance and audit needs

### 6. **Fordefi**
**Type**: Digital asset custody and security platform
**Specialization**: Institutional custody with advanced security features

**Data Types Available:**
- **Vaults**: Custodial vault information and balances
- **Wallets**: Wallet information and addresses

**Use Cases:**
- Security-focused institutions
- Advanced multi-party authorization
- Institutional custody requirements

---

## User Flows

### Flow A — Automatic Daily Sync
- **When:** The system runs automatically at scheduled intervals throughout the day
- **Preconditions:** You've connected at least one supported custodian (Fireblocks, Coinbase Prime, Anchorage, Copper, BitGo, or Fordefi) with valid API credentials
- **Steps:**
  1) System retrieves your current holdings from the custodian
  2) Data is validated and transformed into a consistent format
  3) Your accounts, balances, and wallet information are updated automatically
  4) Integration status changes from "Syncing" to "Completed"
- **Result:** Your dashboard shows the latest balance and account information from your custodian without any action needed
- **Pitfalls:**
  - If API credentials expire or are revoked, the sync will fail and status shows "Failed"
  - Large custodian accounts (thousands of wallets) may take longer to complete the first sync
  - Archived or deleted wallets at the custodian may be removed from your view

### Flow B — Monthly Proof of Funds (POF) Sync
- **When:** Runs automatically on the 1st of each month (if enabled for your integration)
- **Preconditions:** Your custodian integration has Proof of Funds enabled in its configuration
- **Steps:**
  1) System identifies all custodian integrations with POF enabled
  2) Fetches a complete snapshot of holdings from each custodian
  3) Applies any configured filters (e.g., only specific wallet types)
  4) Stores the data for compliance and reporting purposes
- **Result:** A dated snapshot of your assets is available for audits, reporting, or compliance needs
- **Pitfalls:**
  - POF sync may take longer than regular syncs if you have many holdings
  - Filters must be configured correctly to capture the right accounts

### Flow C — First-Time Integration Setup
- **When:** You first connect a new custodian to the platform
- **Preconditions:** You have admin access and valid API credentials from your custodian
- **Steps:**
  1) Provide custodian API credentials through the integration setup
  2) Configure which data types to sync (vaults, wallets, transactions, etc.)
  3) Choose how to organize the data (internal accounts, contacts, or annotations)
  4) Initial sync begins automatically
  5) Status shows "Syncing" until complete
- **Result:** All your custodian holdings appear in the platform, organized according to your configuration
- **Pitfalls:**
  - Incorrect API credentials cause immediate failure—verify credentials with your custodian first
  - Misconfigured data mapping may create accounts in unexpected locations
  - Very large custodian accounts may take 15-30 minutes for the initial sync

---

## Quick Reference Q&A

- **Q:** Which custodians are supported?  
  **A:** Fireblocks, Coinbase Prime, Anchorage, Copper, BitGo, and Fordefi. Each requires separate API credentials and setup.

- **Q:** How often does my data sync?  
  **A:** Automatically throughout the day at regular intervals. You'll always see recent data without manual uploads.

- **Q:** What happens if my sync fails?  
  **A:** The integration status shows "Failed" and syncs stop. Common causes are expired credentials or network issues. Check your API credentials and connection, then retry.

- **Q:** Can I manually trigger a sync?  
  **A:** Typically syncs run automatically, but your support team can trigger a manual sync if needed for your specific integration.

- **Q:** What data is imported from my custodian?  
  **A:** Depends on your configuration, but typically includes: wallet/vault names, balances, asset types, addresses, and optionally transaction metadata.

- **Q:** Will this delete or modify data in my custodian account?  
  **A:** No. The sync only reads data from your custodian—it never writes, deletes, or modifies anything at the custodian.

- **Q:** How do I know if a sync is running?  
  **A:** Check your integration status. "Syncing" means in progress, "Completed" means finished successfully, "Failed" means an error occurred.

- **Q:** What if I archive a wallet at my custodian?  
  **A:** Archived wallets may be removed from your view during the next sync, depending on your configuration settings.

- **Q:** Can I sync multiple custodians at once?  
  **A:** Yes. Each custodian is a separate integration with its own sync schedule and configuration.

- **Q:** How long does a sync take?  
  **A:** Usually a few seconds to a few minutes. Very large accounts with thousands of wallets may take 15-30 minutes on the first sync, then faster on subsequent syncs.

---

## Integration Requirements

### Prerequisites

Before connecting a custodian to TRES, ensure you have:

1. **Active Custodian Account**: Valid account with the custodian
2. **API Access**: API credentials and permissions from the custodian
3. **TRES Admin Access**: Admin role in your TRES organization
4. **Network Access**: Ability to make API calls to custodian services
5. **Compliance Approval**: Internal approval for custodian integration

### Technical Requirements

#### **API Credentials**
Each custodian requires specific API credentials:

##### **Fireblocks Requirements:**
```
- API Key: Your Fireblocks API key
- Private Key: RSA private key for API authentication
- Entity Name: Your organization's entity name in Fireblocks
- API URL: Fireblocks API endpoint (optional, defaults to production)
```

##### **Coinbase Prime Requirements:**
```
- Access Key: Coinbase Prime access key
- Passphrase: API passphrase
- Signing Key: Private key for request signing
- Portfolio ID: Your portfolio identifier
- Entity ID: Your entity identifier
```

##### **Anchorage Requirements:**
```
- API Key: Anchorage API key
- Entity Name: Your organization's entity name
```

##### **Copper Requirements:**
```
- API Key: Copper API key
- Prefix: Your organization prefix
```

##### **BitGo Requirements:**
```
- API Key: BitGo API key
- Additional credentials as required by BitGo
```

##### **Fordefi Requirements:**
```
- API Key: Fordefi API key
- Additional credentials as required by Fordefi
```

#### **Network Requirements**
- **Outbound HTTPS**: Port 443 access to custodian APIs
- **DNS Resolution**: Ability to resolve custodian API domains
- **Firewall Rules**: Allow outbound connections to custodian services
- **Proxy Configuration**: If using corporate proxy, ensure custodian APIs are whitelisted

#### **Security Requirements**
- **Credential Storage**: Secure storage of API credentials
- **Access Control**: Limited access to custodian credentials
- **Audit Logging**: Comprehensive logging of custodian API calls
- **Encryption**: All data transmission encrypted in transit

---

## How to Connect a Custodian

### Step 1: Prepare Custodian Credentials

#### **For Fireblocks:**
1. **Log into Fireblocks Console**
2. **Navigate to Settings → API Keys**
3. **Create New API Key**:
   - Name: "TRES Integration"
   - Permissions: Read-only access to vaults and transactions
   - IP Restrictions: Add TRES IP addresses if required
4. **Download Private Key**: Save the RSA private key securely
5. **Note API Key**: Copy the API key for TRES configuration

#### **For Coinbase Prime:**
1. **Log into Coinbase Prime**
2. **Navigate to API Settings**
3. **Create New API Key**:
   - Name: "TRES Integration"
   - Permissions: Read-only access to balances and transactions
   - IP Restrictions: Add TRES IP addresses if required
4. **Generate Credentials**: Create access key, passphrase, and signing key
5. **Note Portfolio ID**: Copy your portfolio identifier

#### **For Anchorage:**
1. **Log into Anchorage Console**
2. **Navigate to API Management**
3. **Create New API Key**:
   - Name: "TRES Integration"
   - Permissions: Read-only access to vault information
   - IP Restrictions: Add TRES IP addresses if required
4. **Note Entity Name**: Copy your organization's entity name

### Step 2: Configure Custodian Integration in TRES

#### **Access Integration Settings:**
1. **Log into TRES Dashboard**
2. **Navigate to Settings → Integrations**
3. **Click "Add Integration"**
4. **Select "Custodian" as integration type**

#### **Select Custodian:**
1. **Choose your custodian** from the supported list:
   - Fireblocks
   - Coinbase Prime
   - Anchorage
   - Copper
   - BitGo
   - Fordefi

#### **Enter Credentials:**
1. **Integration Name**: Give your integration a descriptive name
2. **API Credentials**: Enter the required credentials for your custodian
3. **Entity Information**: Provide entity name and other required details

#### **Configure Data Types:**
1. **Select Data Types**: Choose which data types to sync:
   - Vaults (recommended)
   - Wallets (if available)
   - Transactions (if available)
   - External addresses (if available)

2. **Configure Sync Settings**:
   - **Sync Frequency**: How often to sync data
   - **Data Retention**: How long to keep historical data
   - **Error Handling**: How to handle sync errors

### Step 3: Test Integration

#### **Validate Credentials:**
1. **Click "Test Connection"**
2. **Verify API Access**: Ensure TRES can connect to custodian
3. **Check Permissions**: Confirm required permissions are granted
4. **Review Error Messages**: Address any configuration issues

#### **Initial Data Sync:**
1. **Trigger Initial Sync**: Start the first data synchronization
2. **Monitor Progress**: Watch the sync progress in TRES dashboard
3. **Verify Data**: Check that custodian data appears correctly
4. **Review Logs**: Check integration logs for any issues

### Step 4: Configure Data Mapping

#### **Asset Mapping:**
1. **Review Asset List**: Check which assets were imported
2. **Map to Internal Accounts**: Associate custodian assets with TRES accounts
3. **Configure Asset Classes**: Ensure proper asset classification
4. **Set Up Cost Basis**: Configure cost basis calculation for custodian assets

#### **Transaction Mapping:**
1. **Review Transaction Types**: Check imported transaction types
2. **Configure Transaction Categories**: Set up transaction categorization
3. **Map to Internal Accounts**: Associate transactions with TRES accounts
4. **Set Up Rules**: Create rules for automatic transaction processing

### Step 5: Enable Ongoing Sync

#### **Schedule Regular Sync:**
1. **Set Sync Frequency**: Configure how often to sync data
2. **Choose Sync Times**: Select optimal times for data synchronization
3. **Configure Notifications**: Set up alerts for sync failures
4. **Monitor Performance**: Track sync performance and reliability

#### **Set Up Monitoring:**
1. **Dashboard Monitoring**: Monitor integration status in TRES dashboard
2. **Error Alerts**: Set up alerts for integration failures
3. **Performance Metrics**: Track sync times and success rates
4. **Audit Logs**: Review integration logs regularly

---

## Data Types and Configuration

### Available Data Types by Custodian

| Custodian | Vaults | Wallets | Transactions | External Addresses |
|-----------|--------|---------|--------------|-------------------|
| **Fireblocks** | ✅ | ✅ | ✅ | ✅ |
| **Coinbase Prime** | ✅ | ❌ | ❌ | ❌ |
| **Anchorage** | ✅ | ❌ | ❌ | ✅ |
| **Copper** | ❌ | ✅ | ❌ | ❌ |
| **BitGo** | ❌ | ✅ | ❌ | ❌ |
| **Fordefi** | ✅ | ✅ | ❌ | ❌ |

### Data Type Configuration

#### **Vaults Configuration:**
```json
{
  "data_type": "vault",
  "sync_frequency": "hourly",
  "include_balances": true,
  "include_metadata": true,
  "proof_of_funds": {
    "enabled": true,
    "filters": [
      {
        "type": "vault_name_contains",
        "value": "main"
      }
    ]
  }
}
```

#### **Wallets Configuration:**
```json
{
  "data_type": "wallet",
  "sync_frequency": "hourly",
  "include_balances": true,
  "include_addresses": true,
  "include_metadata": true
}
```

#### **Transactions Configuration:**
```json
{
  "data_type": "transactions",
  "sync_frequency": "daily",
  "include_metadata": true,
  "date_range": "last_30_days",
  "transaction_types": ["deposit", "withdrawal", "transfer"]
}
```

### How Data Is Organized

Based on your configuration, custodian data maps to different objects:
- **Internal Accounts:** Represent your own wallets/vaults in your account structure
- **Contacts:** Represent external wallets or counterparties you interact with
- **Transaction Comments:** Attach custodian metadata (notes, tags) to existing transactions
- **Ignore:** Skip certain data types entirely if not needed

### Data Import Details

**What Gets Imported:**
- Wallet and vault names, IDs, and hierarchies
- Current asset balances for each account
- Cryptocurrency types (Bitcoin, Ethereum, stablecoins, etc.)
- Wallet addresses and deposit addresses
- Optionally: transaction metadata like notes, tags, or descriptions

**Limits:**
- Syncs process data in batches for reliability
- Very large accounts may take 15-30 minutes for initial sync
- Subsequent syncs are faster because they only process changes
- No hard limit on number of wallets, vaults, or assets

---

## Key Concepts

- **Custodian:** A qualified financial institution (like Fireblocks or Coinbase Prime) that securely stores and manages your digital assets
- **Custodial Holdings:** The crypto assets (tokens, coins) held by a custodian on your behalf
- **Integration:** A configured connection between the platform and one of your custodian accounts using API credentials
- **Sync Status:** The current state of your integration—either "Syncing" (in progress), "Completed" (successful), or "Failed" (error)
- **Data Types:** Different categories of information from custodians—such as vaults, wallets, addresses, or transaction metadata

### How Custodian Sync Works (High-Level)

Custodian Sync automatically connects to your custodian platforms and imports your holdings into the system. When you set up a custodian integration, you provide API credentials that allow read-only access to your custodian data.

The system runs scheduled syncs throughout the day. Each sync retrieves the latest data from your custodian, validates and standardizes it, then updates your accounts and balances. This three-step process ensures consistency regardless of which custodian you use.

You can configure how different data types map into your system. For example, you might import custodian vaults as "Internal Accounts" so they appear in your account hierarchy, or import external wallets as "Contacts" so they're available for transaction categorization.

The sync handles large custodian accounts efficiently by processing data in batches. If you have thousands of wallets or addresses, the system fetches and processes them in chunks to avoid timeouts. Syncs automatically resume if interrupted, so you never lose progress on large initial imports.

Monthly Proof of Funds syncs provide compliance snapshots. If enabled, the system takes a complete inventory of your holdings on the first of each month and stores it for audit trails and regulatory reporting.

---

## Security and Compliance

### Security Best Practices

#### **Credential Management:**
- **Secure Storage**: Store API credentials in secure, encrypted storage
- **Access Control**: Limit access to custodian credentials to authorized personnel
- **Regular Rotation**: Rotate API credentials regularly (every 90 days)
- **Audit Access**: Log all access to custodian credentials

#### **API Security:**
- **IP Restrictions**: Restrict API access to specific IP addresses
- **Rate Limiting**: Implement rate limiting to prevent abuse
- **Monitoring**: Monitor API usage for suspicious activity
- **Error Handling**: Implement proper error handling and logging

#### **Data Security:**
- **Encryption**: Encrypt all data in transit and at rest
- **Access Logging**: Log all data access and modifications
- **Data Retention**: Implement appropriate data retention policies
- **Backup Security**: Secure backup and recovery procedures

### Compliance Considerations

#### **Regulatory Requirements:**
- **Know Your Customer (KYC)**: Ensure custodian meets KYC requirements
- **Anti-Money Laundering (AML)**: Verify AML compliance procedures
- **Data Protection**: Ensure compliance with data protection regulations
- **Audit Requirements**: Maintain audit trails for regulatory compliance

#### **Proof of Funds (POF):**
- **POF Configuration**: Configure POF for relevant custodian data
- **Monthly Reports**: Generate monthly POF reports
- **Audit Trail**: Maintain comprehensive audit trails
- **Documentation**: Keep detailed documentation of POF processes

---

## Troubleshooting Common Issues

### Connection Issues

#### **Issue: Cannot Connect to Custodian API**
**Symptoms:**
- Integration fails to connect
- API authentication errors
- Network timeout errors

**Solutions:**
1. **Verify Credentials**: Check API key and other credentials
2. **Check Network Access**: Ensure outbound HTTPS access to custodian
3. **Review IP Restrictions**: Verify IP addresses are whitelisted
4. **Check API Status**: Verify custodian API is operational
5. **Review Firewall Rules**: Ensure firewall allows custodian API access

#### **Issue: Authentication Failures**
**Symptoms:**
- 401 Unauthorized errors
- Invalid credentials errors
- Permission denied errors

**Solutions:**
1. **Verify API Key**: Check API key is correct and active
2. **Check Private Key**: Verify private key format and validity
3. **Review Permissions**: Ensure API key has required permissions
4. **Check Entity Name**: Verify entity name matches custodian records
5. **Contact Custodian Support**: Escalate to custodian technical support

### Data Sync Issues

#### **Issue: Data Not Syncing**
**Symptoms:**
- No data appears in TRES
- Sync shows as failed
- Partial data synchronization

**Solutions:**
1. **Check Sync Status**: Review integration status in TRES dashboard
2. **Review Error Logs**: Check integration logs for error messages
3. **Verify Data Types**: Ensure selected data types are available
4. **Check Permissions**: Verify API permissions include data access
5. **Test Manual Sync**: Try triggering manual sync to test

#### **Issue: Incorrect Data Mapping**
**Symptoms:**
- Assets appear in wrong accounts
- Incorrect balances displayed
- Missing transaction data

**Solutions:**
1. **Review Asset Mapping**: Check asset mapping configuration
2. **Verify Account Configuration**: Ensure internal accounts are set up correctly
3. **Check Data Filters**: Review any data filters that might exclude data
4. **Validate Custodian Data**: Verify data is correct in custodian system
5. **Reconfigure Mapping**: Update mapping configuration as needed

### Performance Issues

#### **Issue: Slow Data Sync**
**Symptoms:**
- Sync takes longer than expected
- Timeout errors during sync
- Incomplete data synchronization

**Solutions:**
1. **Check Network Performance**: Monitor network latency to custodian
2. **Review Data Volume**: Consider reducing data volume or frequency
3. **Optimize Sync Schedule**: Adjust sync timing to off-peak hours
4. **Check Custodian Performance**: Verify custodian API performance
5. **Contact Support**: Escalate performance issues to TRES support

### Quick Reference Error Table

| Status / Symptom | Likely Cause | Fix |
|------------------|--------------|-----|
| Status: "Failed" | Expired or invalid API credentials | Re-enter valid credentials in your integration settings and retry |
| Status: "Syncing" for over 30 minutes | Very large account or network issue | Wait—first syncs can take time. If stuck after 1 hour, contact support |
| Missing wallets or vaults | Custodian data is archived or filtered out | Check custodian to confirm wallets are active; review filter settings in configuration |
| Status: "Failed" after working previously | Custodian API credentials revoked or changed | Verify credentials haven't expired; regenerate API keys at custodian if needed |
| Balances don't match custodian | Sync hasn't completed yet or in progress | Wait for "Completed" status; refresh after sync finishes |
| Duplicate accounts appearing | Multiple syncs or misconfiguration | Contact support to review and clean up configuration |

---

## Monitoring and Maintenance

### Regular Monitoring

#### **Daily Tasks:**
- **Check Sync Status**: Verify all integrations are syncing successfully
- **Review Error Logs**: Check for any integration errors or warnings
- **Monitor Performance**: Track sync times and success rates
- **Verify Data Accuracy**: Spot-check custodian data against TRES data

#### **Weekly Tasks:**
- **Review Integration Health**: Assess overall integration performance
- **Check Credential Expiry**: Monitor API credential expiration dates
- **Update Documentation**: Keep integration documentation current
- **Review Security Logs**: Check for any security-related issues

#### **Monthly Tasks:**
- **Comprehensive Review**: Full review of all custodian integrations
- **Performance Analysis**: Analyze sync performance trends
- **Security Assessment**: Review security configurations and access
- **Compliance Check**: Verify compliance with regulatory requirements

### Maintenance Procedures

#### **Credential Rotation:**
1. **Plan Rotation**: Schedule credential rotation every 90 days
2. **Generate New Credentials**: Create new API credentials with custodian
3. **Update TRES Configuration**: Update credentials in TRES
4. **Test New Credentials**: Verify new credentials work correctly
5. **Deactivate Old Credentials**: Remove old credentials from custodian

#### **Integration Updates:**
1. **Monitor Custodian Changes**: Stay informed about custodian API changes
2. **Test Updates**: Test any custodian API updates in development
3. **Update Configuration**: Update TRES configuration as needed
4. **Deploy Changes**: Deploy updates to production environment
5. **Monitor Post-Deployment**: Watch for issues after deployment

---

## Best Practices

### Integration Planning

#### **Before Integration:**
- **Assess Requirements**: Determine which data types you need
- **Review Custodian Capabilities**: Understand what each custodian offers
- **Plan Data Mapping**: Plan how to map custodian data to TRES
- **Consider Compliance**: Ensure integration meets compliance requirements
- **Test in Development**: Test integration in development environment first

#### **During Integration:**
- **Start Simple**: Begin with basic data types and expand gradually
- **Monitor Closely**: Watch integration closely during initial setup
- **Document Everything**: Keep detailed documentation of configuration
- **Test Thoroughly**: Test all aspects of the integration
- **Plan for Errors**: Have contingency plans for integration failures

#### **After Integration:**
- **Regular Monitoring**: Monitor integration performance regularly
- **Keep Updated**: Stay current with custodian API changes
- **Maintain Security**: Keep security configurations up to date
- **Review Performance**: Regularly review and optimize performance
- **Plan for Growth**: Plan for scaling as your needs grow

### Security Best Practices

#### **Credential Security:**
- **Use Strong Credentials**: Generate strong, unique API credentials
- **Limit Permissions**: Grant only necessary permissions to API credentials
- **Regular Rotation**: Rotate credentials regularly
- **Secure Storage**: Store credentials in secure, encrypted storage
- **Access Control**: Limit access to credentials to authorized personnel

#### **Network Security:**
- **IP Restrictions**: Restrict API access to specific IP addresses
- **VPN Access**: Use VPN for additional security if needed
- **Firewall Rules**: Implement appropriate firewall rules
- **Monitor Traffic**: Monitor network traffic for suspicious activity
- **Regular Updates**: Keep network security configurations updated

---

## Related Documentation
- [User Roles and Capabilities](./user-roles/README.md) - Required permissions for custodian integration
- [Authentication Configuration](./authentication/README.md) - Security requirements for integrations
- [Organization Settings](./organization-settings/README.md) - Organization-level configuration
- [Reports Module](../modules/reports/README.md) - Generating reports with custodian data

---

## Summary

Custodian integration in TRES provides:

- **Automated Data Sync**: Seamless import of custodial holdings and transactions throughout the day
- **Unified Portfolio View**: Complete view of all assets in one platform
- **Compliance Support**: Built-in compliance and audit capabilities including Proof of Funds
- **Enterprise Security**: Bank-grade security for sensitive financial data with read-only access
- **Scalable Solution**: Support for multiple custodians (Fireblocks, Coinbase Prime, Anchorage, Copper, BitGo, Fordefi) and growing portfolios
- **Real-Time Visibility**: Maintain current holdings without manual data entry or file uploads

By properly configuring custodian integration, you can ensure that your TRES platform provides a complete and accurate view of your digital asset portfolio, including both custodial and non-custodial holdings, while maintaining the highest security and compliance standards.
