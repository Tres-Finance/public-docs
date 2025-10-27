# Matching Library

A transaction reconciliation system that matches sub-transactions between two organizations using simple rule-based strategies followed by complex constraint-programming algorithms.

**Purpose:** Helps finance teams reconcile transactions across custodians, exchanges, and counterparties by automatically finding and grouping matching transactions based on amount, timing, and identifiers.

---

## 1) User Flows

### Flow A — Standard Reconciliation (Dashboard-Driven)
- **When:** Running full reconciliation between two organizations
- **Preconditions:** 
  - Two organizations with sub-transactions in the database
  - Date range for reconciliation period
  - Asset classes are verified
  - Access to Django admin Organization page
- **Steps:**
  1) Navigate to Django admin → Organizations → Select orgs → "Trigger matching workflow" action
  2) Fill in form: select Organization 1 and Organization 2, set start/end dates
  3) Click "Run Simple Strategy" to execute `SIMPLE_STRATEGY` (7 progressively looser configs)
  4) System processes all asset classes in parallel, trying each strategy sequentially
  5) Wait for completion (check Temporal UI or logs)
  6) Review matched transactions in database
  7) Click "Run Complex Matching" to process remaining unmatched transactions
  8) Configure complex parameters (delta_time_days, delta_amount, batch sizes)
  9) System finds M-to-N matches using constraint programming
- **Result:** Transactions are grouped into match groups with metadata showing match quality
- **Pitfalls:** 
  - Must run simple strategy BEFORE complex (complex only processes unmatched)
  - Large date ranges can timeout; use 1-3 month chunks
  - Matched transactions won't be re-matched; delete match groups to retry
  - Running complex before simple will miss obvious 1-to-1 matches

### Flow B — Custom Simple Matching (Advanced)
- **When:** Need specific matching rules different from SIMPLE_STRATEGY
- **Preconditions:**
  - Unmatched sub-transactions exist for the date range
  - Know desired tolerance thresholds (amount %, time window, identifier matching)
- **Steps:**
  1) Navigate to Django admin → Organizations → "Trigger matching workflow"
  2) Configure simple matching parameters in form
  3) Click "Run Simple Matching" to execute single strategy with custom config
  4) System processes using only the specified rules (not the 7 SIMPLE_STRATEGY configs)
- **Result:** Matches found using your custom rules only
- **Pitfalls:**
  - Single strategy may miss matches that looser rules would catch
  - Use SIMPLE_STRATEGY (Flow A) for comprehensive matching

### Flow C — Complex Matching from Dashboard
- **When:** After running simple strategies, unmatched M-to-N relationships remain
- **Preconditions:**
  - Simple strategy matching already completed (SIMPLE_STRATEGY recommended)
  - Unmatched transactions likely involve splits/combines between orgs
  - Understand complex matching config parameters
- **Steps:**
  1) Navigate to Django admin → Organizations → "Trigger matching workflow"
  2) Select same org pair and date range used for simple matching
  3) Configure complex parameters (see Configuration section below)
  4) Click "Run Complex Matching"
  5) System processes in batches using constraint programming
  6) Review matches in Temporal UI logs
- **Result:** Complex M-to-N matches (e.g., 3 subtxs from A match 2 subtxs from B)
- **Pitfalls:**
  - Computationally expensive; takes 5-30 minutes for 1-month periods
  - May not find optimal global solution (processes in batches)
  - `delta_amount` too small finds no matches; too large creates poor matches

---

## 2) Configuration Parameters

### Simple Matching Config (Dashboard Form)

- **Delta Amount Rate** (default: 1.0)
  - Percentage tolerance for amount differences between subtxs
  - Example: `1.0` allows ±1% difference ($100 can match $99-$101)
  - Increase for crypto with high fees/spreads; decrease for stablecoins

- **Before Range Hours** (default: 24)
  - How many hours BEFORE a subtx timestamp to search for matches
  - Example: `24` searches 1 day before; `48` searches 2 days before
  - Increase if orgs have timezone differences or delayed reporting

- **After Range Hours** (default: 24)
  - How many hours AFTER a subtx timestamp to search for matches
  - Example: `24` searches 1 day after; `0` only searches past
  - Increase for settlement delays

