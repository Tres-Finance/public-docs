# How to Set Up TRES AI Connect with Your AI Tools | Crypto Accounting and Web3 Treasury | TRES Finance

Source: https://tres.finance/how-to-set-up-tres-ai-connect-with-your-ai/

How to Set Up TRES AI Connect with Your AI Tools

# How to Set Up TRES AI Connect with Your AI Tools

This guide covers how to set up TRES AI Connect with your preferred AI tool. Whether your team works in chat (Claude, ChatGPT) or in the terminal and IDE (Claude Code, Codex, Gemini CLI), the setup takes under five minutes per tool.

Below is a step-by-step guide for each of the five supported tools. Pick the one your team uses, follow the steps, and you’ll be talking to your TRES account in plain English. Each tool has its own short walkthrough video, configuration block, and a sample prompt to test once you’re connected.

AI Chats

- Claude (recommended)

- ChatGPT

Code Assistants

- Claude Code

- Gemini CLI

### AI Chats

These are the tools your finance team will use most often: conversational AI assistants where you ask questions, run skills, and review output in a chat interface.

#### Claude

Claude is Anthropic’s flagship AI assistant. Recommended for the best experience with TRES AI Connect.

The setup is the same for Claude on the web and Claude Desktop.

- Click on your profile and open Settings.

- Go to Connectors.

- Click Add custom connector.

- Name the connector tres-finance and paste this URL: https://ai.tres.finance/mcp

- Click Add.

- Connect to your TRES account: enter your organization name, then sign in.

Test it:

“Bring me the five latest transactions in my account.”

If Claude returns your five most recent transactions, you’re set up correctly.

#### ChatGPT

ChatGPT is OpenAI’s AI assistant. ChatGPT requires Developer Mode before you can add a custom MCP connector.

- Go to Apps.

- Enable Developer Mode.

- Create a new App.

- Name it tres-finance and paste this URL: https://ai.tres.finance/mcp

- Leave the authentication setting as default (OAuth).

- Toggle the Approval switch on.

- Click Create and complete the authorization in the popup.

Once authorized, you’ll see tres-finance listed as a connected app.

If ChatGPT returns your five most recent transactions, you’re set up correctly.

### Code Assistants

These tools live in your terminal or IDE. They’re useful for engineers, technical finance team members, or anyone who prefers a command-line workflow.

#### Claude Code

Claude Code is Anthropic’s command-line and IDE coding tool. Useful for technical finance team members who want to integrate TRES queries into their development workflow.

- Open your terminal.

- Run this command: claude mcp add tres-finance https://ai.tres.finance/mcp

- Verify the MCP has been installed: run claude mcp list and check that tres-finance appears in the output.

- Run claude to start Claude Code.

- When prompted, allow access to the terminal.

- Ask Claude Code to open your TRES account: “Please open my TRES Finance account.”

- Claude Code will prompt you to authorize. Open the URL it provides in your browser and sign in.

- Once you see “Authentication successful,” return to the terminal.

If Claude Code returns your five most recent transactions, you’re set up correctly. You’re now ready to use the full power of Claude Code: create agents, build skills, and automate your digital asset finance workflows.

#### Codex

Codex is OpenAI’s coding assistant for the terminal and IDE. Codex installs and authenticates in one step.

- Run this command: codex mcp add tres-finance https://ai.tres.finance/mcp. This will install the MCP and prompt you to sign in to your TRES organization.

- Select your organization name and sign in.

- You’ll see confirmation that authentication was successful.

- Return to the terminal and start Codex.

If Codex returns your five most recent transactions, you’re set up correctly.

#### Gemini CLI

Gemini CLI is Google’s command-line AI tool. It requires Gemini and Node.js installed on your machine first.

- Make sure Gemini and Node.js are installed (prerequisite setup guide).

- Open your terminal and navigate to the Gemini configuration folder: cd ~/.gemini

- Open settings.json in the nano editor: nano settings.json

- Press Ctrl+O to enter edit mode.

- Paste the following block, then press Ctrl+X to save and exit:

- Start Gemini.

- When prompted, sign in to your TRES account.

- Return to the terminal once authenticated.

If Gemini CLI returns your five most recent transactions, you’re set up correctly.

### Need help?

If something doesn’t work, the most common issues are: outdated client version, missing TRES credentials, or a typo in the configuration.

For technical questions, our support team is reachable at support@tres.finance.

### What’s next

Now that you’re connected, here’s where to go next:

Start trying it. Ask anything about your TRES account in plain English. Run a multi-step audit. Test a complex workflow. The best way to learn what AI Connect can do is to try it on real questions your team is asking today.

Read the announcement. Want to understand what AI Connect is doing under the hood? Read the launch post →

Learn about MCP. Plain-English explainer of the protocol that makes AI Connect possible. What’s an MCP? →

## Interested in TRES?

Don't Miss Our News
