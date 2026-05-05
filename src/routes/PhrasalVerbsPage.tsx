import { ModuleStub } from "@/src/components/shared/ModuleStub";
import { container } from "@/src/lib/di/container";

export function PhrasalVerbsPage() {
  const all = container.phrasalVerbs.repository.getAll();
  const items = all.slice(0, 8).map((p) => ({
    id: p.id,
    primary: p.verb,
    secondary: p.ipa,
    meaning: p.meaning,
    speechText: p.verb,
    meta: `${p.formality.toUpperCase()} · ${p.synonym ?? "—"}`,
  }));

  return (
    <ModuleStub
      chapterNumber="03"
      chapterName="Phrasal verbs"
      display="Verb plus particle,"
      italic="meaning multiplied."
      description="Where conversational English really lives. Each phrasal carries a register cue — casual, neutral, formal — and a single-word formal twin worth knowing."
      items={items}
      count={all.length}
    />
  );
}
