# TRES Cost Basis Configuration

This guide explains how to configure cost basis calculations in TRES and the differences between various cost basis methods.

**Location**: `initial-setup/`

---

## What is Cost Basis?

Cost basis is the original value of an asset for tax purposes, used to calculate capital gains or losses when the asset is sold. In TRES, cost basis calculations determine how gains and losses are calculated for your cryptocurrency transactions.

---

## Cost Basis Configuration

### How to Configure Cost Basis Settings

#### Step 1: Access Organization Settings
1. Log into your TRES dashboard
2. Navigate to **Settings** → **Organization Settings**
3. Look for the **Cost Basis Configuration** section

#### Step 2: Configure Cost Basis Strategy
1. Find the `cost_basis_strategy` field
2. Select your preferred cost basis method from the dropdown
3. Available options:
   - **FIFO** (First In, First Out) - Default
   - **FIFO_IMPAIRMENT** (FIFO with Impairment)
   - **LIFO** (Last In, First Out)
   - **AVG** (Weighted Average)
   - **MAX_GAINS** (Maximize Gains)
   - **MAX_LOSSES** (Maximize Losses)

#### Step 2a: Configure Different Strategies by Date Range (Optional)
Use date ranges when you want to apply different strategies during different periods (for example, maximize gains in late 2024 and maximize losses in early 2025).

1. In the same Cost Basis Configuration area, click "Add Cost Basis Range".
2. For each range, set:
   - Strategy: choose one of the methods listed above
   - Start date
   - End date
3. Click "Save Settings" when done. The system will recalculate cost basis for the affected periods.

Example setup:
- Sep 1, 2024 – Jan 31, 2025 → Strategy: MAX_GAINS
- Feb 1, 2025 – Jun 30, 2026 → Strategy: MAX_LOSSES

Behavior and rules:
- Ranges cannot overlap; the UI prevents overlapping date ranges.
- Dates are interpreted in your organization’s time zone.
  - Start date is inclusive from 00:00.
  - End date is inclusive through 23:59:59.
- If no range covers a transaction date, the global `cost_basis_strategy` is used as a fallback.
- Editing ranges triggers a recalculation; large datasets may take time to reprocess.
- If "Calculate Cost Basis by Internal Account" is enabled, ranges apply within each internal account’s calculation scope.

#### Step 3: Configure Additional Settings
1. **Calculate Cost Basis by Internal Account**: Enable if you want separate cost basis calculations per internal account
2. **Calculate Cost Basis for Currencies**: Select which currencies to use for cost basis calculations
3. **Use New Cost Basis**: Enable the new cost basis calculation engine (recommended)
4. **Allow Short**: Enable if you want to allow short positions
5. **Use Exact Timestamp**: Use exact timestamps for cost basis reports

#### Step 4: Save Configuration
1. Click **Save Settings**
2. The system will trigger a cost basis recalculation
3. Existing calculations will be updated with the new method

---

## Cost Basis Methods Explained

### 1. FIFO (First In, First Out) - Default

**How it works:**
- Sells the oldest assets first
- Maintains a queue where new purchases are added to the end
- When selling, removes from the beginning of the queue

**Example:**
```
Purchase 1: 1 BTC at $30,000 (Jan 1)
Purchase 2: 1 BTC at $40,000 (Feb 1)
Purchase 3: 1 BTC at $50,000 (Mar 1)

Sell 1 BTC at $45,000 (Apr 1)
→ Sells the Jan 1 purchase (oldest)
→ Cost basis: $30,000
→ Gain: $15,000
```

**Best for:**
- Most common method for tax reporting
- Simple to understand and implement
- Generally accepted by tax authorities
- Good for long-term investors

**Advantages:**
- Straightforward calculation
- Widely accepted for tax purposes
- Easy to audit and verify
- Consistent with traditional accounting

**Disadvantages:**
- May not optimize tax outcomes
- Doesn't consider current market conditions
- Can result in higher taxes in rising markets

### 2. FIFO_IMPAIRMENT (FIFO with Impairment)