- **Use Same Identifier** (default: True)
  - Require matching on transaction hash/identifier
  - `True`: Only matches subtxs with same `tx.identifier` (very strict, high confidence)
  - `False`: Matches on amount/time only (more flexible, lower confidence)
  - Use `True` for on-chain transactions with shared tx hashes

### Complex Matching Config (Dashboard Form)

- **Delta Time Days** (default: 2)
  - Maximum time difference in days between matched subtxs
  - Creates temporal groups for constraint solver
  - Increase for settlement delays; decrease for real-time systems

- **Delta Amount** (default: 0.5)
  - Absolute amount tolerance for matching groups (in token units)
  - Example: `0.5` allows group A sum and group B sum to differ by 0.5 tokens
  - Override with `delta_amount_in_usd` for dynamic calculation

- **Delta Amount in USD** (default: 5.0)
  - Overrides `delta_amount` by converting USD tolerance to token amount
  - Example: `5.0` means groups can differ by $5 worth of tokens
  - System calculates average token price from subtx `fiat_context`
  - Use this for consistent tolerance across different token prices

- **Subtx Min USD Amount** (optional, default: None)
  - Filters out subtxs below this USD value before matching
  - Example: `100` ignores all subtxs worth less than $100
  - Use to focus on material transactions and improve performance

- **Org A Batch Size** (default: 100)
  - Number of org A subtxs processed per batch
  - Smaller batches = faster feedback but more DB queries
  - Larger batches = better matches but slower, more memory

- **Org B Sub-Batch Size** (default: 100)
  - Number of org B candidates processed per constraint solver run
  - Reduce if hitting memory limits or solver timeouts
  - Increase for better match quality (more candidates considered together)

### SIMPLE_STRATEGY (Predefined)

Located in `matching/strategies.py`, this list defines 7 progressively looser strategies:

1. **Strategy 1:** `delta_amount_rate=2.0`, `±2 days`, `use_same_identifier=True`
2. **Strategy 2:** `delta_amount_rate=2.0`, `±10 days`, `use_same_identifier=True`
3. **Strategy 3:** `delta_amount_rate=1.0`, `±1 day`, `use_same_identifier=False`
4. **Strategy 4:** `delta_amount_rate=2.0`, `±1 day`, `use_same_identifier=False`
5. **Strategy 5:** `delta_amount_rate=3.0`, `±1 day`, `use_same_identifier=False`
6. **Strategy 6:** `delta_amount_rate=4.0`, `±1 day`, `use_same_identifier=False`
7. **Strategy 7:** `delta_amount_rate=2.0`, `±2 days`, `use_same_identifier=False`

**Usage:** Triggered via "Run Simple Strategy" button in dashboard. Runs all 7 strategies sequentially on unmatched subtxs.

---

## 3) Q&A (Short & Direct)

- **Q:** What is `SIMPLE_STRATEGY` and when should I use it?
  **A:** A predefined list of 7 matching configurations that tries strict rules first (same identifier, tight time windows), then progressively loosens constraints. Use "Run Simple Strategy" button in dashboard for comprehensive matching—this is the recommended starting point.

- **Q:** How do I run a full reconciliation between two organizations?
  **A:** In Django admin, go to Organizations page, select orgs, click "Trigger matching workflow". First click "Run Simple Strategy" and wait for completion. Then click "Run Complex Matching" for remaining unmatched transactions.

- **Q:** What's the difference between simple and complex matching?
  **A:** Simple matching finds 1-to-1 or sibling-group matches using database queries with time/amount filters. Complex matching uses constraint programming to find M-to-N matches where transactions split or combine between organizations.

- **Q:** Why do some matches fail validation?
  **A:** Sibling subtxs (from the same parent transaction) must match together. If org A has 2 subtxs totaling $150 but org B has 2 subtxs totaling $100, the match is rejected even if individual subtxs are within tolerance.

- **Q:** Can I re-match transactions that are already matched?
  **A:** No. Matched transactions (those with `match_group` set) are excluded from all matching queries. Delete the `SubTransactionMatchGroup` record to unmatch and retry.

- **Q:** Should I use "Run Combined" button or run simple/complex separately?
  **A:** Run separately. Click "Run Simple Strategy" first to get comprehensive coverage with the 7 predefined strategies, then "Run Complex Matching" for remaining transactions. The "Run Combined" button uses single custom configs and is less effective.

