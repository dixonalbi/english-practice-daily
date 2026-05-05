
import { useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import { Link } from "@tanstack/react-router";
import { ArrowLeft, Check, X, RotateCw, ArrowRight } from "lucide-react";
import { motion, AnimatePresence } from "motion/react";
import { container } from "@/src/lib/di/container";
import { VerbDTO, VerbFormDTO } from "@/src/modules/verbs/application/dto/VerbDTO";
import { ConjugationForm } from "@/src/modules/verbs/domain/value-objects/Conjugation";
import { Input } from "@/src/components/ui/Input";
import { Button } from "@/src/components/ui/Button";
import { PronunciationButton } from "@/src/components/learning/PronunciationButton";

const DRILL_SIZE = 10;
const noopSubscribe = () => () => {};

/** seed is unused at runtime but acts as the cache-bust token for useMemo. */
function buildSession(isClient: boolean, seed: number): Question[] {
  if (!isClient) return [];
  void seed;
  const session = container.verbs.useCases.startSession().execute({
    mode: "conjugation",
    prioritizeWeak: true,
    limit: DRILL_SIZE,
  });
  return buildQuestions(session.verbs);
}

type Question = {
  verb: VerbDTO;
  target: VerbFormDTO;
};

const TARGETABLE: ConjugationForm[] = [
  "thirdPerson",
  "pastSimple",
  "pastParticiple",
  "gerund",
];

function buildQuestions(verbs: VerbDTO[]): Question[] {
  return verbs.map((verb) => {
    const targetForm = TARGETABLE[Math.floor(Math.random() * TARGETABLE.length)];
    const target = verb.forms.find((f) => f.form === targetForm)!;
    return { verb, target };
  });
}

function normalize(s: string): string {
  return s.trim().toLowerCase();
}

function isCorrect(input: string, expected: string): boolean {
  const opts = expected.split(/[\/]| or /).map((p) => normalize(p));
  return opts.some((o) => o === normalize(input));
}

export function ConjugationDrill() {
  const isClient = useSyncExternalStore(
    noopSubscribe,
    () => true,
    () => false,
  );

  const [seed, setSeed] = useState(0);
  const [index, setIndex] = useState(0);
  const [input, setInput] = useState("");
  const [reveal, setReveal] = useState<null | "correct" | "wrong">(null);
  const [score, setScore] = useState({ correct: 0, wrong: 0 });
  const inputRef = useRef<HTMLInputElement>(null);

  const questions = useMemo<Question[]>(
    () => buildSession(isClient, seed),
    [isClient, seed],
  );

  function start() {
    setSeed((s) => s + 1);
    setIndex(0);
    setInput("");
    setReveal(null);
    setScore({ correct: 0, wrong: 0 });
  }

  useEffect(() => {
    inputRef.current?.focus();
  }, [index, reveal]);

  const current = questions[index];
  const finished = questions.length > 0 && index >= questions.length;

  function submit(e: React.FormEvent) {
    e.preventDefault();
    if (!current || reveal) return;
    const correct = isCorrect(input, current.target.text);
    container.verbs.useCases.updateMastery().execute(current.verb.id, correct);
    setReveal(correct ? "correct" : "wrong");
    setScore((s) => ({
      correct: s.correct + (correct ? 1 : 0),
      wrong: s.wrong + (correct ? 0 : 1),
    }));
  }

  function next() {
    setReveal(null);
    setInput("");
    setIndex((i) => i + 1);
  }

  const infinitive = useMemo(
    () => current?.verb.forms.find((f) => f.form === "infinitive"),
    [current],
  );

  if (questions.length === 0) {
    return <div className="mx-auto max-w-2xl px-6 py-24 text-center text-ink-muted">Loading…</div>;
  }

  if (finished) {
    const total = score.correct + score.wrong;
    const pct = total === 0 ? 0 : Math.round((score.correct / total) * 100);
    return (
      <div className="mx-auto max-w-xl px-6 py-24 text-center">
        <p className="eyebrow mb-6">Drill complete</p>
        <h2 className="display text-7xl tracking-tight mb-2 tnum">{pct}%</h2>
        <p className="text-ink-muted mb-10">
          {score.correct} correct · {score.wrong} wrong · {total} total
        </p>
        <div className="flex gap-3 justify-center">
          <Button onClick={start}>
            <RotateCw size={14} /> Again
          </Button>
          <Link
            to="/verbs"
            className="inline-flex items-center justify-center gap-2 h-10 px-4 text-sm bg-paper-card text-ink border border-rule-strong hover:border-ink transition-colors"
          >
            Library
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-3xl px-6 pt-10 pb-24">
      <div className="flex items-center justify-between mb-10">
        <Link
          to="/verbs/practice"
          className="text-sm text-ink-muted hover:text-ink inline-flex items-center gap-1"
        >
          <ArrowLeft size={14} /> Practice
        </Link>
        <p className="font-mono text-sm tnum text-ink-muted">
          {String(index + 1).padStart(2, "0")}
          <span className="text-ink-faint"> / {String(questions.length).padStart(2, "0")}</span>
        </p>
      </div>

      <p className="eyebrow mb-2">{labelOf(current!.target.form)}</p>
      <div className="flex items-center gap-3 mb-10">
        <h2 className="display text-[clamp(2.5rem,7vw,4.5rem)] leading-none tracking-tight">
          {infinitive?.text}
        </h2>
        <span className="font-mono text-sm text-ink-muted">{infinitive?.ipa}</span>
        {infinitive && <PronunciationButton text={infinitive.speechText} />}
      </div>

      <p className="text-ink-muted mb-6 italic">{current!.verb.spanishMeaning}</p>

      <form onSubmit={submit} className="space-y-4">
        <Input
          ref={inputRef}
          autoComplete="off"
          autoCorrect="off"
          spellCheck={false}
          placeholder={`Type the ${labelOf(current!.target.form).toLowerCase()}…`}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={Boolean(reveal)}
          className="text-2xl h-16 font-display"
        />
        <div className="flex gap-3">
          {!reveal ? (
            <Button type="submit" disabled={!input.trim()}>
              <Check size={14} /> Check
            </Button>
          ) : (
            <Button type="button" onClick={next} variant="primary">
              Next <ArrowRight size={14} />
            </Button>
          )}
          <span className="ms-auto font-mono text-sm tnum text-ink-muted self-center">
            <span className="text-mastery-mastered">{score.correct}</span>
            <span className="text-ink-faint mx-2">/</span>
            <span className="text-mastery-learning">{score.wrong}</span>
          </span>
        </div>
      </form>

      <AnimatePresence>
        {reveal && (
          <motion.div
            key={reveal + index}
            initial={{ y: 8, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.25 }}
            className="mt-8 border border-rule rounded-sm bg-paper-card p-6"
          >
            <p
              className="eyebrow mb-3"
              style={{
                color:
                  reveal === "correct"
                    ? "var(--color-mastery-mastered)"
                    : "var(--color-mastery-learning)",
              }}
            >
              {reveal === "correct" ? (
                <>
                  <Check size={11} className="inline -mt-0.5 me-1" /> Correct
                </>
              ) : (
                <>
                  <X size={11} className="inline -mt-0.5 me-1" /> Not quite
                </>
              )}
            </p>
            <p className="text-sm text-ink-muted mb-2">Expected:</p>
            <div className="flex items-baseline gap-3">
              <span className="display text-3xl">{current!.target.text}</span>
              <span className="font-mono text-xs text-ink-muted">
                {current!.target.ipa}
              </span>
              <PronunciationButton text={current!.target.speechText} />
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

function labelOf(form: ConjugationForm): string {
  switch (form) {
    case "thirdPerson":
      return "Third person";
    case "pastSimple":
      return "Past simple";
    case "pastParticiple":
      return "Past participle";
    case "gerund":
      return "Gerund (-ing)";
    default:
      return "Form";
  }
}
