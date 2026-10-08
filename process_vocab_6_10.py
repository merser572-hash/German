import json
import re

raw_data = """
**Lektion 6**
Oh Gott! | Voy Xudo! / Ey Xudo!
der Gott, ¨-er | xudo / iloh
viel | ko‘p
die Arbeit, -en | ish
Hilfe! | Yordam!
das Passwort, ¨-er | parol
der Traum, ¨-e | tush / orzu
der Albtraum, ¨-e | dahshatli tush / kabus
die Person, -en | shaxs / odam
der Hunger, -- | ochlik
Hunger haben | och bo‘lmoq
telefonieren mit | ... bilan telefon orqali gaplashmoq
das WLAN, -- | Wi-Fi / simsiz internet
der Stift, -e | ruchka / qalam
brauchen | kerak bo‘lmoq / ehtiyoj sezmoq
der Kaffee, -s | qahva
die Nachricht, -en | xabar
das Büro, -s | ofis / ishxona
neu | yangi
Viele Grüße | Ko‘p salomlar
der Gruß, ¨-e | salom / salomlashuv
das Yoga, -- | yoga
morgen | ertaga / tong
leider | afsuski
(keine) Zeit haben | (vaqt) bo‘lmasligi / vaqt yo‘q
die Zeit, -en | vaqt
der Termin, -e | uchrashuv / belgilangan vaqt
von | ...dan
Liebe Grüße (LG) | Samimiy salomlar
der Laptop, -s | noutbuk
die E-Mail, -s | elektron xat
Auf Wiederhören | Xayr (telefon orqali)
da sein | mavjud boʻlmoq
Was kann ich für Sie tun? | Siz uchun nima qila olaman?
der Drucker, -- | printer
die Maus, ¨-e | sichqoncha
der Computer, -- | kompyuter
hier | Bu yerda
der Kalender, -- | kalendar
der Bildschirm, -e | ekran
das Tablet, -s | planshet
die Visitenkarte, -n | vizitka
die Tastatur, -en | klaviatura
dann | keyin / shunda
notieren | yozib qo‘ymoq
in die Tasche packen | sumkaga solmoq
der Schreibtisch, -e | yozuv stoli
der Arbeitsplatz, ¨-e | ish joyi
Ach, da ist er ja! | Voy, mana u!
ach | voy / eh
schon wieder | yana / yana bir bor
vielleicht | balki
Hallo,... hier. | Salom,... bu yerda.

**Lektion 7**
können (ich kann, du kannst, er/sie/es kann) | qila olmoq
tanzen (du tanzt) | raqsga tushmoq
toll | ajoyib
normal | oddiy
komisch | g‘alati
blöd | ahmoqona
interessant | qiziqarli
lustig | kulgili
überall | hamma joyda
hören | eshitmoq
zurzeit | hozirgi paytda
immer | har doim
Hobbys (Mehrzahl von das Hobby) | sevimli mashg‘ulotlar
kochen | ovqat pishirmoq
singen | qo‘shiq aytmoq
schwimmen | suzmoq
fotografieren | suratga olmoq
Schach spielen | shaxmat o‘ynamoq
malen | chizmoq
backen | pishiriq tayyorlamoq (pechda, tandirda pishirmoq)
Fußball spielen | futbol o‘ynamoq
Tennis spielen | tennis o‘ynamoq
Gitarre spielen | gitara chalmoq
Rad / Fahrrad fahren (du fährst) | velosiped minmoq
Ski fahren (du fährst Ski) | chang‘ida uchmoq
reiten (du reitest) | ot minmoq
wirklich | haqiqatan
aber | lekin
Herzlichen Dank! | chin dildan rahmat
alle / wir alle / alle drei / beide | hamma / hammamiz / uchovimiz / ikkalamiz
auch nicht | ham emas
auflegen | (musiqa) qo‘ymoq
mixen | aralashtirmoq (musiqa mikslash)
der DJ, -s | di-jey
lieben | sevmoq
das Kickboxen (Sg.) | kikboks
die Senioren (Pl.) | qariyalar
das Seniorenheim, -e | qariyalar uyi
richtig | to‘g‘ri
gehen | yurmoq
die Versicherung, -en | sug‘urta
der Kaufmann / die Kauffrau / die Kaufleute | savdogar / savdogar ayol / savdogarlar
der Versicherungskaufmann / die Versicherungskauffrau / die Versicherungskaufleute | sug‘urta bo‘yicha mutaxassis (erkak / ayol / ko‘plik)
die Freizeit (Sg.) | bo‘sh vaqt
oft | tez-tez
der Klub, -s | klub
das Konzert, -e | kontsert
das Start-up, -s | startap (yangi biznes)
die Fitness (Sg.) | fitnes
das Studio / das Fitnessstudio, -s | fitnes zali
nie | hech qachon
lange | uzoq vaqt
manchmal | ba’zida
lesen (du liest) | o‘qimoq
Freunde treffen (du triffst) | do‘stlar bilan uchrashmoq
der Freund, -e / die Freundin, -nen | do‘st / dugona
fahren (du fährst) | haydamoq, minmoq
der Ausflug, -ü-e | sayohat, chiqish
das Radio, -s | radio
im Internet surfen | internetda sayr qilmoq
das Internet (Sg.) | internet
surfen | internetdan foydalanmoq
Spaß machen | zavq bag‘ishlamoq
der Spaß (Sg.) | zavq, quvonch
Lieblings- | sevimli (prefiks sifatida: Lieblingsbuch = sevimli kitob)
gern | mamnuniyat bilan (bajonidil)
in deiner Freizeit | bo‘sh vaqtingda

**Lektion 8**
das Schwimmbad, -¨er | suzish havzasi
das Kino, -s | kino
heute Nachmittag um vier? | bugun tushdan keyin soat to‘rtda?
der Nachmittag, -e | tushdan keyin
um | da (soat ifodasida)
am Montag oder am Dienstag? | dushanba yoki seshanbada?
der Wochentag, -e | hafta kuni
die Wochentage | hafta kunlari
die Woche, -n | hafta
der Montag, -e | dushanba
der Dienstag, -e | seshanba
der Mittwoch, -e | chorshanba
der Donnerstag, -e | payshanba
der Freitag, -e | juma
der Samstag, -e | shanba
der Sonntag, -e | yakshanba
Wann? | qachon?
gehen wir ins Kino? | kinoga boramizmi?
Am Freitag. | juma kuni
das Wochenende, -n | hafta oxiri
am Wochenende | hafta oxirida
Am Samstag und am Sonntag = Wochenende | shanba va yakshanba = hafta oxiri
frei | bo‘sh
Eine Woche frei. | bir hafta dam olish
Was machen Sie? | siz nima qilasiz?
der Chat, -s | chat, yozishma
die Nacht, -¨e | tun
in der Nacht | tunida
am Vormittag, am Nachmittag, am Abend | ertalab, tushdan keyin, kechqurun
Das weiß ich noch nicht. | hali bilmayman
Was machst du heute Nachmittag? | bugun tushdan keyin nima qilasan?
wissen (ich weiß, du weißt, er/sie/es weiß) | bilmoq
Ich weiß noch nicht. | hali bilmayman
Lust auf … | ... qilish istagi
Keine Lust. | istak yo‘q
die Lust (Sg.) | istak, xohish
die Idee, -n | g‘oya, fikr
Gute Idee. | yaxshi g‘oya
um Viertel nach | chorak o‘tgach
um halb | yarimda
spät | kech
oder | yoki
okay | mayli
Bis dann! | ko‘rishguncha!
der Morgen, - | ertalab
der Vormittag, -e | tushdan oldin
der Mittag, -e | peshin payti
der Nachmittag | tushdan keyin
der Abend | kechqurun
die Nacht | tun
der Mittag, -e | peshin
der Abend, -e | kech
Freizeit | bo‘sh vaqt
das Museum, Museen | muzey
das Theater, - | teatr
das Café, -s | kafe
die Ausstellung, -en | ko‘rgazma
der Klub / die Disco, -s | klub / diskoteka
das Konzert, -e | kontsert
das Restaurant, -s | restoran
die Bar, -s | bar
das Fitnessstudio, -s | fitnes zali
in | ichida / ga
Gehen wir in einen Klub? | klubga boramizmi?
Die Uhrzeit | vaqt
Wie viel Uhr …? | soat nechchi?
Es ist halb vier. | soat uch yarim
Wie spät …? | soat nechchi?
Es ist … vier Uhr. | soat ... to‘rt
der Rücken, - | orqa (tanadagi)
Ja, genau. | ha, aynan shunday
Es ist Viertel vor drei? | soat uchgacha chorak qoldi?
Am Morgen | ertalab
Heute | bugun
arbeite ich | ishlayman
aber morgen | lekin ertaga
habe ich frei. | dam olaman
vor … | gacha
Viertel | chorak
nach … | o‘tgach
halb … | yarim
der Vorschlag, -¨e | taklif
die Frage, -n | savol
die Antwort, -en | javob
tut mir leid | uzr, afsusdaman
ich kann leider nicht. | afsuski, qila olmayman

**Lektion 9**
mögen (ich mag, du magst, er/sie/es mag) | yoqtirmoq
Ich mag Hamburger. | Men gamburgerni yoqtiraman
der Hamburger, - | gamburger
die Schokolade (Sg.) | shokolad
der Käse (Sg.) | pishloq
der Salat, -e | salat
Lebensmittel | oziq-ovqat mahsulotlari
der Kuchen, - | tort, pirog
die Suppe, -n | sho‘rva
der Apfel, -¨ | olma
der Tee, -s | choy
die Orange, -n | apelsin
der Fisch, -e | baliq
die Tomate, -n | pomidor
das Brot, -e | non
der Kaffee, -s | qahva
das Fleisch (Sg.) | go‘sht
das Brötchen, - | bulochka
die Marmelade, -n | murabbo
der Saft, -¨e | sharbat
zum Frühstück | nonushtada
das Frühstück (Sg.) | nonushta
besonders | ayniqsa
Guten Appetit! | ishtahangiz ochilsin
lecker | mazali
essen (du isst, er/sie/es isst) | ovqatlanmoq, yemoq
der / das Ketchup (Sg.) | ketchup
der Witz, -e | hazil
fit | sog‘lom, chiniqqan
intelligent | aqlli
prima | juda yaxshi, a’lo
das Gedicht, -e | she’r
auf | ustida
der Tisch, -e | stol
trinken | ichmoq
das Abendessen, - | kechki ovqat
das Mittagessen, - | tushlik
das Frühstück, -e | nonushta
das Getränk, -e | ichimlik
das Essen, - | ovqat
die Butter (Sg.) | sariyog‘
der Schinken, - | kolbasa, dudlangan go‘sht
das Ei, -er | tuxum
das Müsli, -s | musli, suli bo‘tqasi
die Milch (Sg.) | sut
wünschen | tilamoq, buyurtma bermoq
die Tasse, -n | piyola
möchten (du möchtest, er/sie/es möchte) | xohlamoq, istamoq
der Nusskuchen, - | yong‘oqli pirog
der Apfelkuchen, - | olma pirogi
der Schokoladenkuchen, - | shokoladli pirog
schade | afsus
na gut | mayli, bo‘ldi
nehmen (du nimmst, er/sie/es nimmt) | olmoq
unser | bizning
der Gast, -¨e | mehmon
die Speisekarte, -n | menyu, taomnoma
der Apfelsaft, -¨e | olma sharbati
der Orangensaft, -¨e | apelsin sharbati
das Wasser (Sg.) | suv
die Speise, -n | taom
die Vorspeise, -n | boshlang‘ich taom (aperitiv)
der Tomatensalat, -e | pomidor salati
die Kartoffel, -n | kartoshka
das Würstchen, - | kolbasa (kichik)
das Hauptgericht, -e | asosiy taom
die Pommes frites (Pl.) | kartoshka fri
die Nudel, -n | makaron
die Soße, -n | sous
das Huhn, -¨er | tovuq
der Reis (Sg.) | guruch
das Dessert, -s | desert
das Eis (Sg.) | muzqaymoq
die Vanille (Sg.) | vanil
die Erdbeere, -n | qulupnay
die Kugel, -n | sharcha, muzqaymoq porsiyasi
die Portion, -en | porsiya
die Sahne (Sg.) | qaymoq
das Obst (Sg.) | meva
das Stück, -e | bo‘lak
die Zitrone, -n | limon
der Zitronenkuchen, - | limonli pirog
der Nachtisch (Sg.) | desert (shirinlik)
perfekt | mukammal
das Menü, -s | menyu (to‘liq taomlar ketma ketligi)

**Lektion 10**
der Flughafen, -¨e | aeroport
chatten (du chattest, er/sie/es chattet) | chat qilmoq
der Kollege, -n | hamkasb (erkak)
die Kollegin, -nen | hamkasb (ayol)
der Flug, -¨e | parvoz
der Abendflug, -¨e | kechki reys
die Reise, -n | sayohat
kurz | qisqa
abfliegen | uchib ketmoq
starten (du startest, er/sie/es startet) | start olmoq, uchmoq
ankommen | yetib kelmoq
dort | u yerda
so | shunday, taxminan
anrufen | qo‘ng‘iroq qilmoq
noch mal | yana bir marta
früh | erta
sicher | ishonchli, albatta
die Stimme, -n | ovoz
versuchen | urinmoq, harakat qilmoq
hoffentlich | umid qilamanki
die Verspätung, -en | kechikish
kaputt | buzilgan
die Maschine, -n | samolyot, mashina
landen | qo‘nmoq (samolyot)
alles | hammasi
klar | tushunarli
lieber | yaxshiroq, afzal
wenig | oz
der Akku, -s | batareya, quvvat
verstehen | tushunmoq
abholen | olib ketmoq
natürlich | albatta
freuen (sich) | xursand bo‘lmoq
Bis gleich! | hozir ko‘rishamiz
einsteigen | transportga chiqmoq
umsteigen | transport almashtirmoq
aussteigen | transportdan tushmoq
der Verkehr (Sg.) | yo‘l harakati
das Verkehrsmittel, - | transport vositasi
das Gepäck (Sg.) | yuk
der Bahnhof, -¨e | vokzal
die U-Bahn, -en | metro (yerosti)
das Taxi, -s | taksi
der Bus, -se | avtobus
der Zug, -¨e | poyezd
die Straßenbahn, -en | tramvay
die S-Bahn, -en | shahar elektr poyezdi
das Flugzeug, -e | samolyot
der Koffer, - | chamadon
der Rucksack, -¨e | ryukzak
einkaufen | xarid qilmoq
abfahren | jo‘nab ketmoq
fernsehen (du siehst fern, er/sie/es sieht fern) | televizor tomosha qilmoq
die Durchsage, -n | e’lon (stansiyada)
der Intercity, -s | shaharlararo poyezd
der Bahnsteig, -e | platforma
die Richtung, -en | yo‘nalish
einfahren | kirib kelmoq (poyezd haqida)
das Gleis, -e | rels, yo‘l (poyezd uchun)
die Fahrt, -en | safar
enden | tugamoq
beginnen | boshlanmoq
stehen | turmoq
der Ausgang, -¨e | chiqish
nächst- | keyingi
der Halt, -e | to‘xtash joyi
der Hauptbahnhof, -¨e | markaziy vokzal
die Vorsicht (Sg.) | ehtiyotlik
Achtung! | diqqat!
"""

