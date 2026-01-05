# docs/AGENTS.md — Documentation Rules

## Append-only files
These files are APPEND-ONLY:
- `docs/*BIBLE*.md` (historical log)
- changelogs / narrative logs

Rules:
- Append new entries only.
- Do not reorder, rewrite, or “clean up” old entries.
- If a past entry is wrong, append a correction note.

## Overwrite-allowed files
These may be overwritten fully if required:
- `docs/*SNAPSHOT*.yaml`
- state trackers

## Checklists
- Mark completion with repo convention (e.g., ✅)
- Add a one-line factual summary
- Do not rewrite the file unless instructed

## When to update the Bible
Update the Bible when changes affect:
- runtime behavior or defaults
- public API / CLI interface
- schemas, manifests, or determinism contracts
- process rules that agents must follow
