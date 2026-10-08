import json
import re

raw_data = """
**Lektion 16**
der Aufzug, -¨e | lift
der Lift, -e | lift
kennenlernen | tanishmoq
nervös | hayajonlangan
die Angst, -¨e | qo‘rquv
das Netz (Sg.) | tarmoq
funktionieren | ishlamoq
los sein | sodir bo‘lmoq
reparieren | ta’mirlamoq
anbieten (du bietest an, er/es/sie bietet an, hat angeboten) | taklif qilmoq
die Bitte, -n | iltimos
die Dusche, -n | dush
der Kühlschrank, -¨e | muzlatkich
der Fernseher, - | televizor
die Heizung, -en | isitkich
das Licht (Sg.) | yorug‘lik
der Herd, -e | plita
die Klingel, -n | qo‘ng‘iroq
die Glocke, -n | qo‘ng‘iroq
die Steckdose, -n | rozetka
die Waschmaschine, -n | kir yuvish mashinasi
der Handwerker, - | usta
die Handwerkerin, -nen | ayol usta
selbst (A/CH: selber) | o‘zi
erklären | tushuntirmoq
die Reparatur, -en | ta’mir
ausmachen (CH: vereinbaren) | kelishmoq
pünktlich | o‘z vaqtida
vorschlagen (du schlägst vor, hat vorgeschlagen) | taklif qilmoq
absagen | bekor qilmoq
verschieben (hat verschoben) | ko‘chirmoq
Sehr geehrte / r (= Anrede) | hurmatli
Mit freundlichen Grüßen (= Gruß) | hurmat bilan
Freundliche Grüsse (CH) | hurmat bilan
in | ichida
vor | oldin
nach | keyin
bekommen (hat bekommen) | olmoq
das Vorstellungsgespräch, -e | suhbat (ish uchun)
nach Hause | uyga
erst | faqat, endigina
Oje | voy-bo‘ldi
klappen | chiqmoq, ish bermoq
das Training, -s | mashg‘ulot
das Treffen, - | uchrashuv

**Lektion 17**
werden (du wirst, er/es/sie wird, ist geworden) | bo‘lmoq
auf jeden Fall | albatta
unbedingt | shubhasiz
auf keinen Fall | aslo
der Astronaut, -en | kosmonavt
die Astronautin, -nen | ayol kosmonavt
der Polizist, -en | politsiyachi
die Polizistin, -nen | ayol politsiyachi
wollen (ich will, du willst, er/es/sie will) | xohlamoq
der Plan, -¨e | reja
gründen (du gründest, er/es/sie gründet) | asos solmoq
das Geld (Sg.) | pul
Geld verdienen | pul ishlamoq
der Profi, -s | professional
das Berufsleben (Sg.) | mehnat hayoti
jung ↔ alt | yosh ↔ qari
das Marketing (Sg.) | marketing
der Lifestyle, -s | turmush tarzi
die Wirtschaft (Sg.) | iqtisodiyot
die Halbtagsstelle, -n | yarim stavkali ish joyi
selbstständig | mustaqil
eigene / eigener / eigenes / eigenen | o‘ziga tegishli
der Influencer, - | ta’sir o‘tkazuvchi (bloger)
die Influencerin, -nen | ayol ta’sir o‘tkazuvchi
damit | shuning uchun
der Abschluss, -¨e | tamomlash, bitirish
der Studienplatz, -¨e | o‘qish joyi (universitetda)
die Note, -n | baho
der Krankenpfleger, - | hamshira (erkak)
der Pflegefachmann, -¨er | parvarishchi (erkak, CH)
die Krankenpflegerin, -nen | hamshira (ayol)
die Pflegefachfrau, -en | parvarishchi ayol (CH)
ohne (+ Akkusativ) | siz
die Grenze, -n | chegara
die Welt (Sg.) | dunyo
der Mensch, -en | inson
wichtig | muhim
die Freiheit (Sg.) | erkinlik
die Selbstständigkeit (Sg.) | mustaqillik
halbtags | yarim kunlik
der Hund, -e | it
traurig | xafa
der Politiker, - | siyosatchi
die Politikerin, -nen | ayol siyosatchi
die Fremdsprache, -n | chet tili
der Chef, -s | boshliq
die Chefin, -nen | ayol boshliq
heiraten (du heiratest, er/es/sie heiratet) | uylanmoq, turmushga chiqmoq
der Berg, -e | tog‘
Europa (Sg.) | Yevropa
das Ausland (Sg.) | chet el
das Motorrad, -¨er | mototsikl
der Führerschein, -e | haydovchilik guvohnomasi
der Führerausweis, -e | haydovchilik guvohnomasi (CH)
das Instrument, -e | asbob (musiqa)
Norwegen (Sg.) | Norvegiya
der Koch, -¨e | oshpaz
die Köchin, -nen | ayol oshpaz

**Lektion 18**
die Übung, -en | mashq
der Kopf, Köpfe | bosh
der Schmerz, -en | og‘riq
das Weh | og‘riq
müde | charchagan
schlimm | yomon
gegen | ga qarshi
die Situation, -en | vaziyat
üblich | odatiy
sitzen (sitzt, hat/ist gesessen) | o‘tirmoq
krank | kasal
gesund | sog‘lom
die Bewegung, -en | harakat
ungefähr | taxminan
sogar | hatto
bedeuten (bedeutet) | anglatmoq
das Übergewicht | ortiqcha vazn
das Herz, -en | yurak
die Krankheit, -en | kasallik
dagegen | bunga qarshi
aufstehen (ist aufgestanden) | turmoq
benutzen | ishlatmoq
der Ratschlag, Ratschläge | maslahat
der Tipp, -s | tavsiya
schicken | yubormoq
gewinnen (hat gewonnen) | yutmoq
das Frisbee, -s | frizbi
der Roller, - | skuter
der Körper, - | tana
der Körperteil, -e | tana a’zosi
die Brust | ko‘krak
der Bauch, Bäuche | qorin
der Arm, -e | qo‘l
die Hand, Hände | qo‘l panjasi
der Finger, - | barmoq
das Bein, -e | oyoq
das Knie, - | tizza
das Auge, -n | ko‘z
der Hals, Hälse | bo‘yin
der Mund, Münder | og‘iz
die Nase, -n | burun
das Ohr, -en | quloq
das Forum, Foren | forum
der Schnupfen | shamollash
wehtun (tut weh) | og‘rimoq
genug | yetarli
die Erkältung, -en | shamollash
die Verkühlung, -en | shamollash
der Husten | yo‘tal
der Honig | asal
sollen (soll) | kerak (modal fe’l)
das Fieber | isitma
die Ruhe | dam olish
die Tablette, -n | tabletka
das Medikament, -e | dori
die Salbe, -n | surtma dori
der Hustensaft, Säfte | yo‘tal siropi
die Umfrage, -n | so‘rov
kommunikativ | muloqotga kirishuvchan
betreuen | g‘amxo‘rlik qilmoq / boshqarmoq
die Datei, -en | fayl
die Präsentation, -en | prezentatsiya
präsentieren | taqdim qilmoq
schaffen | uddalamoq
öffnen | ochmoq
eilig | shoshilinch
die Software | dasturiy ta’minot
die Teamarbeit | jamoaviy ish
der Workshop, -s | seminar
die Architektur | arxitektura
das Modell, -e | model
die Abteilung, -en | bo‘lim

**Lektion 19**
aufmachen | ochmoq
zumachen | yopmoq
der Abfall, -¨e | chiqindi
der Müll | axlat
der Mist | axlat
sauer | jahli chiqqan, xafa
der Haushalt, -e | uy-ro‘zg‘or ishlari
rausbringen | chiqarmoq (axlatni)
die Spülmaschine, -n | idish yuvish mashinasi
ausräumen | bo‘shatmoq
sauber | toza
das Geschirr | idish-tovoq
putzen | tozalamoq
der Boden, -¨e | pol, yer
wischen | artmoq
vergessen | unutmoq
herkommen | bu yoqqa kelmoq
lieb | mehribon, yoqimli
rauchen | chekish
heiß | issiq
die Luft | havo
anmachen | yoqmoq (svet, chiroq va hokazo)
ausmachen | o‘chirmoq
zuhören | diqqat bilan eshitmoq
das Lied, -er | qo‘shiq
die Notiz, -en | eslatma, yozuv
leise sein | jim bo‘lmoq
das Spiel, -e | o‘yin
lachen | kulmoq
die Tüte, -n | paket, sumka
die Maschine, -n | mashina, apparat
schmutzig | kir, iflos
zurückrufen | qayta qo‘ng‘iroq qilmoq
die Pause, -n | tanaffus
der Grund, -¨e | sabab
in Ordnung | joyida, to‘g‘ri
recht haben | haq bo‘lmoq
böse | g‘azablangan, xafa

**Lektion 20**
Das Team sieht sehr sympathisch aus | jamoa juda yoqimli ko‘rinadi
die Website, -s | veb-sayt
der Service, -s | xizmat
der Fehler, - | xato
beraten | maslahat bermoq
das Team, -s | jamoa
der Berater, - | maslahatchi
der Experte, -n | mutaxassis
das Projekt, -e | loyiha
der Manager, - | menejer
der Psychologe, -n | psixolog
der Fachmann, Fachleute | mutaxassis
die Medien (Pl.) | ommaviy axborot vositalari
die Kommunikation | muloqot
die Szene, -n | muhit, sahna (startap muhiti)
irgendwann | qachondir
probieren | sinab ko‘rmoq
der Schritt, -e | qadam
die Organisation | tashkilot
organisieren | tashkil etmoq
verbessern | yaxshilamoq
die Technik | texnika
das Werkzeug, -e | asbob
mehrere | bir nechta
erfolgreich | muvaffaqiyatli
mitarbeiten | hamkorlikda ishlamoq
der Spezialist, -en | mutaxassis
die Werbung, -en | reklama
transportieren | tashimoq
Haare | sochlar
lange Haare | uzun sochlar
glatte Haare | silliq sochlar
dunkle Haare | qora sochlar
blonde Haare | sarg‘ish sochlar
der Bart, -¨e | soqol
die Locke, -n | jingalak soch
sympathisch | yoqimli
freundlich | do‘stona
kräftig | kuchli, baquvvat
schlank | ozg‘in
fröhlich | quvnoq
kreativ | ijodkor
ruhig | tinch, sokin
langweilig | zerikarli
die Agentur, -en | agentlik
zufrieden | mamnun
aufstehen | o‘rnidan turmoq
verpassen | o‘tkazib yubormoq
verlieren | yo‘qotmoq
das Päckchen, - | kichik posilka
Echt? | Rostdanmi?
Puh! | Voy, uh (yengillik yoki charchoq ifodasi)
lila | binafsha (rang)
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
    if "Spaziergang" in word: return word.replace("Spaziergang", "Spaziergäng")
    if "Wald" in word: return word.replace("Wald", "Wäld")
    if "Vogel" in word: return word.replace("Vogel", "Vögel")
    if "Kuss" in word: return word.replace("Kuss", "Küss")
    if "Laden" in word: return word.replace("Laden", "Läden")
    if "Zahn" in word: return word.replace("Zahn", "Zähn")
    if "Chor" in word: return word.replace("Chor", "Chör")
    if "Anfang" in word: return word.replace("Anfang", "Anfäng")
    if "Schloss" in word: return word.replace("Schloss", "Schlöss")
    if "Garten" in word: return word.replace("Garten", "Gärten")
    if "Anwalt" in word: return word.replace("Anwalt", "Anwält")
    
    # Lektion 16-20 Additions
    if "Aufzug" in word: return word.replace("Aufzug", "Aufzüg")
    if "Schrank" in word: return word.replace("Schrank", "Schränk")
    if "Plan" in word: return word.replace("Plan", "Plän")
    if "Rad" in word: return word.replace("Rad", "Räd")
    if "Koch" in word: return word.replace("Koch", "Köch")
    if "Schlag" in word: return word.replace("Schlag", "Schläg")
    if "Bauch" in word: return word.replace("Bauch", "Bäuch")
    if "Fall" in word: return word.replace("Fall", "Fäll")
    if "Grund" in word: return word.replace("Grund", "Gründ")
    if "Boden" in word: return word.replace("Boden", "Böden")
    if "Bart" in word: return word.replace("Bart", "Bärt")
    
    return word

with open('words.json', 'r', encoding='utf-8') as f:
    existing_words = json.load(f)

max_id = 0
for w in existing_words:
    if int(w['id']) > max_id:
        max_id = int(w['id'])

id_counter = max_id + 1
new_words = []
current_category = "Lektion 16"

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
        elif plural_suffix.startswith("¨-") or plural_suffix.startswith('"e'):
            # handle -"e which was in Lektion 19
            ending = plural_suffix[2:] if plural_suffix.startswith("¨-") else "e"
            plural = f"die {apply_umlaut(word)}{ending}"
        elif plural_suffix.startswith("-"):
            ending = plural_suffix[1:]
            if ending.startswith("¨"): # handle -¨er etc without space
                ending = ending[1:]
                plural = f"die {apply_umlaut(word)}{ending}"
            else:
                plural = f"die {word}{ending}"
        elif plural_suffix == "(Pl.)":
            plural = f"die {word}"
            plural_suffix = ""
        elif plural_suffix == "(Sg.)":
            plural = ""
            plural_suffix = ""
        elif plural_suffix in ["Köpfe", "Ratschläge", "Bäuche", "Hände", "Hälse", "Münder", "Foren", "Säfte", "Fachleute"]:
            plural = f"die {plural_suffix}"
        else:
            plural = plural_suffix 
            
    else:
        # Check for verbs with parenthesis
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
