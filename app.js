const GRAMMAR_DATA = [
  {
    "id": "gender_articles",
    "title": "1. Der, Die, Das & Rod belgilari",
    "tag": "Artikllar",
    "summary": "Nemis tilida otlar 3 ta rodga ega: Muzskoy (der), Jenskiy (die) va Sredniy (das). Ko'plikdagi otlar doim 'die' artiklini oladi.",
    "color": "#74B9FF",
    "rules": [
      {
        "label": "Der (Muzskoy)",
        "tip": "Erkak kishilar/hayvonlar, kunlar, oylar, fasllar va -er, -ling, -or, -ismus bilan tugovchi otlar (der Sommer, der Montag, der Lehrer)."
      },
      {
        "label": "Die (Jenskiy)",
        "tip": "Ayol kishilar/hayvonlar, va -ung, -heit, -keit, -schaft, -tion, -tät, -ei bilan tugovchi otlar (die Zeitung, die Freiheit, die Bäckerei)."
      },
      {
        "label": "Das (Sredniy)",
        "tip": "-chen, -lein kichraytirish qo'shimchalari, fe'ldan yasalgan otlar va -ment, -um, -tum bilan tugovchi otlar (das Mädchen, das Brötchen, das Essen, das Museum)."
      },
      {
        "label": "Die (Ko'plik)",
        "tip": "Barcha ko'plikdagi otlar, original rodidan qat'i nazar, Nominativ kelishigida 'die' oladi!"
      }
    ],
    "table": {
      "headers": [
        "Rod",
        "Aniq (The)",
        "Noaniq (A/An)",
        "Inkor (No/None)"
      ],
      "rows": [
        [
          "Muzskoy",
          "der Tisch",
          "ein Tisch",
          "kein Tisch"
        ],
        [
          "Jenskiy",
          "die Katze",
          "eine Katze",
          "keine Katze"
        ],
        [
          "Sredniy",
          "das Buch",
          "ein Buch",
          "kein Buch"
        ],
        [
          "Ko'plik",
          "die Kinder",
          "(ko'plik yo'q)",
          "keine Kinder"
        ]
      ]
    },
    "fritz_tip": "So'zning oxiriga e'tibor bering! -ung, -heit, -keit, va -schaft bilan tugaydigan so'zlarning 99% qismi DIE hisoblanadi. -chen yoki -lein bilan tugaydiganlar esa doim DAS (hatto das Mädchen ham)! 🦊💡",
    "quiz": [
      {
        "q": "'Zeitung' (gazeta) uchun artikl qaysi?",
        "options": [
          "der",
          "die",
          "das"
        ],
        "answer": 1,
        "hint": "-ung bilan tugovchi so'zlar doim jenskiy rodda!"
      },
      {
        "q": "'Mädchen' (qiz) uchun artikl qaysi?",
        "options": [
          "der",
          "die",
          "das"
        ],
        "answer": 2,
        "hint": "-chen kichraytirish qo'shimchasi otni doim sredniy rodga aylantiradi!"
      },
      {
        "q": "Ko'plikdagi otlar Nominativda qaysi artiklni oladi?",
        "options": [
          "der",
          "die",
          "das"
        ],
        "answer": 1,
        "hint": "Ko'plik doim Nominativda 'die' oladi."
      }
    ]
  },
  {
    "id": "cases_nom_akk",
    "title": "2. Kelishiklar: Nominativ va Akkusativ",
    "tag": "Kelishiklar",
    "summary": "Nominativ kelishigi EGANI (harakatni bajaruvchini) bildiradi. Akkusativ kelishigi esa TO'LDIRUVCHINI (harakat kimga/nimaga qaratilganligini) bildiradi.",
    "color": "#FF7675",
    "rules": [
      {
        "label": "Sehrli o'zgarish",
        "tip": "Akkusativda FAQAT muzskoy rod o'zgaradi: der -> den, ein -> einen, kein -> keinen. Jenskiy, Sredniy va Ko'plik o'zgarmaydi!"
      },
      {
        "label": "Ega (Wer/Was? - Kim/Nima?)",
        "tip": "Der Mann trinkt einen Kaffee. -> 'Der Mann' bu yerda ega (Nominativ)."
      },
      {
        "label": "To'ldiruvchi (Wen/Was? - Kimni/Nimani?)",
        "tip": "Er trinkt den Kaffee. -> 'den Kaffee' bu yerda to'ldiruvchi (Akkusativ)."
      },
      {
        "label": "Akkusativ talab qiluvchi predloglar",
        "tip": "bis, durch, für, gegen, ohne, um. Bu predloglardan keyin DOIM Akkusativ keladi!"
      }
    ],
    "table": {
      "headers": [
        "Kelishik",
        "Muzskoy",
        "Jenskiy",
        "Sredniy",
        "Ko'plik"
      ],
      "rows": [
        [
          "Nominativ",
          "der / ein / kein",
          "die / eine / keine",
          "das / ein / kein",
          "die / - / keine"
        ],
        [
          "Akkusativ",
          "den / einen / keinen",
          "die / eine / keine",
          "das / ein / kein",
          "die / - / keine"
        ]
      ]
    },
    "fritz_tip": "Eslab qoling: Akkusativda faqat muzskoy rod 'N' harfini oladi! 'Ich habe EINEN Hund (m), EINE Katze (f), EIN Auto (n)'. 🦊🐶",
    "quiz": [
      {
        "q": "Bo'sh joyni to'ldiring: 'Ich kaufe _____ Apfel (m)'.",
        "options": [
          "ein",
          "einen",
          "eine"
        ],
        "answer": 1,
        "hint": "Apfel muzskoy rod va bu yerda to'ldiruvchi: ein -> einen."
      },
      {
        "q": "Qaysi predlog DOIM Akkusativ talab qiladi?",
        "options": [
          "mit",
          "nach",
          "für"
        ],
        "answer": 2,
        "hint": "'für' doim akkusativ oladi (Das ist für dich!)."
      },
      {
        "q": "Jenskiy roddagi 'die Tasche' Akkusativda qanday o'zgaradi?",
        "options": [
          "'den' ga",
          "'der' ga",
          "'die' bo'lib qoladi"
        ],
        "answer": 2,
        "hint": "Jenskiy va Sredniy rodlar Nominativ va Akkusativda umuman o'zgarmaydi."
      }
    ]
  },
  {
    "id": "cases_dative",
    "title": "3. Dativ kelishigi asoslari",
    "tag": "Kelishiklar",
    "summary": "Dativ kelishigi VOSITALI TO'LDIRUVCHINI (kimga / kim uchun) bildiradi va ba'zi muhim predloglardan keyin ishlatiladi.",
    "color": "#55EFC4",
    "rules": [
      {
        "label": "Dativ artikl o'zgarishlari",
        "tip": "der -> dem, das -> dem, die -> der, die (ko'plik) -> den + ot oxiriga 'n' qo'shiladi!"
      },
      {
        "label": "Dativ talab qiluvchi predloglar",
        "tip": "aus, bei, mit, nach, seit, von, zu (Yodlab oling: aus-bei-mit, nach-seit-von-zu!)."
      },
      {
        "label": "Dativ oluvchi ko'p uchraydigan fe'llar",
        "tip": "helfen (hilf mir!), danken (ich danke dir), gefallen (das gefällt mir), schmecken (das schmeckt mir)."
      }
    ],
    "table": {
      "headers": [
        "Rod",
        "Nominativ",
        "Akkusativ",
        "Dativ"
      ],
      "rows": [
        [
          "Muzskoy",
          "der / ein",
          "den / einen",
          "dem / einem"
        ],
        [
          "Jenskiy",
          "die / eine",
          "die / eine",
          "der / einer"
        ],
        [
          "Sredniy",
          "das / ein",
          "das / ein",
          "dem / einem"
        ],
        [
          "Ko'plik",
          "die / -",
          "die / -",
          "den / - (+n)"
        ]
      ]
    },
    "fritz_tip": "Sehrli qofiyani kuylang: 'Aus, bei, mit, nach, seit, von, zu — immer mit dem Dativ, du!' 🎶🦊",
    "quiz": [
      {
        "q": "To'ldiring: 'Ich fahre mit _____ Bus (m)'.",
        "options": [
          "den",
          "dem",
          "der"
        ],
        "answer": 1,
        "hint": "'mit' predlogi Dativ talab qiladi, shuning uchun 'der' 'dem' ga aylanadi."
      },
      {
        "q": "Jenskiy roddagi 'die' Dativda nimaga aylanadi?",
        "options": [
          "dem",
          "der",
          "den"
        ],
        "answer": 1,
        "hint": "Jenskiy 'die' Dativda 'der' ga aylanadi."
      },
      {
        "q": "Qaysi fe'l doim Dativ to'ldiruvchi oladi?",
        "options": [
          "helfen",
          "kaufen",
          "sehen"
        ],
        "answer": 0,
        "hint": "'helfen' Dativ oladi: 'Ich helfe dir'."
      }
    ]
  },
  {
    "id": "verb_conjugation",
    "title": "4. Hozirgi zamon fe'l tuslanishi",
    "tag": "Fe'llar",
    "summary": "Nemis tilida fe'llar egaga qarab o'z qo'shimchalarini o'zgartiradi: -e, -st, -t, -en, -t, -en.",
    "color": "#FFEAA7",
    "rules": [
      {
        "label": "To'g'ri (Muntazam) qo'shimchalar",
        "tip": "ich -e | du -st | er/sie/es -t | wir -en | ihr -t | sie/Sie -en."
      },
      {
        "label": "O'zak unlisi o'zgaradigan fe'llar (du/er)",
        "tip": "e -> i/ie (sprechen -> du sprichst, lesen -> er liest); a -> ä (fahren -> du fährst, schlafen -> er schläft)."
      },
      {
        "label": "-t yoki -d bilan tugaydigan fe'llar",
        "tip": "Talaffuz uchun qo'shimcha 'e' qo'shiladi: arbeiten -> du arbeitest, er arbeitet."
      }
    ],
    "table": {
      "headers": [
        "Olmosh",
        "lernen (to'g'ri)",
        "fahren (a->ä)",
        "sprechen (e->i)"
      ],
      "rows": [
        [
          "ich",
          "lerne",
          "fahre",
          "spreche"
        ],
        [
          "du",
          "lernst",
          "fährst",
          "sprichst"
        ],
        [
          "er / sie / es",
          "lernt",
          "fährt",
          "spricht"
        ],
        [
          "wir",
          "lernen",
          "fahren",
          "sprechen"
        ],
        [
          "ihr",
          "lernt",
          "fahrt",
          "sprecht"
        ],
        [
          "sie / Sie",
          "lernen",
          "fahren",
          "sprechen"
        ]
      ]
    },
    "fritz_tip": "Eslab qoling: 'E - ST - T - EN - T - EN'. Infinitivdan -en ni olib tashlang va mos qo'shimchani qo'shing! 🦊✨",
    "quiz": [
      {
        "q": "Tuslang: 'Du _____ (sprechen) sehr gut Deutsch.'",
        "options": [
          "sprechtest",
          "sprechst",
          "sprichst"
        ],
        "answer": 2,
        "hint": "'sprechen' dagi 'e' unlisi 'du' va 'er/sie/es' uchun 'i' ga o'zgaradi."
      },
      {
        "q": "Tuslang: 'Er _____ (fahren) mit dem Zug.'",
        "options": [
          "fahrt",
          "fährst",
          "fährt"
        ],
        "answer": 2,
        "hint": "'fahren' 3-shaxs birlikda umlaut (ä) oladi."
      },
      {
        "q": "'wir' (biz) uchun fe'l qo'shimchasi qanday?",
        "options": [
          "-e",
          "-t",
          "-en"
        ],
        "answer": 2,
        "hint": "'wir' doim '-en' oladi (infinitiv bilan bir xil)."
      }
    ]
  },
  {
    "id": "sein_haben",
    "title": "5. Katta Uchtalik: Sein, Haben va Werden",
    "tag": "Fe'llar",
    "summary": "Bu uchta noto'g'ri yordamchi fe'l nemis tili so'zlashuvining va o'tgan/kelasi zamonlarning asosiy poydevori hisoblanadi.",
    "color": "#A29BFE",
    "rules": [
      {
        "label": "sein (bo'lmoq)",
        "tip": "Shaxsni, kasbni, joylashuvni va sifatlarni ifodalash uchun muhim: 'Ich bin glücklich' (Men baxtliman)."
      },
      {
        "label": "haben (ega bo'lmoq)",
        "tip": "Egalikni va ko'plab iboralarni ifodalaydi: 'Ich habe Hunger/Durst/Zeit'."
      },
      {
        "label": "werden (aylanmoq/bo'lmoq)",
        "tip": "Holat o'zgarishi va kelasi zamon uchun ishlatiladi: 'Es wird kalt' (Sovuq bo'lyapti)."
      }
    ],
    "table": {
      "headers": [
        "Olmosh",
        "sein (bo'lmoq)",
        "haben (ega bo'lmoq)",
        "werden (aylanmoq)"
      ],
      "rows": [
        [
          "ich",
          "bin",
          "habe",
          "werde"
        ],
        [
          "du",
          "bist",
          "hast",
          "wirst"
        ],
        [
          "er / sie / es",
          "ist",
          "hat",
          "wird"
        ],
        [
          "wir",
          "sind",
          "haben",
          "werden"
        ],
        [
          "ihr",
          "seid",
          "habt",
          "werdet"
        ],
        [
          "sie / Sie",
          "sind",
          "haben",
          "werden"
        ]
      ]
    },
    "fritz_tip": "'ihr seid' (sizlar) va 'sie sind' (ular) farqiga e'tibor bering. Ularni adashtirib qo'yish juda oson! 🦊",
    "quiz": [
      {
        "q": "To'ldiring: 'Wir _____ zwei Brüder.' (Bizning ikkita akamiz bor).",
        "options": [
          "sind",
          "haben",
          "werdet"
        ],
        "answer": 1,
        "hint": "Oila a'zolariga ega bo'lish uchun 'haben' ishlatiladi."
      },
      {
        "q": "To'ldiring: 'Wie alt _____ du?' (Yoshing nechada?).",
        "options": [
          "hast",
          "bist",
          "wirst"
        ],
        "answer": 1,
        "hint": "Nemis tilida yosh 'sein' (bo'lmoq) fe'li bilan aytiladi, 'haben' bilan emas."
      },
      {
        "q": "'sein' fe'lining 'ihr' (sizlar) shakli qanday?",
        "options": [
          "sind",
          "seid",
          "bist"
        ],
        "answer": 1,
        "hint": "'ihr seid' bu 2-shaxs ko'plik shakli."
      }
    ]
  },
  {
    "id": "modal_verbs",
    "title": "6. Modal fe'llar va Gap qavsi",
    "tag": "Modal Fe'llar",
    "summary": "Modal fe'llar qobiliyat, zaruriyat yoki xohishni ifodalaydi. Ular asosiy fe'lni (infinitivda) gapning eng oxiriga surib yuboradi!",
    "color": "#FDCB6E",
    "rules": [
      {
        "label": "können (qila olmoq)",
        "tip": "ich kann, du kannst, er kann, wir können"
      },
      {
        "label": "müssen (shart/majbur)",
        "tip": "ich muss, du musst, er muss, wir müssen"
      },
      {
        "label": "wollen (xohlamoq/istamoq)",
        "tip": "ich will, du willst, er will, wir wollen"
      },
      {
        "label": "möchten (xohlardim)",
        "tip": "ich möchte, du möchtest, er möchte, wir möchten"
      },
      {
        "label": "dürfen (ruxsat bo'lmoq)",
        "tip": "ich darf, du darfst, er darf, wir dürfen"
      },
      {
        "label": "sollen (kerak/lozim)",
        "tip": "ich soll, du sollst, er soll, wir sollen"
      }
    ],
    "table": {
      "headers": [
        "1-o'rin",
        "2-o'rin (Modal)",
        "O'rta (Vaqt/Joy/Obyekt)",
        "Oxiri (Infinitiv)"
      ],
      "rows": [
        [
          "Ich",
          "kann",
          "gut Deutsch",
          "sprechen."
        ],
        [
          "Wir",
          "müssen",
          "heute die Hausaufgaben",
          "machen."
        ],
        [
          "Er",
          "möchte",
          "einen Kaffee",
          "trinken."
        ]
      ]
    },
    "fritz_tip": "E'tibor bering: barcha modal fe'llarda 'ich' va 'er/sie/es' shakllari BIR XIL: 'ich kann' = 'er kann'! 🦊🎉",
    "quiz": [
      {
        "q": "Modal fe'l qatnashgan gapda ikkinchi asosiy fe'l qayerda keladi?",
        "options": [
          "Modal fe'ldan darhol keyin",
          "Gapning eng oxirida",
          "Egadan oldin"
        ],
        "answer": 1,
        "hint": "Infinitiv shakldagi asosiy fe'l gapni oxirida yopib turadi (qavs)."
      },
      {
        "q": "Tuslang: 'Er _____ (können) sehr schnell laufen.'",
        "options": [
          "kann",
          "könnt",
          "kannst"
        ],
        "answer": 0,
        "hint": "'können' ning 3-shaxs birlik shakli 'kann' (-t qo'shilmaydi!)."
      },
      {
        "q": "Qaysi modal fe'l 'ruxsat' ma'nosini bildiradi?",
        "options": [
          "müssen",
          "wollen",
          "dürfen"
        ],
        "answer": 2,
        "hint": "'dürfen' ruxsat etilgan, mumkin degan ma'noni bildiradi."
      }
    ]
  },
  {
    "id": "word_order",
    "title": "7. So'z tartibi va Oltin V2 qoidasi",
    "tag": "Sintaksis",
    "summary": "Asosiy gaplarda tuslangan fe'l DOIM 2-o'rinda keladi. Hatto gapni vaqt yoki joy bilan boshlasangiz ham!",
    "color": "#00B894",
    "rules": [
      {
        "label": "Standart tartib (SVO)",
        "tip": "[1-o'rin: Ega] + [2-o'rin: FE'L] + [Qolganlar]. Misol: 'Ich lerne heute Deutsch.'"
      },
      {
        "label": "Inversiya (Vaqt/Joy birinchi)",
        "tip": "[1-o'rin: Vaqt/Joy] + [2-o'rin: FE'L] + [3-o'rin: Ega]. Misol: 'Heute lerne ich Deutsch.'"
      },
      {
        "label": "So'roq gaplar",
        "tip": "Ha/Yo'q so'roq gaplarida Fe'l 1-o'ringa o'tadi: 'Lernst du Deutsch?' So'roq so'zli gaplarda So'roq so'z 1-o'rinda, Fe'l 2-o'rinda: 'Wo lernst du Deutsch?'"
      }
    ],
    "table": {
      "headers": [
        "Turi",
        "1-o'rin",
        "2-o'rin (FE'L)",
        "3-o'rin",
        "Oxiri"
      ],
      "rows": [
        [
          "Ega birinchi",
          "Ich",
          "trinke",
          "morgens Kaffee",
          "-"
        ],
        [
          "Vaqt birinchi",
          "Morgens",
          "trinke",
          "ich",
          "Kaffee"
        ],
        [
          "Ha/Yo'q so'roq",
          "Trinkst",
          "du",
          "morgens Kaffee",
          "?"
        ],
        [
          "Maxsus so'roq",
          "Wann",
          "trinkst",
          "du Kaffee",
          "?"
        ]
      ]
    },
    "fritz_tip": "2-o'rin degani bu ikkinchi so'z degani EMAS — bu ikkinchi grammatik blok degani! 'Meine liebe Oma [1] kocht [2] die Suppe.' 🦊🍲",
    "quiz": [
      {
        "q": "Agar gap 'Gestern' (Kecha) bilan boshlansa, nima bo'ladi?",
        "options": [
          "Keyin ega keladi",
          "Keyin fe'l keladi",
          "Keyin to'ldiruvchi keladi"
        ],
        "answer": 1,
        "hint": "Fe'l DOIM 2-o'rinda qolishi shart: 'Gestern ging ich...'."
      },
      {
        "q": "Qaysi gapda so'z tartibi to'g'ri?",
        "options": [
          "Heute ich fahre nach Berlin.",
          "Heute fahre ich nach Berlin.",
          "Fahre heute ich nach Berlin."
        ],
        "answer": 1,
        "hint": "1-o'rin: Heute, 2-o'rin: fahre, 3-o'rin: ich."
      },
      {
        "q": "Ha/Yo'q so'roq gapida fe'l qayerda keladi?",
        "options": [
          "1-o'rinda",
          "2-o'rinda",
          "Oxirida"
        ],
        "answer": 0,
        "hint": "'Kommst du morgen?' -> Fe'l 1-o'rinda."
      }
    ]
  },
  {
    "id": "negation",
    "title": "8. Inkor: Nicht va Kein",
    "tag": "Grammatika",
    "summary": "Ularni aslo adashtirmang: noaniq artiklli yoki artiklsiz otlarni inkor qilish uchun 'kein', fe'llar, sifatlar va aniq otlar uchun 'nicht' ishlatiladi.",
    "color": "#E17055",
    "rules": [
      {
        "label": "Qachon KEIN ishlatiladi",
        "tip": "'ein' yoki artiklsiz otlarni inkor qilganda: 'Ich habe EIN Auto' -> 'Ich habe KEIN Auto'. 'Ich habe Zeit' -> 'Ich habe KEINE Zeit'."
      },
      {
        "label": "Qachon NICHT ishlatiladi",
        "tip": "Fe'llarni, sifatlarni, ravishlarni va aniq artiklli ('der/die/das') otlarni inkor qilganda: 'Ich schlafe NICHT', 'Das ist NICHT gut', 'Ich kenne DEN Mann NICHT'."
      },
      {
        "label": "Doch!",
        "tip": "Agar kimdir inkorli savol bersa ('Kommst du nicht?') va siz 'ha' deb tasdiqlamoqchi bo'lsangiz, 'Ja' o'rniga 'DOCH!' ishlating."
      }
    ],
    "table": {
      "headers": [
        "Inkor qilinuvchi",
        "Ishlatiladi",
        "Tasdiq misol",
        "Inkor misol"
      ],
      "rows": [
        [
          "'ein' li ot",
          "kein",
          "Ich habe ein Buch.",
          "Ich habe kein Buch."
        ],
        [
          "Artiklsiz ot",
          "keine",
          "Ich trinke Milch.",
          "Ich trinke keine Milch."
        ],
        [
          "Fe'l / Harakat",
          "nicht",
          "Ich schwimme gern.",
          "Ich schwimme nicht gern."
        ],
        [
          "Sifat",
          "nicht",
          "Das Hotel ist teuer.",
          "Das Hotel ist nicht teuer."
        ],
        [
          "Aniq ot",
          "nicht",
          "Ich suche den Schlüssel.",
          "Ich suche den Schlüssel nicht."
        ]
      ]
    },
    "fritz_tip": "Agar ingliz tilida 'no/not any' deyish mumkin bo'lsa, nemis tilida 'kein' ishlating. Qolgan hamma narsa uchun 'nicht'! 🦊⛔",
    "quiz": [
      {
        "q": "To'ldiring: 'Ich habe _____ Zeit.' (Zeit - jenskiy, artiklsiz ot).",
        "options": [
          "nicht",
          "keine",
          "keinen"
        ],
        "answer": 1,
        "hint": "Artiklsiz jenskiy otni inkor qilish 'keine' oladi."
      },
      {
        "q": "To'ldiring: 'Das Essen ist _____ teuer.'",
        "options": [
          "nicht",
          "kein",
          "keine"
        ],
        "answer": 0,
        "hint": "Sifatni ('teuer') inkor qilish 'nicht' oladi."
      },
      {
        "q": "Birov so'radi: 'Hast du keinen Hunger?' Siz judayam ochsiz. Nima deysiz?",
        "options": [
          "Ja!",
          "Doch!",
          "Nein!"
        ],
        "answer": 1,
        "hint": "'Doch' inkorli savolga ijobiy javob berish (haqiqatni tasdiqlash) uchun ishlatiladi."
      }
    ]
  },
  {
    "id": "prepositions",
    "title": "9. Eng muhim predloglar va Kelishiklar",
    "tag": "Predloglar",
    "summary": "Predloglar o'zlaridan keyin keluvchi otning kelishigini belgilab beradi. A1 darajasi uchun muhim predloglarni yodlab oling!",
    "color": "#0984E3",
    "rules": [
      {
        "label": "Dativ Predloglar",
        "tip": "aus (dan), bei (da/yonida), mit (bilan), nach (keyin/ga), seit (-dan beri), von (-ning/dan), zu (ga). DOIM Dativ!"
      },
      {
        "label": "Akkusativ Predloglar",
        "tip": "bis (gacha), durch (orqali), für (uchun), gegen (qarshi/atrofida), ohne (siz), um (da/atrofida). DOIM Akkusativ!"
      },
      {
        "label": "Qisqartmalar",
        "tip": "in + dem = im | an + dem = am | zu + dem = zum | zu + der = zur | bei + dem = beim | für + das = fürs."
      }
    ],
    "table": {
      "headers": [
        "Predlog",
        "Kelishik",
        "Ma'nosi",
        "Misol"
      ],
      "rows": [
        [
          "mit",
          "Dativ",
          "bilan / orqali",
          "Ich fahre mit dem Bus."
        ],
        [
          "für",
          "Akkusativ",
          "uchun",
          "Das Geschenk ist für dich."
        ],
        [
          "zu",
          "Dativ",
          "ga / tomon",
          "Ich gehe zum Arzt."
        ],
        [
          "ohne",
          "Akkusativ",
          "siz (without)",
          "Kaffee ohne Zucker bitte."
        ],
        [
          "bei",
          "Dativ",
          "da / yonida",
          "Ich wohne bei meinen Eltern."
        ],
        [
          "nach",
          "Dativ",
          "keyin / ga",
          "Nach dem Essen schlafe ich."
        ]
      ]
    },
    "fritz_tip": "Yodda tuting: 'zum' = zu dem (muzskoy/sredniy), 'zur' = zu der (jenskiy). 'Ich gehe zum Arzt, aber zur Bank!' 🦊🏦",
    "quiz": [
      {
        "q": "To'ldiring: 'Ein Kaffee _____ (sutsiz) Milch bitte.'",
        "options": [
          "mit",
          "ohne",
          "für"
        ],
        "answer": 1,
        "hint": "'ohne' -siz degani (without)."
      },
      {
        "q": "'in dem' ning qisqartmasi nima?",
        "options": [
          "im",
          "am",
          "ans"
        ],
        "answer": 0,
        "hint": "'in + dem' 'im' ga qisqaradi."
      },
      {
        "q": "Qaysi predlog '-dan beri' ma'nosini bildiradi va Dativ talab qiladi?",
        "options": [
          "nach",
          "seit",
          "von"
        ],
        "answer": 1,
        "hint": "'seit' vaqt davriydiligini bildiradi: 'seit einem Jahr'."
      }
    ]
  },
  {
    "id": "plurals",
    "title": "10. Ko'plik shakllari va Ot qo'shimchalari",
    "tag": "Otlar",
    "summary": "Ingliz tilidan (-s) farqli o'laroq, nemis tilida 5 ta asosiy ko'plik shakli mavjud: -e, -(e)n, -er, -s, va qo'shimchasiz (ko'pincha umlaut bilan).",
    "color": "#6C5CE7",
    "rules": [
      {
        "label": "1-shakl: -e (ko'pincha Umlaut bilan)",
        "tip": "Muzskoy va sredniy otlarda ko'p uchraydi: der Tisch -> die Tische, der Baum -> die Bäume."
      },
      {
        "label": "2-shakl: -(e)n",
        "tip": "Jenskiy otlarning ~90% uchun standart: die Frau -> die Frauen, die Lampe -> die Lampen."
      },
      {
        "label": "3-shakl: -er (odatda Umlaut bilan)",
        "tip": "Ko'pincha qisqa sredniy otlarda: das Kind -> die Kinder, das Buch -> die Bücher, das Bild -> die Bilder."
      },
      {
        "label": "4-shakl: -s",
        "tip": "Chet tilidan kirgan so'zlar va qisqartmalar: das Auto -> die Autos, das Sofa -> die Sofas, das Handy -> die Handys."
      },
      {
        "label": "5-shakl: Qo'shimchasiz (yoki faqat Umlaut)",
        "tip": "-el, -en, -er bilan tugovchi otlar: der Lehrer -> die Lehrer, der Apfel -> die Äpfel, der Computer -> die Computer."
      }
    ],
    "table": {
      "headers": [
        "Birlik",
        "Ko'plik",
        "Shakl",
        "Ma'nosi"
      ],
      "rows": [
        [
          "der Tag",
          "die Tage",
          "+e",
          "kun -> kunlar"
        ],
        [
          "die Zeitung",
          "die Zeitungen",
          "+en",
          "gazeta -> gazetalar"
        ],
        [
          "das Kind",
          "die Kinder",
          "+er",
          "bola -> bolalar"
        ],
        [
          "das Auto",
          "die Autos",
          "+s",
          "mashina -> mashinalar"
        ],
        [
          "der Apfel",
          "die Äpfel",
          "Faqat Umlaut",
          "olma -> olmalar"
        ]
      ]
    },
    "fritz_tip": "Nemis tilida biror otni yodlaganda, uni DOIM artikli VA ko'pligi bilan birga yodlang: 'der Tisch, die Tische'! 🦊📚",
    "quiz": [
      {
        "q": "'das Buch' (kitob) ning ko'pligi nima?",
        "options": [
          "die Buche",
          "die Büchen",
          "die Bücher"
        ],
        "answer": 2,
        "hint": "Das Buch umlaut va -er oladi: die Bücher."
      },
      {
        "q": "-ung bilan tugaydigan ko'pchilik jenskiy otlarning ko'plik qo'shimchasi nima?",
        "options": [
          "-e",
          "-en",
          "-s"
        ],
        "answer": 1,
        "hint": "die Zeitung -> die Zeitungen."
      },
      {
        "q": "'das Auto' ning ko'pligi nima?",
        "options": [
          "die Autos",
          "die Auton",
          "die Autoe"
        ],
        "answer": 0,
        "hint": "Chet tilidan kirgan so'zlar odatda -s oladi."
      }
    ]
  }
];

