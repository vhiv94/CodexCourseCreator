# Course Creator Maturity Ladder

### v1 — Prompt-Guided (Good Starting Point)

- Use role rules (Maestro, Atlas, Riley, Marsh) for behavior and handoffs.
- Keep templates for lesson shape (Concept, Tasks, Acceptance, etc.).
- Manually review outputs.

Outcome: fast iteration, but quality varies by run/model/context.

---

### v2 — Contract-Driven (Your Current Direction)

- Enforce schema contracts for spine + progress.
- Standardize selector-scoped tests (test_glob + lesson_selector).
- Require append-only test growth patterns.
- Add repo validator + CI checks.
- Keep a worked reference module as “golden pattern.”

Outcome: much less drift; errors become detectable instead of subjective.

---

### v3 — Production-Grade Pipeline

- Add policy checks beyond schema (e.g., lesson depth checks, required sections, forbidden phrasing).
- Add regression guards for historical behavior (no selector deletion, no old test loss).
- Add quality scoring for lesson docs (concept depth, tool rationale, test mapping).
- Add release gating: only publish lessons/modules if validation + quality thresholds pass.
- Add periodic rule eval suite (same prompts, compare outputs over time/models).

Outcome: predictable, repeatable course generation with measurable quality.

---

### Practical Recommendation

For your project, keep rules—but treat them as the top layer, not the enforcement layer.
The sweet spot is: Rules + Templates + Schemas + Validators + CI + Reference module.

If you want, next I can draft a concrete v3 backlog (5–8 tasks) prioritized by impact vs effort.