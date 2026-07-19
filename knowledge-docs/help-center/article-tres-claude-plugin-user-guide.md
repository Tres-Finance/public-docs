# TRES Claude Plugin User Guide | TRES Finance Help Center

Source: https://help.tres.finance/article/tres-claude-plugin-user-guide

# TRES Claude Plugin User Guide

## 1. What Is the TRES Claude Plugin?

The TRES Finance Claude Plugin connects your TRES Finance environment directly to Claude, Anthropic’s AI assistant. Instead of switching between browser tabs, copying data into spreadsheets, or writing GraphQL queries by hand, you simply describe what you need in plain language and Claude takes care of the rest.

The plugin turns Claude into a fully operational crypto finance assistant that can read your data, take actions, analyze reports, and walk you through complex workflows, all through a natural conversation.

### Why Connect the Plugin?

Crypto finance operations span wallet management, reconciliation, cost basis, ERP syncing, and audit-ready reporting. Each workflow normally requires navigating multiple screens, exporting data, and stitching results together. The plugin removes that friction by giving Claude direct, real-time access to your TRES Finance environment, so you can handle it all through a single conversation.

Because Claude connects to TRES’s production data layer, it works with structured, validated, and enriched information rather than raw blockchain data. That means accurate results, consistent accounting logic, and a full audit trail. There is no need for custom scripts, and no risk of working with stale or incomplete data. Every action follows a preview-and-confirm pattern, so you stay in control at every step.

## 2. How to Connect the TRES Plugin

### Where does it run?

The same plugin works in two places:

What it is

Best for

Claude Cowork

Anthropic's web-based product that runs the same

plugins in a browser UI, no CLI required

Finance / ops users who prefer a graphical interface

Claude Code

Anthropic's coding assistant: terminal CLI, macOS/Windows desktop app, and VS Code / JetBrains extensions

Power users, anyone comfortable

with a CLI or IDE

If you're not sure which to use, Claude Cowork is the easier entry point.

### Prerequisites

Before you start, make sure you have:

A TRES Finance account with access to the org you want to connect. The first time the plugin runs, a TRES login page opens in your browser. Sign in with the same credentials you use for your TRES account. No manual API token needed.

A Claude account on any Claude.ai plan that includes Claude Code or Cowork (Pro, Max, Team, or Enterprise). Sign up at claude.ai if you don't have one.

### Installing TRES Claude Plugin - Claude Cowork

This section is for users on the Claude Cowork web/desktop app.

Get access to Cowork:

If you don't yet have Cowork access, sign in at claude.ai. Cowork is available on Pro, Max, Team, and Enterprise plans. Open the Cowork desktop or web app and sign in with the same account.

Install the TRES plugin:

In Cowork, click Customize (left sidebar or top-right, depending on your version).

Choose Add plugin (or Browse plugins).

Add the TRES marketplace by entering: tres-finance/tres-claude-plugin

Click Install on the TRES Finance plugin card.

Cowork's plugin UI is graphical. There are no slash commands to type. The exact button labels may differ slightly between versions, but the flow (Customize → Add plugin → Install) is consistent.

First-run setup (connect to TRES):

The first time you use a TRES skill in Cowork (or when you click Connect on the plugin):

A TRES sign-in page opens in your browser.

Sign in with your normal TRES credentials.

Approve the connection request.

The browser confirms success. Close the tab and return to Cowork.

There is no API token to copy or paste. The connection is saved automatically.

Verify it's working:

In a new Cowork chat, type: What TRES skills do I have available?

Claude should list the TRES skills. If you see them, you're done.

### Installing TRES Claude Plugin - Claud Code

#### 1. Method A: Marketplace Install (recommended)

Inside Claude Code (CLI or desktop), type the following two commands one at a time:

That’s it. You can also browse and install graphically by typing /plugin and using the Discover tab.

#### 2. Method B: Downloadable Zip (offline / restricted networks)

Use this method if your environment can’t reach GitHub directly, or if you prefer a fully offline install.

Download the latest plugin zip from the link on the TRES platform "Learn more" page.

Extract the zip to a permanent location (e.g. ~/tres-claude-plugin on macOS/Linux, or C:\Users\<you>\tres-claude-plugin on Windows).

In Claude Code, register the folder: /plugin marketplace add /absolute/path/to/tres-claude-plugin

Install the plugin: /plugin install tres-claude-plugin@tres-finance

Important: Don’t move or delete the extracted folder after installing. Claude Code reads the plugin from that location.

#### 3. First-Run Setup (connect to TRES)

The first time the plugin tries to talk to TRES (for example, when you trigger a TRES skill or click Connect on the plugin in the /plugin UI):

1. Your default browser opens automatically on a TRES sign-in page.

2. Sign in with your normal TRES credentials.

