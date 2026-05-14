# GEMINI.md - Canonic Skill Project

## Project Overview
This project provides an **AI Agent skill** (compatible with Gemini, Claude Code, and others) named `canonic`. It enables an AI agent to open documents in the **Canonic** desktop application for human review and editing. Once the user finishes editing and selects a next step in Canonic, the agent receives the updated content and a prompt to continue the workflow.

### Architecture & Key Technologies
- **Universal Skill Definition:** Defined in `canonic.md`.
- **Canonic Integration:** Uses a local HTTP API (running at `127.0.0.1`) and a discovery lockfile (`~/.canonic/api.lock`).
- **Workflow:** 
    1. Agent reads lockfile for port/token.
    2. Agent launches Canonic if needed.
    3. Agent starts a local callback listener (Python/Node).
    4. Agent sends a POST request to Canonic to open a file.
    5. User edits file in Canonic.
    6. Canonic POSTs edited content and a "next step" prompt back to the agent's callback listener.
    7. Agent updates the local file and continues.

- **Universal Skill Definition:** Defined in `SKILL.md`.
- `SKILL.md`: The core skill definition. Contains the logic for lockfile discovery, Canonic launching, and API interaction. Uses generic placeholders for agent identification.
- `README.md`: General documentation on installation and usage across different agents.

## Development Conventions
- **Skill Format:** Adheres to a common Markdown-based skill specification (YAML frontmatter + step-by-step instructions).
- **Tooling:** Relies on common Unix tools (`curl`, `cat`, `open`) and a lightweight HTTP server (e.g., Python) for the callback.
- **Environment:** Cross-platform (macOS, Windows, Linux). Handles platform-specific launch commands and paths.

## Usage & Installation
To install the skill:
1. Copy `SKILL.md` to the appropriate skills directory for your agent (e.g., `.claude/skills/` for Claude, or a custom skill path for Gemini).

2. For agents without a native skill system, provide the file content as context.
3. Invoke via the agent's command interface: `/canonic <path-to-file>`.

### Testing
- Manual testing requires having [Canonic](https://github.com/Canonical-AI/canonic) installed.
- Verify `~/.canonic/api.lock` exists when Canonic is running.
- Verify `curl http://127.0.0.1:<port>/ping` returns success.
