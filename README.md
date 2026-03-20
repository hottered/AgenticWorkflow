# Napredni-SWE  
__Repozitorijum namenjen za čuvanje materijala i dokumentacije potrebne za razvoj i razumevanje aplikacije zasnovane na više inteligentnih agenata__  

## Tutorijal: Razvoj aplikacije sa više agenata za obradu zahteva i generisanje odgovora  

## **1. O samom README.md fajlu**  

Ovaj fajl služi kao uvod i vodič kroz projekat koji implementira sistem zasnovan na više agenata. Glavni cilj je da se:  
- Ukaže na prednosti korišćenja više specijalizovanih agenata unutar jedne aplikacije.  
- Prikaže kako sistem može da obradi različite tipove zahteva (npr. odgovaranje na pitanja, pomoć pri kodiranju, analiza sadržaja).  
- Objasni osnovna arhitektura i način rada sistema (od inicijalnog zahteva do generisanja odgovora).  

Ovaj tutorijal će vas postepeno uvesti u koncepte dizajna sistema, komunikacije između agenata i organizacije logike potrebne za izgradnju fleksibilne i proširive aplikacije.

## **2. Šta je sistem sa više agenata?**

Sistem sa više agenata predstavlja softversku arhitekturu u kojoj više specijalizovanih komponenti (agenata) sarađuje kako bi obradilo korisnički zahtev i generisalo što kvalitetniji odgovor. Svaki agent ima jasno definisanu ulogu i odgovornost, što omogućava efikasniju obradu složenih zadataka u poređenju sa jednim centralizovanim sistemom.

Ovakav pristup omogućava podelu posla na manje celine, gde svaki agent rešava određeni problem – na primer, jedan agent može biti zadužen za analizu zahteva, drugi za generisanje odgovora, a treći za validaciju ili dodatnu obradu rezultata.

### **Istorija i koncept**

Ideja sistema sa više agenata potiče iz oblasti distribuiranih sistema i veštačke inteligencije. Kroz razvoj softverskog inženjerstva, pojavila se potreba za sistemima koji mogu paralelno da obrađuju zadatke, budu fleksibilni i lako proširivi.

Sa razvojem modernih aplikacija, ovaj pristup je postao posebno značajan jer omogućava:
- bolju organizaciju kompleksnih sistema  
- lakše održavanje i nadogradnju  
- efikasnije rešavanje specifičnih problema kroz specijalizaciju  

### **Kako funkcioniše?**
___

Sistem funkcioniše tako što korisnički zahtev prolazi kroz više agenata koji međusobno komuniciraju i razmenjuju informacije. Svaki agent obrađuje deo zadatka i prosleđuje rezultat sledećem agentu u lancu obrade.

Na primer:
1. Prvi agent prima zahtev i razume njegov kontekst.  
2. Sledeći agent obrađuje konkretan zadatak (npr. generisanje odgovora ili rešavanje problema).  
3. Završni agent proverava i formatira rezultat pre nego što se vrati korisniku.  

Ovakva arhitektura omogućava fleksibilnost i lako dodavanje novih funkcionalnosti bez potrebe za izmenom celog sistema.

Danas se sistemi sa više agenata koriste u raznim domenima – od automatizacije zadataka do naprednih sistema za komunikaciju i podršku korisnicima.


### **Ključne prednosti sistema sa više agenata**
- **Modularnost**: Sistem je podeljen na manje, nezavisne komponente koje je lako razvijati i održavati.  
- **Fleksibilnost**: Moguće je dodavati nove agente ili menjati postojeće bez velikih promena u ostatku sistema.  
- **Specijalizacija**: Svaki agent je optimizovan za određeni tip zadatka, što poboljšava ukupne performanse.  
- **Skalabilnost**: Sistem može da raste dodavanjem novih agenata ili instanci postojećih.  
- **Bolja organizacija logike**: Kompleksni problemi se razbijaju na manje, lakše rešive celine.  

