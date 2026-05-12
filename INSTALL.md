# Installation

Install the Canonic skill to enable human-led design workflows with your AI agent.

## Prerequisites

1.  **Canonic Desktop App**: Install on your machine.
    *   **macOS**: Download from [GitHub Releases](https://github.com/Canonical-AI/canonic/releases).
    *   **Windows/Linux**: Follow the [Canonic setup guide](https://github.com/Canonical-AI/canonic).
2.  **Local Agent**: An AI agent with shell and HTTP capabilities (Claude Code, Gemini CLI, etc.).

---

## 1. Quick Install (Gemini CLI)

The easiest way to install for Gemini CLI is via the extension command:

```bash
gemini extensions install Canonical-AI/canonic-skill
```

Or, to add it as a standalone skill:

```bash
npx skills add Canonical-AI/canonic-skill
```

## 2. Quick Install (Claude Code)

Install as a project-local skill:

```bash
npx skills add Canonical-AI/canonic-skill --local
```

*(This automatically creates `.claude/skills/canonic.md` for you)*

---

## 3. Manual Install

If you prefer manual setup:

```bash
mkdir -p .claude/skills
curl -o .claude/skills/canonic.md https://raw.githubusercontent.com/Canonical-AI/canonic-skill/main/canonic.md
```

---

## Verification

Once installed, verify the connection:

1.  Open Canonic.
2.  In your agent, run:
    ```bash
    /canonic init
    ```
3.  If the agent prompts you for a workspace path and opens Canonic, installation was successful.

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