// WunderDeutsch Core Logic & i18n Engine

const TRANSLATIONS = {
    en: {
        "title_home": "Home", "title_ddd": "Der Die Das", "title_dict": "Dictionary", "title_settings": "Settings",
        "subtitle_ddd": "Gender Trainer", "subtitle_dict": "Your Vocabulary", "title_satzbau": "Sentence Puzzle", "subtitle_satzbau": "Sentence Puzzle",
        "title_grammar": "Grammar", "subtitle_grammar": "Rules", "daily_goal": "Daily Goal", "wotd": "WORD OF THE MOMENT",
        "settings_offline": "Offline Mode", "settings_clear_cache": "Clear Cache & Reload", "listen": "Listen", "search": "Search word...", "settings_pref": "Preferences", "settings_sound": "Sound",
        "settings_vib": "Vibration", "settings_lang": "Language", "settings_notif": "Notifications", "settings_reminder": "Daily Reminders", "about_title": "About WunderDeutsch",
        "about_text": "WunderDeutsch is an interactive learning app specifically designed to master German playfully. Learn vocabulary, train articles, and build sentences!",
        "contact_title": "Contact", "game_prompt": "Which article is correct?", 
        "leave_guard_title": "Are you sure?", "leave_guard": "Are you sure you want to leave your homework? Progress might be lost.",
        "btn_stay": "Stay", "btn_leave": "Leave",
        "coming_soon": "Coming soon!", "coming_desc1": "I am preparing this feature!", "coming_desc2": "Grammar rules will be here soon!",
        "private_access": "Private Access Only", "btn_login": "Login", "msg_wrong": "Incorrect credentials.",
        "mascot_hello": "<strong>Hello! I'm Fritz.</strong>", "mascot_sub": "Let's learn with your own vocabulary!",
        "msg_correct": "Correct! Great job! 🎉", "msg_ohno": "Oh no! It is", "check": "Check"
    },
    de: {
        "title_home": "Home", "title_ddd": "Der Die Das", "title_dict": "Wörterbuch", "title_settings": "Einstellungen",
        "subtitle_ddd": "Artikel Trainer", "subtitle_dict": "Deine Vokabeln", "title_satzbau": "Satzbau", "subtitle_satzbau": "Satz-Puzzle",
        "title_grammar": "Grammatik", "subtitle_grammar": "Regeln", "daily_goal": "Tagesziel", "wotd": "WORT DES MOMENTS",
        "settings_offline": "Offline-Modus", "settings_clear_cache": "Cache leeren & neuladen", "listen": "Aussprache hören", "search": "Wort suchen...", "settings_pref": "Präferenzen", "settings_sound": "Ton",
        "settings_vib": "Vibration", "settings_lang": "Sprache", "settings_notif": "Benachrichtigungen", "settings_reminder": "Tägliche Erinnerungen", "about_title": "Über WunderDeutsch",
        "about_text": "WunderDeutsch ist eine interaktive Lern-App, die speziell entwickelt wurde, um Deutsch auf spielerische Weise zu meistern. Lerne Vokabeln, trainiere Artikel und baue Sätze!",
        "contact_title": "Kontakt", "game_prompt": "Welcher Artikel ist richtig?", 
        "leave_guard_title": "Bist du sicher?", "leave_guard": "Bist du sicher, dass du deine Hausaufgaben verlassen möchtest?",
        "btn_stay": "Bleiben", "btn_leave": "Verlassen",
        "coming_soon": "Kommt bald!", "coming_desc1": "Ich bereite diese Funktion noch vor!", "coming_desc2": "Hier kommen bald Grammatikregeln hin!",
        "private_access": "Nur privater Zugang", "btn_login": "Einloggen", "msg_wrong": "Falsche Zugangsdaten.",
        "mascot_hello": "<strong>Hallo! Ich bin Fritz.</strong>", "mascot_sub": "Lass uns mit deinen eigenen Vokabeln lernen!",
        "msg_correct": "Richtig! Super gemacht! 🎉", "msg_ohno": "Oh nein! Es heißt", "check": "Prüfen"
    },
    uz: {
        "title_home": "Asosiy", "title_ddd": "Der Die Das", "title_dict": "Lug'at", "title_settings": "Sozlamalar",
        "subtitle_ddd": "Artikl Mashqi", "subtitle_dict": "Sizning so'zlaringiz", "title_satzbau": "Gap tuzish", "subtitle_satzbau": "Gap Pazzli",
        "title_grammar": "Grammatika", "subtitle_grammar": "Qoidalar", "daily_goal": "Kunlik maqsad", "wotd": "KUN SO'ZI",
        "settings_offline": "Offlayn rejim", "settings_clear_cache": "Keshni tozalash va yangilash", "listen": "Talaffuzni eshitish", "search": "So'z qidirish...", "settings_pref": "Afzalliklar", "settings_sound": "Ovoz",
        "settings_vib": "Vibratsiya", "settings_lang": "Til", "settings_notif": "Bildirishnomalar", "settings_reminder": "Kunlik eslatmalar", "about_title": "WunderDeutsch haqida",
        "about_text": "WunderDeutsch - nemis tilini o'yin orqali o'rganish uchun maxsus ishlab chiqilgan interaktiv ilova. So'zlarni yodlang, artikllarni mashq qiling va gaplar tuzing!",
        "contact_title": "Aloqa", "game_prompt": "Qaysi artikl to'g'ri?", 
        "leave_guard_title": "Ishonchingiz komilmi?", "leave_guard": "Haqiqatan ham vazifani tark etmoqchimisiz?",
        "btn_stay": "Qolish", "btn_leave": "Chiqish",
        "coming_soon": "Tez orada!", "coming_desc1": "Men ushbu xususiyatni tayyorlayapman!", "coming_desc2": "Grammatika qoidalari tez orada bu yerda bo'ladi!",
        "private_access": "Faqat shaxsiy kirish", "btn_login": "Kirish", "msg_wrong": "Parol noto'g'ri.",
        "mascot_hello": "<strong>Salom! Men Fritsman.</strong>", "mascot_sub": "Keling, o'zingizning so'zlaringiz bilan o'rganamiz!",
        "msg_correct": "To'g'ri! Barakalla! 🎉", "msg_ohno": "Afsus! To'g'risi:", "check": "Tekshirish"
    }
};

