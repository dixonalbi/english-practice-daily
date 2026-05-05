import { Preposition, prepositionId } from "../domain/entities/Preposition";

export const PREPOSITIONS_SEED: Preposition[] = [
  {
    id: prepositionId("in"),
    word: "in",
    ipa: "/ɪn/",
    meanings: ["en", "dentro de"],
    uses: [
      {
        category: "time",
        rule: "Months, years, centuries, long periods.",
        examples: [
          { en: "I was born in May.", es: "Nací en mayo." },
          { en: "She graduated in 2019.", es: "Se graduó en 2019." },
        ],
      },
      {
        category: "place",
        rule: "Enclosed or large spaces — cities, countries, rooms.",
        examples: [{ en: "He lives in Lima.", es: "Vive en Lima." }],
      },
    ],
    commonMistakes: ["in / on", "in / at"],
  },
  {
    id: prepositionId("on"),
    word: "on",
    ipa: "/ɒn/",
    meanings: ["en (sobre)", "sobre"],
    uses: [
      {
        category: "time",
        rule: "Days and dates.",
        examples: [{ en: "We meet on Monday.", es: "Nos vemos el lunes." }],
      },
      {
        category: "place",
        rule: "Surfaces.",
        examples: [{ en: "The book is on the desk.", es: "El libro está sobre el escritorio." }],
      },
    ],
    commonMistakes: ["on / in"],
  },
  {
    id: prepositionId("at"),
    word: "at",
    ipa: "/æt/",
    meanings: ["en (punto exacto)", "a"],
    uses: [
      {
        category: "time",
        rule: "Specific clock times.",
        examples: [{ en: "Class starts at 9.", es: "La clase empieza a las 9." }],
      },
      {
        category: "place",
        rule: "Specific points or addresses.",
        examples: [{ en: "Meet me at the station.", es: "Nos vemos en la estación." }],
      },
    ],
    commonMistakes: ["at / in"],
  },
  {
    id: prepositionId("for"),
    word: "for",
    ipa: "/fɔːr/",
    meanings: ["por", "para", "durante"],
    uses: [
      {
        category: "time",
        rule: "Duration of an action.",
        examples: [{ en: "I waited for an hour.", es: "Esperé durante una hora." }],
      },
    ],
  },
  {
    id: prepositionId("by"),
    word: "by",
    ipa: "/baɪ/",
    meanings: ["por", "junto a"],
    uses: [
      {
        category: "relation",
        rule: "Agent of a passive sentence; means.",
        examples: [{ en: "The novel was written by Borges.", es: "La novela fue escrita por Borges." }],
      },
    ],
  },
  {
    id: prepositionId("with"),
    word: "with",
    ipa: "/wɪð/",
    meanings: ["con"],
    uses: [
      {
        category: "relation",
        rule: "Accompaniment or instrument.",
        examples: [{ en: "Cut it with a knife.", es: "Córtalo con un cuchillo." }],
      },
    ],
  },
  {
    id: prepositionId("from"),
    word: "from",
    ipa: "/frɒm/",
    meanings: ["de", "desde"],
    uses: [
      {
        category: "movement",
        rule: "Origin in space or time.",
        examples: [{ en: "She is from Cusco.", es: "Ella es de Cusco." }],
      },
    ],
  },
  {
    id: prepositionId("to"),
    word: "to",
    ipa: "/tuː/",
    meanings: ["a", "hacia"],
    uses: [
      {
        category: "movement",
        rule: "Destination.",
        examples: [{ en: "I'm going to the market.", es: "Voy al mercado." }],
      },
    ],
  },
  {
    id: prepositionId("between"),
    word: "between",
    ipa: "/bɪˈtwiːn/",
    meanings: ["entre (dos)"],
    uses: [
      {
        category: "place",
        rule: "Between two distinct things.",
        examples: [{ en: "Between you and me.", es: "Entre tú y yo." }],
      },
    ],
    commonMistakes: ["between / among"],
  },
  {
    id: prepositionId("during"),
    word: "during",
    ipa: "/ˈdjʊərɪŋ/",
    meanings: ["durante"],
    uses: [
      {
        category: "time",
        rule: "Throughout a period.",
        examples: [{ en: "He slept during the flight.", es: "Durmió durante el vuelo." }],
      },
    ],
  },
];
