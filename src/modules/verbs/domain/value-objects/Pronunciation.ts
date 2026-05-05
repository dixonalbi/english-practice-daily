export interface Pronunciation {
  readonly ipa: string;
  readonly speechOverride?: string;
}

export function pronunciationOf(ipa: string, speechOverride?: string): Pronunciation {
  return { ipa, speechOverride };
}