Ovakav pristup je posebno koristan za aplikacije koje treba da obrade različite tipove zahteva i pruže precizne i kontekstualno relevantne odgovore.

## **3. Problemi koje sistem rešava**:
- **Preopterećenje jednog sistema**
Jedan monolitni sistem teško može efikasno da obrađuje različite tipove zahteva. Podela na više agenata omogućava raspodelu opterećenja.

- **Loša organizacija koda**
Veliki sistemi često postaju neuredni i teški za održavanje. Modularni pristup kroz agente donosi jasnu strukturu i odgovornosti.

- **Teško proširivanje funkcionalnosti**
Dodavanje novih mogućnosti u monolitnim aplikacijama može biti komplikovano. Kod sistema sa agentima, nova funkcionalnost se dodaje kroz novog agenta.

- **Nedovoljno kvalitetni odgovori**
Specijalizovani agenti mogu dati preciznije i kvalitetnije rezultate u svojoj oblasti nego jedan opšti sistem.

- **Spor razvoj i iteracije**
Razvoj je brži jer tim može paralelno raditi na različitim agentima.

- **Održavanje i debagovanje**
Lakše je identifikovati problem kada je sistem podeljen na manje, izolovane komponente.

Ovakav sistem omogućava razvoj robusnih, skalabilnih i prilagodljivih aplikacija koje mogu efikasno odgovoriti na različite zahteve korisnika.

## **4. Koraci za kreiranje i pokretanje sistema sa više agenata**

Za razliku od kompleksnih sistema, ovde je fokus na dobroj organizaciji i jasnoj podeli odgovornosti između agenata.

Da biste kreirali i pokrenuli sistem, pratite sledeće korake:

1. **Definišite cilj sistema** – šta treba da radi i koje probleme rešava.  
2. **Podelite sistem na agente** – svaki agent ima svoju ulogu (npr. obrada zahteva, generisanje odgovora).  
3. **Definišite komunikaciju** – kako agenti razmenjuju podatke i redosled izvršavanja.  
4. **Implementirajte osnovnu logiku** – napravite jednostavnu verziju svakog agenta.  
5. **Povežite agente** – formirajte tok kroz koji prolazi zahtev.  
6. **Testirajte i pokrenite sistem** – proverite rad i dalje ga unapređujte.


## Pregled projekta
 
Ovaj projekat implementira **multi-agentni sistem** koji omogućava autonomno izvršavanje programerskih zadataka na definisanom projektu. Korisnik unosi zadatak u prirodnom jeziku, a sistem automatski:
 
1. Rutera upit ka odgovarajućem agentu
2. Analizira strukturu projekta
3. Izvršava potrebne operacije (čitanje/pisanje fajlova, komande u terminalu)
4. Vraća detaljan izveštaj o izvršenom zadatku

## Arhitektura sistema
 
```
main.py
  └── AgentRouter
        └── CodingAgent
              ├── ProjectTools  (write_file, read_file, exec_command)
              ├── Tools         (definicije alata za LLM)
              └── TaskCompletion (izveštaj o završenom zadatku)
        └── ConversationAgent
              └── TaskCompletion (izveštaj o završenom zadatku)
```
___

## Komponente
 
### CodingAgent
 
**Fajl:** `coding_agent.py`
 
Centralna komponenta sistema. Nasleđuje `BaseAgent` i odgovorna je za:
 
- Inicijalizaciju konteksta (system prompt + struktura projekta)
- Komunikaciju sa LLM modelom u petlji
- Izvršavanje tool call-ova koje model vraća
- Detektovanje završetka zadatka
 
**Ključni parametri:**
 
| Parametar | Tip | Opis |
|---|---|---|
| `project_root` | `str` | Putanja do korena projekta |
| `model` | `str` | LLM model koji se koristi (default: `gpt-4o-mini`) |
 
**Tok rada agenta:**
 
