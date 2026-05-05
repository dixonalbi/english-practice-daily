import { Pronunciation } from "./Pronunciation";

export type ConjugationForm =
  | "infinitive"
  | "thirdPerson"
  | "pastSimple"
  | "pastParticiple"
  | "gerund";

export interface ConjugatedForm {
  readonly form: ConjugationForm;
  readonly text: string;
  readonly pronunciation: Pronunciation;
}

export interface Conjugation {
  readonly infinitive: ConjugatedForm;
  readonly thirdPerson: ConjugatedForm;
  readonly pastSimple: ConjugatedForm;
  readonly pastParticiple: ConjugatedForm;
  readonly gerund: ConjugatedForm;
}

export const ALL_CONJUGATION_FORMS: readonly ConjugationForm[] = [
  "infinitive",
  "thirdPerson",
  "pastSimple",
  "pastParticiple",
  "gerund",
];

export function getForm(c: Conjugation, form: ConjugationForm): ConjugatedForm {
  return c[form];
}
