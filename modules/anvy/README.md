# AnyV — AI-Powered CSV Transaction Upload

AnyV is an intelligent CSV transformation system that automatically converts transaction data from any spreadsheet format into the platform's required format.

**Purpose:** Helps users upload transaction records from external sources (exchanges, wallets, custom spreadsheets) without manually reformatting their data, saving hours of tedious mapping work.

---

## Getting Started — How to Upload Transactions via AI-Powered CSV

Follow these steps to upload and transform your transaction CSV file:

### Step 1: Navigate to the Feature

1. Go to the **Ledger Tasks** tab in your dashboard
2. Click the **Actions** button
3. Select **Add Transactions**
4. Choose **AI-driven mapping** option

You'll see an introduction screen explaining the process:
- Upload your CSV file
- AI-powered mapping assistance
- Step-by-step guidance for field mapping

### Step 2: Upload Your CSV File

1. Click **Try it out** to proceed
2. Click the file upload area or drag and drop your file
3. Select your CSV or Excel (.xlsx) file from your computer
4. Click **Upload** to submit the file
5. Wait a few moments while the system analyzes your file structure

The system will automatically detect unique row patterns in your CSV to help with mapping.

### Step 3: Map Your Data Fields

Once your file is uploaded, you'll see sample rows from your CSV that need mapping:

1. **Review the sample row** displayed on the left side - this shows your original CSV data
2. **Map each field** to the corresponding platform field on the right side:
   - **Date/Time**: When the transaction occurred
   - **Amount**: Transaction quantity
   - **Asset**: The cryptocurrency or token (e.g., BTC, ETH, USDT)
   - **Network**: The blockchain platform (e.g., Ethereum, Bitcoin, Polygon)
   - **Direction**: Whether you sent (sender) or received (receiver)
   - **Financial Action**: Type of transaction (Trade, Transfer, Deposit, Withdrawal, etc.)
   - **Participating Wallet**: Wallet address involved (use "native" if not applicable)
   - **Fiat Value** (optional): USD or other currency value at the time
3. **Complete at least 3 examples** - the more diverse examples you provide, the better the AI understands your format
4. Click **Next** or **Continue** to move to the next sample row
5. After completing all mappings, click **Submit** or **Finish Mapping**

**Tip:** Choose examples that represent different types of rows in your CSV (e.g., buys, sells, transfers, different date formats) for best results.

### Step 4: AI Transformation Process

After submitting your mapping examples:

1. The AI analyzes your patterns and generates transformation logic
2. Your entire CSV is automatically transformed (typically 1-10 minutes)
3. You'll see status updates:
   - "AI Transforming" - Processing your file
   - "Passed Transforming" - Success, ready for review
   - "Failed Transforming" - Needs additional examples (see troubleshooting below)

### Step 5: Review & Approve Transformed Data

Once transformation succeeds:

1. You'll receive a notification that your file is ready for review
2. Click to view the preview of transformed transactions
3. **Review carefully:**
   - Check dates are correct
   - Verify amounts and assets match your original data
   - Ensure networks and financial actions are properly categorized
4. **Make your decision:**
   - Click **Approve** to import all transactions into your ledger
   - Click **Cancel** or **Reject** if something looks incorrect

**Important:** Once approved, transactions are added to your ledger. Review carefully before confirming.

### Step 6: Transactions Imported

After approval:
- Transactions are processed and added to your ledger
- You can view them in the **Ledger Tasks** tab
- They're now part of your permanent transaction history

### Troubleshooting: If Transformation Fails

If you see "Failed Transforming" status:

1. Check the error messages to understand what went wrong (e.g., invalid dates, unsupported networks)
2. You'll be prompted to provide additional mapping examples
3. Focus your new examples on the specific issues mentioned in the errors
4. Submit the additional examples
5. The AI will retry using both old and new examples combined
6. Repeat until transformation succeeds

**Common fixes:**
- Add examples with different date formats if dates are failing
- Ensure asset symbols match platform standards
- Map missing required fields like Participating Wallet (use "native" as fallback)
- Provide examples for unusual transaction types

---

## 1) User Flows

### Flow A — Upload & Transform Custom CSV

- **When:** A user has transaction data in a custom CSV or Excel file that doesn't match the platform's template
- **Preconditions:** Valid CSV/Excel file with transaction data; must have identifiable columns for core transaction fields
- **Steps:**
  1) User uploads their CSV or Excel file through the "Add Transaction" modal
  2) System detects unique row patterns and presents sample rows to the user
  3) User maps at least 3 sample rows from their format to the platform's template (showing which columns correspond to Date, Amount, Asset, etc.)
  4) AI analyzes the mapping examples and transforms the entire file automatically
  5) System validates the transformed data and displays the status
  6) If successful, user reviews the AI-generated transformation and approves to continue
  7) Transactions are processed and added to the ledger
