### Transaction Classification: What it is and why it helps
The Classification feature automatically organizes your ledger transactions into clear categories (classifications). Once categorized, you can quickly filter, search, and report on your activity in the UI without manual tagging.

In short: it keeps your ledger tidy and consistent so you can find what you need faster and trust your reports.


### What it does
- Assigns a best-fit classification to each transaction based on your organization’s rules and sensible defaults.
- Can focus on all transactions or just a subset you care about (see “Target just what you need” below).
- Keeps your saved ledger views consistent by applying your preferred view rules at the end.


### Why it matters
- Faster analysis: Filter by classification to answer questions in seconds.
- Cleaner reporting: Consistent categories reduce reconciliation time and confusion.
- Less manual work: Let the system apply your rules instead of hand-editing transactions.


### Typical ways you’ll use it
- After importing or syncing new data so recent transactions are immediately filterable.
- When you add or change classification rules and want your ledger to reflect them.


### What you’ll see in the UI afterwards
- Clear categories on each transaction (for example, Income, Transfer, Fees, etc.).
- Easy filtering by classification in your ledger and reports.
- Consistent results in your saved (favorite) ledger views once the run completes.


### Safety and performance
- Non-disruptive: No changes unless a better classification is found.
- Scales automatically: Processes in small chunks to avoid slowing down your workspace.
- Respects locked periods: Transactions in locked periods won’t be changed.


### Examples
- A transaction can have a classification such as "Income: Staking Rewards" or "Expense: Trading Fees"


### What kinds of classification rules you can create
You can create rules that automatically assign a category (classification) to matching transactions. A rule is made of one or more conditions plus the target “Activity” (the category you want applied). Below are the building blocks you can use when creating a rule:

- Activity (required)
  - What the transaction should be classified as (for example, Income, Fee, Transfer, etc.). Provided as `activity`.

- Platform (optional)
  - Limit the rule to a specific platform (chain or parent platform). Provided as `parent_platform`.

- Method (optional)
  - Limit the rule to a specific method such as “swap”, “deposit”, etc. Provided as `method_id`.

- Parties (optional)
  - By address/identifier:
    - `sender_identifier`
    - `recipient_identifier`
    - Tip: If you use both sender and recipient identifiers together, at least one of them must belong to your own internal accounts.
  - By internal account tag:
    - `sender_internal_account_tag`
    - `recipient_internal_account_tag`
  - By contact tag:
    - `sender_contact_tag`
    - `recipient_contact_tag`

- Asset and direction (optional)
  - Match when a specific asset is sent or received:
    - `sent_asset_identifier` → applies to outflows
    - `received_asset_identifier` → applies to inflows
  - You need to set at least one of these if you want the rule to consider direction.

- Priority (optional)
  - If more than one rule could match, `priority` lets you control which rule wins. Higher-priority rules are evaluated first.

- Favorite Ledger View (optional)
  - Link a rule to a saved view by `favorite_ledger_view_id`. This helps keep your favorite views consistent with the categories you expect.

- Minimum needed to save a rule
  - You must provide at least one condition (platform, method, party, asset) or a favorite ledger view. Otherwise, the system will ask you to add more details.

What happens to the rule after saving:
- New or updated rules are created with a status equivalent to “pending/created”. The system will automatically activate them before the next classification run and clean up rules you’ve requested to delete.


### When classification runs
Classification can run automatically or on demand. Here are the ways it starts:

- Automatic after a rule change
  - Whenever you add or edit a classification rule, the system schedules a classification run for your organization. There’s a short delay (about 10 minutes) to combine multiple quick edits into one efficient run. If you keep editing rules within that window, they’ll be batched together.

- Automatic after data is imported/committed
  - After a data sync or import finishes, the system can automatically classify new or updated transactions for that organization. This ensures fresh data becomes filterable with minimal delay.

- Manual, whenever you need it
  - You can start a classification run yourself from the product. This is useful after significant rule changes, or when you want to focus on a specific slice (for example, a method, a platform, or selected transactions).

What you’ll see during/after runs:
- Safe updates only: Transactions are updated only when a better category is found.
- Respect for locked periods: Transactions in locked periods are not changed.
- Favorite views alignment: After the main pass, your favorite ledger view rules can apply a final polish to keep views consistent (built-in categories like operations, internal transfers, and spam are not overridden).


### Practical tips
- Start specific, then broaden: Try a focused rule (method, platform, or a known address) to validate outcomes before expanding.
- Use priority to resolve overlaps: If two rules might match the same transactions, set a higher priority on the one that should win.
- Keep addresses lowercase when entering them: The system treats identifiers in lowercase, so entering them that way avoids mismatches.


### Examples of rules you might create
- Classify all “deposit” method transactions on Ethereum as “Income”.
  - Set `parent_platform = ethereum`, `method_id = deposit`, `activity = INCOME`.

- Classify outflows of a specific token from your treasury account as “Fees”.
  - Set `sender_internal_account_tag = treasury`, `sent_asset_identifier = <token>`, `activity = FEES`.

- Classify inflows from a known counterparty address as “Revenue”.
  - Set `sender_identifier = <counterparty_wallet>`, `received_asset_identifier = <asset>`, `activity = REVENUE`.

- Align a saved view with a specific category.
  - Set `favorite_ledger_view_id = <view_id>`, `activity = <desired_category>`. The system will apply this after the main pass to transactions that match the saved view (excluding built-in categories like operations, internal transfers, and spam).


### FAQ
- Can I create a rule with no conditions?
  - No. Add at least one condition (platform, method, party, or asset) or link to a favorite ledger view.

- What if multiple rules match?
  - The system uses priorities and sensible ordering to decide which rule applies. Use `priority` to control the winner when needed.

- Can I run classification again?
  - Yes. It’s safe to re-run anytime—only transactions that need a better classification are updated.

- How soon after saving a rule will I see changes?
  - The system schedules a run shortly after you save (about 10 minutes, to batch changes). You can always start a run manually if you need immediate results.


### Summary
Use Classification to automatically organize your ledger so you can filter, search, and report with confidence. It’s safe to run, can be as broad or as targeted as you need, and it respects your preferred ledger views for a consistent, business-friendly end result.