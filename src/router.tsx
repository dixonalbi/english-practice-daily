import {
  createRootRoute,
  createRoute,
  createRouter,
  createHashHistory,
} from "@tanstack/react-router";
import { RootLayout } from "./RootLayout";
import { DashboardClient } from "@/src/components/dashboard/DashboardClient";
import { VerbsBrowse } from "@/src/components/verbs/VerbsBrowse";
import { VerbsPracticePicker } from "@/src/routes/VerbsPracticePicker";
import { FlashcardSession } from "@/src/components/verbs/FlashcardSession";
import { ConjugationDrill } from "@/src/components/verbs/ConjugationDrill";
import { PrepositionsPage } from "@/src/routes/PrepositionsPage";
import { PhrasalVerbsPage } from "@/src/routes/PhrasalVerbsPage";
import { EverydayPage } from "@/src/routes/EverydayPage";
import { NotFound } from "@/src/routes/NotFound";

const rootRoute = createRootRoute({
  component: RootLayout,
  notFoundComponent: NotFound,
});

const indexRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/",
  component: DashboardClient,
});

const verbsRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/verbs",
  component: VerbsBrowse,
});

const verbsPracticeRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/verbs/practice",
  component: VerbsPracticePicker,
});

const verbsFlashcardRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/verbs/practice/flashcard",
  component: FlashcardSession,
});

const verbsConjugationRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/verbs/practice/conjugation",
  component: ConjugationDrill,
});

const prepositionsRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/prepositions",
  component: PrepositionsPage,
});

const phrasalRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/phrasal-verbs",
  component: PhrasalVerbsPage,
});

const everydayRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/everyday",
  component: EverydayPage,
});

const routeTree = rootRoute.addChildren([
  indexRoute,
  verbsRoute,
  verbsPracticeRoute,
  verbsFlashcardRoute,
  verbsConjugationRoute,
  prepositionsRoute,
  phrasalRoute,
  everydayRoute,
]);

/**
 * Hash history sidesteps GitHub Pages' lack of SPA fallback — every route
 * resolves to /index.html and the router reads the URL fragment.
 */
export const router = createRouter({
  routeTree,
  history: createHashHistory(),
  defaultPreload: "intent",
});

declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}
