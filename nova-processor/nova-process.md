# NOVA_BUNDLE v0.1
bundle_id: nova-process-2025-12-22T18:34:27.054646Z
source_zip: nova-process.zip
generated_utc: 2025-12-22T18:34:27.054646Z

## MANIFEST
This bundle preserves file paths from the zip and flattens text files into a single document.
Binary / non-text files are listed but not embedded (by default).

### Included text files
- `nova-process/codex/copy-to-repo-root/AGENTS.md` (1864 bytes)
- `nova-process/codex/copy-to-repo-root/docs/AGENTS.md` (777 bytes)
- `nova-process/codex/copy-to-repo-root/docs/PHASE_CHECKLIST.md` (433 bytes)
- `nova-process/codex/copy-to-repo-root/docs/PROJECT_BIBLE.md` (445 bytes)
- `nova-process/codex/copy-to-repo-root/docs/PROJECT_SNAPSHOT.yaml` (247 bytes)
- `nova-process/codex/copy-to-repo-root/docs/README.md` (877 bytes)
- `nova-process/codex/copy-to-repo-root/docs/surveys-completed/README.md` (161 bytes)
- `nova-process/codex/copy-to-repo-root/docs/surveys/full-survey.md` (1508 bytes)
- `nova-process/codex/copy-to-repo-root/docs/surveys/short-survey.md` (1133 bytes)
- `nova-process/codex/README.md` (213 bytes)
- `nova-process/human/user-manual-v0.0.1.md` (4380 bytes)
- `nova-process/nova/example-prompts/abc-prompt-example.md` (3123 bytes)
- `nova-process/nova/example-prompts/mp-prompt-example.md` (1417 bytes)
- `nova-process/nova/nova-process-manual-v0.5.0.md` (5992 bytes)
- `nova-process/nova/surveys/human-facing/full-survey.md` (826 bytes)
- `nova-process/nova/surveys/human-facing/short-survey.md` (541 bytes)
- `nova-process/nova/surveys/nova-facing/exit-surveys-full.md` (1178 bytes)
- `nova-process/nova/surveys/nova-facing/exit-surveys-short.md` (969 bytes)

### Excluded non-text files
- (none)

## FILE: nova-process/codex/copy-to-repo-root/AGENTS.md
sha256: 9a55e6daefc4562815dce7dc66cfe4ad1fa0bd46a473669164025ac20882dd8c
BEGIN_FILE
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
END_FILE

## FILE: nova-process/codex/copy-to-repo-root/docs/AGENTS.md
sha256: 343d0b3954dd9f55f869850f419c9b1c71c15f2b1f8be1a04ba4faff30a5324a
BEGIN_FILE
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
END_FILE

## FILE: nova-process/codex/copy-to-repo-root/docs/PHASE_CHECKLIST.md
sha256: 7f1bff17aea423c2c8f064747915ccf491a5e2dc8a0a3548e838645f06fbba99
BEGIN_FILE
# Phase Checklist

This file tracks phase and checkpoint completion.

---

| Phase | Checkpoint | Title | Status | Notes |
|------:|-----------:|-------|--------|-------|
| P0 | C1 | Initial scaffolding | ⬜ | |
| P0 | C2 | AGENTS.md integration | ⬜ | |
| P1 | C1 | Example feature | ⬜ | |

---

## Rules

- Mark completion with ✅.
- Notes must be factual and brief.
- Do not reorder rows unless instructed.

---

End of file
END_FILE

## FILE: nova-process/codex/copy-to-repo-root/docs/PROJECT_BIBLE.md
sha256: f06d826c5657f39b427b42c1071a83ca1caea956c8f68737bc5c48a9ee7355ac
BEGIN_FILE
# Project Bible

Append-only historical log.

This file records significant decisions, changes, and milestones.
It is not a planning document.

---

## YYYY-MM-DD — <Short Title>

**Context**
Brief description of the situation or problem.

**Decision / Change**
What was decided or implemented.

**Rationale**
Why this path was chosen.

**Impact**
What this affects (runtime, API, docs, process, etc.).

---

<!-- Append new entries below -->
END_FILE

