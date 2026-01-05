
---

## `codex/docs/surveys/full-survey.md` (template v0.1.0)

This is phase-level and should create decision-grade signal (still structured, still not “journaling”).

```md
# Full Exit Survey (Codex)
Version: v0.1.0

Purpose: Capture deeper signal at phase completion (baseline/tag moment).
Run only when Nova instructs you to run it.

## Output Rules

- Be factual.
- Use "unknown" where needed.
- Do not invent process claims.
- Keep free-text short and specific.

## Required Output Format

```yaml
survey: full
version: v0.1.0
timestamp_utc: "<iso-8601>"
phase:
  id: "<string or unknown>"                 # e.g., Phase 4
  tag_or_baseline: "<string or unknown>"    # e.g., v0.32.0-phase4-baseline
summary:
  outcome: "success|partial|fail"
  scope_respected: true|false|unknown
  behavior_change: "none|flagged|unintended|unknown"
quality:
  tests_green: true|false|unknown
  lint_green: true|false|unknown
  formatting_green: true|false|unknown
  determinism_risk: "low|medium|high|unknown"
docs:
  bible_updated: true|false|unknown
  snapshot_updated: true|false|unknown
  checklist_updated: true|false|unknown
  docs_drift_detected: "none|minor|major|unknown"
pain_points:
  top_3:
    - "<brief|scope|tooling|tests|docs|agent_drift|missing_input|other|unknown>"
    - "<...>"
    - "<...>"
wins:
  top_3:
    - "<one sentence>"
    - "<one sentence>"
    - "<one sentence>"
follow_ups:
  recommended_next_actions:
    - "<one sentence>"
    - "<one sentence>"
risk_notes:
  - "<one sentence>"
