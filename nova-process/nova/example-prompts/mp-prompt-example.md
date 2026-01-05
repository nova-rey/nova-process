# === PROJECT MINI-PUSH (MP) — <ID> ===
# === ATOMIC MP AGENT INSTRUCTION ===

You are the Agent assigned to complete this Mini-Push (MP).

This MP describes ONE small, low-risk change.
It MUST be completed in a single uninterrupted execution.

Do NOT ask for confirmation.
Do NOT expand scope.
Do NOT reinterpret intent.

If the requested change requires behavioral or semantic changes,
you MUST fail immediately with a clear explanation.

---

## MP BLOCK — SANITY CHECK + IMPLEMENTATION

1. Perform a quick repository scan sufficient to locate the affected files.
2. Confirm the requested change matches existing behavior and architecture.
3. Apply the change exactly as described.
4. Use full-file replacements where files are modified.
5. Maintain formatting and lint standards.

Constraints:
- NO new runtime behavior.
- NO refactors.
- NO “while I’m here” improvements.
- NO new dependencies.

---

## MP BLOCK — VERIFICATION

1. Run existing tests and linting.
2. Add tests ONLY if explicitly requested.
3. Confirm working tree cleanliness.
4. Update documentation ONLY if explicitly requested.

Documentation rules:
- Append-only for historical logs.
- Overwrite allowed for snapshots/state files.

---

## MP COMPLETION REPORT

Produce a short summary including:
- Files changed
- What was modified
- Tests run
- Confirmation of no behavior change

# END OF MP INSTRUCTIONS
Execute immediately.
