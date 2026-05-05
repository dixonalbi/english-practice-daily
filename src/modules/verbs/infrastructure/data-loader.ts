import { Verb, VerbCategory, verbId } from "../domain/entities/Verb";
import { Conjugation } from "../domain/value-objects/Conjugation";
import { pronunciationOf } from "../domain/value-objects/Pronunciation";
import rawData from "@/src/data/verbs-data.json";

interface RawVerb {
  i: string;
  ip: string;
  sp: string;
  p: string;
  pi: string;
  pSp?: string;
  pp: string;
  ppi: string;
  ppSp?: string;
  g: string;
  gi: string;
  t: string;
  ti: string;
}

interface RawCategory {
  id: string;
  name: string;
  icon: string;
  verbs: RawVerb[];
}

interface RawData {
  fields: Record<string, string>;
  categories: RawCategory[];
}

const data = rawData as RawData;

function buildConjugation(r: RawVerb): Conjugation {
  return {
    infinitive: {
      form: "infinitive",
      text: r.i,
      pronunciation: pronunciationOf(r.ip),
    },
    thirdPerson: {
      form: "thirdPerson",
      text: r.t,
      pronunciation: pronunciationOf(r.ti),
    },
    pastSimple: {
      form: "pastSimple",
      text: r.p,
      pronunciation: pronunciationOf(r.pi, r.pSp),
    },
    pastParticiple: {
      form: "pastParticiple",
      text: r.pp,
      pronunciation: pronunciationOf(r.ppi, r.ppSp),
    },
    gerund: {
      form: "gerund",
      text: r.g,
      pronunciation: pronunciationOf(r.gi),
    },
  };
}

export function loadVerbs(): { verbs: Verb[]; categories: VerbCategory[] } {
  const categories: VerbCategory[] = data.categories.map((c) => ({
    id: c.id,
    name: c.name,
    icon: c.icon,
  }));

  const verbs: Verb[] = data.categories.flatMap((c) =>
    c.verbs.map<Verb>((r) => ({
      id: verbId(r.i),
      category: { id: c.id, name: c.name, icon: c.icon },
      spanishMeaning: r.sp,
      conjugation: buildConjugation(r),
    })),
  );

  return { verbs, categories };
}
