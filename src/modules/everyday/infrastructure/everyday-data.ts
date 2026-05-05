import { EverydayPhrase, everydayId } from "../domain/entities/EverydayPhrase";

export const EVERYDAY_SEED: EverydayPhrase[] = [
  {
    id: everydayId("kinda"),
    phrase: "kinda",
    ipa: "/ˈkaɪndə/",
    formalEquivalent: "kind of",
    meaning: "más o menos",
    register: "informal",
    function: "hedging",
    examples: [
      { en: "I'm kinda tired.", es: "Estoy más o menos cansado.", context: "casual chat" },
    ],
    notes: "Muy común al hablar; evitar en escritura formal.",
  },
  {
    id: everydayId("gonna"),
    phrase: "gonna",
    ipa: "/ˈɡənə/",
    formalEquivalent: "going to",
    meaning: "ir a",
    register: "casual",
    function: "connector",
    examples: [
      { en: "I'm gonna call her.", es: "La voy a llamar.", context: "spoken English" },
    ],
  },
  {
    id: everydayId("wanna"),
    phrase: "wanna",
    ipa: "/ˈwɒnə/",
    formalEquivalent: "want to",
    meaning: "querer",
    register: "casual",
    function: "connector",
    examples: [
      { en: "Do you wanna come?", es: "¿Quieres venir?", context: "spoken English" },
    ],
  },
  {
    id: everydayId("you know"),
    phrase: "you know",
    formalEquivalent: "(filler — sabes)",
    meaning: "sabes / o sea",
    register: "casual",
    function: "filler",
    examples: [
      { en: "It was, you know, complicated.", es: "Fue, o sea, complicado.", context: "narration" },
    ],
  },
  {
    id: everydayId("I mean"),
    phrase: "I mean",
    formalEquivalent: "to clarify",
    meaning: "o sea / quiero decir",
    register: "casual",
    function: "softener",
    examples: [
      { en: "I mean, it's not bad.", es: "O sea, no está mal.", context: "self-correction" },
    ],
  },
  {
    id: everydayId("basically"),
    phrase: "basically",
    ipa: "/ˈbeɪsɪkli/",
    formalEquivalent: "essentially",
    meaning: "básicamente",
    register: "casual",
    function: "softener",
    examples: [
      { en: "Basically, it's a club.", es: "Básicamente, es un club.", context: "summary" },
    ],
  },
  {
    id: everydayId("anyway"),
    phrase: "anyway",
    ipa: "/ˈɛniweɪ/",
    formalEquivalent: "in any case",
    meaning: "en fin / de todos modos",
    register: "casual",
    function: "connector",
    examples: [
      { en: "Anyway, where were we?", es: "En fin, ¿dónde estábamos?", context: "topic shift" },
    ],
  },
  {
    id: everydayId("by the way"),
    phrase: "by the way",
    formalEquivalent: "incidentally",
    meaning: "por cierto",
    register: "casual",
    function: "connector",
    examples: [
      { en: "By the way, she called.", es: "Por cierto, ella llamó.", context: "side note" },
    ],
  },
];
