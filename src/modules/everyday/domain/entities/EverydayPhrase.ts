export type Register = "informal" | "casual" | "slang";
export type PhraseFunction = "hedging" | "filler" | "connector" | "softener";

export interface EverydayExample {
  readonly en: string;
  readonly es: string;
  readonly context: string;
}

export interface EverydayPhrase {
  readonly id: string;
  readonly phrase: string;
  readonly ipa?: string;
  readonly formalEquivalent: string;
  readonly meaning: string;
  readonly register: Register;
  readonly function: PhraseFunction;
  readonly examples: EverydayExample[];
  readonly notes?: string;
}

export function everydayId(phrase: string): string {
  return phrase.trim().toLowerCase().replace(/\s+/g, "-").replace(/'/g, "");
}
