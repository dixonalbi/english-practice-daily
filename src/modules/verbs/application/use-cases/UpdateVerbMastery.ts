import { VerbRepository } from "../../domain/repositories/VerbRepository";
import { evaluateMastery } from "../../domain/services/MasteryEvaluator";
import { MasteryLevel } from "@/src/shared/domain/value-objects/MasteryLevel";

export class UpdateVerbMastery {
  constructor(private readonly repo: VerbRepository) {}

  /**
   * Records a single review outcome and persists the new progress.
   * Returns the resulting mastery level so the UI can react.
   */
  execute(verbId: string, correct: boolean, now: Date = new Date()): MasteryLevel {
    const prev = this.repo.getProgress(verbId);
    const next = evaluateMastery(prev, correct, now);
    this.repo.saveProgress(next);
    return next.masteryLevel;
  }

  /** Manual override — used by the Browse "mark as mastered" affordance. */
  setMastery(verbId: string, level: MasteryLevel): void {
    const prev = this.repo.getProgress(verbId);
    this.repo.saveProgress({ ...prev, masteryLevel: level });
  }
}
