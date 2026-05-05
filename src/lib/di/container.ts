import { LocalStorageVerbRepository } from "@/src/modules/verbs/infrastructure/LocalStorageVerbRepository";
import { GetVerbsByCategory } from "@/src/modules/verbs/application/use-cases/GetVerbsByCategory";
import { GetAllVerbs } from "@/src/modules/verbs/application/use-cases/GetAllVerbs";
import { UpdateVerbMastery } from "@/src/modules/verbs/application/use-cases/UpdateVerbMastery";
import { StartPracticeSession } from "@/src/modules/verbs/application/use-cases/StartPracticeSession";

import { LocalStoragePrepositionRepository } from "@/src/modules/prepositions/infrastructure/LocalStoragePrepositionRepository";
import { LocalStoragePhrasalVerbRepository } from "@/src/modules/phrasal-verbs/infrastructure/LocalStoragePhrasalVerbRepository";
import { LocalStorageEverydayRepository } from "@/src/modules/everyday/infrastructure/LocalStorageEverydayRepository";

import { GetGlobalStats } from "@/src/shared/application/use-cases/GetGlobalStats";
import { sharedSpeech } from "@/src/shared/infrastructure/speech/WebSpeechService";

const verbRepo = new LocalStorageVerbRepository();
const prepositionRepo = new LocalStoragePrepositionRepository();
const phrasalRepo = new LocalStoragePhrasalVerbRepository();
const everydayRepo = new LocalStorageEverydayRepository();

export const container = {
  speech: sharedSpeech,
  verbs: {
    repository: verbRepo,
    useCases: {
      getByCategory: () => new GetVerbsByCategory(verbRepo),
      getAll: () => new GetAllVerbs(verbRepo),
      updateMastery: () => new UpdateVerbMastery(verbRepo),
      startSession: () => new StartPracticeSession(verbRepo),
    },
  },
  prepositions: {
    repository: prepositionRepo,
  },
  phrasalVerbs: {
    repository: phrasalRepo,
  },
  everyday: {
    repository: everydayRepo,
  },
  shared: {
    useCases: {
      globalStats: () => new GetGlobalStats(),
    },
  },
} as const;

export type Container = typeof container;
