# Staking Data in Solana

Gain insightful and comprehensive staking data from Solana to enhance your analysis and decision-making processes.

**Purpose:** Support data engineers and analysts in accessing and understanding different types of staking data available for Solana within the ledger and staking data product.

---

## 1) User Flows

### Flow A — Accessing Staking Data
- **When:** When you need detailed staking insights for Solana.
- **Preconditions:** Access to the ledger.
- **Steps:**
  1) Access the ledger where Solana staking data is stored.
  2) Query for rewards, MEV, commission, or block rewards.
  3) Retrieve the required data efficiently.
- **Result:** Comprehensive data retrieved for analysis.
- **Pitfalls:** 
  - Ensure accurate querying to avoid missing important data.
  - Be aware of rate limits to prevent access issues.

### Flow B — Consuming Staking Data Product
- **When:** When integrating staking data into reports or tools.
- **Preconditions:** Access to the staking data product.
- **Steps:**
  1) Connect to the staking data product.
  2) Identify the type of data needed (e.g., rewards, MEV).
  3) Integrate the data with analytics tools for further analysis.
- **Result:** Integrated data ready for use in analytics.
- **Pitfalls:** 
  - Ensure compatibility with tools used for consumption.
  - Verify data integrity during integration.

---

## 2) Q&A

- **Q:** What types of staking data are available for Solana?
  **A:** You can access rewards, MEV, commission, and block rewards.
- **Q:** Where is the staking data stored?
  **A:** The data is stored in the ledger and is accessible via the staking data product.
- **Q:** Can I consume this data in real-time?
  **A:** Yes, the data is available for integration with your real-time analytics tools.

---

## 3) Detailed Explanation

### Concepts
- **Rewards:** Earnings from staking activities.
- **MEV (Maximal Extractable Value):** Value extracted from executing blockchain strategies.
- **Commission:** Fees taken by validators.
- **Block Rewards:** Compensation received for block validation.

### How it Works (High-Level)
- Data is collected across different staking activities on Solana and stored in a structured format.
- The ledger tracks the owner account of each staking account, and rewards are tracked per staking account.
- For each reward, the validator is the original sender, and the sender is the staking account. The data provides details about the validator rather than the staking account that received the reward.
- This data can be accessed through a dedicated ledger and a staking data product interface.
- Analysts and engineers can query and integrate this data into various analytics tools to glean insights and drive decisions.
