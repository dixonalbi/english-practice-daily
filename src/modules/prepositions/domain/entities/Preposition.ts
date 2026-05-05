export type PrepositionUseCategory = "time" | "place" | "movement" | "relation";

export interface PrepositionExample {
  readonly en: string;
  readonly es: string;
}

export interface PrepositionUse {
  readonly category: PrepositionUseCategory;
  readonly rule: string;
  readonly examples: PrepositionExample[];
}

export interface Preposition {
  readonly id: string;
  readonly word: string;
  readonly ipa: string;
  readonly meanings: string[];
  readonly uses: PrepositionUse[];
  readonly commonMistakes?: string[];
}

export function prepositionId(word: string): string {
  return word.trim().toLowerCase().replace(/\s+/g, "-");
}
