# Jest — per-lesson test appendix

Use when the course repo runs **[Jest](https://jestjs.io/)** instead of Vitest. Patterns mirror [vitest.md](vitest.md); differences are called out here. Prefer Vitest for new Vite-centric TypeScript courses unless you have a reason to standardize on Jest.

## File layout

- **Lesson tests**: `Chk/Ln.test.ts` or `Chk/Ln.spec.ts` (same naming discipline as Vitest).
- **Spine `test_glob`**: single file path, e.g. `Ch1/L1.test.ts`.

## Configuration notes

- **`jest.config.js` / `jest.config.ts`**: map `moduleNameMapper` for path aliases; restrict `testMatch` / `roots` if the monorepo is large.
- **TypeScript**: use `ts-jest` or Babel + `@babel/preset-typescript` consistently; document the stack in `course/overview.md`.

## Lesson-local runner (canonical one-liner)

Run **only** one file (CLI pattern varies slightly by Jest version; the intent is **path-scoped**):

```bash
npx jest Ch1/L1.test.ts
```

For watch mode:

```bash
npx jest --watch Ch1/L1.test.ts
```

## Shared fixtures / helpers

Same conventions as Vitest: **`tests/support/`** or **`Chk/_support/`**; spine still points at the **lesson test file**.

## Pitfalls

- **Projects / workspaces**: in a monorepo, ensure the command uses the **course’s** Jest config (`--config` if needed).
- **Global setup**: `setupFilesAfterEnv` should avoid leaking state across lessons; prefer per-file setup.

## Riley checklist (Jest-specific)

- [ ] One primary test file per lesson; spine `test_glob` matches it.
- [ ] Documented one-liner runs **only** that file’s suite under the repo’s Jest config.
- [ ] Deterministic tests; no snapshot churn without a lesson reason to teach snapshots.
