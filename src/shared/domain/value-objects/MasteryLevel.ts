export const MasteryLevel = {
  NEW: "NEW",
  LEARNING: "LEARNING",
  MASTERED: "MASTERED",
} as const;

export type MasteryLevel = (typeof MasteryLevel)[keyof typeof MasteryLevel];

export const ALL_MASTERY_LEVELS: readonly MasteryLevel[] = [
  MasteryLevel.NEW,
  MasteryLevel.LEARNING,
  MasteryLevel.MASTERED,
];

export function nextMasteryLevel(current: MasteryLevel, correct: boolean): MasteryLevel {
  if (correct) {
    if (current === MasteryLevel.NEW) return MasteryLevel.LEARNING;
    if (current === MasteryLevel.LEARNING) return MasteryLevel.MASTERED;
    return MasteryLevel.MASTERED;
  }
  if (current === MasteryLevel.MASTERED) return MasteryLevel.LEARNING;
  return MasteryLevel.LEARNING;
}
