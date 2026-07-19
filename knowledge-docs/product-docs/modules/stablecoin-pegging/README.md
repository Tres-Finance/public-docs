# TRES Stablecoin Pegging: 1:1 Fiat Value Configuration

This guide explains how to configure stablecoin pegging in TRES to maintain 1:1 fiat value relationships between stablecoins and their underlying fiat currencies, ensuring accurate financial reporting and cost basis calculations.

---

## What is Stablecoin Pegging?

Stablecoin pegging in TRES allows you to configure specific stablecoins to maintain a fixed 1:1 relationship with their underlying fiat currencies, regardless of market fluctuations. This ensures that:

- **USDC** is always valued at **$1.00 USD**
- **USDT** is always valued at **$1.00 USD**  
- **DAI** is always valued at **$1.00 USD**
- **EURT** is always valued at **€1.00 EUR**

### Why Use Stablecoin Pegging?

**Financial Accuracy:**
- Eliminates minor price fluctuations that can affect reporting
- Ensures consistent valuation for accounting purposes
- Maintains stable portfolio values for risk management

**Regulatory Compliance:**
- Meets accounting standards for stable asset valuation
- Provides consistent basis for tax reporting
- Ensures audit trail accuracy

**Operational Benefits:**
- Reduces noise in financial reports
- Simplifies cost basis calculations
- Provides predictable cash flow analysis

---

## How Stablecoin Pegging Works

### 1. **Configuration Process**
When you configure stablecoin pegging, TRES:
1. **Identifies** the stablecoin by its asset name
2. **Maps** it to the corresponding fiat currency
3. **Overrides** market pricing with fixed 1:1 ratio
4. **Applies** the pegging to all historical and real-time data

### 2. **Pricing Override Logic**
```
Normal Pricing: USDC = $0.9998 (market price)
Pegged Pricing: USDC = $1.0000 (fixed 1:1)
```

### 3. **Data Consistency**
- **Historical Data**: All past transactions use 1:1 pricing
- **Real-time Data**: Current balances show 1:1 valuation
- **Reports**: All reports reflect 1:1 stablecoin values
- **Cost Basis**: Calculations use 1:1 pricing for accuracy

---

## Supported Stablecoins and Currencies

### **USD-Pegged Stablecoins**
| Stablecoin | Symbol | Pegged Currency | Use Case |
|------------|--------|-----------------|----------|
| **USD Coin** | USDC | USD | Most popular USD stablecoin |
| **Tether** | USDT | USD | Widely used for trading |
| **Binance USD** | BUSD | USD | Binance ecosystem |
| **Pax Dollar** | USDP | USD | Paxos-issued stablecoin |
| **TrueUSD** | TUSD | USD | TrustToken stablecoin |
| **Gemini Dollar** | GUSD | USD | Gemini exchange stablecoin |
| **Frax** | FRAX | USD | Algorithmic stablecoin |
| **Liquity USD** | LUSD | USD | Decentralized stablecoin |

### **EUR-Pegged Stablecoins**
| Stablecoin | Symbol | Pegged Currency | Use Case |
|------------|--------|-----------------|----------|
| **Euro Tether** | EURT | EUR | Tether's Euro stablecoin |
| **Stasis Euro** | EURS | EUR | Stasis platform stablecoin |

### **Other Supported Currencies**
- **GBP**: British Pound Sterling
- **CHF**: Swiss Franc
- **CAD**: Canadian Dollar
- **AUD**: Australian Dollar
- **JPY**: Japanese Yen
- **AED**: UAE Dirham
- **SEK**: Swedish Krona
- **NZD**: New Zealand Dollar
- **TRY**: Turkish Lira
- **IDR**: Indonesian Rupiah
- **ILS**: Israeli Shekel
- **CLP**: Chilean Peso
- **ZAR**: South African Rand
- **BRL**: Brazilian Real
- **GIP**: Gibraltar Pound

---

## How to Configure Stablecoin Pegging

### Step 1: Access Organization Settings
1. Log into your TRES dashboard
2. Navigate to **Settings** → **Organization Settings**
3. Scroll down to the **Pricing Configuration** section

