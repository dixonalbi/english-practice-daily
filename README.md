# Quiet Library

A focused, local-first English study companion for intermediate Spanish speakers. Four chapters: **verbs**, **prepositions**, **phrasal verbs**, **everyday**. Progress lives on your device — no accounts, no backend.

Live: https://dixonalbi.github.io/english-practice-daily/

## Stack

- **Vite 5** + **React 19** + **TypeScript strict**
- **TanStack Router** (hash history → GitHub Pages friendly)
- **Tailwind CSS v4** (CSS-first `@theme` config in `src/globals.css`)
- **Motion** (Framer Motion v12) · **Lucide** · **Zustand** · **React Hook Form + Zod**
- **Web Speech API** for native pronunciation (no external TTS)
- **@fontsource-variable** for Inter, Fraunces, JetBrains Mono

## Getting started

```bash
pnpm install
pnpm dev          # Vite dev server
pnpm build        # tsc check + vite build → dist/
pnpm preview      # serve dist/
pnpm lint
```

## Architecture

DDD layering, one bounded context per chapter:

```
src/
├── main.tsx · router.tsx · RootLayout.tsx     ← Presentation entry
├── routes/                                    ← Page components
├── modules/
│   ├── verbs/                fully implemented (Browse · Flashcard · Conjugation)
│   ├── prepositions/         seeded placeholder
│   ├── phrasal-verbs/        seeded placeholder
│   └── everyday/             seeded placeholder
│       ├── domain/           pure TS (no React/router imports)
│       ├── application/      use cases + DTOs
│       └── infrastructure/   localStorage repo + JSON loader
├── shared/                                   cross-module pieces
├── components/                               UI primitives & domain components
├── data/verbs-data.json                      authoritative verb corpus
└── lib/
    ├── di/container.ts                       single-file DI graph
    └── hooks/useReactiveSnapshot.ts          useSyncExternalStore-backed store
```

Layering rule: **domain ← application ← infrastructure / presentation**. Domain & application import nothing from React, router, or the storage adapter directly.

### Swapping `localStorage` for an HTTP API

Implement the `*Repository` interface (e.g. `VerbRepository`) with a `fetch`-based adapter and rewire `src/lib/di/container.ts`. Nothing else changes.

## Adding data

### Verbs (`src/data/verbs-data.json`)

Append a verb to a category's `verbs` array using the canonical shape:

```json
{
  "i": "infinitive", "ip": "/ipa/", "sp": "spanish meaning",
  "p": "past", "pi": "/ipa/", "pSp": "speech-override (optional)",
  "pp": "past-participle", "ppi": "/ipa/", "ppSp": "(optional)",
  "g": "gerund", "gi": "/ipa/",
  "t": "third-person", "ti": "/ipa/"
}
```

`pSp` / `ppSp` exist for words whose IPA tells the eye the wrong story (e.g. `read` past simple sounds like “red”). The Web Speech API will pronounce the override instead of the spelling.

To add a new category, append to the `categories` array with `id`, `name`, `icon`, `verbs`. The Browse page picks it up automatically.

### Prepositions / Phrasal verbs / Everyday

Add entries to the corresponding `infrastructure/*-data.ts` file. The exported seed array is the source of truth; the local-storage repository indexes it on construction.

## Pronunciation

`src/shared/infrastructure/speech/WebSpeechService.ts` wraps `window.speechSynthesis`. It picks the best available `en-*` voice on the device. Click any pronunciation chip to hear the form. Speech overrides (`pSp`, `ppSp`) are honoured.

## Progress

Each chapter persists to its own `localStorage` key:

| Chapter        | Key                          |
|----------------|------------------------------|
| Verbs          | `verbs:progress:v1`          |
| Prepositions   | `prepositions:progress:v1`   |
| Phrasal verbs  | `phrasal-verbs:progress:v1`  |
| Everyday       | `everyday:progress:v1`       |

Each entry tracks `masteryLevel` (NEW / LEARNING / MASTERED), `lastReviewedAt`, `correctStreak`, `totalReviews`. The dashboard derives the streak from the union of `lastReviewedAt` days across chapters.

## Design

Aesthetic direction: **Quiet Library** — paper/ink in light mode, umber/parchment in dark, single ochre accent. Display: Fraunces (variable serif). UI: Inter. Mono: JetBrains Mono. Hairline rules, tabular numbers, generous negative space; density only where it earns it (the conjugation grid).

## Deployment

CI builds and publishes to GitHub Pages from `main` via `.github/workflows/deploy.yml`. Vite is configured with `base: '/english-practice-daily/'`. The router uses **hash history** so deep-links work on Pages without an SPA rewrite rule.

## Roadmap

- [x] Verbs end-to-end (Browse · Flashcard · Conjugation drill)
- [ ] Verbs Quiz / Type-it / Listen
- [ ] Prepositions: full corpus + Fill-the-blank
- [ ] Phrasal verbs: full corpus + Match-meaning
- [ ] Everyday: Formal ↔ Informal converter
- [ ] Global cross-chapter search
