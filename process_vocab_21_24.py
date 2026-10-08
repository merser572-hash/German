import json
import re

raw_data = """
**Lektion 21**
werfen | uloqmoq
verboten | taqiqlangan
erlaubt | ruxsat etilgan
der Helm, -e | shlem
gefährlich | xavfli
nutzen | foydalamoq
der Fahrer, - / die Fahrerin, -nen | haydovchi
grillen | go‘sht qovurmoq (barbekyu qilmoq)
stören | bezovta qilmoq
der Nachbar, -n / die Nachbarin, -nen | qo‘shni
die Region, -en | mintaqa
unglaublich | ishonib bo‘lmaydigan, aql bovar qilmas
total | butunlay, juda
der Grill, -s | grill qurilmasi
das Grillfest, -e | grill bayrami
die Terrasse, -n | ayvon, terras
das Grillfleisch (Sg.) | grill go‘shti
der Bekannte, -n / die Bekannte, -n | tanish
schwierig | qiyin
nämlich | ya’ni, aslida
dürfen | ruxsat bo‘lmoq
der Mieter, - / die Mieterin, -nen | ijarachi
müssen | kerak bo‘lmoq
die Hausordnung, -en | uy qoidalari
darin / drin | ichida
meinen | o‘ylamoq, fikr bildirmoq
der Rauch (Sg.) | tutun
gemeinsam | birgalikda
die Umwelt (Sg.) | atrof-muhit
das Gemüse (Sg.) | sabzavot
der Tofu (Sg.) | tofu (soya pishlog‘i)
tragen | ko‘tarmoq, kiyib yurmoq
zelten | chodir qurib yashamoq
baden | cho‘milmoq
abladen | tushirmoq (yukni)
parken | mashina qo‘ymoq
langsam | sekin
die Leine, -n | arqon, bog‘
schieben | itarmoq, surmoq
die Wiese, -n | o‘tloq, maysa
wegwerfen | tashlab yubormoq
das Lokal, -e | kichik restoran, kafeteriy
mitnehmen | o‘zi bilan olib ketmoq
das Verbot, -e | taqiq
die Grundschule, -n | boshlang‘ich maktab
mitbringen | olib kelmoq
angenehm | yoqimli
mega | juda, nihoyatda

**Lektion 22**
die Kleidung, -en | kiyim
das Gewand, -¨er | kiyim
der Platz, -¨e | joy
die Unordnung, -en | tartibsizlik
die Jeans, - | jinsi shim
das Kleidungsstück, -e | kiyim boʻlagi
circa | taxminan
pro | har biri uchun
anziehen | kiymoq
zweimal | ikki marta
der Wahnsinn, - | telbalik
die Billigkleidung, -en | arzon kiyim
anhaben | ustida kiyim bo‘lmoq
der Pullover, - | sviter
das Hemd, -en | ko‘ylak
die Hose, -n | shim
der Mantel, -¨ | palto
die Bluse, -n | bluzka
der Hut, -¨e | shlyapa
die Mütze, -n | shapka
die Haube, -n | qalpoq
die Kappe, -n | kepka
das Kleid, -er | ko‘ylak
der Rock, -¨e | yubka
der Jupe, -s | yubka
der Anzug, -¨e | kostyum
die Socke, -n | paypoq
der Schuh, -e | oyoq kiyim
der Stiefel, - | etik
der Strumpf, -¨e | uzun paypoq
die Kniesocke, -n | tizzagacha paypoq
die Qualität, -en | sifat
tauschen | almashtirmoq
der Billigladen, -¨ | arzon do‘kon
die Möglichkeit, -en | imkoniyat
die Sachen, - | narsalar
die Klamotten, - | kiyim-kechak
nähen | tikmoq
am liebsten | eng yoqadigan tarzda
meistens | ko‘pincha
verschieden | har xil
zusammenpassen | bir-biriga mos kelmoq
am meisten | eng ko‘p
der Roman, -e | roman
hoch | baland
welcher, welches, welche | qaysi
witzig | kulgili

**Lektion 23**
draußen | tashqarida
glücklich | baxtli
die Heimat, -en | vatan
sonnig | quyoshli
kühl | salqin
kalt | sovuq
warm | iliq
der Regen, - | yomg‘ir
der Schnee, - | qor
das Gewitter, - | momaqaldiroq
der Hagel, - | do‘l
die Wolke, -n | bulut
der Wind, -e | shamol
der Nebel, - | tuman
das Grad, -e | daraja
das Meer, -e | dengiz
stark | kuchli
wohl | yaxshi
scheinen | porlamoq, nur sochmoq
der Himmel, - | osmon
irgendwie | qandaydir tarzda
der Schneemann, -¨er | qor odam
der Hai, -e | akula
warum | nima uchun
das Angebot, -e | taklif
der Mond, -e | oy
verfügbar | mavjud
das Reisebüro, -s | sayohat byurosi
still | sokin, jim
das Zelt, -e | chodir
das Kamel, -e | tuya

**Lektion 24**
das Ostern, - | Pasxa bayrami
eigentlich | aslida
schaffen | uddalamoq
die Liebe, -n | sevgi
der Blick, -e | nigoh
die Katze, -n | mushuk
der Unfall, -¨e | baxtsiz hodisa
sterben | o‘lmoq
das Paar, -e | juft, er-xotin
das Datum, -en | sana
das Ereignis, -se | hodisa
das Neujahr, -e | yangi yil
der Karneval, -e | karnaval
der Fasching, -e | karnaval (jan. Germaniya)
die Fastnacht, -en | karnaval (jan. Germaniya)
der Feiertag, -e | bayram kuni
die Hochzeit, -en | to‘y
bestehen | imtihondan o‘tmoq
die Prüfung, -en | imtihon
der Glückwunsch, -¨e | tabrik
alles Gute | eng ezgu tilaklar
gratulieren | tabriklamoq
die Aktion, -en | harakat, aktsiya
die Lösung, -en | yechim
beachten | e’tibor bermoq
der Mitmensch, -en | inson, atrofdagi odam
weltweit | butun dunyo bo‘ylab
stattfinden | bo‘lib o‘tmoq
die Freude, -n | quvonch, zavq
wünschen | tilamoq
es geht um | ...haqida gap ketmoq
die Sympathie, -n | yoqtirish, samimiylik
zusammengehören | bir-biriga tegishli bo‘lmoq
das Haustier, -e | uy hayvoni
das Insekt, -en | hasharot
mitmachen | qatnashmoq
die Generation, -en | avlod
die Veranstaltung, -en | tadbir
im Freien | ochiq havoda
nachsehen | tekshirib ko‘rmoq
der Kommentar, -e | izoh
wunderbar | ajoyib
umarmen | quchoqlamoq
niemals | hech qachon
doof (blöd) | tentak, ahmoq
fast | deyarli
das Kompliment, -e | maqtov
faulenzen | dangasalik qilmoq, bekor yotmoq
die Gesundheit, -en | sog‘liq
die Projektleitung, -en | loyiha rahbari, loyiha boshlig‘i
die Bürogemeinschaft, -en | umumiy ofis (bir nechta odam ishlaydigan joy)
kommunizieren | muloqot qilmoq
mini | juda kichik
eine Mini-Firma | juda kichik firma
das Ziel, -e | maqsad
die Besprechung, -en | yig‘ilish, muhokama
das Programm, -e | dastur
lösen | yechmoq
übernehmen | zimmasiga olmoq, mas’uliyatni o‘z bo‘yniga olmoq
unterstützen | qo‘llab-quvvatlamoq
das Homeoffice | uydan ishlash
das Video, -s | video
kümmern (sich) | g‘amxo‘rlik qilmoq, mas’ul bo‘lmoq
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
    
    # 21-24 Additions
    if "Wand" in word: return word.replace("Wand", "Wänd")
    if "Hut" in word: return word.replace("Hut", "Hüt")
    if "Anzug" in word: return word.replace("Anzug", "Anzüg")
    if "Strumpf" in word: return word.replace("Strumpf", "Strümpf")
    if "Wunsch" in word: return word.replace("Wunsch", "Wünsch")
    
    return word

with open('words.json', 'r', encoding='utf-8') as f:
    existing_words = json.load(f)

max_id = 0
for w in existing_words:
    if int(w['id']) > max_id:
        max_id = int(w['id'])

id_counter = max_id + 1
new_words = []
current_category = "Lektion 21"

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

    # Strip complicated alternates (e.g., "der Fahrer, - / die Fahrerin, -nen") -> "der Fahrer, -"
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
        elif plural_suffix.startswith("¨-") or plural_suffix.startswith('"e'):
            ending = plural_suffix[2:] if plural_suffix.startswith("¨-") else "e"
            plural = f"die {apply_umlaut(word)}{ending}"
        elif plural_suffix.startswith("-"):
            ending = plural_suffix[1:]
            if ending.startswith("¨"): 
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
        elif not plural_suffix.startswith("-") and plural_suffix != "":
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
