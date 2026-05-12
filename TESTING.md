# Testing the Canonic Skill

Test by mocking the Canonic API or using the real app.

## 1. Mock Testing (Recommended)

Verify agent logic without installing Canonic.

1. **Create dummy lockfile**:
   ```bash
   mkdir -p ~/.canonic
   echo '{"port": 8080, "token": "mock-token-123"}' > ~/.canonic/api.lock
   ```

2. **Run mock server**:
   ```bash
   python3 mock_canonic.py
   ```
   (In a separate terminal).

3. **Trigger agent**:
   Ask your agent: `"/canonic init"` or `"/canonic review README.md"`.

4. **Observe**:
   - Agent should read `~/.canonic/api.lock`.
   - Agent should send POST to `localhost:8080/session/start`.
   - Mock server will auto-respond with "Mock Edited Content".
   - Agent should update file and report success.

## 2. Manual Verification

Check if agent follows "Gospel" rules.

- **Requirements Change**: Edit `vision.md` in Canonic (or mock). Change a core requirement. Verify agent immediately acknowledges and adopts the change.
- **Anti-Pattern Check**: Ask agent to "Update the vision doc with X". Verify agent warns that this is an anti-pattern and suggests using Canonic instead.

## 3. Real App Testing

1. Install [Canonic](https://github.com/Canonical-AI/canonic).
2. Open Canonic.
3. Verify `~/.canonic/api.lock` (or Windows equivalent) exists.
4. Run `/canonic init` and follow prompts.
