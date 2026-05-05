import { Link } from "@tanstack/react-router";
import { Layers, Repeat2, ListChecks, Headphones, Pencil } from "lucide-react";
import { PracticeModeCard } from "@/src/components/learning/PracticeModeCard";

export function VerbsPracticePicker() {
  return (
    <div className="mx-auto max-w-6xl px-6 pt-12 pb-24">
      <div className="grid md:grid-cols-12 gap-8 items-end pb-14 border-b border-rule">
        <div className="md:col-span-8">
          <p className="eyebrow mb-4">
            <Link to="/verbs" className="hover:text-accent">← Verbs</Link>
            <span className="mx-2 text-ink-faint">/</span>
            Practice
          </p>
          <h1 className="display text-[clamp(2.4rem,5vw,4rem)] leading-[0.95] tracking-tight">
            Pick a{" "}
            <em className="italic text-accent" style={{ fontStyle: "italic" }}>
              method.
            </em>
          </h1>
          <p className="mt-6 max-w-xl text-[16px] leading-relaxed text-ink-muted">
            Five lenses on the same vocabulary. Spend ten minutes in any of them
            — the muscle memory is what you&rsquo;re building.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-12">
        <PracticeModeCard
          to="/verbs/practice/flashcard"
          number="01"
          title="Flashcard"
          description="One verb at a time. Flip to reveal Spanish meaning and full conjugation. Spaced by mastery."
          meta="Spaced · Untimed"
          icon={Layers}
        />
        <PracticeModeCard
          to="/verbs/practice/conjugation"
          number="02"
          title="Conjugation drill"
          description="You&rsquo;re given the infinitive and asked for a tense. Type the right form. No half measures."
          meta="Type · Reveal"
          icon={Repeat2}
        />
        <PracticeModeCard
          number="03"
          title="Quiz"
          description="Ten multiple-choice questions per session. Score at the end."
          meta="Coming next"
          icon={ListChecks}
          disabled
        />
        <PracticeModeCard
          number="04"
          title="Type-it"
          description="Hear the verb, type what you heard. Rebuilds the audio bridge."
          meta="Coming next"
          icon={Pencil}
          disabled
        />
        <PracticeModeCard
          number="05"
          title="Listen"
          description="Audio comes first. Identify the verb you heard among four options."
          meta="Coming next"
          icon={Headphones}
          disabled
        />
      </div>
    </div>
  );
}
