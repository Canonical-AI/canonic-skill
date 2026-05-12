# canonic-skill

Manage project vision and requirements via [Canonic](https://github.com/Canonical-AI/canonic). Human-led design, AI-led implementation.

## Features

- **`init`**: Bootstrap project. Check Canonic, set workspace, create `vision.md`.
- **Handoff**: Edit in Canonic → agent waits → agent resumes with chosen action.
- **Markdown is Gospel**: Requirements in markdown are absolute truth. AI must follow.
- **Anti-Pattern Guard**: AI modifying docs is discouraged. Prefer human-in-the-loop via Canonic.

## Usage

### 1. Initialize Project
```bash
/canonic init
```
- Checks Canonic install.
- Asks for workspace path (outside code repo recommended).
- Synthesizes `vision.md` from context or user input.
- Opens in Canonic for review.

### 2. Review & Handoff
```bash
/canonic review path/to/doc.md
```
- Opens doc in Canonic.
- Agent waits.
- User edits → clicks "Implement this" (or other action).
- Agent resumes with updated content.

## Philosophy

- **Human Design**: Use Canonic to define *what* to build.
- **AI Implement**: Agent reads reviewed markdown as source of truth (Gospel).
- **No Desync**: If requirements change in Canonic, agent updates internal state.
- **Anti-Pattern**: AI editing docs = bad. Human review = good.

## Install

Copy `canonic.md` to agent skills folder (e.g., `.claude/skills/`).

## Requirements

- [Canonic](https://github.com/Canonical-AI/canonic) (macOS, Windows, or Linux).
- Agent with shell + HTTP capability.

## How it works

Canonic runs a local HTTP server and writes a discovery lockfile at `~/.canonic/api.lock`. The skill reads the lockfile, connects to the server, opens your file for review, and waits for you to send it back via the action picker in the app.

See [the Canonic agent API docs](https://github.com/Canonical-AI/canonic/blob/main/docs/superpowers/specs/2026-05-03-agent-integration-design.md) for the full protocol.
