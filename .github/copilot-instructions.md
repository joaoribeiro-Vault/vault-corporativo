## Quick orientation — what this project is

- This workspace contains a Quartz v4 site (under `site/`) and a few top-level scripts (`scripts/`) used for content and vector-db sync. The primary code you will edit when working on the website is in `site/`.
- Quartz is a Node/TypeScript ESM site generator. The CLI entry point is `site/quartz/bootstrap-cli.mjs` and the build/pipeline code lives under `site/quartz/` (see `build.ts`, `cfg.ts`, `worker.ts`, `processors/`, `plugins/`).

## High-level architecture (big picture)

- Source content: `site/content/` and `content/` (workspace root may hold other inputs).
- Build pipeline: `site/quartz/*` contains the CLI, build steps, processors, and plugins that convert markdown/frontmatter to static HTML/CSS in `site/public/`.
- Config & site metadata: `quartz.config.ts` and `quartz.layout.ts` control site-level behavior and layout decisions.
- Dev/serve: the project uses a workerpool and websocket-based dev server (see dependencies like `workerpool`, `ws` in `site/package.json`).
- Native integrations: OG/social image generation and code highlighting use native or heavy deps (`sharp`, `satori`, `shiki`). On Windows expect native build considerations for `sharp`.

## Developer workflows & commands (how to run/build/test)

- Install and work from the `site/` directory. Node.js 22+ is required (see `site/package.json` engines).

Examples (run from repo root or `site/`):

```powershell
cd site
npm ci         # install node deps (preferred)
npm run docs   # build docs and serve: `npx quartz build --serve -d docs`
npm run check  # tsc + prettier --check
npm run test   # run tests (uses tsx --test)
```

- The `quartz` CLI can be invoked via `./quartz/bootstrap-cli.mjs` (or `npx quartz` when set up). Use it for targeted builds: the CLI accepts `build`, `serve`, and concurrency flags.

## Project-specific conventions and patterns

- ESM + TypeScript: repository uses `type: "module"` and modern ESM import style; prefer `import` over `require`.
- Content files use frontmatter (see `site/content/*.md` and `site/docs/`); utilities use `gray-matter` for parsing.
- Plugins/processors: custom transformations are under `site/quartz/processors/` and `site/quartz/plugins/`. When adding behavior for markdown nodes, follow the existing `remark`/`rehype` pipeline patterns.
- Static output is emitted to `site/public/`. Do not hand-edit files in `public/` as they are generated.

## Integration points & external dependencies

- Image generation: `sharp` + `satori` are used for social images; these are native/CPU heavy — CI and contributor machines must provision the needed binaries.
- Code highlighting: `shiki` is used for syntax highlighting and may be used during build to produce highlighted HTML or images.
- Vector DB / scripts: top-level `scripts/convert_to_vault.py` and `scripts/sync_vector_db.py` interact with external vector DBs. These rely on the Python `requirements.txt` next to `scripts/` — if modifying them, run the Python requirements installation and test locally.

## Files you should inspect before making changes (examples)

- `site/quartz/bootstrap-cli.mjs` — CLI entry point and flags
- `quartz.config.ts` / `quartz.layout.ts` — site configuration and layout hooks
- `site/quartz/build.ts` & `site/quartz/cfg.ts` — build orchestration and configuration
- `site/content/` and `site/docs/` — canonical markdown content and documentation
- `site/package.json` — scripts and dependency notes (Node >= 22)
- `scripts/convert_to_vault.py`, `scripts/requirements.txt` — python helpers for content ingestion and vector sync

## What to watch for when editing

- Typecheck & format: run `npm run check` in `site/` before pushing. The repository expects consistent Prettier formatting.
- Native deps: modifications that touch image generation (`sharp`, `satori`) may fail on CI if native binaries are missing — add lightweight smoke tests if you change those areas.
- Public output: after build, spot-check `site/public/index.html` and representative pages under `site/public/`.
- Tests: the test harness uses `tsx --test`; add small unit tests under the same conventions when changing logic.

## Examples of helpful edits (how to make good commits)

- If changing the markdown pipeline, update `site/quartz/processors/*`, add a unit test, run `npm run check` and `npm run test`, then run a build (`npm run docs`) and include a short smoke-test note in your PR description showing the generated output path.

## When you are unsure

- Prioritize minimal, well-scoped changes. If the change affects CLI flags or build config, run the CLI locally and include sample CLI invocation in the PR.

---
If anything here is unclear or you want more coverage for a specific area (Python scripts, OG image generation, plugin authoring), tell me which area and I will expand this file with targeted examples and commands.