const appState = {
    isAdmin: true, currentLevel: localStorage.getItem('wunderdeutsch_level') || 'A1', // Since only merser572@gmail.com is allowed currently
    streak: parseInt(localStorage.getItem('wunder_streak') || 0), 
    xp: parseInt(localStorage.getItem('wunder_xp') || 0), 
    dailyXP: parseInt(localStorage.getItem('wunder_daily_xp') || 0),
    lives: parseInt(localStorage.getItem('wunder_lives') || 5), 
    lastHeartRegen: parseInt(localStorage.getItem('wunder_last_regen') || Date.now()),
    lastActiveDate: localStorage.getItem('wunder_last_active_date') || new Date().toDateString(),
    words: [], currentWotd: null, dddWord: null, currentView: 'home',
    dddQueue: [],
    satzQueue: [],
    settings: { sound: true, vibration: true, offline: true, language: 'en' }
};

// --- GAMIFICATION LOGIC ---
function checkHeartRegen() {
    if (appState.isAdmin) return; // Admin has infinite
    const now = Date.now();
    const diff = now - appState.lastHeartRegen;
    const mins = Math.floor(diff / 60000);
    
    if (mins >= 30 && appState.lives < 5) {
        const heartsToAdd = Math.floor(mins / 30);
        appState.lives = Math.min(5, appState.lives + heartsToAdd);
        appState.lastHeartRegen = now - ((mins % 30) * 60000); // keep remainder
        saveGamificationState();
        updateStats();
    }
}

