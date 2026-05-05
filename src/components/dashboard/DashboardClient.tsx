
import { Link } from "@tanstack/react-router";
import { motion } from "motion/react";
import { ArrowUpRight } from "lucide-react";
import { container } from "@/src/lib/di/container";
import { GlobalStats, ModuleSource } from "@/src/shared/application/use-cases/GetGlobalStats";
import { ProgressBar } from "@/src/components/learning/ProgressBar";
import { useReactiveSnapshot } from "@/src/lib/hooks/useReactiveSnapshot";
import { pct } from "@/src/lib/utils";

const FALLBACK_STATS: GlobalStats = {
  totalItems: 0,
  totalMastered: 0,
  totalLearning: 0,
  modules: [],
  streakDays: 0,
  lastActivityISO: null,
};

function readStats(): GlobalStats {
  const verbsRepo = container.verbs.repository;
  const prepRepo = container.prepositions.repository;
  const phrasalRepo = container.phrasalVerbs.repository;
  const everydayRepo = container.everyday.repository;

  const sources: ModuleSource[] = [
    {
      id: "verbs",
      label: "Verbs",
      totalCount: verbsRepo.getAll().length,
      progress: verbsRepo.getAllProgress(),
    },
    {
      id: "prepositions",
      label: "Prepositions",
      totalCount: prepRepo.getAll().length,
      progress: prepRepo.getAllProgress(),
    },
    {
      id: "phrasal-verbs",
      label: "Phrasal verbs",
      totalCount: phrasalRepo.getAll().length,
      progress: phrasalRepo.getAllProgress(),
    },
    {
      id: "everyday",
      label: "Everyday",
      totalCount: everydayRepo.getAll().length,
      progress: everydayRepo.getAllProgress(),
    },
  ];
  return container.shared.useCases.globalStats().execute(sources);
}

export function DashboardClient() {
  const stats = useReactiveSnapshot(readStats, FALLBACK_STATS);

  const meta: Record<string, { href: string; description: string; number: string }> = {
    verbs: {
      href: "/verbs",
      description: "Conjugations, tenses, IPA — the load-bearing backbone of speech.",
      number: "01",
    },
    prepositions: {
      href: "/prepositions",
      description: "The tiny words that decide whether you sound native or translated.",
      number: "02",
    },
    "phrasal-verbs": {
      href: "/phrasal-verbs",
      description: "Verb + particle. Where conversational English really lives.",
      number: "03",
    },
    everyday: {
      href: "/everyday",
      description: "Filler, hedges, contractions — the texture of spoken English.",
      number: "04",
    },
  };

  return (
    <div className="mx-auto max-w-6xl px-6">
      {/* Hero */}
      <section className="pt-20 md:pt-28 pb-20 grid md:grid-cols-12 gap-8 md:gap-12 items-end">
        <div className="md:col-span-8">
          <p className="eyebrow mb-6">
            <span className="text-accent">●</span>
            <span className="ms-2">Volume I — A study companion</span>
          </p>
          <motion.h1
            initial={{ y: 8, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.5, ease: [0.22, 0.61, 0.36, 1] }}
            className="display text-[clamp(2.6rem,7vw,5.4rem)] leading-[0.95] tracking-tight"
          >
            English,{" "}
            <em className="italic text-accent" style={{ fontStyle: "italic" }}>
              practised
            </em>
            <br />
            with patience.
          </motion.h1>
          <p className="mt-8 max-w-xl text-[17px] leading-relaxed text-ink-muted">
            Four chapters of focused drilling — verbs, prepositions, phrasal
            verbs, and the everyday filler that fluent speakers lean on. No
            accounts. No noise. Your progress lives on this device.
          </p>
        </div>

        <div className="md:col-span-4 border-t md:border-t-0 md:border-l border-rule md:ps-10 pt-8 md:pt-0">
          <Stat label="Items in library" value={stats.totalItems} />
          <Stat label="Mastered" value={stats.totalMastered} />
          <Stat label="In progress" value={stats.totalLearning} />
          <Stat label="Streak" value={`${stats.streakDays} days`} />
        </div>
      </section>

      <div className="border-t border-rule" />

      {/* Modules */}
      <section className="py-20">
        <div className="flex items-baseline justify-between mb-12">
          <h2 className="display text-3xl tracking-tight">The four chapters</h2>
          <span className="eyebrow tnum">04 modules</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-px bg-rule">
          {(stats.modules.length > 0 ? stats.modules : placeholderModules()).map((m) => {
            const info = meta[m.id]!;
            const completion = pct(m.mastered, m.total || 1);
            return (
              <Link
                key={m.id}
                to={info.href}
                className="group bg-paper-card p-8 md:p-10 transition-colors hover:bg-paper-deep"
              >
                <div className="flex items-start justify-between mb-10">
                  <span className="font-mono text-xs tnum text-ink-faint">
                    {info.number}
                  </span>
                  <ArrowUpRight
                    size={16}
                    className="text-ink-faint group-hover:text-accent group-hover:rotate-12 transition-all"
                  />
                </div>
                <h3 className="display text-3xl md:text-4xl mb-4 tracking-tight leading-[1.05]">
                  {m.label}
                </h3>
                <p className="text-sm text-ink-muted leading-relaxed mb-8 max-w-md">
                  {info.description}
                </p>
                <ProgressBar total={m.total} mastered={m.mastered} learning={m.learning} />
                <div className="mt-4 flex items-baseline justify-between font-mono text-[11px] tnum text-ink-muted">
                  <span>
                    {m.mastered} / {m.total} mastered
                  </span>
                  <span>{completion}%</span>
                </div>
              </Link>
            );
          })}
        </div>
      </section>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: number | string }) {
  return (
    <div className="border-b border-rule last:border-b-0 py-3 first:pt-0">
      <div className="flex items-baseline justify-between">
        <span className="eyebrow">{label}</span>
        <span className="display text-3xl tnum tabular-nums">{value}</span>
      </div>
    </div>
  );
}

function placeholderModules() {
  return [
    { id: "verbs", label: "Verbs", total: 0, mastered: 0, learning: 0, fresh: 0 },
    { id: "prepositions", label: "Prepositions", total: 0, mastered: 0, learning: 0, fresh: 0 },
    { id: "phrasal-verbs", label: "Phrasal verbs", total: 0, mastered: 0, learning: 0, fresh: 0 },
    { id: "everyday", label: "Everyday", total: 0, mastered: 0, learning: 0, fresh: 0 },
  ];
}
