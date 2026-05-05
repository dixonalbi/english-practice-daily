import { Conjugation } from "../value-objects/Conjugation";

export interface VerbCategory {
  readonly id: string;
  readonly name: string;
  readonly icon: string;
}

export interface Verb {
  readonly id: string;
  readonly category: VerbCategory;
  readonly spanishMeaning: string;
  readonly conjugation: Conjugation;
}

export function verbId(infinitive: string): string {
  return infinitive.trim().toLowerCase().replace(/\s+/g, "-");
}