setInterval(checkHeartRegen, 60000); // Check every minute

function loseHeart() {
    if (appState.isAdmin) return true; // Admin never loses hearts
    
    if (appState.lives > 0) {
        appState.lives--;
        appState.lastHeartRegen = Date.now(); // Reset timer if they weren't regenerating
        saveGamificationState();
        updateStats();
        
        if (appState.lives === 0) {
            showNoHeartsModal();
            return false;
        }
        return true;
    } else {
        showNoHeartsModal();
        return false;
    }
}

function showNoHeartsModal() {
    const m = document.getElementById('no-hearts-modal');
    if(m) m.style.display = 'flex';
}
function closeNoHeartsModal() {
    const m = document.getElementById('no-hearts-modal');
    if(m) m.style.display = 'none';
    switchView('home'); // Send them home so they don't get stuck in a broken game loop
}


function checkStreak() {
    const today = new Date().toDateString();
    
    if (appState.lastActiveDate !== today) {
        // A new day!
        // Did they miss yesterday?
        const yesterday = new Date(Date.now() - 86400000).toDateString();
        if (appState.lastActiveDate !== yesterday && appState.lastActiveDate !== today) {
            appState.streak = 0; // Lost streak :(
        }
        
        appState.dailyXP = 0; // Reset daily XP
        appState.lastActiveDate = today;
        saveGamificationState();
    }
    
    // Check if daily goal met (e.g. 20 XP)
    if (appState.dailyXP >= 20 && localStorage.getItem('wunder_goal_met_' + today) !== 'true') {
        appState.streak++;
        localStorage.setItem('wunder_goal_met_' + today, 'true');
        showMascot("Tabriklaymiz! Kunlik maqsadga yetdingiz! 🚀", 3000);
        saveGamificationState();
    }
}

