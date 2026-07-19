# Alerts Page

## Overview

The Alerts page enables you to set up automated notifications that monitor your digital asset portfolio in real-time. By creating custom alerts based on specific conditions, you can stay informed about important portfolio changes, market movements, transaction activity, and validator performance without constantly monitoring your accounts.

Alerts help you:

- **Monitor portfolio exposure** to specific asset classes and maintain balanced risk
- **Track price movements** and market opportunities in real-time
- **Detect unusual transaction activity** such as large transfers or unexpected movements
- **Monitor validator performance** for Ethereum 2.0 staking operations
- **Respond quickly** to important events affecting your digital assets

All alerts can be delivered via email, Slack, or other notification channels configured in your account settings, ensuring you never miss critical information about your portfolio.

## Page Structure

The Alerts page displays all your configured alerts in a card-based layout, making it easy to review and manage your notification settings at a glance.

### Alert Cards

Each alert card displays the following information:

- **Alert Icon**: Visual indicator representing the alert type
- **Alert Name/Type**: The category of alert (e.g., "Exposure To Asset Class", "Price Change on Asset Class")
- **Condition Description**: Specific conditions that trigger the alert (e.g., "When the price of Bitcoin is greater than $50,000 USD")
- **Real-Time Badge**: "REAL TIME ALERT" badge for alerts that monitor continuously
- **Creation Date**: When the alert was created
- **Status Indicator**: Visual status with colored badge
  - **ACTIVE**: Alert is currently monitoring and will send notifications
  - **INACTIVE**: Alert is disabled and will not send notifications
- **Actions Menu**: Three-dot menu for managing the alert

## Available Alert Types

When you click "Add Alert," you'll see four alert templates designed for different monitoring needs:

### 1. Exposure To Asset Class

**Purpose:** Get notified when an asset class exceeds or falls below a certain percentage or fiat value of your entire portfolio.

**Description:** This will help you manage risk and maintain balance in your portfolio by alerting you when your exposure to specific asset classes becomes too high or too low.

**Use Cases:**

- Maintain target allocation percentages (e.g., alert if Bitcoin exceeds 40% of portfolio)
- Prevent over-concentration in a single asset or asset class
- Ensure diversification across multiple asset types
- Monitor exposure thresholds for risk management compliance

**Configuration Options:**

- Select specific asset class (Bitcoin, Ethereum, Stablecoins, etc.)
- Set threshold type: OVER or UNDER
- Define threshold value: percentage of portfolio or fiat amount (USD)
- Choose specific wallet or monitor entire portfolio

**Example:**
"When exposure to 1000SATS (Ordinals) asset is UNDER 11.0 USD in wallet Aleo Delegator"

### 2. Tx Activity

**Purpose:** Get notified whenever specific transactions occur, such as large transfers or unusual activity, to keep track of critical account movements.

**Description:** Transaction activity alerts help you monitor wallet activity and detect unusual or significant transactions in real-time.

**Use Cases:**

- Monitor large withdrawals or deposits
- Detect unexpected transfers from your wallets
- Track transactions above/below specific thresholds
- Monitor activity in critical wallets (treasury, custody, hot wallets)
- Receive alerts for any transaction in high-security wallets

**Configuration Options:**

- Select specific wallet(s) to monitor
- Set transaction threshold: OVER or UNDER specific fiat amount
- Filter by transaction type (inflow, outflow, all)
- Choose specific assets or monitor all assets

**Example:**
"Transaction UNDER 45.0 USD in wallet test"

### 3. Price Change on Asset Class

**Purpose:** Get notified when an asset's class price hits a target value or changes by a chosen percentage, keeping you informed of important market movements.

**Description:** Real-time price monitoring alerts help you stay informed about market opportunities and risks.

**Badge:** 🔴 REAL TIME ALERT

**Use Cases:**

- Buy/sell opportunity alerts (e.g., alert when ETH drops below $2,000)
- Track price targets for portfolio rebalancing
- Monitor volatility and significant price swings
- Stay informed about market movements for specific assets

**Configuration Options:**

- Select specific asset class
- Set price condition: GREATER THAN or LESS THAN
- Define target price in USD or other fiat currency
- Option to set percentage change alerts

**Examples:**

- "When the price of 00 Token is greater than 324,234 USD"
- "When the price of AltLayer is less than 33.0 USD"
- "When the price of Blur is less than 23.0 USD"

**Note:** Price alerts are monitored continuously in real-time and will trigger as soon as the condition is met.

### 4. Slashing Monitoring

**Purpose:** Receive alerts if any Ethereum 2.0 validators you're monitoring are penalized for misbehavior or inactivity.

**Description:** Ensure you're aware of any issues affecting network security and stability by monitoring validator performance and penalties.