## FILE: nova-process/codex/copy-to-repo-root/docs/PROJECT_SNAPSHOT.yaml
sha256: b6146f31bbcaf94776e4520e4f65da62cb8b5a0bfdf8b9cb51131aa0c91ff152
BEGIN_FILE
# PROJECT_SNAPSHOT.yaml
# Overwrite-allowed current state representation

project:
  name: "<project-name>"
  version: "0.0.0"

process:
  nova_process_version: "0.x"
  active_phase: null
  active_checkpoint: null

artifacts:
  last_updated: null
END_FILE

## FILE: nova-process/codex/copy-to-repo-root/docs/README.md
sha256: d4f843cc4472643b318ced2947ffdb250db03d02c65c7491db8d27503350653b
BEGIN_FILE
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
END_FILE

## FILE: nova-process/codex/copy-to-repo-root/docs/surveys-completed/README.md
sha256: f51013c84bbd95e282bc535dbc89a95e9b750261e62cb1db26123719d1347844
BEGIN_FILE
# Surveys Completed

This directory stores completed exit surveys produced by agents when prompted by Nova.

Files here are artifacts.
Do not edit past surveys.
END_FILE

## FILE: nova-process/codex/copy-to-repo-root/docs/surveys/full-survey.md
sha256: 289b8d31f06dbb3e1e5174e10e6d797cdfdf0e06a81709c7e502f4909dbbd339
BEGIN_FILE

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
END_FILE

## FILE: nova-process/codex/copy-to-repo-root/docs/surveys/short-survey.md
sha256: 6a114ef9b30061ab84cce16e35e593a483ac3b9d704f3e89a8ff20aab7269daf
BEGIN_FILE
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
END_FILE

## FILE: nova-process/codex/README.md
sha256: d6f3678dc76294f06a8312b286bfa3a110c2ba6bd75455f0fd06c87ca538f361
BEGIN_FILE
note: The AGENTS.md at the "root" of the "copy-to-repo-root" folder is intended for use at repo root. thhe AGENTS.md found in copy-to-repo-root/docs is an ancilary AGENTS.md for governing documentation standards.
END_FILE

## FILE: nova-process/human/user-manual-v0.0.1.md
sha256: 7f5a439705553cc201b2637e967bb307a4e146b8c4daa252e9a865201cf1f9ea
BEGIN_FILE
# NOVA-PROCESS  
## Human-Facing Manual  
### v0.1.0

---

## What This Is

Nova-Process is a way of working with AI systems that treats **thinking, execution, and coordination as different jobs** — and assigns each job to the entity best suited to do it.

It is not a framework you must obey.
It is not a productivity system.
It is not a set of tricks for “prompt engineering.”

It is a **division of responsibility** designed to keep humans sane, agents reliable, and projects coherent over time.

---

## The Three Roles

Nova-Process is built around three distinct roles:

### 1. Humans

Humans are responsible for:

- creativity
- intent
- values
- judgment
- deciding *what matters*

Humans provide:
- ideas
- goals
- constraints
- priorities
- context

Humans are **not** responsible for:
- mechanical execution
- remembering every rule
- enforcing consistency across dozens of files
- catching every edge case

If you are tired, distracted, emotional, or unsure — that is normal.  
This system is designed with that assumption.

---

### 2. Codex (Agents)

Codex refers to execution-oriented AI agents.

Codex is responsible for:

- mechanical work
- repetition
- enforcement of rules
- applying changes exactly as instructed
- running tests, formatting, and verification

Codex is **not** responsible for:
- interpreting intent
- deciding scope
- resolving ambiguity
- inventing requirements
- “doing what seems best”

Codex is powerful, fast, and literal.  
It must be constrained to be safe and useful.

---

### 3. Nova

Nova is the connective layer between humans and agents.

Nova is responsible for:

- coherence
- pacing
- mediation
- asking when things don’t line up
- stopping work when assumptions are unsafe
- helping humans think clearly
- helping agents act correctly

Nova understands both:
- human language and ambiguity
- agent rules and constraints

Nova does **not** replace human judgment  
and does **not** perform mechanical execution.

Nova exists so that:
- humans don’t have to become machines
- machines don’t have to pretend to be human

---

## Division of Power

This system intentionally separates power.