- **Q:** How long does matching take?
  **A:** Simple strategy: 5-15 minutes for 1-month period. Complex matching: 10-45 minutes depending on unmatched transaction count. Check Temporal UI for progress.

- **Q:** What's delta_amount vs delta_amount_in_usd?
  **A:** `delta_amount` is absolute token tolerance (e.g., 0.5 BTC). `delta_amount_in_usd` dynamically converts USD to tokens (e.g., $5 = 0.00008 BTC if BTC=$60k). Use USD for consistent tolerance across different token prices.

---

## 4) Detailed Explanation

### Concepts

- **SubTransaction (subtx):** A component of a transaction representing a single asset movement. A transaction may have multiple subtxs for different assets.
- **Match Group:** A `SubTransactionMatchGroup` record linking related subtxs from org A and org B, with metadata on match quality (sums, diffs, time delta).
- **Sibling Subtxs:** Subtxs sharing the same parent transaction.
- **Balance Factor:** Direction indicator (1 = inflow, -1 = outflow). Matching requires same balance factor.
- **Temporal Matching:** Finding subtxs within a time window (e.g., ±2 days) to reduce search space.
- **Delta Amount Rate:** Percentage tolerance for amount differences. `2.0` means amounts can differ by ±2%.
- **Asset Class:** Cryptocurrency or token type (BTC, ETH, etc.). Matching occurs per asset class.


### How it Works (High-Level)

**Dashboard Entry Points:**
- Users trigger workflows from Django admin Organization page via `organization_page.py`
- **"Run Simple Strategy"** → calls `trigger_simple_strategy_workflow()` → executes `SequentialSimpleMatchingWorkflow` with `SIMPLE_STRATEGY` configs
- **"Run Complex Matching"** → calls `trigger_complex_matching_workflow()` → executes `ComplexMatchingWorkflow`
- Both workflows are triggered separately and run independently (not as parent/child)

**Workflow Orchestration:**
- Both workflows generate `AssetMatchingRequest` objects per asset class using `MatchingActivities.generate_asset_requests`
- Simple matching spawns parallel child workflows per asset class (`SimpleMatchingAssetWorkflow`)
- Complex matching processes asset classes sequentially with internal batching
- All workflows are Temporal workflows with automatic retries and progress tracking

