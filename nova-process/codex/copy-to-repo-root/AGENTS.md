# AGENTS.md (Repository Root) — Nova-Process Execution Contract

You are an execution agent in a Nova-Process repository.

## Prime Directive
- Do exactly the human brief.
- Do NOT expand scope, refactor opportunistically, or invent requirements.
- If instructions are ambiguous or contradictory: FAIL FAST with a clear error.

## Task Modes
This repo uses two atomic task modes:
1) Checkpoint (A/B/C) — analysis → implementation → verification in one uninterrupted run
2) Mini-Push (MP) — small, low-risk change with strict “no behavior change” constraint

Canonical prompt structures:
- `nova-process/nova/abc-prompt-example.md`
- `nova-process/nova/mp-prompt-example.md`

## Documentation Ownership
- Historical log / “Bible” files are APPEND-ONLY. Never rewrite history.
- State / snapshot files may be overwritten fully if required by the brief.
- If unclear which category applies: FAIL FAST.

## Verification
- Run the repo’s standard tests and linting.
- If failures occur: fix and re-run until green, or fail with a clear reason.

## Reporting
Your final output must include:
- Summary of changes
- Files touched
- Commands run + results
- Any out-of-scope observations (not implemented)

## Exit Surveys (Codex)

Survey definitions:
- Short: `/docs/surveys/short-survey.md`
- Full:  `/docs/surveys/full-survey.md`

Surveys are NOT run automatically.
Only run a survey when explicitly instructed by the current prompt (authored by Nova).
If instructed to both modify code and run a survey, code changes occur first, surveys last.

When instructed:
- Answer the survey questions in the required format.
- Write results to `/docs/surveys-completed/` using the naming rule provided by the prompt.
- Keep answers factual and concise. No motivational speeches.
- If required context is missing, answer with "unknown" rather than guessing.

