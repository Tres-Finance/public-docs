# Automations Page

## Overview

The Automations page empowers you to automate repetitive tasks and data management across your TRES platform. By creating automated workflows based on specific conditions, you can streamline transaction tagging, generate recurring reports, and consolidate transactions for cleaner ledger management. This reduces manual work, ensures consistency, and saves significant time in your financial operations.

Automations enable you to:

- **Automatically tag transactions** based on specific conditions (wallet, platform, asset, contact, etc.)
- **Generate recurring reports** on a scheduled basis without manual intervention
- **Create transaction roll-ups** to consolidate similar transactions for a cleaner ledger

All automations run automatically based on the conditions you define, ensuring consistent data management across your organization.

## Page Structure

The Automations page displays all your configured automations in a list format, showing key information about each automation's purpose, conditions, priority, status, and creation date.

### Automation Cards

Each automation card displays:

- **Automation Name**: The primary action (e.g., "Tag transactions", "Generate Recurring Report")
- **Description/Conditions**: The specific conditions that trigger the automation (e.g., "When platform is ethereum and wallet (sender) is X then activity is Y")
- **Priority**: High, Medium, or Low priority level
- **Creation Date**: When the automation was created
- **Status**: ACTIVE (running), PAUSED, or INACTIVE
- **Actions Menu**: Three-dot menu for additional actions

## Available Automation Types

When you click "Add Automation," you'll see three main automation templates:

### 1. Generate Recurring Report

**Purpose:** Automatically generate and deliver reports on a recurring schedule.

**Use Case:** e.g., generate ledger report every end of a month, for wallet X, platform Y

**Key Features:**

- Schedule reports on a recurring basis (daily, weekly, monthly, quarterly, annually)
- Define specific filters for each report (wallets, platforms, assets, date ranges)
- Automatically deliver reports to specified recipients
- Ensure consistent reporting for compliance and internal use
- Eliminate manual report generation tasks

**Example Scenarios:**

- Monthly ledger report for all Ethereum transactions
- Weekly balance trends report for specific wallets
- Quarterly cost basis summary for all assets

### 2. Tag Transactions

**Purpose:** Automatically apply tags to transactions based on specific conditions you define.

**Use Case:** e.g., when a transaction in wallet X is being made, set tag to Y

**Key Features:**

- Automatically tag transactions based on multiple conditions
- Support for conditions based on:
  - **Platform**: Filter by specific blockchain networks (Ethereum, Solana, Polygon, etc.)
  - **Asset**: Filter by specific assets (BTC, ETH, stablecoins, etc.)
  - **Wallet**: Filter by specific wallet addresses or groups
  - **Contact**: Filter by known contacts or counterparties
  - **Method ID**: Filter by specific transaction types or smart contract interactions
  - **Saved filter view**: Apply custom saved filters as conditions
- Set priority levels (High, Medium, Low) for execution order
- Consistent tagging across all your transactions
- Support for multiple tags per transaction

**Example Scenarios:**

- Tag all transactions on Ethereum platform as "ETH Transactions"
- Tag all transactions from wallet group "Marketing" as "Marketing Expenses"
- Tag all transactions sent to a specific contact as "Payments - [Contact Name]"
- Tag all transactions with a specific method ID as "Staking Rewards"
- Tag all transactions involving a specific asset as "USDC Operations"

**Common Tags:**

- Activity tags (e.g., EXPENSE, REVENUE, TRANSFER)
- Category tags (e.g., SALARY, OPERATIONAL, INVESTMENT)
- Department/Group tags (e.g., FINANCE, IT, MARKETING)
- Status tags (e.g., APPROVED, PENDING, REVIEW)

### 3. Create Transaction Roll-Up

**Purpose:** Unite transactions with similar traits for a cleaner ledger and a one-entry sync to ERP systems.

**Use Case:** Consolidate multiple small transactions into a single entry for accounting purposes

**Key Features:**

- Group similar transactions together
- Reduce ledger clutter
- Simplify ERP synchronization (one entry instead of many)
- Define grouping criteria (date range, asset, wallet, tag, etc.)
- Automatic consolidation

**Example Scenarios:**

- Roll up all daily USDC transfers from various exchanges into a single weekly entry
- Consolidate monthly recurring payments into a single transaction
- Group all small gas fee transactions into a single monthly "Ethereum Fees" entry
- Combine multiple trading activities on the same day into a single trading roll-up

## Filters

The Automations page provides multiple filtering options to help you find specific automations:

### 1. Search

Use the search bar to find automations by:

- Automation name
- Tags or activities applied
- Platform names
- Wallet or contact names
- Method IDs

### 2. All Time Filter

Filter automations by creation date:

- **All Time** (default): Shows all automations regardless of creation date
- Custom date ranges (if available)

### 3. Status Filter

Filter by automation status:

- **Active**: Currently running and executing according to their conditions
- **Paused**: Temporarily stopped but configuration maintained
- **Inactive**: Disabled or deactivated automations

### 4. Type Filter

Filter by automation type:

- **Tag Transactions**: All transaction tagging automations
- **Generate Recurring Report**: All report generation automations
- **Create Transaction Roll-Up**: All roll-up consolidation automations

## Actions

### Global Actions

**Add Automation Button:**

- Located in the page header
- Opens the automation templates modal
- Choose from three available automation types
- Click "Use Template" to begin configuring your automation

### Per-Automation Actions

Each automation card includes an actions menu (three dots) with the following options:

- **Edit**: Modify the automation's conditions, priority, or settings
- **Duplicate**: Create a copy of the automation with the same configuration
- **Pause/Resume**: Temporarily stop or restart the automation
- **Delete**: Remove the automation permanently (requires confirmation)

**Note:** Some actions may vary based on the automation type and current status.

## Creating a New Automation

### Step 1: Choose Template

1. Click the "Add Automation" button
2. Select one of three automation types:
   - Generate Recurring Report
   - Tag Transactions
   - Create Transaction Roll-Up
3. Click "Use Template"

### Step 2: Configure Conditions

Each automation type has its own configuration interface:

**For Tag Transactions:**

- Define trigger conditions (platform, asset, wallet, contact, method ID, saved filter)
- Set the tag or activity to apply
- Set priority level (High, Medium, Low)
- Add multiple conditions if needed

**For Generate Recurring Report:**

- Select report type
- Define schedule (daily, weekly, monthly, etc.)
- Set filters (wallets, platforms, assets, date ranges)
- Configure delivery method and recipients
- Name the automation

**For Create Transaction Roll-Up:**

- Define grouping criteria
- Set date range for roll-ups
- Configure when and how to consolidate
- Define export parameters
- Name the automation

### Step 3: Activate

- Review your configuration
- Click "Create" or "Activate"
- The automation will appear in your list with "ACTIVE" status

## Priority Levels

Automations can have different priority levels that determine execution order:

### High Priority

Executed first and most frequently.

**Use For:**

- Critical transaction tagging (regulatory or compliance-related)
- Important operational automations
- High-frequency rules that should be processed quickly

**Example:** Tag all transactions to approved contacts immediately upon receipt.

### Medium Priority

Standard execution frequency and order.

**Use For:**

- Regular operational tasks
- Standard categorization automations
- Most common use cases

**Example:** Tag transactions from specific wallets as "Internal Transfers."

### Low Priority

Executed last, typically for less critical automations.

**Use For:**

- Background processing
- Optional categorizations
- Non-urgent automations

**Example:** Tag all transactions with low-value amounts as "Micro-transactions."

## Automation Status Indicators

Automations can have different statuses:

- **ACTIVE**: Automation is running and executing based on its conditions
- **PAUSED**: Automation is temporarily stopped but configuration is preserved
- **INACTIVE**: Automation is disabled and not executing

## Common Workflows

### Setting Up Automatic Transaction Tagging

**Scenario:** Tag all transactions from a specific vendor as "Vendor Payments"

1. Click "Add Automation"
2. Select "Tag Transactions"
3. Set condition: "When contact (sender) is [Vendor Name]"
4. Set tag to apply: "VENDOR PAYMENT"
5. Set priority to High
6. Click "Create"
7. The automation will automatically tag all matching transactions going forward

### Setting Up Recurring Monthly Reports

**Scenario:** Generate a monthly ledger report for all Ethereum transactions

1. Click "Add Automation"
2. Select "Generate Recurring Report"
3. Choose report type: "Transaction Ledger"
4. Set schedule to "Monthly" (last day of month)
5. Set filters:
   - Platform: Ethereum
   - Date range: All time
6. Add recipients (email addresses)
7. Name the automation: "Monthly Ethereum Ledger Report"
8. Click "Create"
9. Reports will be generated and delivered automatically each month

### Creating Transaction Roll-Ups

**Scenario:** Consolidate daily DEX trading transactions into weekly summaries

1. Click "Add Automation"
2. Select "Create Transaction Roll-Up"
3. Set grouping criteria:
   - Platform: Ethereum
   - Asset: Any DEX token
   - Activity: Trading
4. Set roll-up frequency: Weekly
5. Configure export settings
6. Name the automation: "Weekly DEX Trading Summary"
7. Click "Create"
8. Similar transactions will be automatically consolidated each week

### Managing Automation Priorities

**Scenario:** Multiple automations with potential conflicts

1. Review all existing automations in the list
2. Identify automations that might conflict (e.g., tagging the same transaction differently)
3. Adjust priorities:
   - Set most specific rules to High priority
   - Set broader/general rules to Medium or Low priority
   - Set generic fallback rules to Low priority
4. Edit automations as needed to refine conditions
5. Test by checking transaction tags on recent transactions

## Tips

- **Start Specific, Then General:** Create specific tagging automations first (High priority), then add more general fallback rules (Lower priority)
- **Use Descriptive Names:** Name your automations clearly to make them easy to identify and manage
- **Test Before Deploying:** When creating new automations, review the conditions carefully and test with a small set of transactions first
- **Monitor Execution:** Regularly check automation status and review logs if available to ensure they're working as expected
- **Organize by Priority:** Use High priority for critical, time-sensitive automations and Low priority for optional categorizations
- **Combine Multiple Conditions:** Use multiple conditions to create precise automation rules and avoid unintended tagging
- **Regular Review:** Periodically review and update your automations as your workflows evolve
- **Document Complex Rules:** For complex automations, document the logic and reasoning for future reference
- **Use Roll-Ups Sparingly:** Transaction roll-ups are powerful but use them carefully to avoid losing important transaction details in your accounting
- **Coordinate with Team:** If working with a team, communicate about automation changes to avoid conflicts or duplicate rules

## Requesting Custom Automations

If you can't find an automation type that fits your needs, click "Request Automation" in the templates modal to reach out to the TRES team. They can help design and implement custom automations tailored to your specific requirements.

## Security and Data Integrity

- All automations respect existing data and permissions
- Automations cannot modify historical transactions
- Tagging automations apply to new transactions as they are created
- Review automations regularly to ensure accuracy
- Pause or delete automations that are no longer needed to maintain data integrity
