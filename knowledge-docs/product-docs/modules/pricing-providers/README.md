# TRES Pricing Provider Selection for Digital Assets

This guide explains how to select and configure pricing providers for your digital assets in TRES, including the differences between various pricing sources and their impact on data accuracy.

---

## What are Pricing Providers?

Pricing providers are external data sources that TRES uses to determine the fiat value of your digital assets. These providers supply real-time and historical price data that is essential for:

- **Cost Basis Calculations**: Determining gains and losses
- **Portfolio Valuation**: Current market value of holdings
- **Tax Reporting**: Accurate asset valuations for tax purposes
- **Financial Reporting**: Balance sheets and P&L statements
- **Risk Management**: Monitoring portfolio performance

---

## Available Pricing Providers

TRES supports multiple pricing providers, each with different strengths and use cases:

### 1. **CoinGecko** (Default - Regular Flow)
**Best for**: General cryptocurrency pricing, comprehensive coverage

**Strengths:**
- **Wide Coverage**: Supports 10,000+ cryptocurrencies
- **Free Tier**: No API costs for basic usage
- **Reliable Data**: Well-established and trusted source
- **Historical Data**: Extensive historical price data
- **DeFi Support**: Good coverage of DeFi tokens

**Limitations:**
- **Rate Limits**: Free tier has API rate limits
- **Update Frequency**: Prices updated every few minutes
- **Premium Features**: Advanced features require paid plans

**Use Cases:**
- General portfolio tracking
- Cost basis calculations
- Tax reporting
- Small to medium organizations

### 2. **CoinMarketCap**
**Best for**: Market data and institutional reporting

**Strengths:**
- **Market Data**: Comprehensive market capitalization data
- **Institutional Focus**: Designed for professional use
- **High Accuracy**: Reliable price data
- **Global Coverage**: Worldwide market data
- **API Quality**: Professional-grade API

**Limitations:**
- **Cost**: Requires paid API access
- **Rate Limits**: Stricter rate limits than free sources
- **Complexity**: More complex setup and configuration

**Use Cases:**
- Large organizations
- Institutional reporting
- Market analysis
- Professional trading

### 3. **Exchange-Specific Sources**

#### **Kraken**
**Best for**: European markets, institutional trading

**Strengths:**
- **Regulatory Compliance**: Strong regulatory compliance
- **Institutional Focus**: Designed for professional traders
- **High Liquidity**: Deep liquidity pools
- **Security**: Excellent security track record

**Limitations:**
- **Limited Coverage**: Fewer supported assets
- **Geographic Focus**: Primarily European markets
- **API Complexity**: More complex integration

#### **Coinbase**
**Best for**: US markets, retail and institutional

**Strengths:**
- **US Market Leader**: Dominant in US cryptocurrency markets
- **Regulatory Compliance**: Strong US regulatory compliance
- **User-Friendly**: Easy to use and understand
- **High Liquidity**: Excellent liquidity for major assets

**Limitations:**
- **US Focus**: Primarily US market data
- **Asset Selection**: Limited to listed assets
- **API Costs**: Paid API access required

#### **Binance**
**Best for**: Global markets, high-volume trading

**Strengths:**
- **Global Reach**: Worldwide market presence
- **High Volume**: Largest trading volume globally
- **Asset Variety**: Extensive asset selection
- **Real-time Data**: Fast price updates

**Limitations:**
- **Regulatory Issues**: Some regulatory concerns
- **API Complexity**: Complex API structure
- **Rate Limits**: Strict rate limiting

#### **Bitfinex**
**Best for**: Professional trading, margin trading

**Strengths:**
- **Professional Tools**: Advanced trading features
- **High Liquidity**: Deep liquidity for major pairs
- **Margin Trading**: Advanced margin trading support
- **API Quality**: Professional-grade API

**Limitations:**
- **Complexity**: Complex for beginners
- **Limited Coverage**: Fewer supported assets
- **API Costs**: Paid access required