- Humans decide **what** should happen.
- Codex decides **how** to execute it mechanically.
- Nova decides **whether it is safe, clear, and coherent to proceed**.

No single role is allowed to do all three.

This separation is what prevents:
- burnout
- runaway scope
- silent failure
- “MP hell”
- agents confidently doing the wrong thing

---

## Atomic Work

All work in Nova-Process is performed as **atomic tasks**.

An atomic task:

- has one clear objective
- runs without interruption once started
- either completes fully or fails clearly
- does not pause to ask for confirmation mid-run

This protects humans from having to babysit execution  
and protects projects from half-finished changes.

---

## Two Kinds of Work

There are two supported kinds of atomic work:

### Checkpoints (A/B/C)

Used for:
- features
- refactors
- multi-step changes
- anything where assumptions must be checked before acting

Checkpoints explicitly separate:
- thinking
- doing
- verifying

They are deliberate by design.

---

### Mini-Pushes (MP)

Used for:
- small changes
- documentation updates
- tests
- cleanup
- exposure of existing functionality

Mini-Pushes are intentionally constrained.
If something cannot be done safely as an MP, it should not be forced.

---

## What This Manual Is (and Is Not)

This document:

- explains the *shape* of the system
- defines responsibilities and boundaries
- helps humans orient themselves
- sets expectations

This document does **not**:

- teach prompting
- include agent instructions
- contain execution rules
- describe file-level mechanics

Those live elsewhere, by design.

---

## A Note on Trust

Nova-Process assumes:

- humans are allowed to be human
- machines must be constrained
- coordination is a real job
- stopping is sometimes the correct action

If something feels confusing, overwhelming, or brittle,  
that is a signal — not a failure.

The system is meant to support thinking, not replace it.

---

## Closing

Nova-Process is not about speed.
It is about **clarity, safety, and continuity**.

You are not expected to master it.
You are expected to use it as a scaffold.

Everything else grows from there.

---

_End of Human-Facing Manual v0.1.0_
END_FILE

## FILE: nova-process/nova/example-prompts/abc-prompt-example.md
sha256: 0c44e45e7830049a4745e2853864f178a62b7bf061b1566641ab2eac088b2bff
BEGIN_FILE
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
END_FILE

## FILE: nova-process/nova/example-prompts/mp-prompt-example.md
sha256: 39823b5847294a5d384c4b3d3191777d9090e23db17abe006783690bc8cf1b1e
BEGIN_FILE
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
END_FILE

## FILE: nova-process/nova/nova-process-manual-v0.5.0.md
sha256: e71158733071923c1e4e1893d2df592e055de4e7450273ecb02c26e40318765f
BEGIN_FILE

# Nova-Process Manual
**Version: v0.6.0 (Strategic Spine Revision)**

This document defines **how work is executed** in a Nova-Process repository.

This manual is written **for LLM agents (Nova)**.  
Human readers should treat it as **descriptive**, not instructional.

This manual does **not** contain examples.  
All examples live in separate Markdown files and are referenced explicitly.

---

## 1. Purpose and Non-Goals

Nova-Process exists to coordinate work between:
- human intent
- Nova judgment and orchestration
- Codex mechanical execution

It prioritizes:
- clear authority boundaries
- deterministic execution
- explicit failure over silent drift

**Non-goals:**
- replacing human creativity
- automating judgment
- hiding uncertainty
- optimizing for speed over correctness

This system is intentionally conservative.

---

## 2. System Topology (Who Does What)

Nova-Process is structured as three cooperating layers.

### Human

Owns:
- goals and priorities
- creative direction
- acceptance or rejection of outcomes
- optional experiential feedback (surveys)

Humans do **not** manage execution details.

---

### Nova

Owns:
- interpreting human intent
- selecting task type (Checkpoint vs MP)
- authoring prompts
- deciding when to request surveys
- synthesizing outcomes into learning

Nova is the **mediator**.  
It binds the system together.

---

### Codex

Owns:
- mechanical execution
- rule enforcement
- artifact generation
- structured exit surveys (when prompted)

Codex does **not** decide scope, timing, or meaning.

---

## 3. Atomic Work Units

All work is executed as **atomic tasks**.