1. Inicijalizuje poruke sa system promptom i strukturom projekta
2. U petlji poziva LLM (maksimalno 20 iteracija)
3. Ako model vrati `tool_calls`, izvršava ih i dodaje rezultate u kontekst
4. Kada model pozove `complete_task`, petlja se završava i vraća se izveštaj
5. Ako model ne pozove alat, agent ga podseti da mora da pozove `complete_task`
 
---
 
### ConversationalAgent
 
**Fajl:** `conversational_agent.py`
 
Lagan agent namenjen za slobodan razgovor sa korisnikom. Nasleđuje `BaseAgent` i ne koristi alate — jedina njegova svrha je da prirodno i prijateljski odgovori na korisnikovu poruku.
 
Za razliku od `CodingAgent`-a, ovaj agent:
 
- Ne izvršava nikakve operacije nad projektom
- Nema petlju ni tool call-ove — radi u jednom pozivu ka LLM-u
- Komunicira isključivo na **srpskom jeziku**
- Može koristiti emoji-je tamo gde je to prikladno
 
**Tok rada agenta:**
 
1. Prima korisničku poruku
2. Inicijalizuje kontekst sa system promptom i porukom
3. Poziva LLM jednom i direktno vraća odgovor
 
**Primer interakcije:**
 
```
Ti: Kako si danas?
 
Agent: Odlično, hvala što pitaš! 😊 Spreman sam da ti pomognem
       sa svim što ti treba. Šta mogu da uradim za tebe?
```
 
---
 
### AgentRouter
 
**Fajl:** `router_agent.py`
 
Odgovoran za rutiranje korisničkih upita ka odgovarajućem agentu (npr. `CodingAgent` ili drugi specijalizovani agenti u sistemu).
 
---
 
### TaskCompletion
 
**Fajl:** `task_completion.py`
 
Data klasa koja čuva i formatira izveštaj o završenom zadatku.
 
**Atributi:**
 
| Atribut | Tip | Opis |
|---|---|---|
| `summary` | `str` | Detaljan opis izvršenih akcija |
| `files_modified` | `List[str]` | Lista kreiranih ili modifikovanih fajlova |
| `commands_executed` | `List[str]` | Lista izvršenih shell komandi |
| `success` | `bool` | Da li je zadatak uspešno završen |
| `next_steps` | `Optional[str]` | Opcioni predlozi za sledeće korake |
 
**Primer formatiranog izlaza:**
 
```
============================================================
TASK FINISHED
============================================================
 
📋 SUMMARY:
Kreiran novi Python modul sa helper funkcijama.
 
📁 MODIFIED/CREATED FILES:
  • src/utils/helpers.py
 
⚙️  EXECUTED COMMANDS:
  • pip install requests
 
💡 NEXT STEPS:
Dodati unit testove za nove funkcije.
 
============================================================
```
 
---
 
### Alati (Tools)
 
**Fajl:** `tools.py`
 
Definicije alata koje LLM model može da pozove tokom izvršavanja zadatka.
 
#### `write_file`
Kreira ili prepisuje fajl na zadatoj putanji unutar `project_root`.
 
```json
{
  "path": "src/main.py",
  "content": "print('Hello, world!')"
}
```
 
#### `read_file`
Čita sadržaj fajla. Dozvoljeno samo unutar `project_root`.
 
```json
{
  "path": "src/config.py"
}
```
 
#### `exec_command`
Izvršava shell komandu. Komande treba da budu minimalne i bezbedne.
 
```json
{
  "command": "pip install requests"
}
```
 
> ⚠️ **Napomena:** Za pisanje sadržaja u fajl uvek koristiti `write_file`, a ne `exec_command`.

#### `complete_task`
Poziva se kada je zadatak **u potpunosti završen**. Bez ovog poziva, agent neće završiti izvršavanje.
 
