import { cn } from "@/src/lib/utils";
import { MasteryLevel } from "@/src/shared/domain/value-objects/MasteryLevel";

export function MasteryDot({ level, className }: { level: MasteryLevel; className?: string }) {
  const color =
    level === "MASTERED"
      ? "bg-mastery-mastered"
      : level === "LEARNING"
        ? "bg-mastery-learning"
        : "bg-mastery-new/60 ring-1 ring-mastery-new ring-inset";
  return (
    <span
      aria-hidden
      className={cn("inline-block h-2 w-2 rounded-full", color, className)}
    />
  );
}

export function MasteryLabel({ level }: { level: MasteryLevel }) {
  const text =
    level === "MASTERED" ? "Mastered" : level === "LEARNING" ? "Learning" : "Untouched";
  const color =
    level === "MASTERED"
      ? "text-mastery-mastered"
      : level === "LEARNING"
        ? "text-mastery-learning"
        : "text-ink-muted";
  return (
    <span className={cn("eyebrow tnum", color)}>
      <MasteryDot level={level} className="me-2 align-middle" />
      {text}
    </span>
  );
}
