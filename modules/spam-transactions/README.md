# Spam Classification

An automated system that identifies and classifies spam tokens and suspicious transactions using multiple security data sources. Once classified, assets and their related transactions are marked with a SPAM tag, which can be filtered in your views. Users can also manually mark or unmark assets as spam.

**Purpose:** Automatically identifies potentially fraudulent or low-value tokens to keep your transaction data clean. Spam classifications help users filter out unwanted transactions and are visible throughout the platform.

---

## 1) How Spam Detection Works

### Automatic Classification Process

- **When:** New or unknown tokens appear in transactions from supported platforms (EVM chains, Solana)
- **How it Works:**
  1) The system automatically detects a new token/asset in your transactions
  2) The spam classification service runs in the background
  3) Multiple security sources are queried (GoPlus, Redefine, RugCheck, and others)
  4) The asset is analyzed for spam indicators and risk factors
  5) If classified as spam, the asset and all related transactions are automatically marked
  6) The SPAM tag appears on the asset and its transactions throughout the platform
- **Result:** Spam tokens are automatically flagged and excluded from normal views by default
- **Limitations:** 
  - Classification runs automatically in the background and may take a moment
  - Works only on supported platforms (EVM chains and Solana)
  - New legitimate tokens may occasionally be misclassified

### How Users See Spam Classifications

- **In Transaction Views:**
  - Transactions marked as spam show a "SPAM" tag in the Tags column
  - The SPAM tag displays with an information icon (hover to see details)
  - By default, spam transactions are hidden from normal views
  - Users can filter to show spam using the Tags filter in the Ledger page
  
- **In Asset Views:**
  - Spam assets display a red "SPAM" badge next to the asset name
  - The badge appears in tables, cards, and other asset listings
  - Spam assets are clearly marked for visibility

- **Filtering Spam Transactions:**
  - In Ledger, use the "Tags" filter dropdown
  - Search for "spam" or scroll to find "SPAM" option
  - Check the SPAM box to include spam transactions in your view
  - Click "Apply" to show filtered results
  - By default, spam is excluded from transaction views

### Manual Spam Management

- **When:** You need to override the automatic classification
- **How to Manually Mark as Spam:**
  1) Navigate to Assets or Ledger view
  2) Find the asset you want to mark
  3) Use the dropdown menu (three dots) next to the asset
  4) Select "Mark as SPAM" option
  5) This opens a support request to manually classify the asset
  6) Once processed, the asset and all related transactions are marked as spam

- **Impact of Manual Classification:**
  - Manual classifications override automated ones
  - All transactions involving that asset are also marked as spam
  - The classification is logged in audit history
  - Manual changes require appropriate permissions

- **Restrictions:**
  - Users may need authorization to modify spam classifications directly
  - Some spam tags show "You are not authorized for this action" if you lack permissions
  - Direct editing may require contacting support through the "Mark as SPAM" feature

---

## 2) Q&A (Short & Direct)

- **Q:** How does the system detect spam?
  **A:** It automatically queries multiple external security sources (GoPlus, Redefine, RugCheck, and others) that provide data about token safety, contract verification, and known scams. The classification runs in the background when new assets are detected.

- **Q:** What platforms are supported?
  **A:** The system supports EVM-based chains (Ethereum, Polygon, Arbitrum, etc.) and Solana. Different classification methods are used for each platform type.

- **Q:** Where do I see spam classifications?
  **A:** Spam appears as a "SPAM" tag on transactions in the Ledger view and as a red "SPAM" badge on assets in the Assets view. By default, spam transactions are hidden - you need to use the Tags filter to show them.

- **Q:** How do I view spam transactions?
  **A:** In the Ledger page, open the "Tags" filter dropdown, check "SPAM", and click "Apply". This will show all transactions marked as spam in your results.

- **Q:** Can I manually mark something as spam?
  **A:** Yes, use the dropdown menu next to any asset and select "Mark as SPAM". This opens a support request. Note that you may need appropriate permissions - some users will see "You are not authorized for this action" when attempting to modify classifications.

- **Q:** Will marking something as spam delete it?
  **A:** No, it doesn't delete anything. Spam tagging is for filtering - the data remains in the system but is hidden by default. You can always include spam in your views using the filter.

- **Q:** What if something is incorrectly classified as spam?
  **A:** Contact support through the "Mark as SPAM" feature or similar channels to request reclassification. Manual corrections are logged in the audit trail.

