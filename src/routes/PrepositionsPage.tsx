import { ModuleStub } from "@/src/components/shared/ModuleStub";
import { container } from "@/src/lib/di/container";

export function PrepositionsPage() {
  const all = container.prepositions.repository.getAll();
  const items = all.slice(0, 8).map((p) => ({
    id: p.id,
    primary: p.word,
    secondary: p.ipa,
    meaning: p.meanings.join(" · "),
    speechText: p.word,
    meta: p.uses[0]?.category.toUpperCase(),
  }));

  return (
    <ModuleStub
      chapterNumber="02"
      chapterName="Prepositions"
      display="Tiny words,"
      italic="enormous reach."
      description="The prepositions decide whether you sound translated or native. Master the dozen that do most of the work, then add the rest."
      items={items}
      count={all.length}
    />
  );
}
