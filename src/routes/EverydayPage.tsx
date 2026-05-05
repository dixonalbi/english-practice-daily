import { ModuleStub } from "@/src/components/shared/ModuleStub";
import { container } from "@/src/lib/di/container";

export function EverydayPage() {
  const all = container.everyday.repository.getAll();
  const items = all.slice(0, 8).map((p) => ({
    id: p.id,
    primary: p.phrase,
    secondary: p.ipa,
    meaning: `${p.meaning} — formal: ${p.formalEquivalent}`,
    speechText: p.phrase,
    meta: `${p.register.toUpperCase()} · ${p.function}`,
  }));

  return (
    <ModuleStub
      chapterNumber="04"
      chapterName="Everyday"
      display="The texture"
      italic="of spoken English."
      description="Filler, hedges, contractions — kinda, gonna, you know, by the way. The bits that fluent speakers lean on but textbooks rarely teach."
      items={items}
      count={all.length}
    />
  );
}
