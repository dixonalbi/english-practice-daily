import { cn } from "@/src/lib/utils";

interface Props {
  total: number;
  mastered: number;
  learning: number;
  className?: string;
}

export function ProgressBar({ total, mastered, learning, className }: Props) {
  const masteredPct = total === 0 ? 0 : (mastered / total) * 100;
  const learningPct = total === 0 ? 0 : (learning / total) * 100;

  return (
    <div
      className={cn("relative h-1.5 w-full bg-paper-deep rounded-full overflow-hidden", className)}
      role="progressbar"
      aria-valuenow={mastered}
      aria-valuemax={total}
    >
      <div
        className="absolute inset-y-0 left-0 bg-mastery-mastered transition-[width] duration-500"
        style={{ width: `${masteredPct}%` }}
      />
      <div
        className="absolute inset-y-0 bg-mastery-learning/70 transition-[width] duration-500"
        style={{ left: `${masteredPct}%`, width: `${learningPct}%` }}
      />
    </div>
  );
}