3. Approve the connection request.

4. The browser tab confirms success. You can close it and return to Claude Code.

The connection is saved automatically and you won't be asked to sign in again on this machine. There is no API token to copy or paste.

If the browser doesn't open automatically, Claude Code will print a URL. Copy it into your browser to complete the sign-in.

#### 4. Verify It’s Working

Type the following into Claude Code:

Claude should list skills starting with tres-... (e.g. tres-onboarding, tres-recon-gaps, tres-asset-balance-validation-v2). If you see them, you’re done.

## 3. Keeping the plugin up to date

We ship updates regularly: bug fixes, new skills, and improvements to existing ones.

### Claude Cowork

In Cowork, plugins update automatically in the background. To force a manual refresh, open Customize → Plugins, find TRES Finance, and click Check for updates (or simply re-install; your settings and connection are preserved).

### Claude Code

Claude Code can auto-update plugins per marketplace. To enable auto-update (recommended):

1. Type /plugin in Claude Code.

2. Open the Marketplaces tab.

3. Find tres-finance in the list.

4. Toggle Enable auto-update on.

To manually check: /plugin marketplace update tres-finance

### Local zip install (Method B)

If you installed via downloaded zip, updates are not automatic. Download the new zip from the TRES platform, replace the contents of your existing folder (keep the same path), and run /plugin marketplace update tres-finance in Claude Code.

## 4. Working with multiple TRES organizations

If your user has access to more than one TRES organization, the plugin connects to one org at a time, whichever org you signed into during the browser connect step.

There is currently no in-chat command to switch orgs. To work in a different org, disconnect the current session and reconnect, signing in with the account that has access to the target org.

### Cowork

1. Open Customize → Plugins (or Connectors) → find TRES Finance.

2. Click Disconnect.

3. Click Connect again. Your browser opens the TRES sign-in page.

4. Sign in with the credentials for the org you want to use, and approve.

1. Type /plugin and open the Installed (or Connectors) tab.

2. Find the tres-finance connector and click Disconnect (or Sign out).

3. Trigger any TRES skill, or click Connect on the connector, to start a new browser sign-in.

4. In the browser, sign in with the credentials for the org you want to use, and approve.

### Tips

• Confirm which org you're connected to at any time by asking Claude: "Which TRES organization am I currently connected to?"

• If your TRES account has multiple related organizations linked at the TRES platform level, signing in once may give you visibility into all of them via TRES's org switcher on app.tres.finance, but the plugin's active context is still set by the account session you authorized.

• A native "switch org" command inside the chat is on the roadmap. Until then, disconnect + reconnect is the supported flow.

## 5. Uninstalling or disabling

Open Customize → Plugins → find TRES Finance → click Disable or Uninstall.

Disable temporarily (keeps your config and connection): /plugin disable tres-claude-plugin@tres-finance

Re-enable with: /plugin enable tres-claude-plugin@tres-finance

Uninstall completely:

/plugin uninstall tres-claude-plugin@tres-finance

Then optionally remove the marketplace: /plugin marketplace remove tres-finance

## 6. Troubleshooting

What to try

/plugin marketplace add fails with a

network or auth error

Check that you're online and (if behind a firewall) that GitHub is reachable. As a fallback, use the zip install.

Skills don't appear after install

Restart Claude Code or reload the Cowork tab. Then re-run the verification prompt.

"Authorization failed" / "Not connected"

Your TRES session may have expired. Open the /plugin menu (or the Cowork plugin panel), click Connect, and sign in again.

Browser doesn't open automatically on first

Claude Code / Cowork will print a sign-in URL in the chat. Copy it into your browser manually.

Skill runs but returns no data

You may be connected to a different TRES org than expected. See section 4.

Wrong / outdated version after update

In Claude Code, run /plugin marketplace update tres-finance and confirm the latest version. In Cowork, click Check for updates.

## 7. Support & feedback

In-product feedback (fastest way): just type "I'd like to submit feedback about the TRES plugin" and Claude will run the built-in feedback skill.

Email: support@tres.finance

## 8. Privacy & security notes

Authentication uses a standard browser-based sign-in flow (OAuth) against TRES. The same login you use for app.tres.finance. You never paste a token into Claude.

The resulting session credential is stored in your OS keychain (Claude Code) or Cowork's secure credential store. It is never written to plain-text config files.

The plugin talks only to ai.tres.finance/mcp over HTTPS. No third-party services receive your TRES data.

All actions taken by the plugin are scoped to the TRES organization you signed into. The plugin cannot access data from other orgs.

You can disconnect at any time from the /plugin menu (Claude Code) or the plugin panel (Cowork). This revokes the local session immediately.

The plugin source code is open and available for review at github.com/tres-finance/tres-claude-plugin (MIT licensed).