function saveGamificationState() {
    localStorage.setItem('wunder_streak', appState.streak);
    localStorage.setItem('wunder_xp', appState.xp);
    localStorage.setItem('wunder_daily_xp', appState.dailyXP);
    localStorage.setItem('wunder_lives', appState.lives);
    localStorage.setItem('wunder_last_regen', appState.lastHeartRegen);
    localStorage.setItem('wunder_last_active_date', appState.lastActiveDate);
}

function addXP(amount) {
    appState.xp += amount;
    appState.dailyXP += amount;
    saveGamificationState();
    checkStreak();
    updateStats();
}



let pendingView = null;

const els = {
    streak: document.getElementById('streak'), xp: document.getElementById('xp'),
    lives: document.getElementById('lives'), dddLives: document.getElementById('ddd-lives'),
    homeWotdTitle: document.getElementById('home-wotd-title'), homeWotdSub: document.getElementById('home-wotd-sub'),
    homeTtsBtn: document.getElementById('home-tts-btn'), dddWord: document.getElementById('ddd-word'),
    dddTrans: document.getElementById('ddd-translation'), dddSearch: document.getElementById('dict-search'),
    dddTtsBtn: document.getElementById('ddd-tts-btn')
};

async function initApp() {
    loadSettings();
    applyLanguage();
    setupAuth();
    setupModals();
    updateStats();
    updateOfflineMode();
    
    let display = appState.currentLevel === 'A1' ? 'Level: A1' : 'Medizin B2 🩺';
    const lvlDisp = document.getElementById('current-level-display');
    if (lvlDisp) lvlDisp.innerText = display;
    
    updateHomeUIForLevel();
    
    await loadVocabulary();
    lucide.createIcons();
    
    els.homeTtsBtn.addEventListener('click', () => {
        triggerVibrate(50);
        if(appState.currentWotd) {
            const t = appState.currentWotd.article ? `${appState.currentWotd.article} ${appState.currentWotd.word}` : appState.currentWotd.word;
            speakText(t);
        }
    });

    els.dddTtsBtn.addEventListener('click', () => {
        if(appState.dddWord) speakText(appState.dddWord.word);
    });

    els.dddSearch.addEventListener('input', renderDictionary);
}

function loadSettings() {
    const saved = localStorage.getItem('wunderdeutsch_settings');
    if (saved) {
        appState.settings = JSON.parse(saved);
        if(!appState.settings.language) appState.settings.language = 'en';
    }
    document.getElementById('toggle-sound').checked = appState.settings.sound;
    document.getElementById('toggle-vibration').checked = appState.settings.vibration;
    document.getElementById('toggle-offline').checked = appState.settings.offline;
    
    document.querySelectorAll('.lang-btn').forEach(btn => {
        if(btn.getAttribute('data-lang') === appState.settings.language) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}


function clearAllCaches() {
    triggerVibrate(50);
    playSound('tap');
    if ('caches' in window) {
        caches.keys().then(names => {
            return Promise.all(names.map(name => caches.delete(name)));
        }).then(() => {
            window.location.reload(true);
        });
    } else {
        window.location.reload(true);
    }
}

function updateOfflineMode() {
    if (appState.settings.offline) {
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('sw.js?v=25');
        }
    } else {
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.getRegistrations().then(function(registrations) {
                for(let registration of registrations) {
                    registration.unregister();
                }
            });
            // also clear caches so offline doesn't work next time
            if ('caches' in window) {
                caches.keys().then(names => Promise.all(names.map(name => caches.delete(name))));
            }
        }
    }
}

function toggleSetting(key) {
    appState.settings[key] = !appState.settings[key];
    saveSettings();
    if (appState.settings.sound && key === 'sound') playSound('success');
    if (appState.settings.vibration && key === 'vibration') triggerVibrate(50);
    if (key === 'offline') updateOfflineMode();
}