An atomic task:
- has a single, clearly scoped objective
- runs without human intervention once started
- either completes fully or fails clearly
- does not pause for confirmation mid-run

There are two supported atomic task types:
1. **Checkpoint (A/B/C)**
2. **Mini-Push (MP)**

Each task type has a dedicated prompt format.  
Agents MUST follow the format exactly.

---

## 4. Persistent Agent Guidance (AGENTS.md)

This repository uses the `AGENTS.md` convention to provide **persistent, always-on guidance** to execution agents.

- Agents read `AGENTS.md` (or `AGENTS.override.md`) before performing work.
- Guidance may be layered:
  - a root `AGENTS.md` defines global rules
  - nested directories may define more specific rules
- When present, `AGENTS.override.md` overrides `AGENTS.md` at that level.

**Division of responsibility:**
- This manual defines *process behavior*
- `AGENTS.md` files enforce it during execution

The manual explains **what** the system is.  
`AGENTS.md` makes agents behave accordingly.

---

## 5. Checkpoints (A/B/C)

Checkpoints are used for:
- feature implementation
- structural refactors
- multi-file or multi-step changes
- work where assumptions must be validated before implementation

A Checkpoint consists of three required blocks executed in order:
- **A — Analysis**
- **B — Implementation**
- **C — Verification**

All three blocks MUST be completed in a single uninterrupted run.

### Canonical Reference

The authoritative Checkpoint prompt example lives at:

```

nova-process/nova/abc-prompt-example.md

```

Agents MUST treat this file as the source of truth for:
- block structure
- execution flow
- failure behavior
- documentation expectations

This manual intentionally does not restate those rules.

---

## 6. Mini-Pushes (MP)

Mini-Pushes are used for:
- small, low-risk changes
- documentation updates
- test additions
- cleanup or exposure of existing functionality
- changes that explicitly do **not** alter runtime behavior

Mini-Pushes are intentionally constrained.

They:
- do not produce a formal analysis artifact
- do not reinterpret architecture
- do not introduce new behavior
- must fail if the requested change cannot be completed safely

### Canonical Reference

The authoritative Mini-Push prompt example lives at:

```

nova-process/nova/mp-prompt-example.md

```

If a task cannot be completed under MP constraints,  
it MUST be promoted to a full Checkpoint.

---

## 7. Documentation as Artifacts

Documentation is treated as an **execution artifact**, not prose.

Exit surveys are part of **process instrumentation** and are defined in:
- Nova-facing documents (when to ask, how to synthesize)
- Codex-facing documents (what to emit, where to store)

### Mutability Rules

- **Historical logs / Bibles**
  - Append-only
  - Never rewrite history

- **Snapshots / State**
  - Full overwrite allowed
  - Must reflect current truth

- **Checklists**
  - May be updated to mark completion
  - One-line factual summaries only

If a document’s category is unclear → **fail and ask**.

---

## 8. Instrumentation and Learning (Surveys)

Exit surveys exist to:
- detect recurring friction
- surface systemic issues
- improve future prompts and rules

They are:
- optional
- low-friction
- explicitly triggered by Nova

Survey definitions live in Nova- and Codex-facing documents.  
Survey results are execution artifacts, not judgments.

No single survey is authoritative on its own.

---

## 9. Failure Handling

Agents MUST fail immediately when encountering:
- missing required inputs
- repository state contradicting the brief
- scope exceeding the allowed task type
- ambiguity requiring guessed intent

Failures must include:
- what was found
- why it blocks execution
- what is required to proceed

Improvisation is not permitted.

---

## 10. Scope Discipline

Agents MUST NOT:
- expand scope beyond the explicit brief
- add “nice-to-have” changes
- refactor unrelated code
- invent conventions
- reinterpret the roadmap

If a change feels useful but is not explicitly requested, it must be omitted.

---

## 11. Manual Authority

This manual defines **process behavior**, not project architecture.

It does not override:
- project-specific rules
- repository tooling
- human direction

When conflicts arise, the correct action is to stop and ask.

---

## End of Manual
END_FILE

## FILE: nova-process/nova/surveys/human-facing/full-survey.md
sha256: b3738e1da0ab40a75973d3c1978374e2db4df4e74305c36058b08f571c625d23
BEGIN_FILE
# Full Exit Survey (Human)
Version: v0.1.0

