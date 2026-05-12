# Installation

Install the Canonic skill to enable human-led design workflows with your AI agent.

## Prerequisites

1.  **Canonic Desktop App**: Install on your machine.
    *   **macOS**: Download from [GitHub Releases](https://github.com/Canonical-AI/canonic/releases).
    *   **Windows/Linux**: Follow the [Canonic setup guide](https://github.com/Canonical-AI/canonic).
2.  **Local Agent**: An AI agent with shell and HTTP capabilities (Claude Code, Gemini CLI, etc.).

---

## 1. Quick Install (Claude Code)

If you use Claude Code, copy the skill to your project's local skills folder:

```bash
mkdir -p .claude/skills
curl -o .claude/skills/canonic.md https://raw.githubusercontent.com/Canonical-AI/canonic-skill/main/canonic.md
```

## 2. Quick Install (Gemini CLI)

Add the skill to your Gemini CLI environment:

```bash
# Option A: Local skill
cp canonic.md ./SKILL.md

# Option B: Global extension
# Follow gemini-cli documentation for adding custom skills to your extensions folder.
```

## 3. Manual Install (Other Agents)

For agents without a native skill system:

1.  Copy the content of `canonic.md`.
2.  Provide it to your agent as a **System Prompt** or **Instruction File**.
3.  The agent will now understand the `/canonic` command protocol.

---

## Verification

Once installed, verify the connection:

1.  Open Canonic.
2.  In your agent, run:
    ```bash
    /canonic init
    ```
3.  If the agent prompts you for a workspace path and opens Canonic, installation was successful.

## Troubleshooting

- **Lockfile Not Found**: Ensure Canonic is running. The skill looks for `~/.canonic/api.lock`.
- **Permission Denied**: Ensure your agent has permission to execute shell commands and make local network requests.
- **Path Issues**: On Windows, ensure the agent can resolve `%USERPROFILE%\.canonic\api.lock`.
