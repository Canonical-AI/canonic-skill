---
name: canonic
description: Manage project vision and requirements via Canonic. Use `init` to bootstrap or `review` to iterate.
---

## Commands

### `canonic init`
Bootstrap a new project vision or requirement doc.
1. Check Canonic installation (see Step 2).
2. Ask user for workspace location (default: `~/Documents/CanonicWorkspaces/<project-name>`).
3. If no existing context, ask "What are you trying to build?".
4. Create `vision.md` with a comprehensive project starter/vision based on context/input.
5. Open `vision.md` in Canonic for human review (Step 5).

### `canonic review <file-path>`
Open existing file for review and handoff.

## Implementation Details

### Step 1 — Check Installation & Launch
Check if Canonic is installed:

```bash
# macOS
[ -d /Applications/Canonic.app ] && echo "installed"

# Linux (assuming standard install path or binary in PATH)
command -v canonic >/dev/null 2>&1 && echo "installed"

# Windows (PowerShell)
if (Get-Command canonic -ErrorAction SilentlyContinue) { echo "installed" }
```

If not installed:
> "Canonic not installed. Download at https://github.com/Canonical-AI/canonic. Install, open, then retry."
Exit.

If installed but not running: launch and wait for `~/.canonic/api.lock` (or `%USERPROFILE%\.canonic\api.lock` on Windows).

**Launch Command:**
- macOS: `open -a Canonic`
- Linux: `canonic &`
- Windows: `start canonic`

### Step 2 — Workspace Setup (`init` only)
1. Prompt user for workspace path. **Warning:** Do not default to current working directory if it's a code repo; keep docs separate to avoid noise.
2. Create directory.
3. If context exists (READMEs, code, previous chat): synthesize `vision.md`.
4. If no context: ask user goal → synthesize `vision.md`.

### Step 3 — Callback & Handoff
(Follow original Steps 4-7 for HTTP listener and `/session/start`).

### Step 4 — Agent Instructions (The Gospel)
When using this skill, you MUST follow these rules:
1. **Markdown is Gospel:** The content returned from Canonic is the absolute source of truth. Do not deviate from the requirements defined in the doc.
2. **Requirement Updates:** If user changes requirements in the doc, discard old assumptions. Sync your internal state to the new version immediately.
3. **Anti-Pattern Warning:** While you *can* modify the docs, it is an **anti-pattern**. Prefer human-led requirement changes in Canonic. You implement; human designs. If you must propose a change, ask user to review it in Canonic first.

## API Protocol
(Keep Step 4-8 from previous version for lockfile, server check, callback listener, and POST calls).
