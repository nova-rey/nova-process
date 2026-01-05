
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