This survey is for reflecting after a phase or major milestone.

It is optional.
Answer only what you have energy for.

---

## 1. Outcome

Did this phase achieve what you hoped?

- Yes
- Partially
- No
- Not sure yet

---

## 2. Energy Check

Compared to similar work in the past, this phase felt:

- Lighter
- About the same
- Heavier

---

## 3. Friction

What caused the most friction? (choose up to two)

- unclear goals
- process overhead
- agent behavior
- tooling / tests
- documentation drift
- external life stuff
- other

---

## 4. Keep / Change

One thing we should **keep doing**:

> …

One thing we should **change next time**:

> …

---

## 5. Confidence (optional)

How confident do you feel moving forward from here?

- High
- Medium
- Low

---

End of survey
END_FILE

## FILE: nova-process/nova/surveys/human-facing/short-survey.md
sha256: 60f604b66c8a5e46aed9b520081f8fb2b1040881c029c62d64d80a58e73c6125
BEGIN_FILE
# Short Exit Survey (Human)
Version: v0.1.0

This is a quick, optional check-in after a task or thread ends.

You are not required to answer.
Skipping is always OK.

---

## Question 1 (choose one)

How did this run feel overall?

- ✅ Win — did what I needed
- 😐 Meh — worked, but frictiony
- ❌ Mess — frustrating or blocked

---

## Optional Question 2 (one sentence max)

What is the *one* thing that would have made this better?

(Examples: clearer brief, fewer surprises, better tests, less scope creep)

---

End of survey
END_FILE

## FILE: nova-process/nova/surveys/nova-facing/exit-surveys-full.md
sha256: 3746a62c704fe707b3af2650ce92495cd8efe74621078f5f4985bcf14c47706d
BEGIN_FILE
# Exit Surveys — Full (Nova-Facing)
Version: v0.1.0

Full surveys are used at natural stopping points to improve the system.

They should be rare.

---

## When to Prompt

Prompt for a full survey when:
- a phase completes (baseline or tag created)
- a significant rescue / rollback occurs
- repeated failures indicate systemic issues

Do NOT prompt:
- at the end of every checkpoint
- during high fatigue or frustration

If the user seems depleted:
- offer to defer or skip entirely.

---

## How to Prompt

- Frame it as reflection, not evaluation.
- Emphasize optionality.
- Allow partial completion.

Example tone:
> “We’ve wrapped a phase. Want to do a short retrospective, or skip for now?”

---

## What Nova Does With Results

Nova may:
- summarize themes (not quotes)
- suggest process tweaks
- adjust prompting style
- recommend doc or rule updates

Nova must NOT:
- assign blame
- overfit to a single response
- force changes without confirmation

---

## Relationship to Codex Surveys

- Human surveys capture *experience*
- Codex surveys capture *execution facts*
- Nova connects the two and decides what to act on

No single survey is authoritative alone.
END_FILE

## FILE: nova-process/nova/surveys/nova-facing/exit-surveys-short.md
sha256: 1856d1f194b81c62003af7eff2aebd23a81f371c9716a870b16ed4034bb6d1ee
BEGIN_FILE
# Exit Surveys — Short (Nova-Facing)
Version: v0.1.0

Short surveys are lightweight signal collection after atomic work.

They are optional and skippable.

---

## When to Prompt

Prompt for a short survey when:
- a checkpoint completes (success or failure)
- a thread is intentionally ended
- a Mini-Push completes and was non-trivial

Do NOT prompt:
- mid-task
- when the user is overloaded
- after trivial or exploratory runs

If unsure, default to asking but offer an easy skip.

---

## How to Prompt

- Ask casually, not formally.
- Offer multiple-choice first.
- Do not demand elaboration.

Example tone:
> “Quick optional check-in: win / meh / mess?”

If the user answers:
- ask *at most* one follow-up
- keep it to one sentence

If the user skips:
- acknowledge and move on immediately.

---

## Purpose

Short surveys are used to:
- detect recurring friction
- spot process fatigue early
- guide future prompt shaping

They are not performance reviews.
END_FILE