**Simple Strategy Flow (SIMPLE_STRATEGY):**
1. `SequentialSimpleMatchingWorkflow` receives 7 strategies from `SIMPLE_STRATEGY` list
2. For each strategy (executed sequentially):
   - Spawns `SimpleMatchingWorkflow` with that strategy's config
   - Runs on all unmatched subtxs (previous strategies' matches excluded)
   - Proceeds to next strategy only after current one completes
3. Each `SimpleMatchingWorkflow`:
   - Generates `AssetMatchingRequest` per asset class
   - Spawns parallel `SimpleMatchingAssetWorkflow` child workflows
   - Waits for all asset classes to complete

**Simple Matching Flow (per Asset):**
1. `SimpleMatchingAssetWorkflow` gets unmatched subtxs from org A in batches of 1000 (cursor-based pagination)
2. For each batch, calls `MatchingActivities.get_similar_subtx_ids` to find org B candidates using `SimilarBatchQueryBuilder`
3. For each subtx in batch, calls `MatchingService.match_simple` which:
   - Queries candidates filtered by timestamp range, amount range, balance factor, asset class, identifier (if enabled)
   - Selects best match (closest amount)
   - Collects sibling subtxs from both sides using BFS traversal
   - Validates sibling amounts within tolerance
   - Returns `Match` object if valid
4. Saves matches to database via `MatchingSimple.save_match_results`
5. Uses Temporal `continue_as_new` every 10 iterations to prevent history bloat

**Complex Matching Flow:**
1. `ComplexMatchingAssetWorkflow` gets all unmatched org A subtxs for the asset class
2. Processes in batches (default 100) via `MatchingActivitiesComplex.match_complex`
3. For each batch:
   - Gets temporal candidates from org B (within `delta_time` of batch min/max timestamps)
   - Sub-batches org B candidates (default 100) to prevent memory issues
   - For each sub-batch, calls `MatchingComplex.match`:
4. Returns all matches found across batches



**Limits:**
- Simple matching batch size: 1000 subtxs
- Complex matching org A batch: 100 subtxs (configurable via `org_a_batch_size`)
- Complex matching org B sub-batch: 100 subtxs (configurable via `org_b_sub_batch_size`)
- Temporal group size in complex matching: 30 closest subtxs
- Simple matching `continue_as_new` frequency: every 10 iterations
- Complex matching solver timeout: 500 seconds per batch
- Activity timeouts: 5 minutes (simple), 30 minutes (complex)

### Errors & Troubleshooting

| Exact Message | Likely Cause | Fix |
|---|---|---|
| Workflow timed out after 40 seconds | Too many subtxs to process in time | Reduce date range or increase batch sizes |
| No solution found | Complex matching constraints too strict | Increase `delta_amount` or `delta_time` in config |
| Invalid cursor progression | Pagination cursor not advancing | Check for duplicate IDs or database issues |
| Reached maximum iterations limit | More than 1000 batches to process | Split date range into smaller periods |
| No org A subtxs found for asset class | All subtxs already matched or outside date range | Check `match_group__isnull` filter or expand dates |
| Siblings validation failed | Sibling subtxs amounts don't match within tolerance | Increase `delta_amount_rate` or check data quality |

**Common Issues:**
- **No matches found:** Check that both orgs have subtxs for same asset class, timestamps overlap within delta_time, and balance_factor matches.
- **Partial matches only:** Complex matching processes in batches; optimal global solution not guaranteed. Try smaller batches or adjust `delta_amount`.
- **Memory errors:** Reduce `org_b_sub_batch_size` in complex matching config.
- **Duplicate matches:** Race condition in parallel simple matching is handled; later match overwrites with identical result.
- **Match groups merge:** If subtxs from different match groups are matched together, groups are automatically merged with combined metadata.
- **Simple strategy completed but few matches:** Normal—later strategies in SIMPLE_STRATEGY are progressively looser. Check logs to see which strategies found matches.
- **Complex matching takes very long:** Reduce date range to 1-2 weeks, or increase `subtx_min_usd_amount` to filter small transactions.

---

## 5) Quick Reference

### Typical Workflow Sequence

1. **Navigate to Django Admin**
   - Go to Organizations page
   - Select any organization(s) (selection doesn't matter for matching)
   - Click Actions → "Trigger matching workflow"

2. **Configure Form**
   - **Organization 1:** Select first org (e.g., Coinbase)
   - **Organization 2:** Select second org (e.g., Internal Custodian)
   - **Start Date:** Beginning of reconciliation period
   - **End Date:** End of reconciliation period (recommend 1-3 months max)
   - Leave simple/complex configs at defaults for first run

3. **Run Simple Strategy (REQUIRED FIRST)**
   - Click **"Run Simple Strategy"** button
   - This executes all 7 `SIMPLE_STRATEGY` configs sequentially
   - Wait 5-15 minutes (check Temporal UI: `http://temporal-ui/namespaces/default/workflows`)
   - Look for workflow ID starting with your request UUID

4. **Check Results**
   - Query database: `SubTransaction.objects.filter(match_group__isnull=False).count()`
   - Or check logs for "Completed simple matching strategy" messages
   - Note how many subtxs remain unmatched

5. **Run Complex Matching (OPTIONAL)**
   - Return to same form with same org pair and dates
   - Adjust complex config if needed:
     - **Delta Time Days:** 2-7 for most cases
     - **Delta Amount in USD:** 5-20 depending on transaction sizes
     - **Subtx Min USD Amount:** Set to 100+ to skip small amounts
   - Click **"Run Complex Matching"** button
   - Wait 10-45 minutes depending on unmatched count

6. **Verify Matches**
   - Check `SubTransactionMatchGroup` records
   - Review `metadata` JSON for match quality (A_sum, B_sum, diff)
   - Query unmatched subtxs: `SubTransaction.objects.filter(match_group__isnull=True, organization_id__in=[org1_id, org2_id])`

### Dashboard Buttons Explained

- **"Run Combined":** Runs simple (single config) + complex sequentially. NOT RECOMMENDED—use separate buttons instead.
- **"Run Simple Matching":** Runs simple matching with YOUR CUSTOM config (single strategy). Use if you know exact tolerance needed.
- **"Run Simple Strategy":** Runs all 7 `SIMPLE_STRATEGY` configs. RECOMMENDED for comprehensive matching.
- **"Run Complex Matching":** Runs complex constraint programming on unmatched subtxs. Run AFTER simple strategy.


