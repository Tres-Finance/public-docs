### Notification Center
The Notification Center keeps your team informed by delivering targeted alerts when important activities finish or need attention.

### How It Works
- Listens for key events across your data (for example, data commits, portfolio changes, and report generation).
- Evaluates your alerting rules to decide if, when, and whom to notify.
- Routes to your chosen channels (email and/or Slack).

### Key Feature Breakdown
- Send timely alerts: Receive messages at the exact moment a process completes or a threshold is crossed, so teams act faster.
- Enforce your policies: Apply your own rules and thresholds to reduce noise and focus on what matters.
- Announce finished reports: Let stakeholders know immediately when results are ready.
- Support on‑demand broadcasts: Allow other parts of the platform to request messages instantly.

---

### Notification Rules You Can Enable
All rules support email and Slack delivery. You can use one or both channels per rule and tailor recipients for each alert.

#### Transaction Activity
- What it watches: Individual transactions within a time window.
- When it fires: When any single transaction is above or below your chosen amount threshold. You can focus the rule on a specific internal account, asset class, or fiat currency.
- Why it’s helpful: Surfaces unusually large or unusually small movements right away.
- Typical recipients: Finance, operations, risk, on‑call.
- Real‑time or not: Real‑time.
- Delivery options: Email, Slack.

#### Exposure to Asset
- What it watches: Your exposure to a specific asset class.
- When it fires: When exposure crosses a threshold you define. You can measure exposure by:
  - Percent of portfolio (e.g., “over 25% in DeFi tokens”),
  - Token amount (e.g., “under 1000 units”), or
  - Fiat value (e.g., “over $500,000”).
- Why it’s helpful: Keeps portfolio concentration and risk within policy limits.
- Typical recipients: Treasury, portfolio managers, finance leadership.
- Real‑time or not: Scheduled digests.
- Delivery options: Email, Slack.

#### Asset Price Deviation
- What it watches: Significant deviations in an asset’s price relative to your configured tolerance.
- When it fires: When price movement is over/under your defined deviation threshold.
- Why it’s helpful: Flags unusual market moves that may require action or review.
- Typical recipients: Treasury, traders, portfolio managers, leadership on major moves.
- Real‑time or not: Real‑time.
- Delivery options: Email, Slack.

#### Data Commit Completed
- What it watches: Data pipeline commits.
- When it fires: When a data commit finishes.
- Why it’s helpful: Confirms new data landed successfully so downstream work can begin.
- Typical recipients: Data engineering, analytics, operations.
- Real‑time or not: Scheduled digests.
- Delivery options: Email, Slack.

#### Report Ready
- What it watches: Report runs initiated by your team.
- When it fires: The moment a report is ready to view or download. Can include an AI‑generated summary if configured.
- Why it’s helpful: Moves stakeholders from waiting to reviewing without polling.
- Typical recipients: Finance, operations, leadership, report requesters.
- Real‑time or not: Real‑time.
- Delivery options: Email, Slack.

#### Recurring Report Ready
- What it watches: Scheduled reports.
- When it fires: As soon as the scheduled report completes.
- Why it’s helpful: Ensures routine reporting cycles are visible and on time.
- Typical recipients: The same audiences as ad‑hoc reports, often broader distribution lists.
- Real‑time or not: Real‑time when each scheduled run completes.
- Delivery options: Email, Slack.

#### Slashing Monitoring
- What it watches: Staking‑related slashing events for your tracked accounts or validators.
- When it fires: When a slashing event is detected for a monitored account.
- Why it’s helpful: Enables immediate awareness and response for at‑risk staked positions.
- Typical recipients: Treasury, staking operators, on‑call.
- Real‑time or not: Real‑time.
- Delivery options: Email, Slack.

Note: Thresholds, time ranges, units, recipients, and channels are configurable per rule. For example, you can set TX_ACTIVITY to “over $10,000 USD in the last 30 days” for a specific internal account, while EXPOSURE_TO_ASSET could be “over 20% in Stablecoins” measured by percent, for the whole organization.

---