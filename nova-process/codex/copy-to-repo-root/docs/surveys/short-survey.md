# Short Exit Survey (Codex)
Version: v0.1.0

Purpose: Capture quick, structured signal after an atomic task.
Run only when Nova instructs you to run it.

## Output Rules

- Keep answers factual and concise.
- Use "unknown" if the information is not available.
- Do not guess at human intent or emotions.
- Do not include long narrative.

## Required Output Format

```yaml
survey: short
version: v0.1.0
timestamp_utc: "<iso-8601>"
task:
  type: "checkpoint|mp|unknown"
  id: "<string or unknown>"         # e.g., P4C2 or MP-VXP-C1 or unknown
  outcome: "success|partial|fail"
execution:
  scan: "deep|quick|unknown"
  tests_run: true|false
  lint_run: true|false
  format_check_run: true|false
  reruns_needed: 0                  # integer, number of retry cycles after failures
change_summary:
  files_touched_count: 0            # integer
  files_touched_examples: []        # list of a few key files
friction:
  primary: "brief|scope|tooling|tests|docs|agent_drift|missing_input|unknown"
  note: "<one sentence>"
recommendation:
  next_improvement: "brief|docs|tests|agent_rules|tooling|examples|unknown"
  note: "<one sentence>"