- **Result:** All transactions from the custom CSV are imported into the platform's ledger without manual row-by-row entry
- **Pitfalls:**
  - **Insufficient mapping examples** — Providing fewer than 3 examples or non-representative samples can cause transformation failures. Always map diverse row types.
  - **Missing required fields** — If the original CSV lacks critical data (date, amount, or asset), AI cannot reliably infer values. Ensure source data is complete.
  - **Format inconsistencies** — Mixed date formats or currency symbols within the same column may confuse the transformation. Clean data before upload when possible.

### Flow B — Retry with Additional Examples

- **When:** The AI transformation fails or produces incorrect results
- **Preconditions:** Previous transformation attempt has completed with "AI Failed Transforming" status
- **Steps:**
  1) User receives notification that transformation needs improvement
  2) System shows which rows or patterns caused validation errors
  3) User provides additional mapping examples focusing on the problematic patterns
  4) AI re-processes the file using both old and new examples
  5) System validates again and either succeeds or requests more examples
- **Result:** User iteratively teaches the AI until transformation succeeds, without starting over
- **Pitfalls:**
  - **Repeating same pattern** — Adding more examples that look identical to existing ones won't help. Focus on edge cases and variations.
  - **Ignoring error messages** — System highlights specific issues (invalid dates, missing fields); new examples should specifically address these.
  - **Timeout waiting** — Users have 7 days to approve transformations before workflow expires. Check notifications regularly.

### Flow C — Review & Approve Transformation

- **When:** AI has successfully transformed the file and awaits user confirmation
- **Preconditions:** Transformation status is "AI Pending Approval"
- **Steps:**
  1) User receives notification that file is ready for review
  2) System displays preview of transformed transactions
  3) User reviews sample rows to verify accuracy
  4) User either approves to process or cancels to reject
  5) If approved, system ingests all transactions into the ledger
- **Result:** User confirms data accuracy before permanent import, preventing bad data from polluting their records
- **Pitfalls:**
  - **Skipping review** — Approving without checking can import incorrect amounts, dates, or assets. Always spot-check critical fields.
  - **Approval timeout** — Workflows expire after 7 days; unreviewed transformations are automatically cancelled.

---

## 2) Q&A (Short & Direct)

- **Q:** What file formats does AnyV support?
  **A:** CSV and Excel (.xlsx) files. The system automatically detects and processes Excel files by converting them internally.

- **Q:** How many mapping examples do I need to provide?
  **A:** Minimum 3 rows, but providing 5-10 diverse examples significantly improves accuracy. The system can use up to 25 unique examples for complex transformations.

- **Q:** What happens if the AI transformation fails?
  **A:** You'll receive a notification with specific error details. You can then provide additional mapping examples to help the AI learn the correct pattern, without re-uploading your file.

- **Q:** Can I cancel a transformation in progress?
  **A:** Yes. Transformations awaiting approval can be cancelled at any time within the 7-day review window.

- **Q:** How long does transformation take?
  **A:** Most files transform within 1-10 minutes depending on size and complexity. You'll receive a notification when ready for review.

- **Q:** What if my CSV has columns the platform doesn't support?
  **A:** That's fine. AnyV only maps the columns you specify in your examples. Extra columns are ignored automatically.

- **Q:** Can I reuse a transformation for similar files?
  **A:** Not directly. Each file upload creates a new transformation session, but you can use the same mapping pattern manually for consistency.

- **Q:** What's the maximum file size?
  **A:** The system can handle standard CSV files. For very large files (100K+ rows), performance may vary. Contact support for bulk imports.

- **Q:** How do I know if my transformation was successful?
  **A:** You'll see status updates throughout the process: "Pending Mapping" → "AI Transforming" → "Passed Transforming" → "Pending Approval". Check the file status in your upload history.

- **Q:** What if I need to modify a transformation after approval?
  **A:** Once approved and processed, transactions become part of your ledger. You'll need to edit or delete individual transactions through the standard ledger interface.

---

## 3) Detailed Explanation

### Concepts

- **Mapping Examples:** Sample rows showing how your CSV columns correspond to the platform's required fields (Date, Amount, Asset, Direction, etc.). The AI learns transformation logic from these examples.
- **Transformation:** The process where AI generates code to convert your entire file from its original format to the platform's standard structure.
- **Validation:** Automated checks that ensure transformed data meets requirements (valid dates, supported networks, required fields present, amounts are numeric, etc.).
- **Transaction Hash:** A unique identifier for blockchain transactions. If your CSV doesn't have this, the system generates one automatically for internal tracking.

