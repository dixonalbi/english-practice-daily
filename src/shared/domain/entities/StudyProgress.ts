import { MasteryLevel } from "../value-objects/MasteryLevel";

export interface StudyProgress {
  readonly itemId: string;
  readonly masteryLevel: MasteryLevel;
  readonly lastReviewedAt: string | null;
  readonly correctStreak: number;
  readonly totalReviews: number;
}

export function emptyProgress(itemId: string): StudyProgress {
  return {
    itemId,
    masteryLevel: MasteryLevel.NEW,
    lastReviewedAt: null,
    correctStreak: 0,
    totalReviews: 0,
  };
}

export function recordReview(
  progress: StudyProgress,
  correct: boolean,
  now: Date,
): StudyProgress {
  return {
    ...progress,
    lastReviewedAt: now.toISOString(),
    correctStreak: correct ? progress.correctStreak + 1 : 0,
    totalReviews: progress.totalReviews + 1,
  };
}