def apply_umlaut(word):
    if "Haus" in word: return word.replace("Haus", "Häus")
    if "Buch" in word: return word.replace("Buch", "Büch")
    if "Stuhl" in word: return word.replace("Stuhl", "Stühl")
    if "Schrank" in word: return word.replace("Schrank", "Schränk")
    if "Vater" in word: return word.replace("Vater", "Väter")
    if "Mutter" in word: return word.replace("Mutter", "Mütter")
    if "Tochter" in word: return word.replace("Tochter", "Töchter")
    if "Bruder" in word: return word.replace("Bruder", "Brüder")
    if "Sohn" in word: return word.replace("Sohn", "Söhn")
    if "Arzt" in word: return word.replace("Arzt", "Ärzt")
    if "Land" in word: return word.replace("Land", "Länd")
    if "Mann" in word: return word.replace("Mann", "Männ")
    if "Hand" in word: return word.replace("Hand", "Händ")
    if "Wort" in word: return word.replace("Wort", "Wört")
    if "Glas" in word: return word.replace("Glas", "Gläs")
    if "Tierarzt" in word: return word.replace("Tierarzt", "Tierärzt")
    if "Großvater" in word: return word.replace("Großvater", "Großväter")
    if "Großmutter" in word: return word.replace("Großmutter", "Großmütter")
    if "Ehemann" in word: return word.replace("Ehemann", "Ehemänn")
    if "Satz" in word: return word.replace("Satz", "Sätz")
    if "Tuch" in word: return word.replace("Tuch", "Tüch")
    if "Holz" in word: return word.replace("Holz", "Hölz")
    if "Gott" in word: return word.replace("Gott", "Gött")
    if "Traum" in word: return word.replace("Traum", "Träum")
    if "Saft" in word: return word.replace("Saft", "Säft")
    if "Apfel" in word: return word.replace("Apfel", "Äpfel")
    if "Gruß" in word: return word.replace("Gruß", "Grüß")
    if "Nacht" in word: return word.replace("Nacht", "Nächt")
    if "Huhn" in word: return word.replace("Huhn", "Hühn")
    if "Flug" in word: return word.replace("Flug", "Flüg")
    if "Zug" in word: return word.replace("Zug", "Züg")
    if "Sack" in word: return word.replace("Sack", "Säck")
    if "Ausgang" in word: return word.replace("Ausgang", "Ausgäng")
    if "Hof" in word: return word.replace("Hof", "Höf")
    if "Maus" in word: return word.replace("Maus", "Mäus")
    if "Platz" in word: return word.replace("Platz", "Plätz")
    if "Bad" in word: return word.replace("Bad", "Bäd")
    if "Vorschlag" in word: return word.replace("Vorschlag", "Vorschläg")
    
    return word