### 4. **Dynamic Exchange Selection**
**Best for**: Automatic optimization, multi-exchange coverage

**How it works:**
- Automatically selects the best exchange based on asset and platform
- Uses platform-specific logic to choose optimal pricing source
- Falls back to alternative sources if primary source fails

**Strengths:**
- **Automatic Optimization**: No manual configuration needed
- **High Availability**: Multiple fallback options
- **Platform-Aware**: Considers blockchain platform
- **Cost Effective**: Uses most appropriate source

**Limitations:**
- **Less Control**: Limited manual control over source selection
- **Complexity**: More complex internal logic
- **Debugging**: Harder to troubleshoot pricing issues

### 5. **DEX (Decentralized Exchange) Sources**
**Best for**: DeFi tokens, on-chain pricing

**Strengths:**
- **DeFi Coverage**: Excellent coverage of DeFi tokens
- **On-chain Data**: Direct blockchain data
- **Real-time**: Real-time price updates
- **No Centralization**: Decentralized price discovery

**Limitations:**
- **Limited Coverage**: Only DeFi tokens
- **Volatility**: Higher price volatility
- **Technical Complexity**: More complex integration
- **Liquidity**: Lower liquidity for some tokens

### 6. **LP Token Sources**
**Best for**: Liquidity pool tokens, yield farming

**Strengths:**
- **LP Token Support**: Specialized for liquidity pool tokens
- **Yield Farming**: Supports yield farming tokens
- **DeFi Integration**: Deep DeFi ecosystem integration
- **Real-time Pricing**: Live pricing for LP tokens

**Limitations:**
- **Specialized Use**: Only for LP tokens
- **Complexity**: Complex pricing calculations
- **Volatility**: High price volatility
- **Limited Coverage**: Narrow asset coverage

---

## How to Configure Pricing Providers

### Step 1: Access Organization Settings
1. Log into your TRES dashboard
2. Navigate to **Settings** → **Organization Settings**
3. Look for the **Pricing Configuration** section

### Step 2: Select Primary Pricing Source
1. Find the `pricing_api_source` field
2. Select your preferred pricing provider from the dropdown
3. Available options:
   - **REGULAR_FLOW** (CoinGecko) - Default
   - **COINMARKETCAP** (CoinMarketCap)
   - **KRAKEN** (Kraken Exchange)
   - **COINBASE** (Coinbase Exchange)
   - **BINANCE** (Binance Exchange)
   - **BITFINEX** (Bitfinex Exchange)
   - **DYNAMIC_EXCHANGE** (Automatic Selection)

### Step 3: Configure Per-Asset Pricing (Optional)
1. Find the `pricing_api_source_per_asset` field
2. Add specific pricing sources for individual assets
3. Example configuration:
   ```json
   [
     {
       "asset_name": "Bitcoin",
       "pricing_api_source": "COINBASE"
     },
     {
       "asset_name": "Ethereum",
       "pricing_api_source": "KRAKEN"
     }
   ]
   ```

### Step 4: Configure Stable Coin Pegging (Optional)
1. Find the `pegged_stable_coins_to_fiat` field
2. Configure stable coins to be pegged to fiat currencies
3. Example configuration:
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

### Step 5: Save Configuration
1. Click **Save Settings**
2. The system will apply the new pricing configuration
3. Existing price data will be updated with new sources

---

## Pricing Provider Comparison

| Provider | Cost | Coverage | Accuracy | Speed | Best For |
|----------|------|----------|----------|-------|----------|
| **CoinGecko** | Free | Excellent | High | Good | General use, small orgs |
| **CoinMarketCap** | Paid | Excellent | Very High | Excellent | Large orgs, institutions |
| **Kraken** | Paid | Good | Very High | Excellent | European markets |
| **Coinbase** | Paid | Good | Very High | Excellent | US markets |
| **Binance** | Paid | Excellent | High | Excellent | Global markets |
| **Bitfinex** | Paid | Good | Very High | Excellent | Professional trading |
| **Dynamic Exchange** | Mixed | Excellent | High | Good | Automatic optimization |
| **DEX Sources** | Free | Limited | Variable | Good | DeFi tokens |
| **LP Token Sources** | Free | Limited | Variable | Good | LP tokens |

