
import { useMemo, useState, useSyncExternalStore } from "react";
import { Link } from "@tanstack/react-router";
import { ArrowLeft, ArrowRight, Check, X, RotateCw } from "lucide-react";
import { container } from "@/src/lib/di/container";
import { VerbDTO } from "@/src/modules/verbs/application/dto/VerbDTO";
import { FlashCard } from "@/src/components/learning/FlashCard";
import { PronunciationButton } from "@/src/components/learning/PronunciationButton";
import { Button } from "@/src/components/ui/Button";
import { MasteryLabel } from "@/src/components/ui/Pill";

const SESSION_SIZE = 12;

const noopSubscribe = () => () => {};

/** seed is unused at runtime but acts as the cache-bust token for useMemo. */
function buildDeck(isClient: boolean, seed: number): VerbDTO[] {
  if (!isClient) return [];
  void seed;
  return container.verbs.useCases.startSession().execute({
    mode: "flashcard",
    prioritizeWeak: true,
    limit: SESSION_SIZE,
  }).verbs;
}

export function FlashcardSession() {
  const isClient = useSyncExternalStore(
    noopSubscribe,
    () => true,
    () => false,
  );

  const [seed, setSeed] = useState(0);
  const [index, setIndex] = useState(0);

  const deck = useMemo<VerbDTO[]>(
    () => buildDeck(isClient, seed),
    [isClient, seed],
  );

  function start() {
    setSeed((s) => s + 1);
    setIndex(0);
  }

  const current = deck[index];

  function rate(correct: boolean) {
    if (!current) return;
    container.verbs.useCases.updateMastery().execute(current.id, correct);
    if (index < deck.length - 1) {
      setIndex((i) => i + 1);
    } else {
      setIndex(deck.length); // finished
    }
  }

  const finished = deck.length > 0 && index >= deck.length;

  const front = useMemo(() => {
    if (!current) return null;
    const inf = current.forms.find((f) => f.form === "infinitive")!;
    return (
      <div className="text-center">
        <p className="eyebrow mb-8">{current.categoryName}</p>
        <h2 className="display text-[clamp(3rem,8vw,5.5rem)] leading-none tracking-tight mb-6">
          {inf.text}
        </h2>
        <p className="font-mono text-sm text-ink-muted mb-8">{inf.ipa}</p>
        <div className="flex justify-center">
          <PronunciationButton text={inf.speechText} size="md" />
        </div>
      </div>
    );
  }, [current]);

  const back = useMemo(() => {
    if (!current) return null;
    return (
      <div>
        <p className="eyebrow mb-6 text-center">Conjugation</p>
        <p className="text-center text-lg italic text-ink-muted mb-8">
          {current.spanishMeaning}
        </p>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-px bg-rule rounded-sm overflow-hidden border border-rule">
          {current.forms.map((f) => (
            <div key={f.form} className="bg-paper-card p-4 text-center">
              <p className="eyebrow mb-2">{f.label}</p>
              <p className="display text-xl leading-tight">{f.text}</p>
              <p className="font-mono text-[10px] text-ink-muted mt-1">{f.ipa}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }, [current]);

  if (deck.length === 0) {
    return <div className="mx-auto max-w-2xl px-6 py-24 text-center text-ink-muted">Loading…</div>;
  }

  if (finished) {
    return (
      <div className="mx-auto max-w-xl px-6 py-24 text-center">
        <p className="eyebrow mb-6">Session complete</p>
        <h2 className="display text-5xl tracking-tight mb-4">Well done.</h2>
        <p className="text-ink-muted mb-10">
          Your progress has been saved on this device.
        </p>
        <div className="flex gap-3 justify-center">
          <Button onClick={start}>
            <RotateCw size={14} /> New session
          </Button>
          <Link
            to="/verbs"
            className="inline-flex items-center justify-center gap-2 h-10 px-4 text-sm bg-paper-card text-ink border border-rule-strong hover:border-ink transition-colors"
          >
            Back to library
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
          <span className="text-ink-faint"> / {String(deck.length).padStart(2, "0")}</span>
        </p>
      </div>

      <div className="mb-6 flex items-center justify-between">
        <MasteryLabel level={current!.masteryLevel} />
      </div>

      <FlashCard cardKey={current!.id} front={front} back={back} />

      <div className="mt-10 grid grid-cols-2 gap-3 max-w-md mx-auto">
        <Button variant="outline" onClick={() => rate(false)}>
          <X size={14} /> Need review
        </Button>
        <Button variant="primary" onClick={() => rate(true)}>
          <Check size={14} /> Got it
        </Button>
      </div>

      <div className="mt-6 flex justify-center">
        <button
          type="button"
          onClick={() => setIndex((i) => Math.min(i + 1, deck.length))}
          className="text-sm text-ink-muted hover:text-ink inline-flex items-center gap-1 cursor-pointer"
        >
          Skip <ArrowRight size={13} />
        </button>
      </div>
    </div>
  );
}
