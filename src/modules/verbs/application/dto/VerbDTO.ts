import { Verb } from "../../domain/entities/Verb";
import { ConjugationForm } from "../../domain/value-objects/Conjugation";
import { MasteryLevel } from "@/src/shared/domain/value-objects/MasteryLevel";
import { StudyProgress } from "@/src/shared/domain/entities/StudyProgress";

export interface VerbFormDTO {
  readonly form: ConjugationForm;
  readonly label: string;
  readonly text: string;
  readonly ipa: string;
  readonly speechText: string;
}

export interface VerbDTO {
  readonly id: string;
  readonly categoryId: string;
  readonly categoryName: string;
  readonly categoryIcon: string;
  readonly spanishMeaning: string;
  readonly forms: VerbFormDTO[];
  readonly masteryLevel: MasteryLevel;
  readonly lastReviewedAt: string | null;
  readonly totalReviews: number;
}

const FORM_LABELS: Record<ConjugationForm, string> = {
  infinitive: "Infinitive",
  thirdPerson: "Third person",
  pastSimple: "Past simple",
  pastParticiple: "Past participle",
  gerund: "Gerund",
};

export function toVerbDTO(verb: Verb, progress: StudyProgress): VerbDTO {
  const c = verb.conjugation;
  const forms: VerbFormDTO[] = [
    formDTO("infinitive", c.infinitive.text, c.infinitive.pronunciation.ipa, c.infinitive.pronunciation.speechOverride),
    formDTO("thirdPerson", c.thirdPerson.text, c.thirdPerson.pronunciation.ipa, c.thirdPerson.pronunciation.speechOverride),
    formDTO("pastSimple", c.pastSimple.text, c.pastSimple.pronunciation.ipa, c.pastSimple.pronunciation.speechOverride),
    formDTO("pastParticiple", c.pastParticiple.text, c.pastParticiple.pronunciation.ipa, c.pastParticiple.pronunciation.speechOverride),
    formDTO("gerund", c.gerund.text, c.gerund.pronunciation.ipa, c.gerund.pronunciation.speechOverride),
  ];

  return {
    id: verb.id,
    categoryId: verb.category.id,
    categoryName: verb.category.name,
    categoryIcon: verb.category.icon,
    spanishMeaning: verb.spanishMeaning,
    forms,
    masteryLevel: progress.masteryLevel,
    lastReviewedAt: progress.lastReviewedAt,
    totalReviews: progress.totalReviews,
  };
}

function formDTO(
  form: ConjugationForm,
  text: string,
  ipa: string,
  override: string | undefined,
): VerbFormDTO {
  return {
    form,
    label: FORM_LABELS[form],
    text,
    ipa,
    speechText: override ?? text,
  };
}
