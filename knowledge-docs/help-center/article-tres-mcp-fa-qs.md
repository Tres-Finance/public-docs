# TRES MCP - FAQs | TRES Finance Help Center

Source: https://help.tres.finance/article/tres-mcp-fa-qs

# TRES MCP - FAQs

### FAQs

Q: I can't find the custom connector option in Claude — where is it?

A: This is almost always a permissions issue, not a missing feature. Custom connectors are admin-controlled on Team and Enterprise plans, and individual users often don't see the option because their workspace admin hasn't enabled it. Two paths forward: ask your admin to add the TRES connector at the org level (which makes it available to everyone in one shot, with no per-user setup needed), or request admin access yourself if that fits your role. Org-level rollout is usually the cleanest option — one configuration, everyone benefits, and the admin retains control over who can use it.

Q: What does the memory tool do, and how is it different from Claude's regular memory?

A: TRES exposes a memory tool through the MCP that lets Claude keep durable notes scoped to your organization. Think of it as a shared scratchpad that survives between conversations — useful for things like "our treasury wallet is 0x...", "we close books on the 5th of the month", "always group these tokens together when reporting". It's separate from Claude's own chat memory: Claude's memory is per-user and lives in Claude; the TRES memory tool is per-organization and lives in TRES, so anyone in your org querying through the connector benefits from the same notes. Don't store secrets or credentials there — treat it like any other shared org document.

Q: Can I build my own custom workflows on top of the connector?

A: Yes — through skills. Skills are reusable playbooks that tell Claude how to handle a specific task: which tools to call, in what order, with what defaults. TRES ships several out of the box (transaction story visualization, reconciliation gap closing, ledger filtering), but you can create your own for workflows specific to your team — month-end close checklists, custom variance reports, a "morning briefing" that pulls yesterday's flows across your wallets, audit prep walkthroughs, and so on. A skill is essentially a markdown file describing the procedure plus optional helper scripts. The easiest way to build one is to describe a workflow you do regularly to Claude and ask it to draft a skill; there's also a built-in skill-creator that walks through the process. Once a skill exists, you trigger it just by describing what you want in natural language — Claude picks it up automatically based on the skill's description.

Q: How is my financial data protected when it flows through Claude?

A: Several layers stack here. Traffic between Claude and TRES is encrypted in transit, and authentication uses OAuth — Claude never sees or stores your TRES password. Claude inherits exactly your TRES access scope and nothing more; if you can't see a wallet in TRES, neither can Claude. Data passed through MCP connectors isn't used to train Anthropic's models. Each session is scoped to a single org, and switching orgs requires re-authentication. Finally, you can revoke the connector at any time from either side — Claude's connector settings or TRES's integrations panel.

Q: Who at Anthropic or TRES can see what I ask Claude?

A: Conversations with Claude are private to your account by default. Anthropic staff don't browse user conversations; access is limited to narrow cases like trust-and-safety review of flagged content. On the TRES side, your queries hit the API as authenticated calls under your user, so your TRES admins see the same audit trail they'd see for any API usage — they see which endpoints were called, not the chat text itself.

Q: What is the TRES MCP connector and what does it let Claude do?

A: It's a bridge between Claude and your TRES Finance workspace. Once connected, Claude can query your ledger, look up specific transaction hashes, analyze reconciliation gaps, fetch balances, and pull organization-level financial data — all using natural language instead of the TRES UI or raw GraphQL.

Q: What data does Claude get access to?

A: Anything your TRES user account can see: transactions, wallets, balances, reconciliation status, and historical ledger entries for your organization. Claude doesn't get broader access than you already have.

Q: Is it read-only or can Claude make changes?

A: Mostly read, but some write actions exist (for example, plugging reconciliation gaps). Write actions should always be confirmed explicitly before Claude executes them. If you want a strictly read-only experience, just tell Claude that at the start of a session.

Q: How does authentication work? Do I share my password?

A: No. Connection happens through TRES's standard auth flow — you log in directly to TRES, not through Claude. Claude never sees or stores your credentials. You can revoke access from your TRES account or from Claude's connector settings at any time.

Q: I have multiple TRES organizations. How does that work?

A: The connector includes a switch_organization flow. Claude can tell you which org you're currently viewing and trigger a re-authentication if you want to switch. Be explicit about which org you mean when you ask questions — Claude can't see all of them at once.

Q: Is my financial data being used to train Claude?

A: No. Data passed through MCP connectors in Claude's consumer products isn't used for training. It's processed to answer your question and that's it.

Q: What about audit trails — does TRES log Claude's actions?

A: Actions Claude takes appear in TRES under your user, since Claude is acting as you. If your org has compliance requirements, treat Claude's queries the same as your own.

Q: How current is the data Claude sees?

A: Live, in most cases — Claude queries TRES at the moment you ask. For reconciliation gaps specifically, the freshness depends on when your last data collect ran; Claude can trigger one if needed.

Q: What if Claude returns wrong numbers or hallucinates a balance?

A: Claude should be pulling numbers from the connector, not generating them. If something looks off, ask Claude to show you the underlying query or transaction IDs so you can verify in TRES directly. Don't treat Claude's output as a substitute for the source of truth.

Q: Does it cost extra?

A: The connector itself doesn't add Anthropic costs beyond your normal Claude usage. Whether it's included in your TRES plan is a question for TRES.

Q: How do I disconnect?

A: In Claude's settings under connectors, or by revoking the integration on the TRES side. Either works.