### How it Works (High-Level)

AnyV orchestrates a multi-step workflow across the platform's AI and data processing systems:

1. **Upload & Initialization:** When you upload a file, the system creates a tracking record and generates a secure storage location. The workflow enters a waiting state for your input.

2. **Mapping Collection:** The system analyzes your file to identify unique row patterns (up to 25 variations). You see these as sample rows in the UI and indicate how each field should map to the platform's template.

3. **AI Transformation:** Once you provide examples, an AI agent generates transformation logic. The agent has access to tools for testing code against your examples, validating output format, and querying the platform for valid values (like supported networks or asset identifiers). It iterates until the transformation passes validation rules.

4. **Content Validation:** The generated transformation runs against your full file. The system checks for data quality issues: invalid dates, unsupported networks, missing required fields, inconsistent transaction hashes, and more. If validation fails, you can provide additional examples to refine the transformation.

5. **Review & Approval:** Once validation passes, you see a preview and decide whether to proceed. This gate prevents importing incorrect data.

6. **Processing:** After approval, transactions flow through the standard import pipeline where they're enriched, categorized, and added to your ledger.

If the AI encounters issues it can't resolve, the workflow pauses and notifies you. You can add more mapping examples to teach the AI about edge cases, and it will retry with the combined knowledge from all examples.

### Data (Public Expectations)

**Entities:**
- **Manual CSV Record:** Tracks your upload's lifecycle, stores references to files and mapping examples, maintains current status
- **Mapping Examples:** Your sample row transformations stored as structured data
- **Transformation Code:** AI-generated logic (not exposed to users) that powers the conversion

**Important Fields in Your Mapping:**
- **Date/Time:** Must map to a valid timestamp (ISO format preferred)
- **Amount:** Numeric value representing transaction quantity
- **Asset/Currency:** Identifier for the token or coin (symbol or contract address)
- **Network/Platform:** Blockchain or platform name (Ethereum, Bitcoin, Manual, etc.)
- **Direction:** Whether you sent or received (Sender/Receiver)
- **Financial Action:** Type of transaction (Trade, Transfer, Deposit, Withdrawal, etc.)
- **Participating Wallet:** Wallet address involved (can be "native" if not applicable)
- **Fiat Value (optional):** USD or other currency value at transaction time

**Limits:**
- Maximum 25 unique mapping examples per file
- Workflow times out after 10 minutes for file upload, 24 hours for mapping, 7 days for approval
- AI transformation has maximum 50 iteration steps before halting

### Errors & Troubleshooting

| Exact Message | Likely Cause | Fix |
|---------------|--------------|-----|
| `Invalid date` | Date format not recognized or contains invalid values | Ensure dates are in ISO format (YYYY-MM-DD) or a standard format. Check for typos in month/day/year values. |
| `Invalid Network` | Network/platform name doesn't match supported options | Use exact platform names: Ethereum, Bitcoin, Polygon, Solana, Manual, etc. |
| `Invalid Participating Wallet` | Wallet field is empty or missing | Map to a valid wallet address. If none exists, use "native" as placeholder. |
| `Missing mandatory values: Participating Wallet` | Required field has no data in source CSV | Provide a fallback value in your mapping examples, or use "native" when wallet information is unavailable. |
| `Invalid Direction` | Direction field doesn't match expected values | Map to exactly "sender" or "receiver" (lowercase). |
| `Invalid financial action` | Financial action type not recognized | Use standard action types: Trade, Transfer, Deposit, Withdrawal, Airdrop, Fee, Income, etc. |
| `Invalid amount` | Amount field contains non-numeric data | Ensure amounts are mapped to numeric columns. Remove currency symbols and formatting. |
| `Invalid fiat currency` | Fiat currency code not supported | Use standard 3-letter currency codes: USD, EUR, GBP, etc. |
| `Invalid asset identifier` | Asset/token identifier not found in system | Verify asset symbol or contract address matches the platform's asset database. |
| `AI_FAILED_TRANSFORMING` status | AI couldn't generate valid transformation | Add more diverse mapping examples covering different row patterns. Focus on edge cases mentioned in error details. |
| `AI_FAILED` status | Transformation failed due to multiple errors | Contact support with your CSV key for assistance. |
| `AI_CANCELLED` status | Workflow timed out or was manually cancelled | Re-upload file and complete mapping within time limits (24 hours for mapping, 7 days for approval). |
| `AI_INVALID` status | Transformed data contains validation errors | Download the CSV with error comments, fix the issues in your original file, and re-upload. |
