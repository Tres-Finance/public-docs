# Transaction Rollups
Summarize many small sub-transactions into a single, clear entry per time interval. Rules let you decide what gets rolled up, how often, and how the resulting transaction is dated.
**Purpose:** Reduce noise in statements and reports while preserving accurate balances and auditability.

---

## 1) User Flows
### Flow A — Scheduled rollups (hands‑off)
- **When:** Rollups run on a schedule for all active rules.
- **Preconditions:** You have at least one active Rollup Rule and your wallets/platforms have synced recently.
- **Steps:**
  1) New activity is collected from your connected platforms ("last synced" is updated).
  2) For each active rule, the system finds the time windows to process since the last run.
  3) It creates one rollup transaction per interval that had activity (e.g., Daily → one per day; Monthly → one per month).
- **Result:** Your ledger shows clean summary entries per interval, labeled as `Rollup Tx`, replacing many tiny lines in reports while keeping totals intact.
- **Pitfalls:** If a wallet hasn’t synced yet, that window won’t roll up; empty intervals produce no rollup for that interval.

### Flow B — Configure a Rollup Rule (UI)
- **When:** You want to set up a new rollup for your organization.
- **Preconditions:** You have access to the TRES dashboard and permissions to manage automations.
- **Steps:**
  1) Go to **Automations** in the left navigation.
  2) Click **Add automation**.
  3) Choose **Create rollup**.
  4) Configure the rule: interval (Daily/Monthly), direction (Inflow/Outflow), asset, platform, internal account, cutoff time, and any optional filters (amount range, identifiers, method_ids, fees, exclude flags).
  5) Save.
- **Result:** A new Rollup Rule is added to your organization. It will run on schedule, and you can also trigger a manual run when needed.
- **Pitfalls:** Ensure the target wallet/platform is connected and has completed a recent sync; otherwise the first run will wait for "last synced".

---

## 2) Q&A (Short & Direct)
- **Q:** What does “partitioning by interval” mean?
  **A:** Each interval produces its own rollup entry. For example, with a Daily rule, 3 active days create 3 rollup transactions.
- **Q:** Which intervals can I use?
  **A:** Choose the interval on the Rollup Rule (e.g., Daily or Monthly). Pick the cadence that matches your reporting period.
- **Q:** Where is the rollup dated on the timeline?
  **A:** Inflows are dated at the start of the interval; outflows are dated at the end. This respects your configured `cutoff_time` (a second before/after the cutoff boundary as applicable).
- **Q:** Why start‑of‑interval for inflows and end‑of‑interval for outflows?
  **A:** It improves period clarity: inflows contribute to the opening position; outflows reduce the closing position, aligning with how many teams read statements. It also helps prevent temporary negative balances from rollups.
- **Q:** How do rollups interact with data collection (“last synced”)?
  **A:** Rollups work only with synced data. The run processes windows up to the most recent "last synced" point; new data picked up later is included in the next run.
- **Q:** What if a window has no activity?
  **A:** No rollup is created for that interval (nothing to summarize).

---

## 3) Detailed Explanation
### Concepts
- **Rollup Rule:** Your configuration that defines scope (asset/account/platform), direction (inflow or outflow), interval, and other options.
- **Interval:** The cadence for summarization (e.g., Daily or Monthly). Each interval becomes one potential rollup.
- **Partition (by interval):** The system splits time into interval “buckets”; one rollup per bucket that contains activity.
- **Direction:** Whether the rule summarizes inflows or outflows. This controls the dating behavior.
- **Cutoff Time:** The time boundary your organization uses to mark the end/start of a reporting day; rollup timestamps respect this.
- **Last Synced (Data Collection):** The latest timestamp up to which your wallet/platform data is available; rollups don’t go beyond it.
- **Rollup Transaction:** The summarized entry that represents many granular sub‑transactions within a single interval.

### How it Works (High‑Level)
- Data is collected from your connected platforms. Once synced, the system knows up to which point data is reliable ("last synced").
- For each active Rollup Rule, the system determines the date window since the rule’s last run and divides it into intervals (Daily/Monthly).
- It scans each interval for relevant sub‑transactions. If there’s activity, it creates exactly one rollup transaction for that interval.
- Dating rules:
  - Inflow rollups are dated at the start of the interval.
  - Outflow rollups are dated at the end of the interval.
  - Both honor your `cutoff_time` (the timestamp sits just before/after the boundary as appropriate).
- The rule is then marked ready for the next activation, and future runs continue from where this one finished.

### Data (Public Expectations)
- **Entities (names & purpose)**
  - `SubTransactionRollupRule` — Your rule definition (scope, direction, interval, and options like cutoff time).
  - `Rollup Transaction` — The summary entry created per interval that had activity.
- **Important fields (names & meaning)**
  - `name` — Friendly label shown in the UI/reports; does not affect logic.
  - `status` — `ACTIVE` to run on schedule; pause to stop new rollups.
  - `start_date` / `end_date` — Date range when the rule is in effect; windows outside are ignored.
  - `interval` — How often to summarize (`day`, `month`); drives partitioning and one-result-per-interval behavior.
  - `internal_account_id` — The specific wallet/account to summarize into; rollup entries are posted to this account.
  - `asset_id` — The asset to include (e.g., BTC, ETH); only sub-transactions in this asset are considered.
  - `platform` — Source platform to include and to respect for "last synced"; runs never go past that platform’s last-synced point. also for filtering sub transactions.
  - `balance_factor` (direction) — Inflow or Outflow; controls which transactions are rolled up and the dating rule (inflow at interval start, outflow at interval end).
  - `fees` — Whether to include related fees in the rollup; when enabled, fee amounts are summarized (often as separate fee rollup entries).
  - `cutoff_time` — Reporting boundary used to place the rollup timestamp at the interval start/end (per direction).
  - `buffer_in_days` — Expands the scan window backwards by N days to catch late/adjusted activity.
  - `sender_identifier` / `recipient_identifier` — Optional filters to include only transactions from/to specific addresses/identifiers.
  - `method_ids` — Optional allow-list of transaction method IDs to include; useful to target certain on-chain methods.
  - `activity` — Optional category/tag to filter matching activity.
  - `min_amount` / `max_amount` — Include only sub-transactions within this amount range.
  - `exclude_fiat` — skip fiat amounts when aggregating sub-transactions; the rollup transaction will not carry fiat totals.
  - `exclude_internal` — Exclude internal transfers between your own accounts.
  - `merge_with_inflow_tx` — When summarizing outflows that pair with inflows, merge the outflow rollup into the inflow entry to reduce clutter.
  - `subtx_type` — Restrict to a specific financial action (e.g., fee, reward); creates narrowly targeted rollups.
  - `run_internal_transfer_classification_on_rollups` — After creating rollups, also attempt to auto-classify/link internal transfers to keep books aligned.
  - `last_synced_at` — Operational concept: the latest collected data point for the platform; rollups won’t go past this cutoff.
  - `next_activation_date` — Scheduler hint: the next date the rule will run from; updated after each run.
- **Limits**
  - One rollup per interval per rule (only when activity exists in that interval).
  - First‑time runs require synced data; without a last‑synced timestamp, the system waits until your first sync completes.