### Step 2: Locate Pegging Configuration
1. Find the `pegged_stable_coins_to_fiat` field
2. This field accepts a list of pegging pairs
3. Each pair consists of:
   - **Asset Name**: The exact name of the stablecoin
   - **Currency**: The fiat currency to peg to

### Step 3: Configure Pegging Pairs

#### **Basic Configuration Example:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  },
  {
    "asset_name": "Tether", 
    "currency": "USD"
  }
]
```

#### **Advanced Configuration Example:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  },
  {
    "asset_name": "Tether",
    "currency": "USD"
  },
  {
    "asset_name": "Binance USD",
    "currency": "USD"
  },
  {
    "asset_name": "Euro Tether",
    "currency": "EUR"
  },
  {
    "asset_name": "Stasis Euro",
    "currency": "EUR"
  }
]
```

### Step 4: Save Configuration
1. Click **Save Settings**
2. The system will validate the configuration
3. Existing data will be updated with new pegging rules
4. All future transactions will use 1:1 pricing

---

## Configuration Examples by Use Case

### **Example 1: US-Based Organization**
**Configuration:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  },
  {
    "asset_name": "Tether",
    "currency": "USD"
  },
  {
    "asset_name": "Binance USD",
    "currency": "USD"
  }
]
```

**Benefits:**
- All major USD stablecoins pegged to $1.00
- Consistent USD valuation across all stablecoins
- Simplified accounting for US-based operations

### **Example 2: European Organization**
**Configuration:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  },
  {
    "asset_name": "Tether",
    "currency": "USD"
  },
  {
    "asset_name": "Euro Tether",
    "currency": "EUR"
  },
  {
    "asset_name": "Stasis Euro",
    "currency": "EUR"
  }
]
```

**Benefits:**
- USD stablecoins pegged to $1.00
- EUR stablecoins pegged to €1.00
- Multi-currency support for European operations

### **Example 3: Global Organization**
**Configuration:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  },
  {
    "asset_name": "Tether",
    "currency": "USD"
  },
  {
    "asset_name": "Binance USD",
    "currency": "USD"
  },
  {
    "asset_name": "Euro Tether",
    "currency": "EUR"
  },
  {
    "asset_name": "Stasis Euro",
    "currency": "EUR"
  }
]
```

**Benefits:**
- Comprehensive stablecoin coverage
- Multi-currency support
- Consistent valuation across all major stablecoins

---

## Impact on Financial Data

### 1. **Portfolio Valuation**

**Before Pegging:**
```
Portfolio Value: $1,000,000.50
- Bitcoin: $500,000.00
- USDC: $250,000.25 (market price: $1.001)
- USDT: $250,000.25 (market price: $1.001)
```

**After Pegging:**
```
Portfolio Value: $1,000,000.00
- Bitcoin: $500,000.00
- USDC: $250,000.00 (pegged: $1.000)
- USDT: $250,000.00 (pegged: $1.000)
```

### 2. **Cost Basis Calculations**

**Before Pegging:**
```
Transaction: Buy 1000 USDC for $1000
Market Price: $1.001
Cost Basis: $1001.00
Gain/Loss: -$1.00 (if sold at $1.000)
```

**After Pegging:**
```
Transaction: Buy 1000 USDC for $1000
Pegged Price: $1.000
Cost Basis: $1000.00
Gain/Loss: $0.00 (if sold at $1.000)
```

### 3. **Financial Reports**

**Balance Sheet Impact:**
- **Assets**: Stablecoin values remain constant
- **Liabilities**: No impact on liabilities
- **Equity**: Consistent equity calculations

**P&L Impact:**
- **Revenue**: No artificial gains from stablecoin fluctuations
- **Expenses**: No artificial losses from stablecoin fluctuations
- **Net Income**: More accurate profit/loss calculations

---

## Best Practices for Stablecoin Pegging

### 1. **Asset Name Accuracy**
**✅ Correct:**
```json
{
  "asset_name": "USD Coin",
  "currency": "USD"
}
```

**❌ Incorrect:**
```json
{
  "asset_name": "USDC",
  "currency": "USD"
}
```

**Why:** TRES uses the full asset name, not the symbol. Check your asset list for exact names.

### 2. **Currency Consistency**
**✅ Correct:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  },
  {
    "asset_name": "Euro Tether",
    "currency": "EUR"
  }
]
```

