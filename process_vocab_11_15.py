import json
import re

raw_data = """
**Lektion 11**
gestern | kecha
der Spaziergang, -¨e | sayr
der Wald, -¨er | o‘rmon
die Zeitung, -en | gazeta
aufräumen | tartibga keltirmoq
zu wenig | juda oz
zu viel | juda ko‘p
der Vogel, -¨ | qush
der Film, -e | film
die Pause, -n | tanaffus
der Doktor, -en | shifokor
die Doktorarbeit, -en | doktorlik ishi
abwaschen | yuvmoq (idish-tovoqni)
schlafen | uxlash
die Hausaufgabe, -n | uy vazifasi
die Serie, -n | serial
von … bis | … dan … gacha
der Basketball (Sg.) | basketbol
danach | keyin
kaufen | sotib olmoq
das T-Shirt, -s | futbolka
ab | dan boshlab
ganze | butun
zurückkommen | qaytib kelmoq
der Kuss, -¨e | o‘pich
geöffnet | ochiq
das Schild, -er | belgi, yozuv
der Kinderarzt, -¨e | bolalar shifokori
die Kinderärztin, -nen | ayol bolalar shifokori
die Boutique, -en | butik, kiyim do‘koni
die Mode, -n | moda
der Urlaub, -e | ta’til
der Unterricht (Sg.) | dars
der Kursleiter, - | kurs rahbari (erkak)
die Kursleiterin, -nen | kurs rahbari (ayol)
die Blume, -n | gul
der Laden, -¨ | do‘kon
geschlossen | yopiq
das Eiscafé, -s | muzqaymoqxona
die Praxis, Praxen | shifokor qabulxonasi
der Kiosk, -e | kioska
der Zahn, -¨e | tish
letzt- | oxirgi, so‘nggi
der Sport (Sg.) | sport
einladen | taklif qilmoq
der Chor, -¨e | xor (qo‘shiqchilar jamoasi)
der Handball (Sg.) | gandbol
die Wäsche (Pl.) | kirlar
waschen | yuvmoq
das Geschenk, -e | sovg‘a

**Lektion 12**
der Marathon, -s | marafon
laufen | yugurmoq
gibt es | bor, mavjud
seit | dan beri
der Kilometer, - (km) | kilometr
unterwegs | yo‘lda, safarda
der August (Sg.) | avgust
die Radtour, -en | velosiped sayohati
nach | ga (yo‘nalish bildiradi)
bis | gacha
weiterfahren | yo‘lni davom ettirmoq
die Tour, -en | sayohat, safar
das Wetter (Sg.) | ob-havo
der Herbst (Sg.) | kuz
paar (ein paar) | bir necha
besuchen | tashrif buyurmoq
bleiben | qolmoq
das Volksfest, -e | xalq bayrami
also | demak
fast | deyarli
die Mitte (Sg.) | o‘rtasi
der Oktober (Sg.) | oktyabr
der Anfang, -¨e | boshlanish
der November (Sg.) | noyabr
dieser / dieses / diese | bu (erkak / o‘rta / ayol / ko‘plik shakllar)
etwa | taxminan
der Besucher, - | mehmon, tashrif buyuruvchi (erkak)
die Besucherin, -nen | tashrif buyuruvchi (ayol)
der Winter, - | qish
der Dezember (Sg.) | dekabr
(das) Weihnachten, - | Rojdestvo
feiern | nishonlamoq
zurückfahren | orqaga qaytmoq
(das) Silvester, - | Yangi yil arafasi (31-dekabr)
ziemlich | anchagina
cool | zo‘r, ajoyib
der Sommer, - | yoz
durch | orqali
die Jahreszeit, -en | fasl
der Monat, -e | oy (kalendardagi)
der Geburtstag, -e | tug‘ilgan kun

**Lektion 13**
die Mauer, -n | devor
geteilt (teilen) | bo‘lingan (bo‘lish)
der Mietpreis, -e | ijara narxi
der Tipp, -s | maslahat
der Zoo, -s / der Tierpark, -s | hayvonot bog‘i
die Informatik (Sg.) | informatika
zeigen | ko‘rsatmoq
die Kunst, -e | san’at
die Kultur (Sg.) | madaniyat
das Festival, -s | festival
mancher / manches / manche / manche | ba’zi, ayrim
verrückt | tentak, g‘alati
anders | boshqacha
denken (hat gedacht) | o‘ylamoq
gefallen (hat gefallen) | yoqmoq
billig ↔ teuer | arzon ↔ qimmat
die Wohnung, -en | kvartira
recht haben (hat recht) | haq bo‘lmoq
der Spielplatz, -e | o‘yin maydoni
zum Beispiel (z. B.) | masalan
das Märchen, - | ertak
ganz | butunlay, juda
die Nähe (Sg.) | yaqin joy, atrof
danken | rahmat aytmoq
helfen (hat geholfen) | yordam bermoq
der Park, -s / Pärke | bog‘
der Kinderfilm, -e | bolalar filmi
die Stadt, -e | shahar
die Altstadt, -e | eski shahar qismi
die Kirche, -n | cherkov
das Rathaus, -er | shahar hokimiyati binosi
das Schloss, -er | saroy, qal’a
der Brunnen, - | favvora, quduq
der Markt, -e | bozor
der See, -n | ko‘l
gehören | tegishli bo‘lmoq
wohin | qayerga
reisen (ist gereist) | sayohat qilmoq
Italien | Italiya
die Bibliothek, -en | kutubxona
fehlen | yetishmaslik
das Viertel, - / das Quartier, -e (CH) | tuman, mahalla (kvartal)
das Picknick, -e | piknik
das Boot, -e | qayiq
mieten (hat gemietet) | ijaraga olmoq
der Volleyball, -e | voleybol
die Natur (Sg.) | tabiat
der Ball, -e | to‘p
angeln / fischen (CH) | baliq tutmoq

**Lektion 14**
das Kaufhaus / das Warenhaus (CH), -er | savdo uyi, universal do‘kon
weit | uzoq
der Weg, -e | yo‘l
der Fuß, -e | oyoq
(nach) rechts | o‘ng tomonga
(nach) links | chap tomonga
geradeaus | to‘g‘riga
abbiegen (ist abgebogen) | burilmoq
über | ustidan, orqali
der Meter, - | metr
die Ampel, -n / das Lichtsignal (CH), -e | svetofor
der Platz, -e | maydon
in | ichida
auf | ustida
über | ustidan
unter | ostida
an | yonida, oldida
vor | oldida
hinter | orqasida
neben | yonida
zwischen | orasida
die Brücke, -n | ko‘prik
der Baum, -e | daraxt
das Foto, -s | surat, rasm
das Smartphone, -s | smartfon
beschreiben (hat beschrieben) | tasvirlab bermoq
aussehen (hat ausgesehen) | ko‘rinmoq
ausschauen | tashqi ko‘rinishga ega bo‘lmoq
der Plan, -e | reja, xarita
das Zentrum / die Stadtmitte, -n | shahar markazi
die Ecke / das Eck (A), -n / -en | burchak
das Krankenhaus / das Spital (CH/A), -er / -äler | shifoxona
die Post (Sg.) | pochta
die Bank, -en | bank
die Kreuzung, -en | chorraha
die Polizei (Sg.) | politsiya
die Apotheke, -n | dorixona
die Schule, -n | maktab
der Kindergarten, -n | bolalar bog‘chasi
erste, -n = 1. | birinchi
zweite, -n = 2. | ikkinchi
dritte, -n = 3. | uchinchi
fremd | begona

**Lektion 15**
die Wohngemeinschaft (WG), -en / -s | birga yashash joyi (talabalar uyi, xonadoshlar guruhi)
gemütlich | qulay, shinam
ordentlich | tartibli
überhaupt | umuman
der Balkon, -e | balkon
das Fenster, - | deraza
die Tür, -en | eshik
der Garten, -ä | bog‘
das Zimmer, - | xona
die Küche, -n | oshxona
das Kinderzimmer, - | bolalar xonasi
das Wohnzimmer, - | yashash xonasi
das Arbeitszimmer, - | ish xonasi
das Bad / das Badezimmer, -er / - | hammom
der Flur / der Gang / der Korridor, -e | yo‘lak
das Schlafzimmer, - | yotoqxona
die Toilette, -n | hojatxona
oben | tepada
hinten | orqada
vorn | oldinda
unten | pastda
ihr / ihre | uning (ayol kishiniki)
sein / seine | uning (erkak kishiniki)
umziehen (ist umgezogen) / übersiedeln (ist übersiedelt) | ko‘chib o‘tmoq
laut | shovqinli
die Miete, -n | ijara haqi
der Quadratmeter, - (m²) | kvadrat metr
übermorgen | indinga
das Semester, - | semestr
anfangen (hat angefangen) | boshlanmoq
schlecht | yomon
die Leute (Pl.) | odamlar
inklusive (inkl.) | jumladan, ichiga olgan holda
die Nebenkosten (NK) (Pl.) | qo‘shimcha xarajatlar (kommunal to‘lovlar)
dabei | shu bilan birga
bald | tez orada
die Anzeige / das Inserat (CH), -n / -e | e’lon
möbliert | mebellangan
das Apartment, -s | kichik kvartira
der Stock / das Stockwerk, -e | qavat
sofort | darhol
maximal | eng ko‘pi bilan
bezahlen | to‘lamoq
Traum- | orzudagi (prefiks sifatida: Traumwohnung = orzudagi uy)
gleich | darrov, yonida
der Anwalt, -äe / die Anwältin, -nen | advokat
das Recht (Sg.) | huquq
die Stelle, -n | ish o‘rni
das Einzelbüro, -s | bir kishilik ofis
das Zweierbüro, -s | ikki kishilik ofis
das Dachgeschoss / Dachgeschoß (A), -e | tom osti qavati
die Treppe / die Stiege (A), -n | zina
das Erdgeschoss / Erdgeschoß (A) / Parterre (CH), -e / -s | birinchi qavat (yer qavati)
der Keller, - | yerto‘la (podval)
der (erste) Stock | birinchi qavat
das Großraumbüro, -s | ochiq ofis (ko‘p xodimlar xonasi)
der Empfang / die Reception (CH) | qabulxona, resepsiya
die Kantine, -n | oshxona (ish joyida)
die Konferenz, -en | konferensiya
der Kopierraum, -e | nusxa olish xonasi
die Teeküche, -n | kichik oshxona (pauza uchun joy)
der Briefumschlag / das Kuvert (A), -e / -s | konvert
der Tacker / die Klammerlmaschine (A) / der Bostitch (CH), - / -n / -e | stepler
der Papierkorb, -e | qog‘oz chiqindilar qutisi
der Lautsprecher, - | karnay, dinamika (kolonka)
der Locher, - | teshik qilgich
der Ordner, - | papka
der Notizzettel, - | eslatma varaqasi
die Schere, -n | qaychi
das Headset, -s | quloqchin (mikrofonli)
der Textmarker, - | marker, ajratuvchi ruchka
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
    
    # Lektion 11-15 Additions
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
current_category = "Lektion 11"

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
    
    # Strip complicated alternates (e.g., "das Kaufhaus / das Warenhaus (CH), -er") -> "das Kaufhaus"
    if " / " in german:
        # Keep the first part, but extract the suffix if it exists at the very end
        suffix_match = re.search(r',\s*(-.+)$', german)
        german = german.split(" / ")[0].strip()
        if suffix_match and "," not in german:
            german = german + ", " + suffix_match.group(1).split(" / ")[0].strip()

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
        elif plural_suffix in ["Praxen"]:
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
