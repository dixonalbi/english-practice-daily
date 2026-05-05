
import { Link } from "@tanstack/react-router";
import { motion } from "motion/react";
import { PronunciationButton } from "@/src/components/learning/PronunciationButton";

interface StubItem {
  id: string;
  primary: string;
  secondary?: string;
  meaning: string;
  speechText: string;
  meta?: string;
}

interface Props {
  chapterNumber: string;
  chapterName: string;
  display: string;
  italic: string;
  description: string;
  items: StubItem[];
  count: number;
}

export function ModuleStub({
  chapterNumber,
  chapterName,
  display,
  italic,
  description,
  items,
  count,
}: Props) {
  return (
    <div className="mx-auto max-w-6xl px-6 pt-12 pb-24">
      <div className="grid md:grid-cols-12 gap-8 items-end pb-10 border-b border-rule">
        <div className="md:col-span-8">
          <p className="eyebrow mb-4">
            Chapter {chapterNumber} — {chapterName}
            <span className="mx-2 text-ink-faint">/</span>
            <Link to="/" className="hover:text-accent">
              Index
            </Link>
          </p>
          <h1 className="display text-[clamp(2.4rem,5vw,4rem)] leading-[0.95] tracking-tight">
            {display}
            <br />
            <em className="italic text-accent" style={{ fontStyle: "italic" }}>
              {italic}
            </em>
          </h1>
          <p className="mt-6 max-w-xl text-[16px] leading-relaxed text-ink-muted">
            {description}
          </p>
        </div>
        <div className="md:col-span-4 md:text-right">
          <span className="font-mono text-5xl tnum text-ink">
            {String(count).padStart(2, "0")}
          </span>
          <p className="eyebrow mt-2">items in this chapter</p>
        </div>
      </div>

      <div className="mt-10">
        <p className="eyebrow mb-6">Sample entries · placeholder</p>
        <div className="divide-y divide-rule border-y border-rule">
          {items.map((it, i) => (
            <motion.div
              key={it.id}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: i * 0.04 }}
              className="py-6 grid grid-cols-12 gap-4 items-baseline"
            >
              <span className="col-span-1 font-mono text-[11px] tnum text-ink-faint">
                {String(i + 1).padStart(3, "0")}
              </span>
              <div className="col-span-11 md:col-span-5">
                <div className="flex items-baseline gap-3 flex-wrap">
                  <span className="display text-2xl tracking-tight leading-none">
                    {it.primary}
                  </span>
                  {it.secondary && (
                    <span className="font-mono text-xs text-ink-muted">
                      {it.secondary}
                    </span>
                  )}
                  <PronunciationButton text={it.speechText} />
                </div>
                <p className="text-sm text-ink-muted mt-1 italic">{it.meaning}</p>
              </div>
              <div className="col-span-12 md:col-span-6 md:text-right">
                {it.meta && <span className="eyebrow">{it.meta}</span>}
              </div>
            </motion.div>
          ))}
        </div>

        <div className="mt-12 max-w-md">
          <p className="eyebrow mb-3">Coming next</p>
          <p className="text-sm text-ink-muted leading-relaxed">
            Practice modes and the full corpus arrive once the verbs chapter is
            road-tested. The architecture is in place — see{" "}
            <Link to="/" className="underline underline-offset-2 hover:text-accent">
              the index
            </Link>{" "}
            for progress.
          </p>
        </div>
      </div>
    </div>
  );
}
