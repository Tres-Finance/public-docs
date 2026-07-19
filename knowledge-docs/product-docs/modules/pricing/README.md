# Pricing Module

## Overview

The Pricing module calculates fiat values for digital assets using multiple data sources and pricing strategies. It provides historical and real-time pricing data across various blockchain platforms.

## Data Sources

### Primary Sources
- **CoinGecko**: General cryptocurrency pricing data
- **CoinMarketCap**: Market data and historical prices
- **DEX Sources**: On-chain decentralized exchange pricing
- **LP Token Sources**: Liquidity pool token pricing

### Exchange-Specific Sources
- **Kraken**: Exchange-specific pricing
- **Coinbase**: Exchange-specific pricing
- **Bitfinex**: Exchange-specific pricing
- **Huobi**: Exchange-specific pricing
- **OKX**: Exchange-specific pricing
- **Binance**: Exchange-specific pricing
- **Other Exchanges**: Bitstamp, Crypto.com, Bitget, BTCMarkets, Deribit, Gemini, KuCoin, Gate.io, Mercado

### Custom Strategies
- **Custom Asset Pricing**: Special handling for specific tokens
- **Fiat Currency Pricing**: Direct fiat-to-fiat conversions
- **Dynamic Exchange Selection**: Automatic platform-based source selection

## Pricing Strategies

### Strategy Hierarchy
1. **Custom Strategies**: Apply special pricing logic for specific assets
2. **Primary Sources**: CoinGecko, CoinMarketCap, or exchange-specific
3. **DEX/LP Sources**: On-chain pricing for DeFi tokens
4. **Fallback**: Use default strategy if specific strategy fails

## Price Calculation Process

### Time-Based Pricing
- **Historical Prices**: Uses exact timestamp when available
- **Hourly Granularity**: Prices are normalized to hourly intervals

### Price Resolution Flow
1. **Query Processing**: Validates asset and platform information
2. **Strategy Selection**: Chooses appropriate pricing strategy
3. **Source Iteration**: Tries each source in strategy order
4. **Price Validation**: Ensures price quality and availability
5. **Currency Conversion**: Converts to requested fiat currencies
6. **Caching**: Stores results for future requests

### Supported Currencies
- **Primary**: USD, EUR
- **Additional**: IDR, CHF, ILS, GBP, TRY, AUD, CAD, JPY, AED, NZD, SEK, CLP, ZAR, BRL

## Configuration

### Organization Settings
- **Pricing API Source**: Configurable default source per organization
- **Fiat Currencies**: Organization-specific currency preferences
- **Asset Class Mapping**: Pegged fiat currency assignments

## Timing Updates

### Update Frequency
- **Real-time**: Live pricing data from exchange APIs
- **Hourly**: Historical price data with hourly granularity
- **On-demand**: Price requests processed as needed

### Data Freshness
- **Exchange Sources**: Real-time pricing from live exchange feeds
- **Historical Data**: Stored prices with timestamp accuracy
- **Custom Strategies**: Updated based on specific token requirements

### Update Triggers
- **Transaction Processing**: Prices fetched when transactions are processed
- **Report Generation**: Historical prices retrieved for reporting
- **Balance Calculations**: Real-time prices for current balance valuations

## Error Handling

### Common Issues
- **Asset Not Found**: When asset doesn't exist in any source
- **Price Unavailable**: When no price data exists for requested time
- **Source Failures**: Automatic fallback to alternative sources
- **Network Timeouts**: Retry mechanisms with exponential backoff

### Quality Assurance
- **Price Validation**: Checks for anomalous price values
- **Source Reliability**: Tracks success rates of different sources
- **Data Consistency**: Ensures price data integrity across sources 