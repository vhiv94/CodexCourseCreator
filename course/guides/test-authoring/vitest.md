# Vitest — per-lesson test appendix

Use when the course repo runs **[Vitest](https://vitest.dev/)** on TypeScript (or JavaScript). Goal: **one lesson → one test file → one scoped `vitest run` path**, aligned with spine `test_glob`.

## File layout

- **Lesson tests**: `Chk/Ln.test.ts` (or `Chk/Ln.spec.ts`—pick one convention per repo and stay consistent).
- **Spine `test_glob`**: a single path, e.g. `Ch1/L1.test.ts`, or a glob that resolves **only** that file, e.g. `Ch1/L1.test.ts` (avoid `Ch1/**/*.test.ts` for one lesson).
- **Learner implementation**: typically under `src/` (or packages); tests **import** public surfaces from there, not from other lessons’ private helpers.

## Minimal configuration (orienting)

- **`vitest.config.ts`**: set `test.include` / `test.exclude` so accidental discovery of unrelated suites is unlikely; many repos use defaults plus explicit `include: ['Ch**/*.test.ts']` or similar.
- **Path aliases**: if lessons use `src/` aliases (`@/foo`), mirror them in Vitest config (`resolve.alias`) so test imports match learner imports.
- **Typecheck**: keep `tsc --noEmit` (or `vitest typecheck` if you adopt it) separate from “lesson green” unless the spine says otherwise.

## Lesson-local runner (canonical one-liner)

Run **only** one lesson file (example):

```bash
npx vitest run Ch1/L1.test.ts
```

For watch mode while developing:

```bash
npx vitest Ch1/L1.test.ts
```

Document the **exact** command—copy-paste stable—in `course/overview.md` and in each `Chk/Ln.md` (Marsh template placeholder).

## Shared fixtures / helpers

- Prefer **`tests/support/`** (repo-wide) or **`Chk/_support/`** (chapter-scoped) for builders, sample payloads, and golden files.
- **Imports**: tests may import helpers; spine `test_glob` should still point at **the lesson’s** test file. Do not broaden `test_glob` to “all tests in chapter” unless `overview.md` defines that contract and Riley’s checklist allows it.
- Avoid global mocks in `setupFiles` that couple lessons; scope mocks inside `Ln.test.ts` when possible.

## Spine and naming

- **`test_glob`** must match the file Vitest collects for that lesson (exact path is clearest).
- **`depends_on`**: later lessons assert **new** behavior; depend on stable **public** APIs from earlier steps, not on other lessons’ test utilities unless those are published as intentional API (rare).

## Pitfalls

- **Over-broad globs**: `vitest run` without a path, or globs like `**/*.test.ts`, defeat “one lesson at a time”; students should not need to green the whole repo to validate `L3`.
- **ESM/CJS edge cases**: align `package.json` `"type"` with Vitest config; document any extension rules (`.mts`, `.cts`) in `overview.md`.
- **Flakes**: no real timers/network unless the lesson concept requires it; use Vitest fake timers when teaching time-dependent logic.

## Riley checklist (Vitest-specific)

- [ ] `Chk/Ln.test.ts` exists and matches lesson `id` and spine `test_glob`.
- [ ] `npx vitest run <that path>` executes **only** that lesson’s suite (plus explicitly allowed shared modules).
- [ ] No dependency on execution order across lesson files.