- **Q:** What are the most common types of spam tokens?
  **A:** The most common types are dusting attacks (small amounts sent to track users), phishing tokens (designed to steal information), honeypot tokens (that can't be sold), rug pull tokens (projects that disappear after collecting funds), and unsolicited airdrops (sent without permission for tracking purposes).

---

## 3) Detailed Explanation

### Concepts

- **Spam Token:** A digital asset that is unsolicited, low-value, or potentially malicious. Common types include:
  - **Dusting Attacks**: Small amounts of crypto sent to many addresses to track and de-anonymize users
  - **Phishing Tokens**: Fraudulent tokens designed to trick users into revealing sensitive information
  - **Honeypot Tokens**: Tokens that appear legitimate but cannot actually be sold once purchased
  - **Rug Pull Tokens**: Tokens from projects that disappear after collecting funds
  - **Unsolicited Airdrops**: Tokens sent without permission that may be used for tracking or scams
  - **Low-Value Tokens**: Tokens with no real value or trading volume
  
- **Automatic Classification:** The system runs spam detection automatically when new assets are detected, using multiple security data sources and internal analysis
  
- **Manual Override:** Users can manually mark assets as spam or not spam through support requests, which takes precedence over automated classifications
  
- **Spam Transactions:** Transactions involving spam assets are automatically marked with the spam classification for easy filtering
  
- **Audit Trail:** All spam classifications (automatic and manual) are logged with timestamps, sources, and who made the decision

### Why Tokens Get Classified as Spam

The system considers an asset as spam if it exhibits multiple risk indicators. Here are the key factors:

**Malicious Behavior Indicators:**
- Contracts flagged for honeypot schemes (cannot be sold)
- Phishing activities detected
- Stealing attacks or known scam patterns
- Unverified or suspicious contract code

**Low Legitimacy Signals:**
- Very new contracts (less than 5 days old, indicating potential pump-and-dump schemes)
- No price history or trading volume
- No significant fiat value in transactions
- Doesn't interact with verified or valuable assets
- No gas transactions (indicating lack of legitimate usage)

**Risk Factors:**
- Code vulnerabilities in the smart contract
- Liquidity issues (tokens that can't be easily traded)
- Supply manipulation risks
- Associated with risky addresses or known scam senders

**Platform-Specific Checks:**
- **EVM Chains**: Analyzes contract code, token supply, liquidity pools, and sender reputation through services like GoPlus and Asteriskscan
- **Solana**: Uses RugCheck and other Solana-specific security services to verify token legitimacy and detect known scam patterns

**What Makes an Asset Safe (Not Spam):**
- Has a trading price with multiple pricing records
- Interacts with verified or valuable assets (like major cryptocurrencies)
- Has significant transaction volume and legitimate usage
- Contract has been verified on blockchain explorers
- Associated with reputable addresses and trading activity

### How it Works (High-Level)

The system runs automatically in the background when new assets are detected. It first checks if an asset is "safe" using internal heuristics (price data, transaction history, interactions with valuable assets). If the asset doesn't pass these safety checks, it queries external security providers (GoPlus, Redefine, RugCheck, Asteriskscan) to assess token safety, contract verification, malicious behavior, and known scam databases. Based on this combined analysis, assets are classified as spam or not spam. When classified as spam, both the asset and all transactions involving that asset receive the SPAM tag. By default, spam transactions are excluded from normal ledger views, but users can opt to include them using the Tags filter. Manual classifications override automated ones and are logged in the audit history. The SPAM tag appears consistently across the platform - in transaction tables, asset listings, and filter options.

### Data (Public Expectations)

- **Spam Tags:** Assets are tagged with either "spam" or "not spam" based on classification results
- **Classification Sources:** Each classification shows its source - either automated (model-based) or manual (user decision)
- **Transaction Impact:** When an asset is marked as spam, all transactions involving that asset are also marked as spam
- **Platform Support:** 
  - EVM chains (Ethereum, Polygon, Arbitrum, etc.) - uses EVM classifier
  - Solana - uses Solana-specific classifier
  - Other platforms may not have spam detection enabled
- **Supported Assets:** The system works with token contracts and can classify most fungible tokens (ERC-20, SPL tokens, etc.)

### Errors & Troubleshooting

| Error Message | What Happened | How to Fix |
|---|---|---|
| Classification skipped - unsupported platform | The platform doesn't have spam detection enabled | Currently, only EVM chains and Solana are supported |
| Asset already classified | This asset was already checked for spam | No action needed - check the classification status |
| Classification failed | External security sources are temporarily unavailable | Try again later; the system will retry automatically |