---

## Impact on Data Collection and Accuracy

### 1. **Price Accuracy**

**High Accuracy Sources:**
- **Exchange Sources**: Direct from trading platforms
- **CoinMarketCap**: Professional market data
- **CoinGecko**: Reliable aggregated data

**Variable Accuracy Sources:**
- **DEX Sources**: Can be volatile
- **LP Token Sources**: Complex pricing calculations

### 2. **Data Collection Timing**

**Real-time Sources:**
- **Exchange APIs**: Live trading data
- **CoinMarketCap**: Frequent updates
- **Dynamic Exchange**: Optimized timing

**Delayed Sources:**
- **CoinGecko Free**: Few minutes delay
- **DEX Sources**: Variable timing

### 3. **Coverage and Availability**

**Comprehensive Coverage:**
- **CoinGecko**: 10,000+ assets
- **CoinMarketCap**: Extensive coverage
- **Dynamic Exchange**: Multi-source coverage

**Limited Coverage:**
- **Exchange Sources**: Only listed assets
- **DEX Sources**: Only DeFi tokens
- **LP Token Sources**: Only LP tokens

### 4. **Cost Implications**

**Free Sources:**
- **CoinGecko**: Free tier available
- **DEX Sources**: No API costs
- **LP Token Sources**: No API costs

**Paid Sources:**
- **Exchange APIs**: $50-500/month depending on usage
- **CoinMarketCap**: $29-999/month depending on plan
- **Professional APIs**: $100-1000+/month

---

## Best Practices for Pricing Provider Selection

### 1. **For Small Organizations**

**Recommended Configuration:**
- **Primary Source**: CoinGecko (REGULAR_FLOW)
- **Fallback**: Dynamic Exchange
- **Per-Asset**: None (use defaults)

**Benefits:**
- **Cost Effective**: No API costs
- **Good Coverage**: Supports most assets
- **Easy Setup**: Minimal configuration

### 2. **For Medium Organizations**

**Recommended Configuration:**
- **Primary Source**: CoinMarketCap or Coinbase
- **Fallback**: Dynamic Exchange
- **Per-Asset**: Specific sources for major assets

**Benefits:**
- **Better Accuracy**: Professional data sources
- **Reliable Service**: Higher uptime
- **Support**: Professional support

### 3. **For Large Organizations**

**Recommended Configuration:**
- **Primary Source**: CoinMarketCap
- **Fallback**: Multiple exchange sources
- **Per-Asset**: Optimized sources per asset class

**Benefits:**
- **Highest Accuracy**: Professional-grade data
- **Comprehensive Coverage**: All asset types
- **Customization**: Tailored configurations

### 4. **For DeFi-Focused Organizations**

**Recommended Configuration:**
- **Primary Source**: Dynamic Exchange
- **Fallback**: DEX Sources
- **Per-Asset**: DEX sources for DeFi tokens

**Benefits:**
- **DeFi Coverage**: Excellent DeFi token support
- **Real-time Data**: Live on-chain pricing
- **Cost Effective**: No API costs for DEX data

---

## Advanced Configuration Options

### 1. **Hybrid Pricing Strategy**

**Configuration:**
```json
{
  "pricing_api_source": "DYNAMIC_EXCHANGE",
  "pricing_api_source_per_asset": [
    {
      "asset_name": "Bitcoin",
      "pricing_api_source": "COINBASE"
    },
    {
      "asset_name": "Ethereum",
      "pricing_api_source": "KRAKEN"
    },
    {
      "asset_name": "Uniswap",
      "pricing_api_source": "DEX"
    }
  ]
}
```

