# Report Analyst

Chat with your financial reports in plain English - have a conversation, ask follow-ups, and dive deeper into your data. The Report Analyst uses AI to understand your exported report data and provide insights, comparisons, and summaries.

**Purpose:** Helps finance teams and analysts quickly understand their exported report data without manually analyzing spreadsheets. You can have ongoing conversations about your data, not just single questions. Only works with completed reports that have been exported from the platform (Excel, CSV formats).

**Tip:** In the Reports section, use the search bar and filters to quickly find the reports you want to analyze. Look for the Analyst icon in the STATUS column for reports that support this feature.

---

## 1) User Flows

### Flow A — Chat with an Exported Report

- **When:** You have an exported report (Excel/CSV) and want to understand it without reading the whole file
- **Preconditions:** Report must be exported and marked as "available for report analyst" (not all report types support this feature)
- **Steps:**
  1) Navigate to the **Reports** section from the left-hand menu
  2) In the reports table, look for reports with status showing "DONE" (green status indicator)
  3) Check the STATUS column - reports that support the analyst will show an icon (looks like a downward arrow in a circle)
  4) Hover over the icon to see the tooltip "Ask TRES Analyst about this report"
  5) Click the icon to open the chat interface
  6) Ask questions like "Get daily inflow summary in fiat value" or "What is the highest outflow fiat value?"
  7) Get back formatted summaries with numbers and insights
  8) Ask follow-up questions to dive deeper - the assistant remembers your conversation
- **Result:** Clear, formatted answers about your exported report data with comparisons and context
- **Pitfalls:** 
  - Only works when the STATUS shows "DONE" - processing or incomplete reports won't have the icon
  - The analyst icon only appears for supported report types (if you don't see the icon, that report type doesn't support chat)
  - Reports over 100MB are too large to process
  - Each new chat session starts fresh (no history saved between sessions)

### Flow B — Ask Specific Questions About Report Data

- **When:** You want to find specific information or patterns in your exported report data
- **Preconditions:** Have a completed exported report available (STATUS: DONE)
- **Steps:**
  1) In the Reports table, find the report you want to analyze (must show "DONE" status)
  2) Click the Analyst icon in the STATUS column of that report
  3) Wait for the chat interface to open
  4) Ask specific questions about your data, for example:
     - "Get daily inflow / outflow / fees summary in fiat value"
     - "Find anomalies transfers and explain why"
     - "What is the highest outflow fiat value?"
     - "Help me produce 12 months cash flow forecast"
  5) Get focused answers with exact numbers and relevant context
  6) Ask follow-up questions to narrow down or expand the analysis
- **Result:** Specific answers pulled from your report data with clear formatting
- **Pitfalls:** 
  - Can only answer questions about data that exists in the specific report you're viewing
  - Each new report chat starts fresh

### Flow C — Compare Data Across Time or Categories

- **When:** You want to understand changes or differences in your report data
- **Preconditions:** Have a report with historical or comparative data (STATUS: DONE)
- **Steps:**
  1) In Reports, locate a DONE status report that contains comparative data
  2) Click the Analyst icon in the STATUS column
  3) Once the chat opens, ask comparative questions like:
     - "How much has my total net worth changed?"
     - "What's the difference between this month and last month?"
     - "Which accounts had the biggest increases?"
     - "Compare my current asset allocation to last quarter"
  4) Get side-by-side comparisons with clear differences highlighted
  5) Ask for explanations when the data shows significant changes
- **Result:** Comparative analysis showing changes, trends, and differences in your data
- **Pitfalls:** 
  - Only works if the report contains the historical data you're asking about
  - Each report is independent - can't compare across different report files
  - Make sure the report status is DONE before trying to open the analyst

---

### Common Questions You Can Ask

The Report Analyst can answer various questions about your exported report data. Here are examples of what you might ask:

**Cash Flow & Transactions:**
- "Get daily inflow / outflow / fees summary in fiat value"
- "Get daily inflow / outflow / fees summary in token amount"
- "Get daily inflow / outflow / fees summary in fiat value by method id"
- "What is the highest outflow fiat value?"
- "Show me all withdrawals this month"

**Anomaly Detection & Analysis:**
- "Find anomalies transfers and explain why"
- "Show me unusual transaction patterns"
- "Which accounts have the highest volatility?"
- "Identify transactions that seem out of pattern"

**Forecasting & Planning:**
- "Help me produce 12 months cash flow forecast"
- "What trends do you see in my balance changes?"
- "Predict likely outcomes based on current data"

**Balance & Asset Analysis:**
- "What are my top 10 assets by value?"
- "Show me all balances over $5,000"
- "Which assets have the highest fiat value?"
- "What's my total net worth?"

