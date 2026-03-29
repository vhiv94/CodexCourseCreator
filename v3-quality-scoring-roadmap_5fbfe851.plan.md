---
name: v3-quality-scoring-roadmap
overview: Define a roadmap-only V3 backlog centered on lesson quality scoring, with phased rollout, measurable gates, and low-risk adoption before enforcement.
todos:
  - id: define-scoring-rubric
    content: Define weighted rubric for concept depth, tool rationale, and test mapping.
    status: pending
  - id: build-report-only-scorer
    content: Add a non-blocking lesson quality scoring script and output format.
    status: pending
  - id: ci-report-integration
    content: Publish lesson quality reports in CI without failing builds initially.
    status: pending
  - id: baseline-and-thresholds
    content: Score existing lessons and set initial quality thresholds.
    status: pending
  - id: progressive-gating
    content: Roll out soft gates first, then hard gates for severe misses only.
    status: pending
isProject: false
---

# V3 Roadmap: Lesson Quality Scoring First

## Goal

Move from contract-valid outputs to measurable lesson quality by introducing a scoring system for lesson depth, tool rationale clarity, and test-mapping fidelity, then gradually wiring it into CI/release gates.

## Phase 1: Define the scoring contract (no enforcement)

- Create a quality spec document that defines score dimensions, weights, and pass bands.
- Start with 3 primary dimensions:
  - **Concept depth** (definition, mechanics, boundary/tradeoff, project tie-in)
  - **Tool rationale quality** (each required tool has lesson-specific purpose)
  - **Test mapping quality** (acceptance criteria map to `test_glob` + `lesson_selector` behavior)
- Add examples of high/medium/low scoring snippets using existing lesson format.
- Keep this informational first: no CI failure yet.

Suggested files:

- [ROADMAP.md](/home/honey/workspace/courses/coursecreator/ROADMAP.md)
- [course/templates/lesson.md](/home/honey/workspace/courses/coursecreator/course/templates/lesson.md)
- [python/reference-module/Ch1/L1.md](/home/honey/workspace/courses/coursecreator/python/reference-module/Ch1/L1.md)
- [python/reference-module/Ch1/L2.md](/home/honey/workspace/courses/coursecreator/python/reference-module/Ch1/L2.md)

## Phase 2: Build a non-blocking scorer

- Add a script that reads lesson markdown and emits per-file scores + reasons.
- Output format:
  - overall score
  - per-dimension scores
  - failing signals and suggested fixes
- Wire into CI as **report-only** (warnings/artifacts), not a hard fail.

Suggested files:

- [scripts/validate_repo.py](/home/honey/workspace/courses/coursecreator/scripts/validate_repo.py) (or a sibling scorer script)
- [.github/workflows/ci.yml](/home/honey/workspace/courses/coursecreator/.github/workflows/ci.yml)

## Phase 3: Calibrate with baselines and regression tracking

- Score current lessons across modules and store baseline results.
- Define anti-regression rule: no drop below agreed floor in modified lessons.
- Add trend tracking for median lesson quality over time.

Suggested files:

- [python/fundamentals](/home/honey/workspace/courses/coursecreator/python/fundamentals)
- [python/data-structures](/home/honey/workspace/courses/coursecreator/python/data-structures)
- [python/reference-module](/home/honey/workspace/courses/coursecreator/python/reference-module)

## Phase 4: Introduce soft gate then hard gate

- **Soft gate:** PR warning when changed lessons score below threshold.
- **Hard gate (after calibration):** fail CI only for severe misses (e.g., missing required sections or no evidence mapping).
- Keep score thresholds configurable to avoid brittle rollout.

Suggested files:

- [.github/workflows/ci.yml](/home/honey/workspace/courses/coursecreator/.github/workflows/ci.yml)
- [course/templates/lesson.md](/home/honey/workspace/courses/coursecreator/course/templates/lesson.md)
- [.cursor/rules/marsh-lesson-author.mdc](/home/honey/workspace/courses/coursecreator/.cursor/rules/marsh-lesson-author.mdc)

## Phase 5: Expand to V3 full pipeline

After lesson scoring is stable:

- Add policy linting beyond lesson docs.
- Add release gating for publishable modules.
- Add prompt-eval regression suite for role rules.

## Initial backlog (prioritized)

1. Define lesson quality rubric + scoring weights.
2. Implement scorer CLI (report-only).
3. Integrate report into CI artifacts/comments.
4. Baseline existing lessons and set provisional thresholds.
5. Add anti-regression rule for changed lessons.
6. Promote severe structural misses to hard CI failures.
7. Document operator playbook (how to interpret and fix low scores).
8. Schedule periodic threshold review to prevent metric drift.

## Success metrics

- 100% of new/changed lessons receive a score report.
- Reduced review churn on lesson quality comments.
- No lesson merged with missing evidence mapping.
- Upward trend in median lesson quality score over 4+ iterations.