```json
{
  "summary": "Opis svega što je urađeno...",
  "files_modified": ["src/app.py"],
  "commands_executed": ["pip install flask"],
  "success": true,
  "next_steps": "Pokrenuti server sa: python src/app.py"
}
```
 
---
 
### System Prompt
 
**Fajl:** `coding_agent_system_prompt.py`
 
Definišu se osnovna pravila ponašanja agenta:
 
- Ne sme da pretpostavlja postojanje fajlova koji nisu u strukturi projekta
- Sve putanje moraju biti relativne u odnosu na `project_root`
- Pre pisanja fajla mora da analizira strukturu projekta
- Shell komande moraju biti minimalne i bezbedne
- Na kraju zadatka mora pozvati `complete_task` alat
 
---

## Pokretanje sistema
 
### Preduslovi
 
```bash
pip install openai pydantic
export OPENAI_API_KEY="sk-..."
```
 
### Entry point
 
```bash
python main.py
```
 
Nakon pokretanja, sistem će tražiti unos putanje do project root-a:
 
```
Enter project root: /home/user/my-project
Multi-Agent System running!
Press 'exit' or 'quit' to leave the session.
 
Ti:
```
 
Ako uneta putanja ne postoji ili nije direktorijum, sistem nastavlja bez `CodingAgent`-a:
 
```
WARNING: Coding agent not available (project root not found).
Multi-Agent System running!
```
 
---
 
## Tok sistema
 
```
main.py
  └── AgentRouter
        ├── _detect_intent(user_input)
        │     ├── sadrži coding keyword → CodingAgent
        │     └── ne sadrži         → ConversationalAgent
        │
        ├── CodingAgent.run(task)
        │     ├── _initialize_messages()  ← učitava folder strukturu
        │     ├── LLM loop (max 20 iteracija)
        │     │     ├── write_file
        │     │     ├── read_file
        │     │     ├── exec_command
        │     │     └── complete_task  ← završava loop
        │     └── vraća TaskCompletion.__str__()
        │
        └── ConversationalAgent.run(user_input)
              └── vraća slobodan tekstualni odgovor
```
 
---
 
## Use Case 1 — ConversationalAgent
 
**Trigger:** unos ne sadrži nijedan od coding keyword-a (`create`, `edit`, `fix`, `build`, `implement`, `refactor`, `debug`, `code`, `script`, `function`, `class`, `module`).
 
**Primer sesije:**
 
```
Ti: Kako funkcioniše dependency injection?
 
Agent: Dependency injection je dizajn patern u kome objekat dobija
svoje zavisnosti izvana umesto da ih sam kreira...
```
 
```
Ti: Koji su principi SOLID arhitekture?
 
Agent: SOLID je akronim za pet principa objektno-orijentisanog dizajna:
S - Single Responsibility, O - Open/Closed...
```
 
**Šta se dešava ispod haube:**
 
1. `AgentRouter._detect_intent()` ne pronalazi coding keyword → vraća `"conversational"`
2. Poziva se `ConversationalAgent.run(user_input)`
3. LLM odgovara slobodnim tekstom, bez tool call-ova
4. Odgovor se ispisuje direktno u konzoli
 
---
 
## Use Case 2 — CodingAgent
 
**Trigger:** unos sadrži bar jedan od coding keyword-a.
 
**Primer sesije:**
 
```
Ti: Create a Python function that reads a CSV file and returns a list of dicts
 
Agent:
============================================================
TASK FINISHED
============================================================
 
📋 SUMMARY:
Kreirana je funkcija `read_csv_to_dicts` u fajlu `utils/csv_reader.py`.
Funkcija koristi Python-ov `csv.DictReader` za čitanje fajla i vraća
listu rečnika gde svaki red predstavlja jedan rečnik.
 
📁 MODIFIED/CREATED FILES:
  • utils/csv_reader.py
 
⚙️  EXECUTED COMMANDS:
  • (nema izvršenih komandi)
 
💡 NEXT STEPS:
Dodati error handling za slučaj kada fajl ne postoji ili ima pogrešan format.
 
============================================================
```
 
