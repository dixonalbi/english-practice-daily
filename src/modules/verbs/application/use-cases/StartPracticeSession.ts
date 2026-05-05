import { VerbRepository } from "../../domain/repositories/VerbRepository";
import { VerbDTO, toVerbDTO } from "../dto/VerbDTO";
import { MasteryLevel } from "@/src/shared/domain/value-objects/MasteryLevel";
import { emptyProgress } from "@/src/shared/domain/entities/StudyProgress";

export type PracticeMode = "flashcard" | "conjugation" | "quiz" | "listen" | "type-it";

export interface PracticeSessionConfig {
  readonly mode: PracticeMode;
  readonly categoryId?: string;
  /** When true, prioritise NEW + LEARNING over MASTERED. */
  readonly prioritizeWeak?: boolean;
  readonly limit?: number;
}

export interface PracticeSession {
  readonly mode: PracticeMode;
  readonly verbs: VerbDTO[];
}

const MASTERY_WEIGHT: Record<MasteryLevel, number> = {
  NEW: 3,
  LEARNING: 2,
  MASTERED: 1,
};

export class StartPracticeSession {
  constructor(private readonly repo: VerbRepository) {}

  execute(config: PracticeSessionConfig): PracticeSession {
    const pool = config.categoryId
      ? this.repo.getByCategory(config.categoryId)
      : this.repo.getAll();

    const progressMap = this.repo.getAllProgress();
    let dtos = pool.map((v) => toVerbDTO(v, progressMap[v.id] ?? emptyProgress(v.id)));

    if (config.prioritizeWeak) {
      dtos = weightedShuffle(dtos);
    } else {
      dtos = shuffle(dtos);
    }

    if (config.limit && config.limit > 0) {
      dtos = dtos.slice(0, config.limit);
    }

    return { mode: config.mode, verbs: dtos };
  }
}

function shuffle<T>(arr: readonly T[]): T[] {
  const out = [...arr];
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

function weightedShuffle(verbs: readonly VerbDTO[]): VerbDTO[] {
  return [...verbs]
    .map((v) => ({ v, key: Math.random() / MASTERY_WEIGHT[v.masteryLevel] }))
    .sort((a, b) => a.key - b.key)
    .map(({ v }) => v);
}
