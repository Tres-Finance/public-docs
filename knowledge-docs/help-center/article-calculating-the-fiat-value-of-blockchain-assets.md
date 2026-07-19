# Calculating the Fiat Value of Blockchain Assets | TRES Finance Help Center

Source: https://help.tres.finance/article/calculating-the-fiat-value-of-blockchain-assets

# Calculating the Fiat Value of Blockchain Assets

Valuation involves the analytical evaluation of an asset's present or anticipated value. Various valuation methods exist, and each approach can produce distinct outcomes. The suitability of a particular way depends on factors such as the asset class and the company being assessed.

TRES helps crypto organizations to calculate real-time and historical fiat values of their balances and transactions. We built a waterfall methodology to maximize our coverage and accuracy.

## Maximize fiat value coverage and accuracy of Crypto Assets

TRES fiat value calculation leverages different methodologies to automate the evaluation process and saves you time.

### Trades / Swaps

In the case of an on-chain swap via a known decentralized exchange like Uniswap or Curve, we are aligning the fiat value of the swapped assets to be equal. This means that we are ignoring slippage or liquidity pool fees. We are aligning the price of the received token with the sent token.

For example, in the swap below, the fiat value of the USDS is aligned with the fiat value of the sUSDS.

In the case of an off-chain trade via a centralized exchange like Binance or Coinbase, we align the fiat value of the non-stable asset with the stable/fiat asset (minus fees).

For example, in the trade below, the fiat value of LDO (which is a non-stable/fiat asset) is aligned with the fiat value of the inflow USDT (minus fees).

1,997 USD - 2 USD = 1,995 USD

### Liquidity Pool Lockup / Return

This feature is taken into action during two activities:

When a customer is locking (=depositing) assets into a liquidity pool and receives an LP token.

When a customer is returning (=withdrawing) the LP token to the liquidity pool and receives the underlying assets.

In both cases, we are aligning the fiat value of the LP token with the sum of the two underlying assets.

In the example below, we calculate the fiat value of UNI-V2 by summing the fiat value of WETH and AGI.

4,078 USD + 4,043 USD = 8,121 USD

### Stable and Fiat Pegging [Customized]

Advanced users can select certain stablecoins like USDC and BUSD to be 1-1 pegged to fiat assets. If you are interested in fully pegging your stablecoins to fiat assets, contact the TRES support team. The default behavior is aligning the stablecoins price with Coingecko.

In the example below, you can see that BUSD equals $1, even though the public price was $0.998.

### Assets Transfers

In regular token transfers which are not fitting to the methodologies mentioned above, we are using external resources to fetch the price:

Coingecko - The price of a cryptoasset is calculated using the pairings available and collected by CoinGecko from the various exchanges for a particular cryptoasset. The price shown on CoinGecko for a particular cryptoasset is calculated using a global volume-weighted average price formula.

DEX Tracking - If there is no official pricing in Coingecko, we are fetching the prices from the known liquidity pools.

For example, although G$ does not have an official price in Coingecko, we are using G$/WETH Uniswap V2 on top of Celo network to calculate the fiat pricing.

Token Pegging - In case, we do not find the fiat value at Coingecko and not by tracking DEX, we exploring options to peg the token with other known tokens.

For example, we pegged anyDAI with DAI since anyDAI is not found in Coingecko and is not traded in the liquidity pool. Our research team found that it is 1-1 with the official DAI token.

### Manual fiat value [Customized]

Customers are also allowed to set manual fiat value for each transfer, just click on the edit icon and set Unit Price or Total Transfer Fiat (="Entire transaction value").