**How it works:**
- Same as FIFO but includes impairment calculations
- Impairment occurs when asset value drops below cost basis
- Allows for loss recognition even without selling

**Example:**
```
Purchase: 1 BTC at $50,000
Current value: $30,000
→ Impairment loss: $20,000 (recognized even without selling)
```

**Best for:**
- Organizations that want to recognize losses early
- Companies following conservative accounting practices
- Situations where asset values have declined significantly

**Advantages:**
- Recognizes losses early
- More conservative approach
- Better reflects current market conditions
- Can reduce tax burden in declining markets

**Disadvantages:**
- More complex calculations
- May not be suitable for all tax jurisdictions
- Requires careful tracking of impairment events

### 3. LIFO (Last In, First Out)

**How it works:**
- Sells the most recently purchased assets first
- Maintains a queue where new purchases are added to the end
- When selling, removes from the end of the queue

**Example:**
```
Purchase 1: 1 BTC at $30,000 (Jan 1)
Purchase 2: 1 BTC at $40,000 (Feb 1)
Purchase 3: 1 BTC at $50,000 (Mar 1)

Sell 1 BTC at $45,000 (Apr 1)
→ Sells the Mar 1 purchase (newest)
→ Cost basis: $50,000
→ Loss: $5,000
```

**Best for:**
- Tax optimization in rising markets
- Reducing current tax burden
- Companies in high tax brackets

**Advantages:**
- Can reduce taxes in rising markets
- Matches current costs with current revenues
- May be beneficial for tax planning

**Disadvantages:**
- Not accepted in all jurisdictions
- Can create higher taxes in declining markets
- More complex to implement and audit

### 4. AVG (Weighted Average)

**How it works:**
- Calculates the average cost of all holdings
- Uses this average as the cost basis for all sales
- Updates the average with each new purchase

**Example:**
```
Purchase 1: 1 BTC at $30,000
Purchase 2: 1 BTC at $40,000
Purchase 3: 1 BTC at $50,000

Average cost: ($30,000 + $40,000 + $50,000) / 3 = $40,000

Sell 1 BTC at $45,000
→ Cost basis: $40,000
→ Gain: $5,000
```

**Best for:**
- Simplifying calculations
- Reducing volatility in gains/losses
- Organizations with frequent trading

**Advantages:**
- Simple to calculate and understand
- Reduces volatility in tax outcomes
- Easy to implement and maintain
- Good for frequent traders

**Disadvantages:**
- May not optimize tax outcomes
- Doesn't allow for strategic tax planning
- Can result in higher taxes overall

### 5. MAX_GAINS (Maximize Gains)

**How it works:**
- Strategically selects which assets to sell to maximize gains
- Sells assets with the highest cost basis first
- Minimizes current tax burden by reducing gains

**Example:**
```
Purchase 1: 1 BTC at $30,000
Purchase 2: 1 BTC at $40,000
Purchase 3: 1 BTC at $50,000

Sell 1 BTC at $45,000
→ Sells the $50,000 purchase (highest cost basis)
→ Cost basis: $50,000
→ Loss: $5,000 (instead of gain)
```

**Best for:**
- Tax optimization strategies
- Reducing current tax burden
- Sophisticated tax planning

**Advantages:**
- Optimizes tax outcomes
- Reduces current tax burden
- Strategic tax planning capability

**Disadvantages:**
- Complex calculations
- May not be suitable for all jurisdictions
- Requires careful tax planning

### 6. MAX_LOSSES (Maximize Losses)

**How it works:**
- Strategically selects which assets to sell to maximize losses
- Sells assets with the lowest cost basis first
- Maximizes current tax benefits from losses

**Example:**
```
Purchase 1: 1 BTC at $30,000
Purchase 2: 1 BTC at $40,000
Purchase 3: 1 BTC at $50,000

Sell 1 BTC at $45,000
→ Sells the $30,000 purchase (lowest cost basis)
→ Cost basis: $30,000
→ Gain: $15,000 (maximizes the gain)
```

