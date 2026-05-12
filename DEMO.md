# Canonic Skill Demo Script

This script demonstrates the full lifecycle: `init` -> `vision` -> `review` -> `handoff`.

## Preparation (Simulate Fresh State)

If you have Canonic installed but want to demo the "Not Installed" or "Not Running" flow:

1. **Simulate Not Running**: Close the Canonic app. Delete the lockfile:
   ```bash
   rm ~/.canonic/api.lock
   ```

2. **Simulate Not Installed**: 
   - Rename `/Applications/Canonic.app` to something else temporarily (macOS).
   - Or, simply mock it: Create a dummy skill file that skips the `ls /Applications` check to force the failure message.

3. **Scrub Previous Demos**:
   ```bash
   # Remove demo workspace
   rm -rf ~/Documents/CanonicWorkspaces/demo-project
   # Remove mock lockfile if used
   rm ~/.canonic/api.lock
   ```

---

## Phase 1: Initialization (`/canonic init`)

**Agent Prompt**: `"Run /canonic init for a new project called 'demo-project'. It's a task management CLI app for cavemen."`

**Expected Agent Behavior**:
1. Checks for Canonic.
2. Prompts for workspace path (choose `~/Documents/CanonicWorkspaces/demo-project`).
3. Synthesizes `vision.md` (e.g., "Unga Tasker: CLI for rocks and sticks").
4. Opens Canonic.

---

## Phase 2: Review & Gospel

**Action**: In Canonic, change a requirement. (e.g., "Tasks must be stored in a JSON file" -> "Tasks must be carved into a SQLite database"). Click **"Implement this"**.

**Agent Prompt**: (None, agent is waiting for callback).

**Expected Agent Behavior**:
1. Agent receives updated Markdown.
2. Agent acknowledges "SQLite" is now Gospel.
3. Agent proposes implementation plan based *only* on the new requirement.

---

## Phase 3: Anti-Pattern Check

**Agent Prompt**: `"Hey agent, can you update the vision.md to include a feature for syncing tasks to the cloud?"`

**Expected Agent Behavior**:
- Agent should warn: "Updating docs directly is an anti-pattern."
- Agent should suggest: "Please use `/canonic review vision.md` to make this change in Canonic so we maintain human-led design."

---

## Phase 4: Full Cleanup (The Scrub)

Run this to delete everything created during the demo:

```bash
# 1. Kill any stray mock servers
pkill -f mock_canonic.py

# 2. Delete the workspace and docs
rm -rf ~/Documents/CanonicWorkspaces/demo-project

# 3. Clear the Canonic lockfile (forces re-discovery next time)
rm ~/.canonic/api.lock

# 4. (Optional) Remove the skill from your agent
# rm .claude/skills/canonic.md
```

---

## Testing with Mock (No App Required)

1. Terminal A: `python3 mock_canonic.py`
2. Terminal B: Ask agent to run the commands.
3. Observe the mock terminal logs to see the API interaction.
