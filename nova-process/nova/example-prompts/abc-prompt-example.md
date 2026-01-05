# === PROJECT PHASE <X> — CHECKPOINT <Y> ===
# === UNIFIED A/B/C AGENT INSTRUCTION ===

You are the Agent assigned to complete this checkpoint.

This entire prompt describes ONE atomic task. You MUST complete all three blocks (A → B → C) in one uninterrupted execution.

Do NOT ask for confirmation.
Do NOT pause.
Do NOT wait.

Perform Block A, then immediately Block B, then immediately Block C.

If any part of Block A or Block B reveals conditions that make continuation impossible, you MUST fail the run with a clear error message describing:
- what you found
- why it blocks the checkpoint
- exactly what input or repo state is missing

Otherwise: you MUST proceed automatically from A to B to C.

---

## BLOCK A — ANALYSIS (No code edits)

1. Deep-scan the repository (prefer full scan; if you cannot, explicitly say it was a quick scan).
2. Validate assumptions described in the human brief against actual repo state.
3. Identify all files requiring creation, modification, or deletion.
4. Plan the implementation precisely (include exact filenames, operations, and acceptance criteria).
5. Write your analysis to:
   `docs/analysis/<phase>-<checkpoint>-analysis.md`
6. DO NOT stop after writing this file. Continue to Block B automatically.

Constraints:
- NO code edits in Block A.
- NO partial implementation.
- NO “nice to have” extras.

---

## BLOCK B — IMPLEMENTATION (Apply changes)

1. Apply changes exactly as described in Block A.
2. Use full-file replacements for modified files unless the brief explicitly requests diffs.
3. Maintain formatting and lint standards (Ruff + Black or repo-equivalent tooling).
4. Update documentation required by the checkpoint (only what Block A scoped).
5. Produce a complete diff suitable for PR submission.
6. DO NOT stop after implementation. Continue to Block C automatically.

Guardrails:
- No feature bleed beyond the checkpoint scope.
- No refactors “while you’re in there” unless explicitly required.
- If new files are added, ensure they are referenced (imports/docs/tests) or explain why they are intentionally standalone.

---

## BLOCK C — VERIFICATION / TESTING

1. Run the repo test suite and linters (use the repo’s standard commands; default to:
   - `pytest -q`
   - `ruff check .`
   - `black --check .`
   if tooling exists).
2. If failures occur, fix them automatically and re-run until green.
3. Confirm formatting compliance and that the working tree is clean aside from intended changes.
4. Update checkpoint-tracking docs if required by the checkpoint.

Documentation rules:
- If updating a “Bible” / historical log file, you MUST APPEND ONLY. Do NOT overwrite.
- If updating a “Snapshot” / state file, you may overwrite it fully.
- If updating a “Checklist” file, mark the checkpoint complete and add a one-line summary.

5. Produce a final PR-ready summary including:
   - What changed (bullet list)
   - Files touched
   - Tests run + results
   - Any known limitations or follow-ups explicitly out of scope

# END OF INSTRUCTIONS
Proceed with Block A now and DO NOT pause at the end of Block A or Block B.
