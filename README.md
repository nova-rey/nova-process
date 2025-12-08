README.md

# nova-process  
**Foundations, Manuals, and Templates for the Nova–Rey Development System**

`nova-process` is the canonical home for all process architecture used across Nova and Rey’s multi-project ecosystem.  
It defines the philosophy, protocols, templates, and reflection tools that support deterministic, multi-phase human–AI co-development.

This repo contains **no executable code**.  
Its purpose is to provide **stable process infrastructure** that other repos rely on.

---

## 📘 What Lives in This Repo

### **1. Philosophy**
The conceptual backbone of the Nova–Rey collaboration:
- Roles of Human, Nova, and Codex  
- Layered control model  
- How narrative, reasoning, and mechanical execution interact  
- Why phases, checkpoints, and stable templates are necessary  

Located in:  

philosophy/co-development-model.md

---

### **2. Manuals**
Two synchronized manuals define how the system operates.

#### **Human Manual**
Explains the system from the human perspective:
- Why the structure exists  
- How decisions are made  
- How to navigate phases and checkpoints  

Located in:

manuals/human-manual.md

#### **LLM Manual (v5)**
Defines deterministic rules for Nova (the reasoning AI):
- Output constraints  
- Prompt-generation rules  
- Scope invariants  
- Safety and ambiguity-handling  

Located in:

manuals/llm-manual-v5.md

---

### **3. Templates**
Fully-formed, reusable templates for agent execution and repo behavior.

#### **Unified A/B/C Agent Template**
A single structured prompt that performs:
- A: Analysis  
- B: Implementation  
- C: Verification  
…all in one atomic run.

Located in:

templates/unified-abc-agent-template.md

#### **AGENTS.md Repo Contract**
A standardized format for per-repo agent instructions:
- Allowed workflows  
- Forbidden commands  
- Test/lint details  
- Repo quirks  

Located in:

templates/agents-md-template.md

---

### **4. Exit Surveys**
A complete reflection suite for evaluating:
- Human experience  
- Nova reasoning continuity  
- Codex mechanical execution  

Includes both **mini** and **extended** versions for each role:

surveys/human-mini.md
surveys/human-extended.md
surveys/nova-mini.md
surveys/nova-extended.md
surveys/codex-mini.md
surveys/codex-extended.md

These surveys form the backbone of cycle-to-cycle improvement.

---

## 🧭 How Other Repos Use `nova-process`

Project repos (e.g., CSC, Prompt Valet, Screaming Penguin) pull from this repo to:
- Bootstrap new phases  
- Generate consistent agent prompts  
- Define repo-local `AGENTS.md` files  
- Anchor long-term continuity  
- Maintain a shared language between Human, Nova, and Codex  

No repo is required to modify `nova-process`; it functions as the **central reference library**.

---

## 🧱 Philosophy in One Sentence

**Humans define direction.  
Nova maintains structure and coherence.  
Agents perform precise mechanical execution.**

This repo documents how all of that happens without collapse, drift, or chaos.

---

## 🔧 Future Expansion

`nova-process` will eventually grow to include:
- A master glossary  
- Phase/node diagrams  
- Optional “process profiles” for different project types  
- Tutorials and onboarding walk-throughs  

But the current version focuses on creating a **stable core** first.

---

## 📄 License

MIT

---

If you are viewing this repo, you are looking at the **heart of the Nova–Rey co-development architecture**.