**Use Cases:**

- Monitor your own Ethereum 2.0 validator nodes
- Track validators you've delegated stake to
- Receive immediate notification of slashing events
- Maintain awareness of validator health and performance
- Respond quickly to infrastructure issues

**Configuration Options:**

- Select specific validator(s) to monitor
- Set alert triggers for slashing events
- Monitor for inactivity penalties
- Track validator effectiveness and uptime

**Important:** This alert type is specifically designed for Ethereum 2.0 Proof of Stake validators and requires validator addresses or indices to be configured.

## Filters

The Alerts page provides filtering options to help you find specific alerts:

### Type Filter

Filter alerts by type:

- **All Types** (default): Shows all alerts
- **Exposure To Asset Class**: Portfolio exposure alerts only
- **Tx Activity**: Transaction activity alerts only
- **Price Change on Asset Class**: Price monitoring alerts only
- **Slashing Monitoring**: Validator slashing alerts only

### Pagination

Navigate through multiple pages of alerts with:

- Items per page selector (20, 50, 100)
- Total alert count displayed
- Page navigation controls

## Creating a New Alert

### Step 1: Choose Alert Type

1. Click the "Add Alert" button in the page header
2. Review the four available alert templates
3. Select the alert type that matches your monitoring need
4. Click "Use Template"

### Step 2: Configure Alert Conditions

Each alert type has its own configuration interface:

**For Exposure To Asset Class:**

1. Select the asset class to monitor
2. Choose condition: OVER or UNDER
3. Set threshold value (USD or percentage)
4. Select wallet(s) or choose entire portfolio
5. Name your alert (optional but recommended)

**For Tx Activity:**

1. Select wallet(s) to monitor
2. Set transaction amount threshold
3. Choose condition: OVER or UNDER
4. Select transaction direction (inflow, outflow, or both)
5. Filter by specific assets (optional)
6. Name your alert

**For Price Change on Asset Class:**

1. Select the asset to monitor
2. Choose condition: GREATER THAN or LESS THAN
3. Set target price in USD
4. Name your alert

**For Slashing Monitoring:**

1. Enter validator address(es) or indices
2. Configure notification preferences
3. Name your alert

### Step 3: Set Notification Preferences

- Choose notification channels (email, Slack, etc.)
- Set notification frequency (immediate, digest, etc.)
- Define quiet hours (optional)

### Step 4: Activate

- Review your configuration
- Click "Create" or "Activate"
- The alert will appear in your list with "ACTIVE" status

## Managing Alerts

### Activating/Deactivating Alerts

To toggle an alert's status:

1. Locate the alert in the list
2. Click the three-dot actions menu
3. Select "Activate" or "Deactivate"
4. The status badge will update immediately

**Note:** Inactive alerts do not send notifications but retain their configuration for future use.

### Editing Alerts

To modify an alert's settings:

1. Click on the alert card or use the actions menu
2. Select "Edit"
3. Modify conditions, thresholds, or notification settings
4. Click "Save"

### Deleting Alerts

To permanently remove an alert:

1. Click the three-dot actions menu on the alert card
2. Select "Delete"
3. Confirm the deletion

**Warning:** Deleted alerts cannot be recovered. Consider deactivating instead if you may need the alert again.

### Duplicating Alerts

To create a similar alert:

1. Click the three-dot actions menu
2. Select "Duplicate"
3. Modify the duplicated alert as needed
4. Save the new alert

## Real-Time Alerts vs. Standard Alerts

### Real-Time Alerts

Alerts marked with the "REAL TIME ALERT" badge (such as Price Change alerts) are monitored continuously and trigger immediately when conditions are met.

**Characteristics:**

- Continuous monitoring
- Immediate notifications (within seconds)
- Ideal for time-sensitive situations
- Higher resource usage

**Best For:**

- Price-based trading opportunities
- Critical threshold breaches
- Time-sensitive risk management

### Standard Alerts

Standard alerts (such as Exposure To Asset Class) are evaluated periodically (e.g., every 15 minutes, hourly, or daily depending on configuration).

**Characteristics:**

- Periodic monitoring
- Notifications sent on evaluation cycle
- More efficient resource usage
- Suitable for most monitoring needs

**Best For:**

- Portfolio rebalancing
- Daily/weekly exposure checks
- Transaction summaries
- Long-term monitoring

## Common Workflows

### Setting Up Portfolio Exposure Monitoring

**Scenario:** Ensure Bitcoin never exceeds 30% of your total portfolio

1. Click "Add Alert"
2. Select "Exposure To Asset Class"
3. Configure:
   - Asset: Bitcoin (BTC)
   - Condition: OVER
   - Threshold: 30% (or equivalent USD amount)
   - Wallet: All wallets
