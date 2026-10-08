import json
import re

uz_grammar = [
  {
    "id": "gender_articles",
    "title": "1. Der, Die, Das & Rod belgilari",
    "tag": "Artikllar",
    "summary": "Nemis tilida otlar 3 ta rodga ega: Muzskoy (der), Jenskiy (die) va Sredniy (das). Ko'plikdagi otlar doim 'die' artiklini oladi.",
    "color": "#74B9FF",
    "rules": [
      {"label": "Der (Muzskoy)", "tip": "Erkak kishilar/hayvonlar, kunlar, oylar, fasllar va -er, -ling, -or, -ismus bilan tugovchi otlar (der Sommer, der Montag, der Lehrer)."},
      {"label": "Die (Jenskiy)", "tip": "Ayol kishilar/hayvonlar, va -ung, -heit, -keit, -schaft, -tion, -tät, -ei bilan tugovchi otlar (die Zeitung, die Freiheit, die Bäckerei)."},
      {"label": "Das (Sredniy)", "tip": "-chen, -lein kichraytirish qo'shimchalari, fe'ldan yasalgan otlar va -ment, -um, -tum bilan tugovchi otlar (das Mädchen, das Brötchen, das Essen, das Museum)."},
      {"label": "Die (Ko'plik)", "tip": "Barcha ko'plikdagi otlar, original rodidan qat'i nazar, Nominativ kelishigida 'die' oladi!"}
    ],
    "table": {
      "headers": ["Rod", "Aniq (The)", "Noaniq (A/An)", "Inkor (No/None)"],
      "rows": [
        ["Muzskoy", "der Tisch", "ein Tisch", "kein Tisch"],
        ["Jenskiy", "die Katze", "eine Katze", "keine Katze"],
        ["Sredniy", "das Buch", "ein Buch", "kein Buch"],
        ["Ko'plik", "die Kinder", "(ko'plik yo'q)", "keine Kinder"]
      ]
    },
    "fritz_tip": "So'zning oxiriga e'tibor bering! -ung, -heit, -keit, va -schaft bilan tugaydigan so'zlarning 99% qismi DIE hisoblanadi. -chen yoki -lein bilan tugaydiganlar esa doim DAS (hatto das Mädchen ham)! 🦊💡",
    "quiz": [
      {"q": "'Zeitung' (gazeta) uchun artikl qaysi?", "options": ["der", "die", "das"], "answer": 1, "hint": "-ung bilan tugovchi so'zlar doim jenskiy rodda!"},
      {"q": "'Mädchen' (qiz) uchun artikl qaysi?", "options": ["der", "die", "das"], "answer": 2, "hint": "-chen kichraytirish qo'shimchasi otni doim sredniy rodga aylantiradi!"},
      {"q": "Ko'plikdagi otlar Nominativda qaysi artiklni oladi?", "options": ["der", "die", "das"], "answer": 1, "hint": "Ko'plik doim Nominativda 'die' oladi."}
    ]
  },
  {
    "id": "cases_nom_akk",
    "title": "2. Kelishiklar: Nominativ va Akkusativ",
    "tag": "Kelishiklar",
    "summary": "Nominativ kelishigi EGANI (harakatni bajaruvchini) bildiradi. Akkusativ kelishigi esa TO'LDIRUVCHINI (harakat kimga/nimaga qaratilganligini) bildiradi.",
    "color": "#FF7675",
    "rules": [
      {"label": "Sehrli o'zgarish", "tip": "Akkusativda FAQAT muzskoy rod o'zgaradi: der -> den, ein -> einen, kein -> keinen. Jenskiy, Sredniy va Ko'plik o'zgarmaydi!"},
      {"label": "Ega (Wer/Was? - Kim/Nima?)", "tip": "Der Mann trinkt einen Kaffee. -> 'Der Mann' bu yerda ega (Nominativ)."},
      {"label": "To'ldiruvchi (Wen/Was? - Kimni/Nimani?)", "tip": "Er trinkt den Kaffee. -> 'den Kaffee' bu yerda to'ldiruvchi (Akkusativ)."},
      {"label": "Akkusativ talab qiluvchi predloglar", "tip": "bis, durch, für, gegen, ohne, um. Bu predloglardan keyin DOIM Akkusativ keladi!"}
    ],
    "table": {
      "headers": ["Kelishik", "Muzskoy", "Jenskiy", "Sredniy", "Ko'plik"],
      "rows": [
        ["Nominativ", "der / ein / kein", "die / eine / keine", "das / ein / kein", "die / - / keine"],
        ["Akkusativ", "den / einen / keinen", "die / eine / keine", "das / ein / kein", "die / - / keine"]
      ]
    },
    "fritz_tip": "Eslab qoling: Akkusativda faqat muzskoy rod 'N' harfini oladi! 'Ich habe EINEN Hund (m), EINE Katze (f), EIN Auto (n)'. 🦊🐶",
    "quiz": [
      {"q": "Bo'sh joyni to'ldiring: 'Ich kaufe _____ Apfel (m)'.", "options": ["ein", "einen", "eine"], "answer": 1, "hint": "Apfel muzskoy rod va bu yerda to'ldiruvchi: ein -> einen."},
      {"q": "Qaysi predlog DOIM Akkusativ talab qiladi?", "options": ["mit", "nach", "für"], "answer": 2, "hint": "'für' doim akkusativ oladi (Das ist für dich!)."},
      {"q": "Jenskiy roddagi 'die Tasche' Akkusativda qanday o'zgaradi?", "options": ["'den' ga", "'der' ga", "'die' bo'lib qoladi"], "answer": 2, "hint": "Jenskiy va Sredniy rodlar Nominativ va Akkusativda umuman o'zgarmaydi."}
    ]
  },
  {
    "id": "cases_dative",
    "title": "3. Dativ kelishigi asoslari",
    "tag": "Kelishiklar",
    "summary": "Dativ kelishigi VOSITALI TO'LDIRUVCHINI (kimga / kim uchun) bildiradi va ba'zi muhim predloglardan keyin ishlatiladi.",
    "color": "#55EFC4",
    "rules": [
      {"label": "Dativ artikl o'zgarishlari", "tip": "der -> dem, das -> dem, die -> der, die (ko'plik) -> den + ot oxiriga 'n' qo'shiladi!"},
      {"label": "Dativ talab qiluvchi predloglar", "tip": "aus, bei, mit, nach, seit, von, zu (Yodlab oling: aus-bei-mit, nach-seit-von-zu!)."},
      {"label": "Dativ oluvchi ko'p uchraydigan fe'llar", "tip": "helfen (hilf mir!), danken (ich danke dir), gefallen (das gefällt mir), schmecken (das schmeckt mir)."}
    ],
    "table": {
      "headers": ["Rod", "Nominativ", "Akkusativ", "Dativ"],
      "rows": [
        ["Muzskoy", "der / ein", "den / einen", "dem / einem"],
        ["Jenskiy", "die / eine", "die / eine", "der / einer"],
        ["Sredniy", "das / ein", "das / ein", "dem / einem"],
        ["Ko'plik", "die / -", "die / -", "den / - (+n)"]
      ]
    },
    "fritz_tip": "Sehrli qofiyani kuylang: 'Aus, bei, mit, nach, seit, von, zu — immer mit dem Dativ, du!' 🎶🦊",
    "quiz": [
      {"q": "To'ldiring: 'Ich fahre mit _____ Bus (m)'.", "options": ["den", "dem", "der"], "answer": 1, "hint": "'mit' predlogi Dativ talab qiladi, shuning uchun 'der' 'dem' ga aylanadi."},
      {"q": "Jenskiy roddagi 'die' Dativda nimaga aylanadi?", "options": ["dem", "der", "den"], "answer": 1, "hint": "Jenskiy 'die' Dativda 'der' ga aylanadi."},
      {"q": "Qaysi fe'l doim Dativ to'ldiruvchi oladi?", "options": ["helfen", "kaufen", "sehen"], "answer": 0, "hint": "'helfen' Dativ oladi: 'Ich helfe dir'."}
    ]
  },
  {
    "id": "verb_conjugation",
    "title": "4. Hozirgi zamon fe'l tuslanishi",
    "tag": "Fe'llar",
    "summary": "Nemis tilida fe'llar egaga qarab o'z qo'shimchalarini o'zgartiradi: -e, -st, -t, -en, -t, -en.",
    "color": "#FFEAA7",
    "rules": [
      {"label": "To'g'ri (Muntazam) qo'shimchalar", "tip": "ich -e | du -st | er/sie/es -t | wir -en | ihr -t | sie/Sie -en."},
      {"label": "O'zak unlisi o'zgaradigan fe'llar (du/er)", "tip": "e -> i/ie (sprechen -> du sprichst, lesen -> er liest); a -> ä (fahren -> du fährst, schlafen -> er schläft)."},
      {"label": "-t yoki -d bilan tugaydigan fe'llar", "tip": "Talaffuz uchun qo'shimcha 'e' qo'shiladi: arbeiten -> du arbeitest, er arbeitet."}
    ],
    "table": {
      "headers": ["Olmosh", "lernen (to'g'ri)", "fahren (a->ä)", "sprechen (e->i)"],
      "rows": [
        ["ich", "lerne", "fahre", "spreche"],
        ["du", "lernst", "fährst", "sprichst"],
        ["er / sie / es", "lernt", "fährt", "spricht"],
        ["wir", "lernen", "fahren", "sprechen"],
        ["ihr", "lernt", "fahrt", "sprecht"],
        ["sie / Sie", "lernen", "fahren", "sprechen"]
      ]
    },
    "fritz_tip": "Eslab qoling: 'E - ST - T - EN - T - EN'. Infinitivdan -en ni olib tashlang va mos qo'shimchani qo'shing! 🦊✨",
    "quiz": [
      {"q": "Tuslang: 'Du _____ (sprechen) sehr gut Deutsch.'", "options": ["sprechtest", "sprechst", "sprichst"], "answer": 2, "hint": "'sprechen' dagi 'e' unlisi 'du' va 'er/sie/es' uchun 'i' ga o'zgaradi."},
      {"q": "Tuslang: 'Er _____ (fahren) mit dem Zug.'", "options": ["fahrt", "fährst", "fährt"], "answer": 2, "hint": "'fahren' 3-shaxs birlikda umlaut (ä) oladi."},
      {"q": "'wir' (biz) uchun fe'l qo'shimchasi qanday?", "options": ["-e", "-t", "-en"], "answer": 2, "hint": "'wir' doim '-en' oladi (infinitiv bilan bir xil)."}
    ]
  },
  {
    "id": "sein_haben",
    "title": "5. Katta Uchtalik: Sein, Haben va Werden",
    "tag": "Fe'llar",
    "summary": "Bu uchta noto'g'ri yordamchi fe'l nemis tili so'zlashuvining va o'tgan/kelasi zamonlarning asosiy poydevori hisoblanadi.",
    "color": "#A29BFE",
    "rules": [
      {"label": "sein (bo'lmoq)", "tip": "Shaxsni, kasbni, joylashuvni va sifatlarni ifodalash uchun muhim: 'Ich bin glücklich' (Men baxtliman)."},
      {"label": "haben (ega bo'lmoq)", "tip": "Egalikni va ko'plab iboralarni ifodalaydi: 'Ich habe Hunger/Durst/Zeit'."},
      {"label": "werden (aylanmoq/bo'lmoq)", "tip": "Holat o'zgarishi va kelasi zamon uchun ishlatiladi: 'Es wird kalt' (Sovuq bo'lyapti)."}
    ],
    "table": {
      "headers": ["Olmosh", "sein (bo'lmoq)", "haben (ega bo'lmoq)", "werden (aylanmoq)"],
      "rows": [
        ["ich", "bin", "habe", "werde"],
        ["du", "bist", "hast", "wirst"],
        ["er / sie / es", "ist", "hat", "wird"],
        ["wir", "sind", "haben", "werden"],
        ["ihr", "seid", "habt", "werdet"],
        ["sie / Sie", "sind", "haben", "werden"]
      ]
    },
    "fritz_tip": "'ihr seid' (sizlar) va 'sie sind' (ular) farqiga e'tibor bering. Ularni adashtirib qo'yish juda oson! 🦊",
    "quiz": [
      {"q": "To'ldiring: 'Wir _____ zwei Brüder.' (Bizning ikkita akamiz bor).", "options": ["sind", "haben", "werdet"], "answer": 1, "hint": "Oila a'zolariga ega bo'lish uchun 'haben' ishlatiladi."},
      {"q": "To'ldiring: 'Wie alt _____ du?' (Yoshing nechada?).", "options": ["hast", "bist", "wirst"], "answer": 1, "hint": "Nemis tilida yosh 'sein' (bo'lmoq) fe'li bilan aytiladi, 'haben' bilan emas."},
      {"q": "'sein' fe'lining 'ihr' (sizlar) shakli qanday?", "options": ["sind", "seid", "bist"], "answer": 1, "hint": "'ihr seid' bu 2-shaxs ko'plik shakli."}
    ]
  },
  {
    "id": "modal_verbs",
    "title": "6. Modal fe'llar va Gap qavsi",
    "tag": "Modal Fe'llar",
    "summary": "Modal fe'llar qobiliyat, zaruriyat yoki xohishni ifodalaydi. Ular asosiy fe'lni (infinitivda) gapning eng oxiriga surib yuboradi!",
    "color": "#FDCB6E",
    "rules": [
      {"label": "können (qila olmoq)", "tip": "ich kann, du kannst, er kann, wir können"},
      {"label": "müssen (shart/majbur)", "tip": "ich muss, du musst, er muss, wir müssen"},
      {"label": "wollen (xohlamoq/istamoq)", "tip": "ich will, du willst, er will, wir wollen"},
      {"label": "möchten (xohlardim)", "tip": "ich möchte, du möchtest, er möchte, wir möchten"},
      {"label": "dürfen (ruxsat bo'lmoq)", "tip": "ich darf, du darfst, er darf, wir dürfen"},
      {"label": "sollen (kerak/lozim)", "tip": "ich soll, du sollst, er soll, wir sollen"}
    ],
    "table": {
      "headers": ["1-o'rin", "2-o'rin (Modal)", "O'rta (Vaqt/Joy/Obyekt)", "Oxiri (Infinitiv)"],
      "rows": [
        ["Ich", "kann", "gut Deutsch", "sprechen."],
        ["Wir", "müssen", "heute die Hausaufgaben", "machen."],
        ["Er", "möchte", "einen Kaffee", "trinken."]
      ]
    },
    "fritz_tip": "E'tibor bering: barcha modal fe'llarda 'ich' va 'er/sie/es' shakllari BIR XIL: 'ich kann' = 'er kann'! 🦊🎉",
    "quiz": [
      {"q": "Modal fe'l qatnashgan gapda ikkinchi asosiy fe'l qayerda keladi?", "options": ["Modal fe'ldan darhol keyin", "Gapning eng oxirida", "Egadan oldin"], "answer": 1, "hint": "Infinitiv shakldagi asosiy fe'l gapni oxirida yopib turadi (qavs)."},
      {"q": "Tuslang: 'Er _____ (können) sehr schnell laufen.'", "options": ["kann", "könnt", "kannst"], "answer": 0, "hint": "'können' ning 3-shaxs birlik shakli 'kann' (-t qo'shilmaydi!)."},
      {"q": "Qaysi modal fe'l 'ruxsat' ma'nosini bildiradi?", "options": ["müssen", "wollen", "dürfen"], "answer": 2, "hint": "'dürfen' ruxsat etilgan, mumkin degan ma'noni bildiradi."}
    ]
  },
  {
    "id": "word_order",
    "title": "7. So'z tartibi va Oltin V2 qoidasi",
    "tag": "Sintaksis",
    "summary": "Asosiy gaplarda tuslangan fe'l DOIM 2-o'rinda keladi. Hatto gapni vaqt yoki joy bilan boshlasangiz ham!",
    "color": "#00B894",
    "rules": [
      {"label": "Standart tartib (SVO)", "tip": "[1-o'rin: Ega] + [2-o'rin: FE'L] + [Qolganlar]. Misol: 'Ich lerne heute Deutsch.'"},
      {"label": "Inversiya (Vaqt/Joy birinchi)", "tip": "[1-o'rin: Vaqt/Joy] + [2-o'rin: FE'L] + [3-o'rin: Ega]. Misol: 'Heute lerne ich Deutsch.'"},
      {"label": "So'roq gaplar", "tip": "Ha/Yo'q so'roq gaplarida Fe'l 1-o'ringa o'tadi: 'Lernst du Deutsch?' So'roq so'zli gaplarda So'roq so'z 1-o'rinda, Fe'l 2-o'rinda: 'Wo lernst du Deutsch?'"}
    ],
    "table": {
      "headers": ["Turi", "1-o'rin", "2-o'rin (FE'L)", "3-o'rin", "Oxiri"],
      "rows": [
        ["Ega birinchi", "Ich", "trinke", "morgens Kaffee", "-"],
        ["Vaqt birinchi", "Morgens", "trinke", "ich", "Kaffee"],
        ["Ha/Yo'q so'roq", "Trinkst", "du", "morgens Kaffee", "?"],
        ["Maxsus so'roq", "Wann", "trinkst", "du Kaffee", "?"]
      ]
    },
    "fritz_tip": "2-o'rin degani bu ikkinchi so'z degani EMAS — bu ikkinchi grammatik blok degani! 'Meine liebe Oma [1] kocht [2] die Suppe.' 🦊🍲",
    "quiz": [
      {"q": "Agar gap 'Gestern' (Kecha) bilan boshlansa, nima bo'ladi?", "options": ["Keyin ega keladi", "Keyin fe'l keladi", "Keyin to'ldiruvchi keladi"], "answer": 1, "hint": "Fe'l DOIM 2-o'rinda qolishi shart: 'Gestern ging ich...'."},
      {"q": "Qaysi gapda so'z tartibi to'g'ri?", "options": ["Heute ich fahre nach Berlin.", "Heute fahre ich nach Berlin.", "Fahre heute ich nach Berlin."], "answer": 1, "hint": "1-o'rin: Heute, 2-o'rin: fahre, 3-o'rin: ich."},
      {"q": "Ha/Yo'q so'roq gapida fe'l qayerda keladi?", "options": ["1-o'rinda", "2-o'rinda", "Oxirida"], "answer": 0, "hint": "'Kommst du morgen?' -> Fe'l 1-o'rinda."}
    ]
  },
  {
    "id": "negation",
    "title": "8. Inkor: Nicht va Kein",
    "tag": "Grammatika",
    "summary": "Ularni aslo adashtirmang: noaniq artiklli yoki artiklsiz otlarni inkor qilish uchun 'kein', fe'llar, sifatlar va aniq otlar uchun 'nicht' ishlatiladi.",
    "color": "#E17055",
    "rules": [
      {"label": "Qachon KEIN ishlatiladi", "tip": "'ein' yoki artiklsiz otlarni inkor qilganda: 'Ich habe EIN Auto' -> 'Ich habe KEIN Auto'. 'Ich habe Zeit' -> 'Ich habe KEINE Zeit'."},
      {"label": "Qachon NICHT ishlatiladi", "tip": "Fe'llarni, sifatlarni, ravishlarni va aniq artiklli ('der/die/das') otlarni inkor qilganda: 'Ich schlafe NICHT', 'Das ist NICHT gut', 'Ich kenne DEN Mann NICHT'."},
      {"label": "Doch!", "tip": "Agar kimdir inkorli savol bersa ('Kommst du nicht?') va siz 'ha' deb tasdiqlamoqchi bo'lsangiz, 'Ja' o'rniga 'DOCH!' ishlating."}
    ],
    "table": {
      "headers": ["Inkor qilinuvchi", "Ishlatiladi", "Tasdiq misol", "Inkor misol"],
      "rows": [
        ["'ein' li ot", "kein", "Ich habe ein Buch.", "Ich habe kein Buch."],
        ["Artiklsiz ot", "keine", "Ich trinke Milch.", "Ich trinke keine Milch."],
        ["Fe'l / Harakat", "nicht", "Ich schwimme gern.", "Ich schwimme nicht gern."],
        ["Sifat", "nicht", "Das Hotel ist teuer.", "Das Hotel ist nicht teuer."],
        ["Aniq ot", "nicht", "Ich suche den Schlüssel.", "Ich suche den Schlüssel nicht."]
      ]
    },
    "fritz_tip": "Agar ingliz tilida 'no/not any' deyish mumkin bo'lsa, nemis tilida 'kein' ishlating. Qolgan hamma narsa uchun 'nicht'! 🦊⛔",
    "quiz": [
      {"q": "To'ldiring: 'Ich habe _____ Zeit.' (Zeit - jenskiy, artiklsiz ot).", "options": ["nicht", "keine", "keinen"], "answer": 1, "hint": "Artiklsiz jenskiy otni inkor qilish 'keine' oladi."},
      {"q": "To'ldiring: 'Das Essen ist _____ teuer.'", "options": ["nicht", "kein", "keine"], "answer": 0, "hint": "Sifatni ('teuer') inkor qilish 'nicht' oladi."},
      {"q": "Birov so'radi: 'Hast du keinen Hunger?' Siz judayam ochsiz. Nima deysiz?", "options": ["Ja!", "Doch!", "Nein!"], "answer": 1, "hint": "'Doch' inkorli savolga ijobiy javob berish (haqiqatni tasdiqlash) uchun ishlatiladi."}
    ]
  },
  {
    "id": "prepositions",
    "title": "9. Eng muhim predloglar va Kelishiklar",
    "tag": "Predloglar",
    "summary": "Predloglar o'zlaridan keyin keluvchi otning kelishigini belgilab beradi. A1 darajasi uchun muhim predloglarni yodlab oling!",
    "color": "#0984E3",
    "rules": [
      {"label": "Dativ Predloglar", "tip": "aus (dan), bei (da/yonida), mit (bilan), nach (keyin/ga), seit (-dan beri), von (-ning/dan), zu (ga). DOIM Dativ!"},
      {"label": "Akkusativ Predloglar", "tip": "bis (gacha), durch (orqali), für (uchun), gegen (qarshi/atrofida), ohne (siz), um (da/atrofida). DOIM Akkusativ!"},
      {"label": "Qisqartmalar", "tip": "in + dem = im | an + dem = am | zu + dem = zum | zu + der = zur | bei + dem = beim | für + das = fürs."}
    ],
    "table": {
      "headers": ["Predlog", "Kelishik", "Ma'nosi", "Misol"],
      "rows": [
        ["mit", "Dativ", "bilan / orqali", "Ich fahre mit dem Bus."],
        ["für", "Akkusativ", "uchun", "Das Geschenk ist für dich."],
        ["zu", "Dativ", "ga / tomon", "Ich gehe zum Arzt."],
        ["ohne", "Akkusativ", "siz (without)", "Kaffee ohne Zucker bitte."],
        ["bei", "Dativ", "da / yonida", "Ich wohne bei meinen Eltern."],
        ["nach", "Dativ", "keyin / ga", "Nach dem Essen schlafe ich."]
      ]
    },
    "fritz_tip": "Yodda tuting: 'zum' = zu dem (muzskoy/sredniy), 'zur' = zu der (jenskiy). 'Ich gehe zum Arzt, aber zur Bank!' 🦊🏦",
    "quiz": [
      {"q": "To'ldiring: 'Ein Kaffee _____ (sutsiz) Milch bitte.'", "options": ["mit", "ohne", "für"], "answer": 1, "hint": "'ohne' -siz degani (without)."},
      {"q": "'in dem' ning qisqartmasi nima?", "options": ["im", "am", "ans"], "answer": 0, "hint": "'in + dem' 'im' ga qisqaradi."},
      {"q": "Qaysi predlog '-dan beri' ma'nosini bildiradi va Dativ talab qiladi?", "options": ["nach", "seit", "von"], "answer": 1, "hint": "'seit' vaqt davriydiligini bildiradi: 'seit einem Jahr'."}
    ]
  },
  {
    "id": "plurals",
    "title": "10. Ko'plik shakllari va Ot qo'shimchalari",
    "tag": "Otlar",
    "summary": "Ingliz tilidan (-s) farqli o'laroq, nemis tilida 5 ta asosiy ko'plik shakli mavjud: -e, -(e)n, -er, -s, va qo'shimchasiz (ko'pincha umlaut bilan).",
    "color": "#6C5CE7",
    "rules": [
      {"label": "1-shakl: -e (ko'pincha Umlaut bilan)", "tip": "Muzskoy va sredniy otlarda ko'p uchraydi: der Tisch -> die Tische, der Baum -> die Bäume."},
      {"label": "2-shakl: -(e)n", "tip": "Jenskiy otlarning ~90% uchun standart: die Frau -> die Frauen, die Lampe -> die Lampen."},
      {"label": "3-shakl: -er (odatda Umlaut bilan)", "tip": "Ko'pincha qisqa sredniy otlarda: das Kind -> die Kinder, das Buch -> die Bücher, das Bild -> die Bilder."},
      {"label": "4-shakl: -s", "tip": "Chet tilidan kirgan so'zlar va qisqartmalar: das Auto -> die Autos, das Sofa -> die Sofas, das Handy -> die Handys."},
      {"label": "5-shakl: Qo'shimchasiz (yoki faqat Umlaut)", "tip": "-el, -en, -er bilan tugovchi otlar: der Lehrer -> die Lehrer, der Apfel -> die Äpfel, der Computer -> die Computer."}
    ],
    "table": {
      "headers": ["Birlik", "Ko'plik", "Shakl", "Ma'nosi"],
      "rows": [
        ["der Tag", "die Tage", "+e", "kun -> kunlar"],
        ["die Zeitung", "die Zeitungen", "+en", "gazeta -> gazetalar"],
        ["das Kind", "die Kinder", "+er", "bola -> bolalar"],
        ["das Auto", "die Autos", "+s", "mashina -> mashinalar"],
        ["der Apfel", "die Äpfel", "Faqat Umlaut", "olma -> olmalar"]
      ]
    },
    "fritz_tip": "Nemis tilida biror otni yodlaganda, uni DOIM artikli VA ko'pligi bilan birga yodlang: 'der Tisch, die Tische'! 🦊📚",
    "quiz": [
      {"q": "'das Buch' (kitob) ning ko'pligi nima?", "options": ["die Buche", "die Büchen", "die Bücher"], "answer": 2, "hint": "Das Buch umlaut va -er oladi: die Bücher."},
      {"q": "-ung bilan tugaydigan ko'pchilik jenskiy otlarning ko'plik qo'shimchasi nima?", "options": ["-e", "-en", "-s"], "answer": 1, "hint": "die Zeitung -> die Zeitungen."},
      {"q": "'das Auto' ning ko'pligi nima?", "options": ["die Autos", "die Auton", "die Autoe"], "answer": 0, "hint": "Chet tilidan kirgan so'zlar odatda -s oladi."}
    ]
  }
]

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Make sure we don't accidentally append twice.
app_js = re.sub(r'const GRAMMAR_DATA = \[.*?\}\];\n', '', app_js, flags=re.DOTALL)

# Insert it back
new_code = f"const GRAMMAR_DATA = {json.dumps(uz_grammar, ensure_ascii=False, indent=2)};\n\n"
app_js = app_js.replace("let currentLang = 'en';", new_code + "let currentLang = 'en';")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print('Translation applied successfully!')
