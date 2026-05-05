# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

## Stack

- **Next.js 16.2.4** with App Router (`app/`). This is a major version newer than most training data — see AGENTS.md and consult `node_modules/next/dist/docs/01-app/` for canonical APIs before writing code.
- **React 19.2.4** — assume Server Components by default; mark Client Components with `"use client"`.
- **Tailwind CSS v4** via `@tailwindcss/postcss` plugin (no `tailwind.config.js` — v4 uses CSS-first config in `app/globals.css`).
- **TypeScript** strict mode. Path alias `@/*` maps to project root.
- **pnpm** package manager.

## Commands

```bash
pnpm dev          # next dev — local server on :3000
pnpm build        # next build — production build
pnpm start        # next start — serve production build
pnpm lint         # eslint (flat config in eslint.config.mjs)
```

No test runner is configured.

## Skills routing

This project ships skills in `.claude/skills/`. Invoke the matching skill instead of reinventing guidance it already encodes.

| When you are… | Use |
|---|---|
| Building any UI (page, component, layout, artifact) | `frontend-design` (Anthropic) — bold aesthetic direction first, then code |
| Making a design decision (color, type, layout) and unsure | `bencium-controlled-ux-designer` — asks before deciding |
| Pushing creative direction without permission | `bencium-innovative-ux-designer` — commits boldly |
| Reviewing finished UI for quality / a11y / UX | `web-design-guidelines` (Vercel) |
| Writing or refactoring React / Next.js code | `react-best-practices` (Vercel) — follow priority order: waterfalls → bundle → server → client |
| Designing a component API or refactoring boolean-prop sprawl | `composition-patterns` (Vercel) |
| Touching React Native / Expo (not used here yet) | `react-native-skills` (Vercel) |
| Auditing or fixing WCAG accessibility | `accesslint-audit` *(requires accesslint MCP server)* |

## Project standards

@.claude/rules/standards.md

## Layout

The codebase is currently a fresh `create-next-app` scaffold: `app/layout.tsx` (root layout, Geist font), `app/page.tsx` (landing), `app/globals.css` (Tailwind v4 directives). There is no domain logic, routing tree, data layer, or component library yet — when adding features, establish conventions deliberately rather than inferring them from the scaffold.
