# E-postkonversation: Schemaläggning

**Från:** Ville Andersson <ville.andersson@example.com>  
**Skickat:** Thursday, November 20, 2025 8:27:40 PM  
**Till:** Stoffe Stoffsson <stoffe.stoffsson@example.com>  
**Ämne:** Sv: Schemaläggning

Lokal fackling part

---

**Från:** Stoffe Stoffsson <stoffe.stoffsson@example.com>  
**Skickat:** den 20 november 2025 20:34  
**Till:** Ville Andersson <ville.andersson@example.com>  
**Ämne:** Re: Schemaläggning

Förhandlade med vem?

---

**Från:** Ville Andersson <ville.andersson@example.com>  
**Skickat:** Thursday, November 20, 2025 8:27:40 PM  
**Till:** Stoffe Stoffsson <stoffe.stoffsson@example.com>  
**Ämne:** Sv: Schemaläggning

Snarare en benämning på ett arbetschema med vilka dagar man ska jobba. Så i en grupp kan några medarbetare gå på schema X1, några andra på X2 och någon på X3. Det är förhandlade arbetsscheman man har lokalt som man får använda för att schemalägga medarbetare.

I längden hade det såklart varit intressant att få hjälp att plocka fram optimerade sådana arbetsscheman men ofta är det en mängd såna här man har förhandlade som sen ska matchas mellan det behov man har för att lösa driften och de olika medarbetare man har.

---

**Från:** Stoffe Stoffsson <stoffe.stoffsson@example.com>  
**Skickat:** den 20 november 2025 20:24  
**Till:** Ville Andersson <ville.andersson@example.com>  
**Ämne:** Re: Schemaläggning

Kolumnerna x1, x2 etc. Är det anvisade medarbetare?

---

**Från:** Ville Andersson <ville.andersson@example.com>  
**Skickat:** Thursday, November 20, 2025 7:30:25 PM  
**Till:** Stoffe Stoffsson <stoffe.stoffsson@example.com>  
**Ämne:** Sv: Schemaläggning

Det är hur mycket som skulle behövas i tiden av någon som jobbar heltid. Så om det krävs 1 heltidsekvivalent är det en hel dags arbete 0,25 av det är ju att det behövs en fjärdedel av dagen eller 2 timmar på en 8 timmars dag. Vi använder det för att kunna få en översikt kopplat till hur mkt huvuden som kan behövas för att lösa uppdraget.

Schemarader är ett resultat av olika förhandlade scheman.

Så om man har dessa scheman som är förhandlade med vilka dagar man ska arbeta och när man har lediga dagar:

## Vecka 1

| Dag  | X1 | X2 | X3 | X4 | X5 | X6 | X7 |
|------|----|----|----|----|----|----|----| 
| mån  | 1  | 1  |    | 1  | 1  | 1  |    |
| tis  |    | 1  | 1  | 1  | 1  | 1  |    |
| ons  | 1  | 1  | 1  |    | 1  | 1  |    |
| tors | 1  |    | 1  | 1  | 1  | 1  |    |
| fre  | 1  | 1  | 1  | 1  | 1  | 1  |    |
| lör  |    | 1  |    | 1  |    |    |    |
| sön  |    | 1  |    | 1  |    |    |    |
| **Σ** | **4** | **6** | **4** | **6** | **5** | **5** | **0** |

## Vecka 2

| Dag  | X1 | X2 | X3 | X4 | X5 | X6 | X7 |
|------|----|----|----|----|----|----|----| 
| mån  | 1  | 1  | 1  |    | 1  | 1  |    |
| tis  | 1  |    | 1  | 1  | 1  | 1  |    |
| ons  | 1  | 1  |    | 1  | 1  | 1  |    |
| tors |    | 1  | 1  | 1  |    | 1  |    |
| fre  | 1  | 1  | 1  | 1  |    | 1  |    |
| lör  | 1  |    | 1  |    | 1  |    |    |
| sön  | 1  |    | 1  |    | 1  |    |    |
| **Σ** | **6** | **4** | **6** | **4** | **5** | **5** | **0** |

Där X benämningar är ett förhandlat schema över en två veckors period så kan du se på schema X1 där grönt är dagar man arbetar och blanka är dagar man inte jobbar.

En schemarad för det schemat skulle kunna se ut så här:

## Vecka 1

| Tid             | Mån | Tis   | Ons | Tor | Fre | Lör   | Sön   |
|-----------------|-----|-------|-----|-----|-----|-------|-------|
| Coop 7-10       | ✓   | LEDIG | ✓   | ✓   | ✓   | LEDIG | LEDIG |
| Willys 10-13    | ✓   |       | ✓   | ✓   | ✓   |       |       |
| Trappstäd 13-16 | ✓   |       | ✓   | ✓   | ✓   |       |       |

## Vecka 2

