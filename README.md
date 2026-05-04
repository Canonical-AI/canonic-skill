# canonic-skill

A [Claude Code](https://claude.ai/code) skill that lets AI agents open documents in [Canonic](https://github.com/Canonical-AI/canonic) for human review, then continue with the edited content and a chosen next step.

## What it does

```
Agent writes a spec → opens it in Canonic → you edit and annotate → 
click "Implement this" → agent picks up with your reviewed version
```

The agent:
- Auto-launches Canonic if it's not running
- Opens your workspace and the file
- Optionally leaves inline comments while you read
- Waits for you to choose a next action ("Implement this", "Research this", etc.)
- Resumes with the full edited content

## Install

Copy `canonic.md` into your project's `.claude/skills/` directory:

```bash
mkdir -p .claude/skills
curl -o .claude/skills/canonic.md \
  https://raw.githubusercontent.com/Canonical-AI/canonic-skill/main/canonic.md
```

Then use it in Claude Code:

```
/canonic path/to/your-doc.md
```

## Requirements

- [Canonic](https://github.com/Canonical-AI/canonic) installed at `/Applications/Canonic.app` (macOS)
- Claude Code

## How it works

Canonic runs a local HTTP server and writes a discovery lockfile at `~/.canonic/api.lock`. The skill reads the lockfile, connects to the server, opens your file for review, and waits for you to send it back via the action picker in the app.

See [the Canonic agent API docs](https://github.com/Canonical-AI/canonic/blob/main/docs/superpowers/specs/2026-05-03-agent-integration-design.md) for the full protocol.