**❌ Incorrect:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "EUR"
  }
]
```

**Why:** Each stablecoin should be pegged to its intended fiat currency.

### 3. **Comprehensive Coverage**
**✅ Recommended:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  },
  {
    "asset_name": "Tether",
    "currency": "USD"
  },
  {
    "asset_name": "Binance USD",
    "currency": "USD"
  }
]
```

**Why:** Configure all stablecoins you hold to ensure consistent valuation.

### 4. **Regular Review**
- **Monthly**: Review stablecoin holdings
- **Quarterly**: Update pegging configuration
- **Annually**: Audit pegging accuracy

---

## Advanced Configuration Options

### 1. **Selective Pegging**
**Configuration:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  }
]
```

**Use Case:** Only peg USDC, let other stablecoins use market pricing

**Benefits:**
- Maintains 1:1 for primary stablecoin
- Allows market pricing for others
- Flexible approach to valuation

### 2. **Multi-Currency Pegging**
**Configuration:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  },
  {
    "asset_name": "Euro Tether",
    "currency": "EUR"
  },
  {
    "asset_name": "Stasis Euro",
    "currency": "EUR"
  }
]
```

**Use Case:** International operations with multiple fiat currencies

**Benefits:**
- Consistent valuation across currencies
- Simplified multi-currency reporting
- Reduced currency conversion complexity

### 3. **Platform-Specific Pegging**
**Configuration:**
```json
[
  {
    "asset_name": "USD Coin",
    "currency": "USD"
  },
  {
    "asset_name": "Tether",
    "currency": "USD"
  }
]
```

**Use Case:** Different stablecoins on different platforms

**Benefits:**
- Platform-agnostic pegging
- Consistent valuation across platforms
- Simplified cross-platform reporting

---

## Monitoring and Validation

### 1. **Configuration Validation**
TRES automatically validates your pegging configuration:
- **Asset Name Check**: Verifies asset exists in system
- **Currency Check**: Ensures currency is supported
- **Duplicate Check**: Prevents multiple pegging for same asset
- **Format Check**: Validates JSON structure

### 2. **Pricing Verification**
**Dashboard Monitoring:**
- Check portfolio values for expected stablecoin amounts
- Verify no unexpected gains/losses from stablecoins
- Monitor cost basis calculations

**Report Validation:**
- Review balance sheets for consistent stablecoin values
- Check P&L for absence of stablecoin-related gains/losses
- Validate cost basis reports for accurate calculations

### 3. **Common Issues and Solutions**

**Issue: Stablecoin showing market price instead of $1.00**
- **Cause**: Asset name mismatch in configuration
- **Solution**: Check exact asset name in asset list
- **Prevention**: Copy asset names directly from TRES interface

**Issue: Configuration not saving**
- **Cause**: Invalid JSON format or unsupported currency
- **Solution**: Validate JSON syntax and currency codes
- **Prevention**: Use TRES interface for configuration

**Issue: Historical data not updated**
- **Cause**: Configuration applied after data collection
- **Solution**: Recalculate cost basis for affected periods
- **Prevention**: Configure pegging before data collection

---

## Integration with Other Features

### 1. **Cost Basis Calculations**
**Impact:**
- Stablecoin transactions use 1:1 pricing
- More accurate gain/loss calculations
- Consistent tax reporting

**Configuration:**
```json
{
  "pegged_stable_coins_to_fiat": [
    {
      "asset_name": "USD Coin",
      "currency": "USD"
    }
  ],
  "calculate_cost_basis_for_currencies": ["USD"],
  "cost_basis_strategy": "FIFO"
}
```

### 2. **Pricing Provider Selection**
**Impact:**
- Pegged stablecoins override pricing provider selection
- Market pricing sources ignored for pegged assets
- Consistent 1:1 valuation regardless of provider

**Configuration:**
```json
{
  "pegged_stable_coins_to_fiat": [
    {
      "asset_name": "USD Coin",
      "currency": "USD"
    }
  ],
  "pricing_api_source": "COINMARKETCAP",
  "pricing_api_source_per_asset": [
    {
      "asset_name": "Bitcoin",
      "pricing_api_source": "COINBASE"
    }
  ]
}
```

