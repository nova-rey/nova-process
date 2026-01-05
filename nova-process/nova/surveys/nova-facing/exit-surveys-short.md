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