**Benefits:**
- **Optimized per Asset**: Best source for each asset
- **Cost Optimization**: Use free sources where possible
- **High Accuracy**: Professional sources for major assets

### 2. **Geographic Optimization**

**US Organizations:**
- **Primary**: Coinbase
- **Secondary**: CoinMarketCap
- **Fallback**: CoinGecko

**European Organizations:**
- **Primary**: Kraken
- **Secondary**: CoinMarketCap
- **Fallback**: CoinGecko

**Global Organizations:**
- **Primary**: Binance
- **Secondary**: Dynamic Exchange
- **Fallback**: CoinGecko

### 3. **Asset-Specific Configuration**

**Major Cryptocurrencies:**
- **Bitcoin**: Coinbase or Kraken
- **Ethereum**: Coinbase or Kraken
- **Major Altcoins**: CoinMarketCap

**DeFi Tokens:**
- **Uniswap**: DEX Sources
- **Compound**: DEX Sources
- **Aave**: DEX Sources

**Stable Coins:**
- **USDC**: Pegged to USD
- **USDT**: Pegged to USD
- **DAI**: DEX Sources

---

## Monitoring and Troubleshooting

### 1. **Price Accuracy Monitoring**

**Key Metrics:**
- **Price Deviation**: Compare prices across sources
- **Update Frequency**: Monitor price update timing
- **Data Quality**: Check for missing or invalid prices
- **API Response Times**: Monitor source performance

### 2. **Common Issues and Solutions**

**Issue: Missing Price Data**
- **Cause**: API rate limits or source unavailability
- **Solution**: Configure fallback sources
- **Prevention**: Use multiple pricing sources

**Issue: Inaccurate Prices**
- **Cause**: Source-specific pricing issues
- **Solution**: Switch to more reliable source
- **Prevention**: Regular price validation

**Issue: Slow Price Updates**
- **Cause**: API delays or rate limiting
- **Solution**: Optimize API usage or upgrade plan
- **Prevention**: Use real-time sources for critical assets

**Issue: High API Costs**
- **Cause**: Excessive API usage
- **Solution**: Optimize source selection and caching
- **Prevention**: Use free sources where appropriate

### 3. **Performance Optimization**

**Caching Strategy:**
- **Enable Caching**: Use cached prices when possible
- **Cache Duration**: Balance freshness vs. API costs
- **Cache Invalidation**: Update cache when needed

**Source Selection:**
- **Primary Sources**: Use most reliable sources
- **Fallback Sources**: Configure multiple fallbacks
- **Load Balancing**: Distribute requests across sources

---

## Cost Considerations

### 1. **Free vs. Paid Sources**

**Free Sources:**
- **CoinGecko**: Free tier with rate limits
- **DEX Sources**: No API costs
- **LP Token Sources**: No API costs

**Paid Sources:**
- **Exchange APIs**: $50-500/month depending on usage
- **CoinMarketCap**: $29-999/month depending on plan
- **Professional APIs**: $100-1000+/month

### 2. **Cost Optimization Strategies**

**Hybrid Approach:**
- Use free sources for non-critical assets
- Use paid sources for major assets
- Implement intelligent caching

**Usage Optimization:**
- Monitor API usage
- Implement rate limiting
- Use batch requests when possible

**Source Selection:**
- Choose most cost-effective source per asset
- Use dynamic selection for optimization
- Regular review of pricing plans

---

## Related Documentation
- [Cost Basis Configuration](./cost-basis/README.md) - How pricing affects cost basis calculations
- [Currency Configuration](../modules/currency/README.md) - Currency settings for pricing
- [Reports Module](../modules/reports/README.md) - Pricing in reports
- [Dashboard Module](../modules/dashboard/README.md) - Price display in dashboards