function changeLanguage(lang) {
    appState.settings.language = lang;
    saveSettings();
    applyLanguage();
    
    document.querySelectorAll('.lang-btn').forEach(btn => {
        if(btn.getAttribute('data-lang') === lang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
    
    if (appState.currentView === 'grammar') {
        renderGrammar();
    }
}

function saveSettings() {
    localStorage.setItem('wunderdeutsch_settings', JSON.stringify(appState.settings));
}

function applyLanguage() {
    const lang = appState.settings.language;
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (TRANSLATIONS[lang] && TRANSLATIONS[lang][key]) {
            if (el.tagName === 'INPUT' && el.hasAttribute('placeholder')) {
                el.setAttribute('placeholder', TRANSLATIONS[lang][key]);
            } else {
                el.innerHTML = TRANSLATIONS[lang][key];
            }
        }
    });
}



const AUTH_EMAIL = 'merser572@gmail.com';
const AUTH_HASH = '1776510484'; // custom hash for Hasanboy0412

async function hashPassword(str) {
    let hash = 5381;
    for (let i = 0; i < str.length; i++) {
        hash = ((hash << 5) + hash) + str.charCodeAt(i); /* hash * 33 + c */
    }
    return Math.abs(hash).toString();
}


function setupAuth() {
    // TEMPORARY BYPASS to unblock the user completely
    localStorage.setItem('wunderdeutsch_auth', 'true');
    appState.isAdmin = true;
    
    document.getElementById('login-overlay').style.display = 'none';
    document.getElementById('app-container').style.display = 'block';
}

function setupModals() {
    document.getElementById('modal-cancel-btn').addEventListener('click', () => {
        document.getElementById('custom-modal-overlay').style.display = 'none';
        pendingView = null;
    });

    document.getElementById('modal-confirm-btn').addEventListener('click', () => {
        document.getElementById('custom-modal-overlay').style.display = 'none';
        if (pendingView) {
            executeSwitchView(pendingView);
            pendingView = null;
        }
    });
}

async function loadVocabulary() {
    try {
        const response = await fetch('words.json');
        appState.words = await response.json();
        setWordOfTheMoment();
        
        const resSentences = await fetch('sentences.json');
        appState.satzSentences = await resSentences.json();
    } catch (e) { console.error("Failed to load vocabulary or sentences:", e); }
}

function setWordOfTheMoment() {
    if(appState.words.length === 0) return;
    const nouns = appState.words.filter(w => w.article);
    if(nouns.length === 0) return;
    const rw = nouns[Math.floor(Math.random() * nouns.length)];
    appState.currentWotd = rw;
    els.homeWotdTitle.textContent = `${rw.article} ${rw.word}`;
    let sub = rw.translation;
    if(rw.plural) sub += ` (${rw.plural})`;
    els.homeWotdSub.textContent = sub;
}

function updateStats() {
    const streakElements = document.querySelectorAll('#streak');
    const xpElements = document.querySelectorAll('#xp, #fc-xp');
    const livesElements = document.querySelectorAll('#lives, #ddd-lives, #satz-lives');
    
    streakElements.forEach(el => el.textContent = appState.streak);
    xpElements.forEach(el => el.textContent = appState.xp);
    
    let displayLives = appState.isAdmin ? '∞' : appState.lives;
    livesElements.forEach(el => el.textContent = displayLives);
}

function switchView(viewId) {
    // Custom Navigation Guard
    if (appState.currentView === 'derdiedas' && viewId !== 'derdiedas') {
        pendingView = viewId;
        document.getElementById('custom-modal-overlay').style.display = 'flex';
        return; // Wait for modal response
    }
    executeSwitchView(viewId);
}

function executeSwitchView(viewId) {
    triggerVibrate(30);
    playSound('tap');
    
    const mascot = document.getElementById('global-mascot');
    if (mascot) mascot.classList.remove('show');
    
    // reset fox state
    const fox = document.getElementById('ddd-mascot-inner');
    if (fox) {
        fox.classList.remove('fail');
        document.getElementById('mascot-mouth').style.borderRadius = '0 0 10px 10px';
    }

    document.querySelectorAll('.view').forEach(v => v.style.display = 'none');
    document.getElementById('view-' + viewId).style.display = 'block';
    
    document.querySelectorAll('.nav-item').forEach(btn => btn.classList.remove('active'));
    const iconMap = { 'home': 0, 'derdiedas': 1, 'satzbau': 2, 'dictionary': 3, 'grammar': 4 };
    if (iconMap[viewId] !== undefined) {
        document.querySelectorAll('.nav-item')[iconMap[viewId]].classList.add('active');
    }

    appState.currentView = viewId;
    if (viewId === 'derdiedas') { renderCategories(); initDerDieDas(); }
    if (viewId === 'dictionary') { renderCategories(); renderDictionary(); }
        renderDictionary();
    if (viewId === 'satzbau') loadSatzbau();
    if (viewId === 'grammar') renderGrammar();
}

function initDerDieDas() {
    appState.failedCurrentWord = false; // Reset failure state for the new word

    // Re-enable and restore button colors
    document.querySelectorAll('.ddd-controls .btn-3d').forEach(b => {
        b.disabled = false;
        b.classList.remove('btn-disabled');
    });

    let categoryFiltered = appState.words;
    if (appState.selectedCategory && appState.selectedCategory !== 'all') {
        categoryFiltered = appState.words.filter(w => w.category === appState.selectedCategory);
    }
    const nouns = categoryFiltered.filter(w => w.article && ['der', 'die', 'das'].includes(w.article.toLowerCase()));
    
    if (nouns.length === 0) {
        // fallback if no nouns in this category
        document.getElementById('ddd-word').innerText = "Hech qanday so'z yo'q";
        document.getElementById('ddd-translation').innerText = "Boshqa bo'limni tanlang";
        appState.dddWord = null;
        return;
    }
    if(nouns.length === 0) return;
    
    // reset extra info
    document.getElementById('ddd-extra-info').style.display = 'none';
    document.getElementById('ddd-buttons-container').style.display = 'grid';

    // Shuffling algorithm: Deck/Bag system to prevent repeats
    if (!appState.dddQueue || appState.dddQueue.length === 0) {
        appState.dddQueue = [...nouns];
        for (let i = appState.dddQueue.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [appState.dddQueue[i], appState.dddQueue[j]] = [appState.dddQueue[j], appState.dddQueue[i]];
        }
    }
    appState.dddWord = appState.dddQueue.pop();
    
    els.dddWord.textContent = appState.dddWord.word;
    els.dddTrans.textContent = appState.dddWord.translation;
}


function getMnemonicForArticle(w) {
    if (w.article === 'der') return "Fritz Tip: Picture masculine words as active, bold characters or in vibrant blue. (Muzskoy so'zlarni ko'k rangda tasavvur qiling).";
    if (w.article === 'die') return "Fritz Tip: Feminine words often end in -e, -ung, -heit. Picture them in soft red. (Jenskiy so'zlarni qizil rangda tasavvur qiling).";
    if (w.article === 'das') return "Fritz Tip: Neuter words are solid and balanced. Picture them in natural green. (Sredniy so'zlarni yashil rangda tasavvur qiling).";
    return "";
}

function showDDDExtra() {
    const w = appState.dddWord;
    document.getElementById('ddd-buttons-container').style.display = 'none';
    document.getElementById('ddd-extra-info').style.display = 'block';
    
    document.getElementById('ddd-mnemonic-title').innerText = `${w.article.toUpperCase()} ${w.word}`;
    document.getElementById('ddd-mnemonic-badge').innerText = w.article.toUpperCase();
    document.getElementById('ddd-mnemonic-badge').style.color = w.article === 'der' ? '#0984E3' : (w.article === 'die' ? '#D63031' : '#00B894');
    document.getElementById('ddd-mnemonic-text').innerText = w.mnemonic || getMnemonicForArticle(w);
    
    let exDe = w.example || `Ich lerne das Wort "${w.word}".`;
    let exUz = w.example_uz || `Men "${w.word}" so'zini o'rganyapman.`;
    if(w.article === 'der') { exDe = `Der ${w.word} ist hier.`; exUz = `${w.word} shu yerda.`; }
    else if(w.article === 'die') { exDe = `Die ${w.word} ist schön.`; exUz = `${w.word} chiroyli.`; }
    else if(w.article === 'das') { exDe = `Das ${w.word} ist neu.`; exUz = `${w.word} yangi.`; }
    
    document.getElementById('ddd-example-de').innerText = exDe;
    document.getElementById('ddd-example-uz').innerText = exUz;
}

function checkArticle(guess) {
    if(!appState.dddWord) return;
    
    const correctArticle = appState.dddWord.article.toLowerCase();
    const correctMsg = TRANSLATIONS[appState.settings.language]['msg_correct'];
    const wrongMsg = TRANSLATIONS[appState.settings.language]['msg_ohno'];

    if(guess === correctArticle) {
        // Correct answer! Disable all buttons to prevent double tap
        document.querySelectorAll('.ddd-controls .btn-3d').forEach(b => {
            b.disabled = true;
            b.classList.add('btn-disabled');
        });
        // Keep the correct button highlighted
        const correctBtn = document.querySelector(`.btn-${correctArticle}`);
        if(correctBtn) correctBtn.classList.remove('btn-disabled');

        // Only award XP if they got it right on the first try!
        if (!appState.failedCurrentWord) {
            addXP(10);
        }

        playSound('success');
        triggerVibrate(40);
        showMascot(correctMsg, 1200); 
        setTimeout(initDerDieDas, 700); 
    } else {
        // Wrong answer!
        appState.failedCurrentWord = true;
        if (!loseHeart()) return;
        
        const explanation = typeof getGrammarExplanation === 'function' ? getGrammarExplanation(appState.dddWord, appState.settings.language) : '';
        
        playSound('error');
        triggerVibrate([100, 50, 100]);
        showMascot(`${wrongMsg} "${appState.dddWord.article} ${appState.dddWord.word}".<br><span style="font-size:14px; opacity:0.9; margin-top:5px; display:block; font-weight:normal;">${explanation}</span>`, 0);
        
        // Disable ONLY the button they just incorrectly tapped
        const wrongBtn = document.querySelector(`.btn-${guess}`);
        if (wrongBtn) {
            wrongBtn.disabled = true;
            wrongBtn.classList.add('btn-disabled');
        }
        
        // Notice: No setTimeout here! The app now waits for them to pick the right one.
    }
}


let flashcardWords = [];
let currentFlashcardIndex = 0;

function openFlashcards() {
    playSound('tap');
    const cat = appState.selectedCategory || 'all';
    let wordsToPick = cat === 'all' ? appState.words : appState.words.filter(w => w.category === cat);
    
    // shuffle and pick 20
    flashcardWords = wordsToPick.sort(() => 0.5 - Math.random()).slice(0, 20);
    if(flashcardWords.length === 0) return;
    
    currentFlashcardIndex = 0;
    document.getElementById('modal-flashcard').style.display = 'flex';
    updateFlashcardUI();
}

function closeFlashcards() {
    playSound('tap');
    document.getElementById('modal-flashcard').style.display = 'none';
}

function updateFlashcardUI() {
    const w = flashcardWords[currentFlashcardIndex];
    document.getElementById('fc-counter').innerText = `${currentFlashcardIndex + 1} / ${flashcardWords.length}`;
    document.getElementById('fc-word').innerText = w.word;
    document.getElementById('fc-category').innerText = w.category || 'Vocab';
    document.getElementById('fc-translation').innerText = w.translation;
    
    const inner = document.getElementById('fc-card-inner');
    inner.style.transform = 'rotateY(0deg)'; // reset flip
}

function flipFlashcard() {
    playSound('tap');
    const inner = document.getElementById('fc-card-inner');
    if (inner.style.transform === 'rotateY(180deg)') {
        inner.style.transform = 'rotateY(0deg)';
    } else {
        inner.style.transform = 'rotateY(180deg)';
    }
}

function nextFlashcard() {
    playSound('tap');
    if (currentFlashcardIndex < flashcardWords.length - 1) {
        currentFlashcardIndex++;
        updateFlashcardUI();
    } else {
        closeFlashcards();
    }
}

function prevFlashcard() {
    playSound('tap');
    if (currentFlashcardIndex > 0) {
        currentFlashcardIndex--;
        updateFlashcardUI();
    }
}

appState.selectedCategory = 'all';


function renderCategories() {
    // Update labels
    const dLabel = document.getElementById('dict-category-label');
    const dddLabel = document.getElementById('ddd-category-label');
    const fcLabel = document.getElementById('fc-category-label');
    
    let displayTxt = appState.selectedCategory === 'all' ? "Barcha bo'limlar" : appState.selectedCategory;
    if (dLabel) dLabel.textContent = displayTxt;
    if (dddLabel) dddLabel.textContent = displayTxt;
    if (fcLabel) fcLabel.textContent = displayTxt;
}

function openCategoryModal() {
    const listContainer = document.getElementById('category-modal-list');
    listContainer.innerHTML = '';
    
    let cats = [...new Set(appState.words.map(w => w.category).filter(Boolean))];
    
    // If in Der Die Das, filter out categories that have NO nouns
    if (appState.currentView === 'derdiedas') {
        cats = cats.filter(c => {
            return appState.words.some(w => w.category === c && w.article && ['der', 'die', 'das'].includes(w.article.toLowerCase()));
        });
    }
    
    // Natural sort
    cats.sort((a, b) => {
        return a.localeCompare(b, undefined, {numeric: true, sensitivity: 'base'});
    });
    
    let html = `<button class="category-list-item ${appState.selectedCategory === 'all' ? 'active' : ''}" onclick="selectCategory('all')">Barcha bo'limlar</button>`;
    cats.forEach(c => {
        html += `<button class="category-list-item ${appState.selectedCategory === c ? 'active' : ''}" onclick="selectCategory('${c.replace(/'/g, "\'")}')">${c}</button>`;
    });
    
    listContainer.innerHTML = html;
    document.getElementById('category-modal').style.display = 'flex';
}

function closeCategoryModal() {
    document.getElementById('category-modal').style.display = 'none';
}

function selectCategory(cat) {
    playSound('tap');
    appState.selectedCategory = cat;
    appState.dddQueue = []; // Reset queue
    renderCategories();
    closeCategoryModal();
    
    if (appState.currentView === 'dictionary') {
        renderDictionary();
    } else if (appState.currentView === 'derdiedas') {
        initDerDieDas();
    } else if (appState.currentView === 'flashcards') {
        startFlashcards();
    }
}


// Intercept renderDictionary to filter by category

function renderDictionary() {
    const query = (els.dddSearch && els.dddSearch.value) ? els.dddSearch.value.toLowerCase() : "";
    const list = document.getElementById('dict-list');
    list.innerHTML = '';
    
    // FIRST filter by category
    let categoryFiltered = appState.words;
    if (appState.selectedCategory && appState.selectedCategory !== 'all') {
        categoryFiltered = appState.words.filter(w => w.category === appState.selectedCategory);
    }
    
    // THEN filter by search query
    const filtered = categoryFiltered.filter(w => w.word.toLowerCase().includes(query) || (w.translation && w.translation.toLowerCase().includes(query)));
    
    filtered.forEach(w => {
        const div = document.createElement('div');
        div.className = 'dict-item';
        let artHtml = w.article ? `<span class="artikel">${w.article}</span> ` : '';
        let pluralHtml = w.plural ? ` (Pl: ${w.plural})` : '';
        div.innerHTML = `
            <div>
                <h4>${artHtml}${w.word}</h4>
                <p>${w.translation}${pluralHtml}</p>
            </div>
            <button class="icon-btn small-btn" onclick="speakText('${w.article ? w.article + ' ' : ''}${w.word}')"><i data-lucide="volume-2"></i></button>
        `;
        list.appendChild(div);
    });
    if(typeof lucide !== 'undefined') lucide.createIcons();
}

function showMascot(text, duration = 3500) {
    document.getElementById('mascot-msg').innerHTML = text;
    const mascot = document.getElementById('global-mascot');
    mascot.classList.add('show');
    if(window.mascotTimeout) clearTimeout(window.mascotTimeout);
    if(duration > 0) {
        window.mascotTimeout = setTimeout(() => { mascot.classList.remove('show'); }, duration);
    }
}

function triggerVibrate(pattern) {
    if (appState.settings.vibration && 'vibrate' in navigator) navigator.vibrate(pattern);
}

function playSound(type) {
    if (!appState.settings.sound) return;

    try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain); gain.connect(ctx.destination);
        if (type === 'success') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(800, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(1200, ctx.currentTime + 0.1);
            gain.gain.setValueAtTime(0.5, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.1);
            osc.start(); osc.stop(ctx.currentTime + 0.1);
        } else if (type === 'error') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(150, ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(80, ctx.currentTime + 0.3);
            gain.gain.setValueAtTime(0.5, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
            osc.start(); osc.stop(ctx.currentTime + 0.3);
        } else if (type === 'tap') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(600, ctx.currentTime);
            gain.gain.setValueAtTime(0.05, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.05);
            osc.start(); osc.stop(ctx.currentTime + 0.05);
        }
    } catch(e) {}
}

