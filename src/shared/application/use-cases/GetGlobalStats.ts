import { MasteryLevel } from "@/src/shared/domain/value-objects/MasteryLevel";
import { StudyProgress } from "@/src/shared/domain/entities/StudyProgress";

export interface ModuleStats {
  readonly id: string;
  readonly label: string;
  readonly total: number;
  readonly mastered: number;
  readonly learning: number;
  readonly fresh: number;
}

export interface GlobalStats {
  readonly totalItems: number;
  readonly totalMastered: number;
  readonly totalLearning: number;
  readonly modules: ModuleStats[];
  readonly streakDays: number;
  readonly lastActivityISO: string | null;
}

export interface ModuleSource {
  readonly id: string;
  readonly label: string;
  readonly totalCount: number;
  readonly progress: Record<string, StudyProgress>;
}

export class GetGlobalStats {
  execute(sources: readonly ModuleSource[], today: Date = new Date()): GlobalStats {
    const modules: ModuleStats[] = sources.map((s) => {
      let mastered = 0;
      let learning = 0;
      for (const p of Object.values(s.progress)) {
        if (p.masteryLevel === MasteryLevel.MASTERED) mastered++;
        else if (p.masteryLevel === MasteryLevel.LEARNING) learning++;
      }
      const fresh = Math.max(0, s.totalCount - mastered - learning);
      return {
        id: s.id,
        label: s.label,
        total: s.totalCount,
        mastered,
        learning,
        fresh,
      };
    });

    const totalItems = modules.reduce((a, m) => a + m.total, 0);
    const totalMastered = modules.reduce((a, m) => a + m.mastered, 0);
    const totalLearning = modules.reduce((a, m) => a + m.learning, 0);

    const allDates = sources
      .flatMap((s) => Object.values(s.progress))
      .map((p) => p.lastReviewedAt)
      .filter((d): d is string => Boolean(d))
      .map((iso) => isoDay(new Date(iso)))
      .sort();

    const lastActivityISO = allDates.length === 0 ? null : allDates[allDates.length - 1];
    const streakDays = computeStreak(new Set(allDates), today);

    return {
      totalItems,
      totalMastered,
      totalLearning,
      modules,
      streakDays,
      lastActivityISO,
    };
  }
}

function isoDay(d: Date): string {
  return new Date(d.getFullYear(), d.getMonth(), d.getDate()).toISOString().slice(0, 10);
}

function computeStreak(days: Set<string>, today: Date): number {
  let streak = 0;
  const cursor = new Date(today.getFullYear(), today.getMonth(), today.getDate());
  while (days.has(cursor.toISOString().slice(0, 10))) {
    streak += 1;
    cursor.setDate(cursor.getDate() - 1);
  }
  return streak;
}