### 3. **Multi-Entity Support**
**Impact:**
- Pegging applies across all entities
- Consistent valuation for consolidated reporting
- Simplified inter-entity transactions

**Configuration:**
```json
{
  "pegged_stable_coins_to_fiat": [
    {
      "asset_name": "USD Coin",
      "currency": "USD"
    }
  ],
  "enable_multi_entity": true
}
```

---

## Troubleshooting Guide

### 1. **Configuration Issues**

**Problem: Configuration not applying**
**Symptoms:**
- Stablecoins still showing market prices
- No change in portfolio values
- Configuration appears to be ignored

**Solutions:**
1. **Verify Asset Names**: Check exact asset names in your asset list
2. **Validate JSON**: Ensure proper JSON formatting
3. **Check Permissions**: Ensure you have admin access
4. **Refresh Data**: Force recalculation of affected data

**Problem: Invalid configuration error**
**Symptoms:**
- Error message when saving
- Configuration not saved
- System validation failures

**Solutions:**
1. **Check Currency Codes**: Use supported currency codes (USD, EUR, etc.)
2. **Validate Asset Names**: Ensure asset names match exactly
3. **Review JSON Format**: Check for syntax errors
4. **Remove Duplicates**: Ensure no duplicate asset names

### 2. **Data Issues**

**Problem: Historical data not updated**
**Symptoms:**
- Old transactions still show market prices
- Inconsistent historical values
- Reports showing mixed pricing

**Solutions:**
1. **Recalculate Cost Basis**: Trigger cost basis recalculation
2. **Regenerate Reports**: Create new reports with updated data
3. **Check Date Ranges**: Ensure configuration covers all relevant periods
4. **Contact Support**: For complex historical data issues

**Problem: Inconsistent pricing across reports**
**Symptoms:**
- Different reports showing different values
- Inconsistent stablecoin valuations
- Mixed pricing in same time period

**Solutions:**
1. **Verify Configuration**: Ensure pegging is properly configured
2. **Check Report Dates**: Ensure reports cover same time periods
3. **Regenerate Reports**: Create fresh reports with current configuration
4. **Review Data Sources**: Check for conflicting pricing sources

### 3. **Performance Issues**

**Problem: Slow data processing**
**Symptoms:**
- Delayed report generation
- Slow dashboard loading
- Timeout errors

**Solutions:**
1. **Optimize Configuration**: Use only necessary pegging pairs
2. **Batch Updates**: Process large data sets in batches
3. **Check System Load**: Monitor system performance
4. **Contact Support**: For persistent performance issues

---

## Cost Considerations

### 1. **No Additional Costs**
- **Configuration**: Free to configure
- **Data Processing**: No additional processing costs
- **Storage**: No additional storage requirements
- **API Usage**: No impact on API usage

### 2. **Potential Savings**
- **Reduced Complexity**: Simplified pricing logic
- **Faster Processing**: Less complex price calculations
- **Improved Accuracy**: Reduced need for price corrections
- **Better Reporting**: More consistent financial reports

---

## Related Documentation
- [Pricing Provider Selection](./pricing-providers/README.md) - How pegging integrates with pricing sources
- [Cost Basis Configuration](./cost-basis/README.md) - Impact on cost basis calculations
- [Currency Configuration](../modules/currency/README.md) - Currency settings and pegging
- [Reports Module](../modules/reports/README.md) - How pegging affects reports
- [Dashboard Module](../modules/dashboard/README.md) - Display of pegged values

---

## Summary

Stablecoin pegging in TRES provides a powerful way to maintain consistent 1:1 fiat valuations for stablecoins, ensuring:

- **Financial Accuracy**: Eliminates minor price fluctuations
- **Regulatory Compliance**: Meets accounting standards
- **Operational Benefits**: Simplified reporting and calculations
- **Cost Effectiveness**: No additional costs for configuration

By properly configuring stablecoin pegging, you can ensure that your financial data accurately reflects the intended 1:1 relationship between stablecoins and their underlying fiat currencies, providing a solid foundation for accurate financial reporting and decision-making.