with open('words.json', 'r', encoding='utf-8') as f:
    existing_words = json.load(f)

# Find max id
max_id = 0
for w in existing_words:
    if int(w['id']) > max_id:
        max_id = int(w['id'])

id_counter = max_id + 1

new_words = []
current_category = "Lektion 6"

for line in raw_data.strip().split('\n'):
    line = line.strip()
    if not line: continue
    if line.startswith("**"):
        current_category = line.replace("**", "").strip()
        continue
        
    parts = line.split(" | ")
    if len(parts) != 2: continue
    
    german = parts[0].strip()
    uzbek = parts[1].strip()
    
    article = ""
    word = german
    plural_suffix = ""
    plural = ""
    
    # Check for noun with article
    match = re.match(r"^(der|die|das)\s+([^,]+)(?:,\s*(.+))?$", german)
    if match:
        article = match.group(1)
        word = match.group(2).strip()
        if match.group(3):
            plural_suffix = match.group(3).strip()
            
        if plural_suffix == "--":
            plural = f"die {word}"
        elif plural_suffix == "¨-":
            plural = f"die {apply_umlaut(word)}"
        elif plural_suffix.startswith("¨-"):
            ending = plural_suffix[2:]
            plural = f"die {apply_umlaut(word)}{ending}"
        elif plural_suffix.startswith("-"):
            ending = plural_suffix[1:]
            plural = f"die {word}{ending}"
        elif plural_suffix == "(Pl.)":
            plural = f"die {word}"
            plural_suffix = ""
        elif plural_suffix == "(Sg.)":
            plural = ""
            plural_suffix = ""
        elif plural_suffix in ["Firmen", "Praktika", "Museen"]:
            plural = f"die {plural_suffix}"
        else:
            plural = plural_suffix 
            
    else:
        # Check for verbs with parenthesis "heißen (heißt)"
        v_match = re.match(r"^([^\(]+)\s*\((.+)\)$", german)
        if v_match:
            word = v_match.group(1).strip()
        
    new_words.append({
        "id": str(id_counter),
        "word": word,
        "article": article,
        "plural": plural,
        "plural_suffix": plural_suffix,
        "translation": uzbek,
        "category": current_category
    })
    id_counter += 1

existing_words.extend(new_words)

with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=4)

print(f"Appended {len(new_words)} words to words.json. Total words: {len(existing_words)}")