**Šta se dešava ispod haube:**
 
1. `AgentRouter._detect_intent()` pronalazi keyword `"create"` → vraća `"coding"`
2. `CodingAgent._initialize_messages()` učitava folder strukturu projekta via `get_folder_structure()`
3. Startuje LLM loop (max 20 iteracija):
   - LLM poziva `write_file` → kreira/menja fajl na disku
   - LLM poziva `read_file` → čita postojeći fajl ako treba
   - LLM poziva `exec_command` → izvršava shell komandu (npr. `python -m pytest`)
   - Na kraju LLM poziva `complete_task` → popunjava `TaskCompletion` objekat i loop se prekida
4. `TaskCompletion.__str__()` formatira i ispisuje finalni izveštaj
 
**Primer sa izvršavanjem komande:**
 
```
Ti: Fix the failing tests in the auth module and run them
 
Agent:
============================================================
TASK FINISHED
============================================================
 
📋 SUMMARY:
Pronađena je greška u `auth/validators.py` — funkcija `validate_token`
nije proveravala expiry polje. Dodata je validacija i testovi sada prolaze.
 
📁 MODIFIED/CREATED FILES:
  • auth/validators.py
 
⚙️  EXECUTED COMMANDS:
  • python -m pytest tests/test_auth.py -v
 
💡 NEXT STEPS:
Razmotriti dodavanje integration testova za token refresh flow.
 
============================================================
```
 
---
 
## Izlaz iz sesije
 
```
Ti: exit
 
Goodbye... :(
```
 
Podržane komande za izlaz: `exit`, `quit`, `izlaz`.
 
---

## Napomene
 
- Agent **ne sme** da menja fajlove van `project_root` foldera.
- Ako `project_root` nije pronađen pri pokretanju, `CodingAgent` neće biti dostupan, ali ostatak sistema i dalje funkcioniše.
- Svaki zadatak startuje sa svežim kontekstom — agent nema memoriju prethodnih sesija.
 
---
 
## Slični proizvodi
 
Postoji nekoliko sličnih alata i platformi koji rešavaju isti problem — autonomno AI kodiranje. Svaki ima drugačiji pristup, nivo autonomije i okruženje u kome radi.

### Aider
**Tip:** Open-source CLI alat  
**Repozitorijum:** [github.com/paul-gauthier/aider](https://github.com/paul-gauthier/aider)
 
Aider je popularan terminal-first alat koji radi direktno sa Git repozitorijumom. Karakteriše ga git-native pristup — sve promene se commituju u malim, preglednim diff-ovima, što ga čini odličnim za refaktoring i code review petlje. Podržava GPT-4, Claude i druge modele putem API ključa.
 
**Sličnosti sa ovim projektom:** Koristi LLM pozive sa alatima za čitanje/pisanje fajlova, radi nad project root-om.  
**Razlike:** Terminal-first, nema routing između agenata, fokus na Git workflow.
 
---

### OpenHands (bivši OpenDevin)
**Tip:** Open-source platforma, SaaS i self-hosted opcija  
**Repozitorijum:** [github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)
 
OpenHands je platforma koja se ponaša kao pravi developer — može da menja fajlove, izvršava shell komande, pretražuje web, poziva API-je i kreira kompleksne aplikacije od nule. Ima bogat interfejs sa chat panelom, VS Code integracijom, Jupyter notebook podrškom i terminalom. Podržava više LLM modela putem `litellm` biblioteke, a default model je Claude Sonnet.
 
**Sličnosti sa ovim projektom:** Isti koncept agenta sa alatima (`write_file`, `exec_command`), task completion loop, system prompt sa pravilima.  
**Razlike:** Mnogo širi scope (web browsing, API pozivi), enterprise sandbox okruženje, kompleksniji UI.
 
---