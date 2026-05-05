
import { useMemo, useState } from "react";
import { Link } from "@tanstack/react-router";
import { Search, Check, RotateCcw, ChevronDown } from "lucide-react";
import { motion, AnimatePresence } from "motion/react";
import { container } from "@/src/lib/di/container";
import { VerbDTO } from "@/src/modules/verbs/application/dto/VerbDTO";
import { CategoryTabs } from "@/src/components/learning/CategoryTabs";
import { Input } from "@/src/components/ui/Input";
import { Button } from "@/src/components/ui/Button";
import { PronunciationButton } from "@/src/components/learning/PronunciationButton";
import { MasteryDot, MasteryLabel } from "@/src/components/ui/Pill";
import { ProgressBar } from "@/src/components/learning/ProgressBar";
import { MasteryLevel } from "@/src/shared/domain/value-objects/MasteryLevel";
import {
  bumpStore,
  useReactiveSnapshot,
} from "@/src/lib/hooks/useReactiveSnapshot";
import { cn } from "@/src/lib/utils";

type Group = { categoryId: string; categoryName: string; verbs: VerbDTO[] };

const EMPTY_GROUPS: Group[] = [];

function readGroups(): Group[] {
  return container.verbs.useCases
    .getByCategory()
    .execute()
    .map((g) => ({
      categoryId: g.category.id,
      categoryName: g.category.name,
      verbs: g.verbs,
    }));
}

