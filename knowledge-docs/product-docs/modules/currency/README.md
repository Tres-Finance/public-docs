# TRES Currencies: How to Select and Which Ones are Available

This guide explains the currencies supported by TRES and how to select them for your organization and reports.

---

## Available Currencies

TRES supports **17 major fiat currencies** for pricing, reporting, and cost basis calculations.

### Complete Currency List

| Currency Code | Currency Name | Symbol | Country/Region | Decimal Places | Primary Use Cases |
|---------------|---------------|--------|----------------|----------------|-------------------|
| **USD** | United States Dollar | $ | United States | 2 | Global reserve currency, crypto pricing, international trade |
| **EUR** | Euro | € | European Union | 2 | European operations, EU regulatory reporting, cross-border transactions |
| **GBP** | British Pound Sterling | £ | United Kingdom | 2 | UK operations, Commonwealth countries, financial services |
| **CHF** | Swiss Franc | CHF | Switzerland | 2 | Safe haven currency, wealth management, international banking |
| **CAD** | Canadian Dollar | CAD | Canada | 2 | North American operations, commodity trading, resource sector |
| **AUD** | Australian Dollar | $ | Australia | 2 | Asia-Pacific operations, commodity exports, mining sector |
| **JPY** | Japanese Yen | ¥ | Japan | 0 | Asian markets, carry trade, technology sector |
| **AED** | United Arab Emirates Dirham | د.إ | United Arab Emirates | 2 | Middle East operations, oil trading, regional hub |
| **SEK** | Swedish Krona | kr | Sweden | 2 | Nordic operations, technology sector, export-oriented |
| **NZD** | New Zealand Dollar | $ | New Zealand | 2 | Pacific operations, agricultural exports, tourism |
| **TRY** | Turkish Lira | ₺ | Turkey | 2 | Emerging markets, cross-border trade, regional operations |
| **IDR** | Indonesian Rupiah | Rp | Indonesia | 2 | Southeast Asian operations, commodity trading, emerging markets |
| **ILS** | Israeli New Shekel | ₪ | Israel | 2 | Middle East operations, technology sector, innovation hub |
| **CLP** | Chilean Peso | $ | Chile | 0 | Latin American operations, mining sector, commodity exports |
| **ZAR** | South African Rand | R | South Africa | 2 | African operations, mining sector, emerging markets |
| **BRL** | Brazilian Real | R$ | Brazil | 2 | Latin American operations, agricultural exports, BRICS |
| **GIP** | Gibraltar Pound | £ | Gibraltar | 2 | European operations, financial services, tax optimization |

### Currency Categories

#### **Major Reserve Currencies**
- **USD**: Global reserve currency, used for most crypto pricing
- **EUR**: Second most traded currency, EU regulatory compliance
- **GBP**: Historical reserve currency, financial services hub
- **JPY**: Third most traded currency, carry trade favorite

#### **Regional Currencies**
- **CHF**: Safe haven during market volatility
- **CAD/AUD**: Commodity-linked currencies
- **AED**: Oil-rich economy, regional financial center
- **SEK**: Technology and export-focused economy

#### **Emerging Market Currencies**
- **TRY**: High volatility, emerging market exposure
- **IDR**: Southeast Asian growth markets
- **ILS**: Technology and innovation sector
- **CLP/ZAR**: Resource-rich economies
- **BRL**: Largest Latin American economy

---

## How Currency Selection Works

### Default Currency
- **USD** is the default currency for all TRES operations
- All fiat values are calculated and stored in USD by default
- This ensures consistency across all calculations and reporting

### Currency Selection Hierarchy
When generating reports or configuring your organization, currency selection follows this priority order:

1. **Report-specific currency selection** (highest priority)
2. **Organization cost basis currencies**
3. **ERP integration currency**
4. **USD default** (lowest priority)

---

## How to Select Currencies

### For Your Organization

#### Step 1: Access Organization Settings
1. Log into your TRES dashboard
2. Navigate to **Settings** → **Organization Settings**
3. Look for the **Currency Configuration** section
4. Find the field labeled `calculate_cost_basis_for_currencies`

#### Step 2: Configure Your Currencies
1. Click **Edit** or **Configure** next to the currency field
2. Select the currencies you need for your operations
3. Consider these factors:
   - **Primary Operating Currency**: Your main business currency
   - **Tax Jurisdictions**: Currencies required for tax reporting
   - **Trading Partners**: Currencies used with major partners
   - **Regulatory Requirements**: Currencies mandated by regulations

#### Step 3: Save and Verify
1. Click **Save Settings**
2. Test report generation with different currencies
3. Verify that cost basis calculations use the correct currencies

### For Reports