**Best for:**
- Tax loss harvesting strategies
- Maximizing current tax benefits
- Sophisticated tax planning

**Advantages:**
- Maximizes tax benefits from losses
- Strategic tax planning capability
- Can offset other gains

**Disadvantages:**
- Complex calculations
- May not be suitable for all jurisdictions
- Requires careful tax planning

---

## Advanced Cost Basis Settings

### Calculate Cost Basis by Internal Account
- **Purpose**: Separate cost basis calculations for different internal accounts
- **Use Case**: Multi-entity organizations or different business units
- **Configuration**: Enable `calculate_cost_basis_by_internal_account`

### Calculate Cost Basis for Currencies
- **Purpose**: Specify which currencies to use for cost basis calculations
- **Use Case**: Multi-currency organizations
- **Configuration**: Set `calculate_cost_basis_for_currencies` array

### Allow Short Positions
- **Purpose**: Enable short selling and borrowing
- **Use Case**: Advanced trading strategies
- **Configuration**: Enable `allow_short`

### Use Exact Timestamp
- **Purpose**: Use exact timestamps for cost basis reports
- **Use Case**: Precise tax reporting
- **Configuration**: Enable `use_exact_timestamp_for_cost_basis_report`

---

## Cost Basis Method Comparison

| Method | Tax Optimization | Complexity | Audit Trail | Best For |
|--------|------------------|------------|-------------|----------|
| **FIFO** | Low | Low | Excellent | General use, compliance |
| **FIFO_IMPAIRMENT** | Medium | Medium | Good | Conservative accounting |
| **LIFO** | High | Medium | Good | Rising markets, tax planning |
| **AVG** | Low | Low | Good | Frequent trading, simplicity |
| **MAX_GAINS** | High | High | Medium | Tax optimization |
| **MAX_LOSSES** | High | High | Medium | Loss harvesting |

---

## Best Practices

### Choosing the Right Method
1. **Consider Tax Jurisdiction**: Some methods may not be accepted in your jurisdiction
2. **Evaluate Tax Impact**: Calculate the tax implications of each method
3. **Consider Complexity**: Simpler methods are easier to audit and maintain
4. **Plan for the Future**: Consider how market conditions might affect your choice

### Configuration Recommendations
1. **Start with FIFO**: Default method that's widely accepted
2. **Enable New Cost Basis**: Use the latest calculation engine
3. **Set Appropriate Currencies**: Configure currencies you actually use
4. **Consider Internal Accounts**: Enable if you have multiple entities

### Monitoring and Maintenance
1. **Regular Reviews**: Review cost basis settings quarterly
2. **Tax Planning**: Consult with tax professionals before making changes
3. **Audit Trail**: Maintain clear records of all cost basis calculations
4. **Testing**: Test new configurations with sample data

---

## Troubleshooting

### Common Issues

**Cost Basis Not Calculating**
- **Problem**: Cost basis calculations not running
- **Solution**: Check if `use_new_cost_basis` is enabled
- **Action**: Verify organization settings and trigger recalculation

**Incorrect Gains/Losses**
- **Problem**: Cost basis calculations seem incorrect
- **Solution**: Verify cost basis strategy and currency settings
- **Action**: Check transaction data and recalculate

**Method Not Available**
- **Problem**: Desired cost basis method not showing
- **Solution**: Some methods may not be available in all jurisdictions
- **Action**: Contact support for availability

**Performance Issues**
- **Problem**: Cost basis calculations taking too long
- **Solution**: Consider using simpler methods or reducing data volume
- **Action**: Optimize settings and monitor performance

### Getting Help
For cost basis issues:
1. Check organization settings
2. Verify transaction data
3. Review cost basis reports
4. Contact support with specific error messages

---

## Related Documentation
- [Currency Configuration](../modules/currency/README.md) - Currency settings for cost basis
- [Reports Module](../modules/reports/README.md) - Cost basis reports
- [Dashboard Module](../modules/dashboard/README.md) - Cost basis display in dashboards
- [Organization Settings](../modules/organization/README.md) - General organization configuration

