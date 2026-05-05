import {
  MasteryLevel,
  nextMasteryLevel,
} from "@/src/shared/domain/value-objects/MasteryLevel";
import {
  StudyProgress,
  recordReview,
} from "@/src/shared/domain/entities/StudyProgress";

const STREAK_TO_MASTER = 3;

/**
 * Pure domain rules for advancing mastery from a single review outcome.
 * - Two correct in a row promotes NEW → LEARNING.
 * - Three correct in a row from LEARNING promotes to MASTERED.
 * - Any incorrect drops MASTERED back to LEARNING and resets the streak.
 */
export function evaluateMastery(
  prev: StudyProgress,
  correct: boolean,
  now: Date,
): StudyProgress {
  const reviewed = recordReview(prev, correct, now);

  if (!correct) {
    return {
      ...reviewed,
      masteryLevel:
        prev.masteryLevel === MasteryLevel.MASTERED
          ? MasteryLevel.LEARNING
          : prev.masteryLevel === MasteryLevel.NEW
            ? MasteryLevel.LEARNING
            : MasteryLevel.LEARNING,
    };
  }

  if (prev.masteryLevel === MasteryLevel.LEARNING && reviewed.correctStreak >= STREAK_TO_MASTER) {
    return { ...reviewed, masteryLevel: MasteryLevel.MASTERED };
  }

  if (prev.masteryLevel === MasteryLevel.NEW) {
    return { ...reviewed, masteryLevel: nextMasteryLevel(prev.masteryLevel, true) };
  }

  return { ...reviewed, masteryLevel: prev.masteryLevel };
}
