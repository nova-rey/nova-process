# Documentation Overview

This directory contains authoritative documentation for the project.

These documents are read and updated by both humans and agents.
Rules governing how each file may be modified are defined in `docs/AGENTS.md`.

---

## Document Types

### Historical Logs
Append-only records of decisions, changes, and rationale.
Examples:
- `*_BIBLE.md`
- changelogs
- narrative logs

### Snapshots / State
Overwrite-allowed representations of current truth.
Examples:
- `*_SNAPSHOT.yaml`
- manifests
- current configuration state

### Checklists
Progress tracking for phases and checkpoints.
Examples:
- `PHASE_CHECKLIST.md`

---

## Authority

- This directory is the **source of truth** for documentation.
- If documentation conflicts with code, the discrepancy must be resolved explicitly.
- If unsure which document to update, stop and ask.

---

End of file