export function VerbsBrowse() {
  const groups = useReactiveSnapshot(readGroups, EMPTY_GROUPS);
  const [active, setActive] = useState<string>("__all__");
  const [query, setQuery] = useState("");
  const [expanded, setExpanded] = useState<string | null>(null);

  const tabs = useMemo(() => {
    const total = groups.reduce((a, g) => a + g.verbs.length, 0);
    return [
      { id: "__all__", label: "All", count: total },
      ...groups.map((g) => ({
        id: g.categoryId,
        label: g.categoryName,
        count: g.verbs.length,
      })),
    ];
  }, [groups]);

  const filtered = useMemo(() => {
    const all =
      active === "__all__"
        ? groups.flatMap((g) => g.verbs)
        : (groups.find((g) => g.categoryId === active)?.verbs ?? []);

    if (!query.trim()) return all;
    const q = query.trim().toLowerCase();
    return all.filter((v) =>
      [v.spanishMeaning, ...v.forms.map((f) => f.text)].some((t) =>
        t.toLowerCase().includes(q),
      ),
    );
  }, [groups, active, query]);

  const stats = useMemo(() => {
    const all = groups.flatMap((g) => g.verbs);
    return {
      total: all.length,
      mastered: all.filter((v) => v.masteryLevel === "MASTERED").length,
      learning: all.filter((v) => v.masteryLevel === "LEARNING").length,
    };
  }, [groups]);

  function cycleMastery(verb: VerbDTO) {
    const next: MasteryLevel =
      verb.masteryLevel === "NEW"
        ? "LEARNING"
        : verb.masteryLevel === "LEARNING"
          ? "MASTERED"
          : "NEW";
    container.verbs.useCases.updateMastery().setMastery(verb.id, next);
    bumpStore();
  }

  function resetAll() {
    if (!confirm("Reset all verb progress on this device?")) return;
    container.verbs.repository.resetProgress();
    bumpStore();
  }

  return (
    <div className="mx-auto max-w-6xl px-6 pt-12 pb-24">
      {/* Header */}
      <div className="grid md:grid-cols-12 gap-8 items-end pb-10">
        <div className="md:col-span-7">
          <p className="eyebrow mb-4">
            Chapter 01 — Verbs
            <span className="mx-2 text-ink-faint">/</span>
            <Link to="/verbs/practice" className="hover:text-accent">
              Practice
            </Link>
          </p>
          <h1 className="display text-[clamp(2.4rem,5vw,4rem)] leading-[0.95] tracking-tight">
            The verb,
            <br />
            <em className="italic text-accent" style={{ fontStyle: "italic" }}>
              conjugated.
            </em>
          </h1>
        </div>
        <div className="md:col-span-5 md:text-right">
          <div className="inline-flex md:flex-col gap-6 md:gap-2 md:items-end items-baseline">
            <span className="font-mono text-5xl tnum text-ink">
              {String(stats.mastered).padStart(2, "0")}
              <span className="text-ink-faint">/{stats.total}</span>
            </span>
            <span className="eyebrow">mastered</span>
          </div>
          <ProgressBar
            className="mt-4"
            total={stats.total}
            mastered={stats.mastered}
            learning={stats.learning}
          />
        </div>
      </div>

      {/* Controls */}
      <div className="sticky top-16 z-10 bg-paper/85 backdrop-blur supports-[backdrop-filter]:bg-paper/60 -mx-6 px-6 py-4 border-y border-rule">
        <div className="flex flex-col md:flex-row gap-3 md:items-center">
          <div className="relative flex-1 min-w-0">
            <Search
              size={14}
              className="absolute left-3 top-1/2 -translate-y-1/2 text-ink-faint"
            />
            <Input
              placeholder="Search by infinitive, conjugation, or Spanish meaning…"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="ps-9"
            />
          </div>
          <div className="flex gap-2">
            <Link
              to="/verbs/practice"
              className="inline-flex items-center justify-center gap-2 h-10 px-4 text-sm bg-ink text-paper hover:bg-ink-soft transition-colors active:translate-y-px"
            >
              Practice
            </Link>
            <Button variant="outline" size="icon" onClick={resetAll} aria-label="Reset progress">
              <RotateCcw size={14} />
            </Button>
          </div>
        </div>
        <div className="mt-3">
          <CategoryTabs tabs={tabs} active={active} onChange={setActive} />
        </div>
      </div>

      {/* List */}
      <div className="divide-y divide-rule mt-2">
        {filtered.length === 0 && (
          <p className="py-16 text-center text-ink-muted">
            Nothing matches that search.
          </p>
        )}
        {filtered.map((v, i) => {
          const isOpen = expanded === v.id;
          const infinitive = v.forms.find((f) => f.form === "infinitive")!;
          return (
            <motion.div
              key={v.id}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: Math.min(i * 0.012, 0.3), duration: 0.25 }}
              className="group"
            >
              <div
                className={cn(
                  "flex items-center gap-3 px-2 -mx-2 py-5 transition-colors rounded-sm",
                  isOpen ? "bg-paper-deep/60" : "hover:bg-paper-deep/40",
                )}
              >
                <button
                  type="button"
                  onClick={() => setExpanded(isOpen ? null : v.id)}
                  className="flex-1 min-w-0 flex items-baseline gap-6 text-left cursor-pointer"
                  aria-expanded={isOpen}
                  aria-label={`Toggle conjugation for ${infinitive.text}`}
                >
                  <span className="font-mono text-[11px] tnum text-ink-faint w-10 shrink-0">
                    {String(i + 1).padStart(3, "0")}
                  </span>

                  <span className="flex-1 min-w-0 block">
                    <span className="flex items-baseline gap-3 flex-wrap">
                      <span
                        className={cn(
                          "display text-2xl md:text-3xl tracking-tight leading-none transition-colors",
                          isOpen
                            ? "text-accent"
                            : "group-hover:text-accent",
                        )}
                      >
                        {infinitive.text}
                      </span>
                      <span className="font-mono text-xs text-ink-muted">
                        {infinitive.ipa}
                      </span>
                      <span
                        className={cn(
                          "eyebrow opacity-0 -translate-x-1 transition-all duration-200",
                          isOpen
                            ? "opacity-100 translate-x-0 text-accent"
                            : "group-hover:opacity-100 group-hover:translate-x-0",
                        )}
                      >
                        {isOpen ? "tap to close" : "tap for tenses"}
                      </span>
                    </span>
                    <span className="block text-sm text-ink-muted mt-1 italic">
                      {v.spanishMeaning}
                    </span>
                  </span>

                  <span className="hidden md:block w-40 shrink-0">
                    <MasteryLabel level={v.masteryLevel} />
                  </span>

                  <span
                    aria-hidden
                    className={cn(
                      "shrink-0 inline-flex items-center justify-center h-7 w-7 rounded-full border border-rule text-ink-muted transition-all duration-300",
                      isOpen
                        ? "rotate-180 border-accent text-accent bg-accent-bg"
                        : "group-hover:border-rule-strong group-hover:text-ink",
                    )}
                  >
                    <ChevronDown size={14} />
                  </span>
                </button>

                <PronunciationButton text={infinitive.speechText} />

                <button
                  type="button"
                  onClick={() => cycleMastery(v)}
                  className={cn(
                    "shrink-0 inline-flex items-center justify-center h-8 w-8 rounded-full border transition-colors cursor-pointer",
                    v.masteryLevel === "MASTERED"
                      ? "bg-mastery-mastered border-mastery-mastered text-paper"
                      : "border-rule-strong text-ink-muted hover:text-accent hover:border-accent",
                  )}
                  aria-label="Cycle mastery"
                >
                  {v.masteryLevel === "MASTERED" ? (
                    <Check size={13} />
                  ) : (
                    <MasteryDot level={v.masteryLevel} />
                  )}
                </button>
              </div>

              <AnimatePresence initial={false}>
                {isOpen && (
                  <motion.div
                    key="details"
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.28, ease: [0.22, 0.61, 0.36, 1] }}
                    className="overflow-hidden"
                  >
                    <div className="ms-16 mb-6 mt-1 grid grid-cols-1 md:grid-cols-5 gap-px bg-rule rounded-sm overflow-hidden border border-rule">
                      {v.forms.map((f) => (
                        <div
                          key={f.form}
                          className="bg-paper-card p-4 flex flex-col gap-1 group/cell hover:bg-paper-deep transition-colors"
                        >
                          <div className="flex items-center justify-between">
                            <span className="eyebrow">{f.label}</span>
                            <PronunciationButton text={f.speechText} size="sm" />
                          </div>
                          <span className="display text-xl mt-2 leading-tight">
                            {f.text}
                          </span>
                          <span className="font-mono text-[11px] text-ink-muted">
                            {f.ipa}
                          </span>
                        </div>
                      ))}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