**Comparative Analysis:**
- "How much has my balance changed since last month?"
- "What's the difference between this report and the previous one?"
- "Which accounts had the biggest increases?"
- "Compare current vs previous asset allocation"

---

## 2) Q&A (Short & Direct)

- **Q:** What types of reports can I use?
  **A:** Only exported reports from the platform that are specifically marked as available for report analyst. In the Reports section, look for reports with STATUS showing "DONE" and check the STATUS column for the Analyst icon (tooltip: "Ask TRES Analyst about this report").

- **Q:** What can I ask about?
  **A:** Anything in your exported report data - cash flow summaries (daily inflow/outflow/fees in fiat or token amounts), transaction anomalies, highest/lowest values, balance changes, cost basis, historical trends, forecasting, and more. The assistant understands finance terms and makes comparisons automatically.

- **Q:** Can I ask questions about data that's not in a report?
  **A:** No, the Report Analyst only works with exported reports. If you need to analyze raw data that hasn't been exported to a report yet, you'll need to export it first.

- **Q:** Can I have a full conversation or just single questions?
  **A:** You can have a full conversation! The assistant remembers the context throughout your chat session, so you can ask follow-up questions, dive deeper into specific areas, and build on previous answers. This is a chat interface, not just a Q&A tool.

- **Q:** I don't see the Analyst icon on my report - why?
  **A:** The feature only works with certain report types. If the STATUS is "DONE" but you don't see the Analyst icon in the STATUS column, that report type doesn't support chat functionality.

- **Q:** Will it explain why values changed?
  **A:** Yes, the assistant can include relevant market news or financial context to help explain significant changes when that information would be useful.

---

## 3) Detailed Explanation

### Concepts

- **Exported Reports:** Financial data files (Excel, CSV) that you've generated from the platform. Examples include:
  - Transaction reports (raw transactions, extended with cost basis)
  - Balance reports (current, historical, trends)
  - Accounting reports (cost basis, reconciliation, journals)
  - Specialized reports (staking, audit logs, roll forwards)
  
- **Report Analyst Chat:** A full conversation interface where you can have ongoing discussions about a specific report - not just single questions. The assistant remembers the context throughout your session, allowing you to ask follow-ups, explore different angles, and dive deeper into your data.

- **Enhanced Answers:** When helpful, the assistant adds relevant market news or context to explain significant changes in your data.

- **Supported Report Types:** The feature only works with certain report types marked as "available for report analyst" - look for the Analyst icon (circle with downward arrow) in the STATUS column on compatible reports.

### How it Works (High-Level)

The Report Analyst uses AI to read your exported report data and conduct conversations in plain English. When you start chatting about a report, it loads the report file and maintains context throughout your session. As you ask questions and follow-ups, the assistant analyzes the relevant data, provides answers with formatted numbers and insights, and remembers what you discussed earlier. The system can also add relevant market news or context when it might help explain significant changes in your data.

### Data (Public Expectations)

- **What Reports Are:** In Tres, reports are exported Excel/CSV files containing detailed financial data. Common report types include:
  - **Transaction Reports:** Basic/Extended Raw Transactions with wallet context, counterparties, decoded data, and valuations
  - **Balance Reports:** Current balances, historical balances, and balance trends across wallets and assets
  - **Accounting Reports:** Cost basis, realized gains/losses, COGS, pre/post-sync journals, reconciliation status
  - **Specialized Reports:** Staking data, audit logs, internal accounts, asset roll forwards, and more
  
- **Available Report Data:** Depending on the report type, you can ask about:
  - Transactions: timestamps, amounts, directions (inflow/outflow), counterparties, platforms, transaction hashes
  - Balances: current and historical balances in token and fiat values, balance changes over time
  - Accounting: cost basis, realized P/L, COGS, ERP mappings, inventory impacts
  - Staking: validator performance, rewards, APY, staking status
  - Audit: user actions, timestamps, resources, compliance data

- **Chat vs Single Questions:** You can have a full conversation! Ask follow-up questions, dive deeper into specific areas, and build on previous answers within the same chat session.

- **Important Information:**
  - Only exported reports that are completed can be analyzed
  - The assistant can only answer questions about data that exists in the specific report you're chatting with
  - Each report is independent - you can't chat about data across multiple reports at once
- **Limits:** 
  - Maximum report size: 100MB (larger reports cannot be processed)
  - Each question has up to 10 minutes to process
  - Report data is cached for faster access during your session

### Errors & Troubleshooting

| Error Message | What Happened | How to Fix |
|---|---|---|
| "Report is still processing" | Your report isn't ready yet | Wait for the report to finish generating, then try again |
| Report exceeds size limit | Your report is over 100MB | Request a smaller, filtered, or summarized version of your report |
| "Sorry, something went wrong..." | A processing error occurred | Try your question again. If it persists, contact support |

