export type Formality = "casual" | "neutral" | "formal";

export interface PhrasalVerbExample {
  readonly en: string;
  readonly es: string;
}

export interface PhrasalVerb {
  readonly id: string;
  readonly verb: string;
  readonly particles: string[];
  readonly baseVerb: string;
  readonly ipa: string;
  readonly meaning: string;
  readonly separable: boolean;
  readonly formality: Formality;
  readonly synonym?: string;
  readonly examples: PhrasalVerbExample[];
}

export function phrasalId(verb: string): string {
  return verb.trim().toLowerCase().replace(/\s+/g, "-");
}