function speakText(text) {
    if (!appState.settings.sound) return;
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'de-DE';
        window.speechSynthesis.speak(utterance);
    }
}

window.addEventListener('DOMContentLoaded', initApp);

// --- SATZBAU LOGIC ---
function loadSatzbau() {
    if (!appState.satzSentences || appState.satzSentences.length === 0) return;
    
    // Reset state
    // appState.satzLives is deprecated; we use global lives now
    updateStats();
    
    startSatzbauRound();
}

let satzSortableDropzone, satzSortableTiles;

function startSatzbauRound() {
    const eb = document.getElementById('satzbau-error-box');
    if(eb) eb.style.display = 'none';
    
    // Shuffling algorithm: Deck/Bag system to prevent repeats
    if (!appState.satzQueue || appState.satzQueue.length === 0) {
        appState.satzQueue = [...appState.satzSentences];
        for (let i = appState.satzQueue.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [appState.satzQueue[i], appState.satzQueue[j]] = [appState.satzQueue[j], appState.satzQueue[i]];
        }
    }
    const sentence = appState.satzQueue.pop();
    appState.currentSentence = sentence;
    
    document.getElementById('satz-translation').textContent = sentence.uz;
    
    const words = sentence.de.replace(/[.!?]/g, '').split(' ');
    const cleanWords = words.filter(w => w.trim().length > 0);
    
    for(let i = cleanWords.length - 1; i > 0; i--){
        const j = Math.floor(Math.random() * (i + 1));
        [cleanWords[i], cleanWords[j]] = [cleanWords[j], cleanWords[i]];
    }
    
    appState.satzAvailableWords = cleanWords;
    renderSatzbau();
}

function renderSatzbau() {
    const tilesContainer = document.getElementById('satz-tiles');
    const dropzone = document.getElementById('satz-dropzone');
    const checkBtn = document.getElementById('satz-check-btn');
    
    tilesContainer.innerHTML = '';
    dropzone.innerHTML = '';
    checkBtn.style.display = 'block'; // Always show button, or check dynamically
    
    appState.satzAvailableWords.forEach((word) => {
        const btn = document.createElement('button');
        btn.className = 'satz-tile';
        btn.textContent = word;
        btn.onclick = () => {
            playSound('tap');
            if (btn.parentElement === tilesContainer) {
                dropzone.appendChild(btn);
            } else {
                tilesContainer.appendChild(btn);
            }
        };
        tilesContainer.appendChild(btn);
    });
    
    // Initialize SortableJS
    if (window.Sortable) {
        if (satzSortableDropzone) satzSortableDropzone.destroy();
        if (satzSortableTiles) satzSortableTiles.destroy();
        
        satzSortableDropzone = new Sortable(dropzone, {
            group: 'satzbau',
            animation: 150,
            onEnd: () => playSound('tap')
        });
        
        satzSortableTiles = new Sortable(tilesContainer, {
            group: 'satzbau',
            animation: 150,
            onEnd: () => playSound('tap')
        });
    }
}

function checkSatzbau() {
    const target = appState.currentSentence.de.replace(/[.!?]/g, '').toLowerCase().trim();
    
    const dropzone = document.getElementById('satz-dropzone');
    const currentWords = [];
    dropzone.querySelectorAll('.satz-tile').forEach(btn => {
        currentWords.push(btn.textContent);
    });
    const current = currentWords.join(' ').toLowerCase().trim();
    const checkBtn = document.getElementById('satz-check-btn');
    const errorBox = document.getElementById('satzbau-error-box');
    
    if (current === target) {
        playSound('success');
        addXP(15);
        dropzone.style.borderColor = 'var(--green-btn)';
        dropzone.style.backgroundColor = '#e8fce8';
        if (checkBtn) checkBtn.style.display = 'none';
        
        // Show correct mascot!
        const correctMsg = TRANSLATIONS[appState.settings.language]['msg_correct'];
        showMascot(correctMsg, 1500);
        
        setTimeout(() => {
            dropzone.style.borderColor = '#ccc';
            dropzone.style.backgroundColor = '#f7f7f7';
            startSatzbauRound();
        }, 1500);
    } else {
        playSound('error');
        if (!loseHeart()) return;
        
        dropzone.style.borderColor = 'var(--red-btn)';
        dropzone.style.backgroundColor = '#ffebeb';
        
        // Shake animation
        dropzone.style.transition = 'transform 0.05s';
        dropzone.style.transform = 'translateX(5px)';
        setTimeout(() => dropzone.style.transform = 'translateX(-5px)', 50);
        setTimeout(() => dropzone.style.transform = 'translateX(5px)', 100);
        setTimeout(() => dropzone.style.transform = 'translateX(-5px)', 150);
        setTimeout(() => dropzone.style.transform = 'translateX(0)', 200);
        
        // Show the error box
        if (checkBtn) checkBtn.style.display = 'none';
        if (errorBox) {
            errorBox.style.display = 'block';
            document.getElementById('satzbau-correct-text').innerText = appState.currentSentence.de;
            if (appState.currentSentence.explanation) {
                document.getElementById('satzbau-explanation').innerText = appState.currentSentence.explanation;
            } else {
                document.getElementById('satzbau-explanation').innerText = "Nemis tilida darak gaplarda fe'l 2-o'rinda keladi.";
            }
        }
    }
}

// --- GRAMMAR TAB LOGIC ---


function renderGrammar() {
    const container = document.getElementById('grammar-cards-container');
    if (!container) return;
    container.innerHTML = '';

    GRAMMAR_DATA.forEach((chap, idx) => {
        const card = document.createElement('div');
        card.className = 'grammar-item';
        card.style.marginBottom = '12px';
        card.style.cursor = 'pointer';
        
        card.innerHTML = `
            <div class="grammar-header" style="background: #fff;">
                <span style="font-size: 16px; font-weight: 800; color: #2D3436;">${chap.title}</span>
                <span style="font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 12px; background: #E8F8F5; color: #16A085; border: 1px solid #16A085;">${chap.tag}</span>
            </div>
            <div class="grammar-body" style="display: block; max-height: none; padding: 0 20px 15px 20px; background: #fff; border-bottom: 2px solid transparent;">
                <p style="font-size:13px; color:var(--text-muted); line-height:1.4;">${chap.summary}</p>
            </div>
        `;
        
        card.onclick = () => openGrammarChapter(idx);
        container.appendChild(card);
    });
}

let activeGrammarChap = null;

