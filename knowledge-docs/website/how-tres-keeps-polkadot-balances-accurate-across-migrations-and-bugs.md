# How TRES Keeps Polkadot Balances Accurate- Across Migrations and Bugs | Crypto Accounting and Web3 Treasury | TRES Finance

Source: https://tres.finance/how-tres-keeps-polkadot-balances-accurate-across-migrations-and-bugs/

How TRES Keeps Polkadot Balances Accurate- Across Migrations and Bugs

# How TRES Keeps Polkadot Balances Accurate- Across Migrations and Bugs

For Polkadot validators and ecosystem operators, reporting accuracy is mission-critical. When networks evolve, broken history can mean failed audits, compliance gaps, and lost trust.

Polkadot currently operates with around 600 active validators, and TRES already monitors 57 of them.

That leaves more than 90 % of the validator set without automated protection, even though they face the same reporting challenges.

The past year highlighted how real those risks are.Polkadot encountered two very different network events that tested historical accuracy at scale:

- A planned but complex migration of accounts to the new Asset Hub chain

- An unexpected “Era 1870” rewards bug that sent staking rewards to the wrong destination

Both events demonstrated a single truth: major protocol changes can – and do – put institutional reporting at risk.TRES kept every balance accurate and verifiable.

### Challenge 1: Asset Hub Migration – Hidden Reporting Risk

As part of the move to Polkadot 3.0 and the JAM upgrade, balances and logic shifted from the Relay Chain to a dedicated Asset Hub.

Unlike a single-cutover upgrade, the migration happened in batches across multiple blocks, meaning:

- At any given block, some accounts still followed the old schema while others had already migrated.

- Historical snapshots and balance calculations depended on exactly when an account switched.

For large validators and treasury teams, this created a serious audit and reconciliation risk.

#### TRES Solution: Block-by-Block Historical Indexing

To guarantee audit-grade history, TRES built a migration index that records the precise block and timestamp when every account moved.

Our platform:

- Checks Spec Version at each block to detect migration status

- Scans extrinsics (block-level operations) to identify accounts migrated at that moment

- Dynamically applies the correct schema when calculating historical balances or reconciling transactional events

The result: reliable holdings and unbroken audit trails, even during phased network updates that typically break analytics tools.

### Challenge 2: The Era 1870 Rewards Bug – Unexpected Discrepancy

During Polkadot’s Era 1870, a protocol-level bug caused some staking rewards to be sent to liquid (transferable) balances instead of being restaked as intended.

The discrepancy was subtle and difficult to trace – leaving validators and nominators with unexplained balances and potential reporting errors.

#### TRES Solution: Advanced Balance-Diff Analysis

TRES’ automated balance-diff engine compared before-and-after snapshots of on-chain accounts to detect every mismatch.

Our process included:

- Automated balance change tracking for every reward era

- Destination mapping to flag unexpected reward destinations

- Timestamp and event correlation to isolate the exact cause and era of every incident

After confirming the root cause, we reported our findings directly to the Polkadot team, sharing the full dataset and on-chain references so the issue could be verified and addressed quickly.

“It’s great to have such sharp and alert people in the ecosystem.” – Juan Risonanti, Blockchain Architect at Polkadot.

### Why It Matters for Validators and the Polkadot Ecosystem

By sharing these findings and the tooling behind them, Polkadot can help its entire validator ecosystem harden reporting practices.

Discover why TRES Finance is the must-have platform for Polkadot validators.

## Interested in TRES?

Don't Miss Our News
