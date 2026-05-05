
import { cn } from "@/src/lib/utils";

export interface CategoryTab {
  id: string;
  label: string;
  count: number;
}

interface Props {
  tabs: CategoryTab[];
  active: string;
  onChange: (id: string) => void;
}

export function CategoryTabs({ tabs, active, onChange }: Props) {
  return (
    <div
      role="tablist"
      className="flex gap-1 overflow-x-auto -mx-2 px-2 py-1"
    >
      {tabs.map((t) => {
        const isActive = t.id === active;
        return (
          <button
            key={t.id}
            type="button"
            role="tab"
            aria-selected={isActive}
            onClick={() => onChange(t.id)}
            className={cn(
              "shrink-0 px-3 py-2 text-sm rounded-sm transition-colors flex items-baseline gap-2",
              isActive
                ? "bg-ink text-paper"
                : "text-ink-muted hover:text-ink hover:bg-paper-deep",
            )}
          >
            <span>{t.label}</span>
            <span
              className={cn(
                "font-mono text-[10px] tnum",
                isActive ? "text-paper/60" : "text-ink-faint",
              )}
            >
              {t.count}
            </span>
          </button>
        );
      })}
    </div>
  );
}