#### Step 1: Create a Report
1. Go to **Reports** section in dashboard
2. Click **Create New Report**
3. Select report type (Cost Basis, Balance, etc.)

#### Step 2: Select Currency
1. Choose from available currency options:
   - **Primary Options**: Your organization's configured currencies
   - **Secondary Options**: All 17 supported currencies
   - **Default**: USD (always available)
2. The system will validate your selection

#### Step 3: Generate Report
1. All fiat values will be converted to your selected currency
2. Historical rates will be used for accuracy
3. Exchange rate documentation will be included

### For ERP Integration

#### Automatic Currency Detection
When you connect your accounting system (Xero, QuickBooks), TRES will:
1. **Xero**: Automatically detect your Xero organization's base currency
2. **QuickBooks**: Automatically detect your QuickBooks company's currency
3. **Validation**: Check if the detected currency is supported by TRES
4. **Configuration**: Set up your organization with the detected currency

#### Manual ERP Setup
If you choose manual ERP setup:
1. Go to **Integrations** → **ERP Systems**
2. Click **Manual ERP** or **Universal ERP**
3. Select your currency from the dropdown
4. Upload your chart of accounts
5. Complete the setup process

---

## Currency Selection Examples

### Single Currency Setup
**For US-based companies:**
- Primary Currency: USD
- Configuration: `["USD"]`
- Use Case: Simple US operations, single tax jurisdiction

### Multi-Currency Setup
**For European companies:**
- Primary Currency: EUR
- Configuration: `["EUR", "GBP", "CHF"]`
- Use Case: EU operations with UK and Swiss subsidiaries

### Global Operations
**For international corporations:**
- Primary Currency: USD
- Configuration: `["USD", "EUR", "GBP", "JPY", "CAD", "AUD"]`
- Use Case: Worldwide operations, multiple tax jurisdictions

### Regional Examples

**North American Operations:**
- US Company: `["USD"]`
- Canadian Company: `["CAD", "USD"]`
- US-Canada Operations: `["USD", "CAD"]`

**European Operations:**
- EU Company: `["EUR"]`
- UK Company: `["GBP", "EUR"]`
- Swiss Company: `["CHF", "EUR"]`
- Multi-EU Operations: `["EUR", "GBP", "CHF", "SEK"]`

**Asia-Pacific Operations:**
- Japanese Company: `["JPY", "USD"]`
- Australian Company: `["AUD", "USD"]`
- Singapore Company: `["USD", "EUR"]`
- Regional Operations: `["USD", "JPY", "AUD", "IDR"]`

---

## Best Practices

### Currency Selection Guidelines
1. **Start with Primary Currency**: Always include your main operating currency
2. **Add Tax Currencies**: Include currencies for all tax jurisdictions
3. **Consider Future Needs**: Add currencies for planned expansion
4. **Avoid Over-Configuration**: Too many currencies can complicate reporting

### Report Generation
1. **Consistent Currency**: Use same currency across related reports
2. **Historical Consistency**: Maintain currency for year-over-year comparisons
3. **Tax Compliance**: Use appropriate currency for tax jurisdictions
4. **Documentation**: Document currency choices in report notes

### ERP Integration
1. **Verify Before Connecting**: Check your ERP's base currency before connecting
2. **Test After Connection**: Generate test reports to verify currency accuracy
3. **Monitor Changes**: Set up alerts for currency changes in ERP systems
4. **Regular Reviews**: Periodically review currency settings for accuracy

---

## Troubleshooting

### Common Issues

**Currency Not Supported**
- **Problem**: Selected currency not in supported list
- **Solution**: Use USD as fallback or request currency addition

**ERP Currency Mismatch**
- **Problem**: ERP currency differs from TRES settings
- **Solution**: Update organization settings to match ERP

**Historical Data Issues**
- **Problem**: Missing historical prices for selected currency
- **Solution**: Check pricing data availability or use USD

**Report Generation Errors**
- **Problem**: Currency-related errors in reports
- **Solution**: Verify currency configuration and data availability

### Getting Help
For currency-related issues:
1. Check organization settings
2. Verify ERP integration currency
3. Contact support with specific error messages
4. Provide organization ID and currency details

---

## Requesting New Currencies

To request support for additional currencies:
1. Contact TRES support team
2. Provide business justification
3. Specify currency code and requirements
4. Allow 2-4 weeks for implementation

---

## Related Documentation
- [Dashboard Module](./dashboard/README.md) - Currency display in dashboards
- [Reports Module](./reports/README.md) - Currency selection in reports
- [Pricing Module](./pricing/README.md) - Currency pricing mechanisms
- [ERP Integration](./erp/README.md) - Currency synchronization with ERP systems