| Tid             | Mån | Tis | Ons | Tor   | Fre | Lör | Sön |
|-----------------|-----|-----|-----|-------|-----|-----|-----|
| Coop 7-10       | ✓   | ✓   | ✓   | LEDIG | ✓   | ✓   | ✓   |
| Willys 10-13    | ✓   | ✓   | ✓   |       | ✓   | ✓   | ✓   |
| Trappstäd 13-16 | ✓   | ✓   | ✓   |       | ✓   | ✓   | ✓   |

En schemarad är ett "tomt" schema där man ser hur man kan fylla en dag för en medarbetare och sen vill man knyta medarbetare till en sådan. Om sen den medarbetaren slutar och man behöver ersätta så får man en tydlig bild av vad man behöver ersätta.

Detta gör vi tillsammans med schemaläggningen i QPlanner idag så den är helt bunden till person, vilket då gör att raden försvinner om personen slutar eller byter chef.

Att skapa schemarader görs som sagt helt manuellt idag så lite ovan är utdrag ur olika tester och prototyper jag gjort med olika insatser genom åren.

---

**Från:** Stoffe Stoffsson <stoffe.stoffsson@example.com>  
**Skickat:** den 20 november 2025 19:11  
**Till:** Ville Andersson <ville.andersson@example.com>  
**Ämne:** Re: Schemaläggning

Förklara heltidsekvivalent

Ge mig ett par exempel på olika schemarader

---

**Från:** Ville Andersson <ville.andersson@example.com>  
**Skickat:** Thursday, November 20, 2025 6:51:33 PM  
**Till:** Stoffe Stoffsson <stoffe.stoffsson@example.com>  
**Ämne:** Sv: Schemaläggning

QPlanner har vi bara som ren schemaläggning så det sista steget här. Sen får vi då varningar för om vi överträder regler i kollektivavtalet. Så den ger ju oss en möjlighet att säkerställa att vi schemalagt korrekt.

För själva Driftplaneringen som vi kallar det och för att generera behov av schemarader har vi inget systemstöd. Det görs manuellt med excelark och whiteboards. Allt det är sen mer eller mindre egenproducerat av en chef.

Det är ett stort gap i vår nuvarande lösning

---

**Från:** Stoffe Stoffsson <stoffe.stoffsson@example.com>  
**Skickat:** den 20 november 2025 18:47  
**Till:** Ville Andersson <ville.andersson@example.com>  
**Ämne:** Re: Schemaläggning

Fantastiskt

Vilket system stöd har vi nu för det här.
Och var kommer QPlanner in i bilden

---

**Från:** Ville Andersson <ville.andersson@example.com>  
**Skickat:** Thursday, November 20, 2025 6:33:58 PM  
**Till:** Stoffe Stoffsson <stoffe.stoffsson@example.com>  
**Ämne:** Schemaläggning

Hej

Se nedan. Va det något sådant du tänker dig eller behöver du mer detaljer? Har bifogat en basic kartläggning av olika kunduppdrag från Halmstad på gamla goda tiden som kanske kan vara till hjälp - där finns redan grupper för samplanering skapat också utifrån en verklig situation:

En FLC är chef över ett område kan vi kalla det.
På det området finns det någonstans mellan 5-20 uppdrag.
Dessa uppdrag har leverans olika veckodagar och tider på dagarna. Vissa uppdrag finns det då tidskrav på och andra kan vara heldagsuppdrag medan andra kan vi lösa uppdraget när som helst på dagen.
Vissa uppdrag kan vara tre dagar i veckan och många är 7 dagar i veckan där något ska göras. Alla uppdrag har inte nödvändigtvis samma tidskrav men minst 25% av uppdragen måste bemannas från start varje dag där är leverans och alla de uppdragen är 7 dagar i veckan.
Dessa uppdrag behöver samplaneras så att man kan få ihop en gruppering som löser en viss mängd uppdrag som matchar så bra som möjligt med tider och dagar för att kunna smeta ut tiderna över veckan. Det är då viktigt med geografisk närhet för att kunna ta sig runt.
Detta i sin tur blir schemarader med vad som ska göras av en viss person och när i veckan. Totalen av det behöver blir antalet medarbetare som behövs för att täcka behovet. Dessa schemarader måste vara baserade på de regelverk vi har med schemaläggning enligt kollektivavtal.
För enkelhetens skull kan vi säga att alla arbetar 38 timmars veckor där röda dagar ingår att arbeta på. Under en 2 veckors period ska man ha 4 lediga dagar och det finns en veckovila regel på 36 timmar. Schemat behöver repeteras på antingen 2 eller 4 veckor.

Stegen är ju enkelt uttryck för oss:
1. Planera ihop olika uppdrag så det blir så få schemarader som möjligt
2. Schemaraderna måste följa vissa regelverk
3. Schemalägg medarbetare mot schemarader

Hör av dig om du behöver något mer som underlag eller du vill att jag förtydligar något. Har säkert en massa annat material också men man kanske inte vill ge dem för mycket heller...

Trevlig kväll!

mvh
Ville