function openGrammarChapter(idx) {
    playSound('tap');
    activeGrammarChap = GRAMMAR_DATA[idx];
    document.getElementById('gm-title').innerText = activeGrammarChap.title;
    document.getElementById('gm-summary').innerText = activeGrammarChap.summary;
    document.getElementById('gm-fritz-tip').innerText = activeGrammarChap.fritz_tip;

    const rulesBox = document.getElementById('gm-rules-list');
    rulesBox.innerHTML = '';
    activeGrammarChap.rules.forEach(r => {
        const div = document.createElement('div');
        div.style.marginBottom = '10px';
        div.innerHTML = `<span style="font-weight:800; font-size:16px; color:#0984E3;">• ${r.label}:</span> <span style="font-size:15px; color:#2D3436; line-height:1.5;">${r.tip}</span>`;
        rulesBox.appendChild(div);
    });

    const tableBox = document.getElementById('gm-table-container');
    tableBox.innerHTML = '';
    if (activeGrammarChap.table) {
        let ths = activeGrammarChap.table.headers.map(h => `<th>${h}</th>`).join('');
        let trs = activeGrammarChap.table.rows.map(row => `<tr>${row.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
        tableBox.innerHTML = `<div style="width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; margin-bottom: 16px;"><table class="rule-table" style="min-width: 450px;"><thead><tr>${ths}</tr></thead><tbody>${trs}</tbody></table></div>`;
    }

    const quizBox = document.getElementById('gm-quiz-container');
    quizBox.innerHTML = '';
    activeGrammarChap.quiz.forEach((qObj, qIdx) => {
        const qDiv = document.createElement('div');
        qDiv.style.margin = '14px 0';
        qDiv.style.background = '#F8F9FA';
        qDiv.style.border = '2px solid var(--border-color)';
        qDiv.style.borderRadius = '14px';
        qDiv.style.padding = '14px 16px';
        
        let opts = qObj.options.map((opt, oIdx) => `
            <button style="margin-top:8px; font-size:15px; font-weight:800; color:#2D3436; background:#fff; border:2px solid var(--border-color); border-radius:12px; padding:12px 16px; width: 100%; text-align:left; cursor:pointer; box-shadow: 0 4px 0 var(--border-color);" onclick="answerGrammarQuiz(${qIdx}, ${oIdx}, this)">
                ${opt}
            </button>
        `).join('');

        qDiv.innerHTML = `
            <div style="font-weight:800; font-size:16px; margin-bottom:8px; color:#2D3436;">Frage ${qIdx + 1}: ${qObj.q}</div>
            <div class="opts-group" id="quiz-opts-${qIdx}">${opts}</div>
            <div id="quiz-feedback-${qIdx}" style="font-size:14px; font-weight:700; margin-top:10px; display:none; line-height:1.5;"></div>
        `;
        quizBox.appendChild(qDiv);
    });

    const modal = document.getElementById('modal-grammar-detail');
    modal.style.display = 'flex';
}

function answerGrammarQuiz(qIdx, oIdx, btn) {
    if (!activeGrammarChap) return;
    const qObj = activeGrammarChap.quiz[qIdx];
    const feed = document.getElementById(`quiz-feedback-${qIdx}`);
    const parent = document.getElementById(`quiz-opts-${qIdx}`);
    
    parent.querySelectorAll('button').forEach(b => b.disabled = true);
    
    feed.style.display = 'block';
    if (oIdx === qObj.answer) {
        playSound('success');
        btn.style.background = '#55EFC4';
        feed.style.color = '#00B894';
        feed.innerText = '✅ Richtig! ' + qObj.hint;
        addXP(10);
    } else {
        playSound('error');
        btn.style.background = '#FF7675';
        feed.style.color = '#D63031';
        feed.innerText = '❌ Nicht ganz: ' + qObj.hint;
    }
}

function closeGrammarModal() {
    playSound('tap');
    document.getElementById('modal-grammar-detail').style.display = 'none';
}


// --- FLASHCARDS LOGIC ---

function startFlashcards() {
    switchView('flashcards');
    
    // Build Queue based on selected category
    let wordsArray = appState.words;
    let levelPrefix = appState.currentLevel === 'A1' ? 'Goethe A1' : 'Medizin';
    
    if (appState.selectedCategory && appState.selectedCategory !== 'all') {
        wordsArray = appState.words.filter(w => w.category === appState.selectedCategory);
    } else {
        wordsArray = appState.words.filter(w => w.category && w.category.startsWith(levelPrefix));
    }
    
    if (window.SRS) {
        appState.fcQueue = window.SRS.buildQueue(wordsArray, 15);
    } else {
        // Fallback if srs-engine didn't load
        appState.fcQueue = [...wordsArray].slice(0, 15);
    }
    
    loadNextFlashcard();
}

function loadNextFlashcard() {
    document.getElementById('fc-queue-count').textContent = appState.fcQueue.length;
    
    const cardEl = document.getElementById('fc-card');
    const frontEl = cardEl.querySelector('.fc-front');
    const backEl = cardEl.querySelector('.fc-back');
    const btnsEl = document.getElementById('fc-rating-buttons');
    const msgEl = document.getElementById('fc-done-msg');
    
    if (appState.fcQueue.length === 0) {
        cardEl.style.display = 'none';
        btnsEl.style.display = 'none';
        msgEl.style.display = 'block';
        return;
    }
    
    msgEl.style.display = 'none';
    cardEl.style.display = 'flex';
    frontEl.style.display = 'block';
    backEl.style.display = 'none';
    btnsEl.style.display = 'none';
    
    // Get next word (first in queue)
    appState.currentFcWord = appState.fcQueue[0];
    
    document.getElementById('fc-word').textContent = appState.currentFcWord.word;
    
    let artHtml = appState.currentFcWord.article ? appState.currentFcWord.article + ' ' : '';
    document.getElementById('fc-word-back').textContent = artHtml + appState.currentFcWord.word;
    
    if (appState.currentFcWord.plural) {
        document.getElementById('fc-plural').textContent = `(Pl: ${appState.currentFcWord.plural})`;
        document.getElementById('fc-plural').style.display = 'block';
    } else {
        document.getElementById('fc-plural').style.display = 'none';
    }
    
    document.getElementById('fc-translation').textContent = appState.currentFcWord.translation;
}

function flipFlashcard() {
    const cardEl = document.getElementById('fc-card');
    const frontEl = cardEl.querySelector('.fc-front');
    const backEl = cardEl.querySelector('.fc-back');
    const btnsEl = document.getElementById('fc-rating-buttons');
    
    if (frontEl.style.display !== 'none') {
        playSound('tap');
        frontEl.style.display = 'none';
        backEl.style.display = 'block';
        btnsEl.style.display = 'grid';
        
        speakText(document.getElementById('fc-word-back').textContent);
    }
}

function rateCard(quality) {
    if (!appState.currentFcWord) return;
    
    playSound('tap');
    
    if (window.SRS) {
        window.SRS.reviewCard(appState.currentFcWord.id, quality);
    }
    
    // Remove from front of queue
    appState.fcQueue.shift();
    
    // If it was a 'fail' (quality 1), maybe we push it to the back of the queue so they see it again today?
    if (quality === 1) {
        appState.fcQueue.push(appState.currentFcWord);
    }
    
    // XP reward
    addXP(5);
    
    loadNextFlashcard();
}


function openLevelModal() {
    playSound('tap');
    document.getElementById('level-modal').style.display = 'flex';
}

function closeLevelModal() {
    playSound('tap');
    document.getElementById('level-modal').style.display = 'none';
}

function selectLevel(levelStr) {
    playSound('tap');
    localStorage.setItem('wunderdeutsch_level', levelStr);
    appState.currentLevel = levelStr;
    
    let display = levelStr === 'A1' ? 'Level: A1' : 'Medizin B2 🩺';
    document.getElementById('current-level-display').innerText = display;
    
    // Automatically select 'all' categories of the new level
    appState.selectedCategory = 'all';
    
    renderCategories();
    closeLevelModal();
    updateHomeUIForLevel();
    
    // Refresh current view if needed
    if (appState.currentView === 'flashcards') {
        startFlashcards();
    } else if (appState.currentView === 'derdiedas') {
        initDerDieDas();
    }
}


let toastTimeout;
function showComingSoonToast() {
    playSound('tap');
    const toast = document.getElementById('toast-notification');
    if (!toast) return;
    
    let msg = "Tez orada! (Coming soon)";
    if (appState.settings.language === 'en') msg = "Coming soon!";
    if (appState.settings.language === 'de') msg = "Kommt bald!";
    
    document.getElementById('toast-message').innerText = msg;
    
    toast.style.bottom = '40px';
    
    clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => {
        toast.style.bottom = '-100px';
    }, 3000);
}


function updateHomeUIForLevel() {
    const isMed = appState.currentLevel === 'Medizin';
    
    // Update Mascot text
    const mascotSub = document.querySelector('.mascot-section .speech-bubble .small');
    if (mascotSub) {
        if (isMed) {
            if (appState.settings.language === 'uz') mascotSub.innerText = "Salom doktor! Tibbiy nemis tilini o'rganamiz!";
            else if (appState.settings.language === 'en') mascotSub.innerText = "Hello doctor! Let's learn Medical German!";
            else mascotSub.innerText = "Hallo Herr Doktor! Lass uns medizinisches Deutsch lernen!";
        } else {
            mascotSub.innerText = TRANSLATIONS[appState.settings.language]['mascot_sub'];
        }
    }
    
    // Update Menu Titles
    const btnDDD = document.querySelector('.menu-card.blue h3');
    const btnSatz = document.querySelector('.menu-card.green h3');
    const btnDict = document.querySelector('.menu-card.yellow h3');
    
    if (btnDDD && btnSatz && btnDict) {
        if (isMed) {
            btnDDD.innerText = "Tibbiyot: Der Die Das";
            btnSatz.innerText = "Klinik Gaplar";
            btnDict.innerText = "Tibbiy Lug'at";
        } else {
            btnDDD.innerText = TRANSLATIONS[appState.settings.language]['title_ddd'];
            btnSatz.innerText = TRANSLATIONS[appState.settings.language]['title_satzbau'];
            btnDict.innerText = TRANSLATIONS[appState.settings.language]['title_dict'];
        }
    }
}