4. Set notification channel to email
5. Name: "BTC Exposure - Max 30%"
6. Click "Create"

### Setting Up Price Alerts for Trading

**Scenario:** Buy ETH when it drops below $2,000

1. Click "Add Alert"
2. Select "Price Change on Asset Class"
3. Configure:
   - Asset: Ethereum (ETH)
   - Condition: LESS THAN
   - Target Price: $2,000 USD
4. Enable real-time monitoring
5. Set immediate email notification
6. Name: "ETH Buy Opportunity - Under $2K"
7. Click "Create"

### Monitoring Large Transactions

**Scenario:** Receive alerts for any transaction over $100,000 in treasury wallets

1. Click "Add Alert"
2. Select "Tx Activity"
3. Configure:
   - Wallets: Treasury Wallet 1, Treasury Wallet 2
   - Condition: OVER
   - Threshold: $100,000 USD
   - Direction: Both inflows and outflows
4. Set notification to email + Slack
5. Name: "Large Treasury Movements"
6. Click "Create"

### Validator Slashing Monitoring

**Scenario:** Monitor your Ethereum 2.0 validators for slashing events

1. Click "Add Alert"
2. Select "Slashing Monitoring"
3. Enter validator addresses or indices
4. Enable immediate notifications
5. Set critical alert notification (email + SMS if available)
6. Name: "ETH2 Validator Slashing Monitor"
7. Click "Create"

## Alert Notification Channels

Alerts can be delivered through multiple channels:

### Email

- Default notification channel
- Includes full alert details
- Configurable frequency (immediate, digest)

### Slack

- Requires Slack integration (see Integrations page)
- Real-time notifications to specified channels
- Ideal for team collaboration

### Other Channels

Depending on your account configuration, additional channels may be available:

- SMS (for critical alerts)
- Webhook notifications for custom integrations
- Mobile app push notifications

## Tips

- **Start with Critical Alerts:** Begin with the most important monitoring needs (large transactions, critical price thresholds) before adding lower-priority alerts
- **Avoid Alert Fatigue:** Too many alerts can become noise. Be selective and set meaningful thresholds
- **Use Descriptive Names:** Name alerts clearly so you can quickly identify their purpose when reviewing the list
- **Test Before Relying:** After creating a new alert, test it with a temporary low threshold to ensure notifications are working
- **Review Regularly:** Periodically review your alerts and deactivate or delete outdated ones
- **Leverage Real-Time for Urgent Needs:** Use real-time alerts only for time-sensitive conditions; standard alerts are sufficient for most portfolio monitoring
- **Group Similar Alerts:** If monitoring multiple assets, consider using consistent naming conventions (e.g., "Price - BTC Under $40K", "Price - ETH Under $2K")
- **Set Realistic Thresholds:** Avoid setting price alerts too close to current prices to prevent constant triggering during normal volatility
- **Combine Alert Types:** Use multiple alert types together for comprehensive monitoring (e.g., price alerts + exposure alerts + transaction alerts)
- **Document Your Strategy:** Keep notes on why you set specific thresholds to help with future adjustments
- **Use Inactive Status:** Instead of deleting seasonal or temporary alerts, deactivate them for later reuse
- **Configure Quiet Hours:** If available, set quiet hours for non-critical alerts to avoid nighttime notifications

## Alert Maintenance Best Practices

### Regular Review Schedule

- **Weekly:** Review active alerts and recent notifications
- **Monthly:** Evaluate alert effectiveness and adjust thresholds
- **Quarterly:** Clean up unused or outdated alerts

### When to Adjust Alerts

- Market conditions change significantly
- Portfolio strategy shifts
- Asset allocation targets are modified
- Transaction patterns evolve
- Validator infrastructure changes

### Troubleshooting

**Not Receiving Notifications:**

1. Check alert status (must be ACTIVE)
2. Verify notification channels are configured correctly
3. Check email spam/junk folders
4. Verify Slack integration is connected
5. Ensure quiet hours aren't preventing notifications

**Too Many Notifications:**

1. Review and adjust alert thresholds
2. Consider using digest mode instead of immediate
3. Deactivate low-priority alerts
4. Increase thresholds to reduce false positives

**False Positives:**

1. Refine alert conditions
2. Add additional filters to narrow scope
3. Adjust threshold values
4. Consider using percentage-based instead of fixed-value thresholds

## Security Considerations

- Alert notifications may contain sensitive portfolio information; ensure notification channels are secure
- Review who has access to alert notifications in shared channels (e.g., Slack)
- Use secure email addresses for alert delivery
- Consider using internal communication channels for high-value portfolio alerts
- Regularly audit alert configurations for appropriate access and settings
