# POMAK Kolokwium 2

## 1. Jakie rodzaje laminatów są stosowane do wytwarzania obwodów drukowanych?

Laminaty płytek drukowanych składają się z osnowy (w formie filcu, tkaniny lub maty) i wypełniacza.

### Przykładowe materiały osnowy:
- Celuloza
- Szkło
- Węgiel
- Kevlar

### Przykładowe materiały wypełniacza:
- Żywica fenolowa, epoksydowa, poliimidowa, triazynowa
- Poliester
- Teflon
- Polistyren
- Polietylen

| Zastosowanie | Laminat |
| --- | --- |
| Sprzęt Powszechnego użytku | fenolowo lub epoksydowo papierowy |
| Sprzęt Profesjonalny | epoksydowo szklany |
| Wysokie częstotliwości | Teflonowo, polistyrenowo lub polietylenowo szklany |
| Wysokie temperatury | Poliimidowo lub triazynowo szklany |
| Obwody mikrofalowe | Kevlarowo-szklane, ceramiczne |

### Najczęściej stosowane laminaty:
- FR4 (włókno szklane + żywica epoksydowa)
- CEM (papier + żywica epoksydowa)

## 2. Parametry laminatów
- Rezystancja izolacji [MOhm * 10^5 ???]
- Względna przenikalność elektryczna
- Stratność (?)
- Odporność na temperaturę lutowania
- Max. temperatura pracy
- Wytrzymałość na odrywanie miedzi
- Wytrzymałość mechaniczna
- Odporność na wilgoć

## 3. Rodzaje ceramik stosowanych na podłoża w elektronice:
- Steatytowa
- Alundowa
- Berylowa

## 4. Parametry laminatów stosowanych jako podłoża w mikroelektronice:
- Współczynnik rozszerzalności cieplnej
- Przewodność cieplna
- Rezystancja izolacji, rezystywność skrośna i objętościowa
- Odporność na wilgoć

## 5. W jaki sposób jest wytwarzana mozaika ścieżek przewodzących w obwodzie drukowanym?

Przygotowany gotowy laminat jest czyszczony i pokrywany warstwą fotorezystu. Fotorezyst następnie jest utrwalany (zależnie od jego rodzaju) i naświetlany przez maskę zawierającą wzór ścieżek. Zależnie od rodzaju fotorezystu - części zaciemnione lub naświetlone twardnieją i stają się nierozpuszczalne w wywoływaczu.
Kolejnym krokiem jest wywoływanie - laminat jest zanurzany w wywoływaczu usuwającym rozpuszczalne obszary fotorezystu i odsłaniając w tych miejscach miedź. Następnie laminat zanurzany jest w roztworze trawiącym miedź - obszary chronione przez fotorezyst pozostają nietknięte. Ostatecznie, pozostały fotorezyst jest usuwany (chemicznie lub mechanicznie) a na laminat nakładana jest maska chroniąca ścierzki przed utlenianiem i zwarciom.

## 6. W jaki sposób są wytwarzane wielowarstwowe obwody drukowane?

Poszczególne warstwy (laminat + ścieżki) ułożone są warstwami, z "rdzeniami" - w pełni utwardzonymi laminatami i "preimpregnantami" - nie w pełnie utwardzonymi laminatami, ułożonymi na zmianę.

## 7. Omów pojęcie temperatury kinetycznej.

Jest to średnia energia kinetyczna cząsteczek w danym układzie.

Energię kinetyczną cząsteczki opisuje równanie:

`Ek = 3/2 k * T`

Gdzie:

- Ek - średnia energia kinetyczna cząsteczki [J]
- k - stała Boltzmanna
- T - temperatura [K]

W przypadku gazu doskonałego, temperatura kinetyczna jest wprost proporcjonalne do średniej energii kinetycznej częsteczek gazu.

Równanie gazu doskonałego wynika bezpośrednio z interpretacji temperatury kinetycznej - wyższa temperatura prowadzi do wyższego ciśnienia, ponieważ cząsteczki zderzają się ze ściankami naczynia z większą energią.

Punkt odniesienia temperatury kelvina - 0K odpowiada zerowej energii kinetycznej cząsteczek.

## 8. Energia Termiczna

Jest to suma energii kinetycznej i potencjalnej wszystkich cząsteczek wynikającej z ich ruchów translacyjnych, rotacyjnych, drgań i oddziaływań między nimi.

Jest bezpośrednio związana z temperaturą:

`Et = 3/2 * N * k * T`

Gdzie:

- Et - energia termiczna [J]
- N - liczba cząsteczek w układzie
- k - stała Boltzmanna
- T - temperatura [K]

## 9. Z czym związana jest bariera hydrodynamiczna?

Bariera hydrodynamiczna jest zjawiskiem związanym z siłami hydrodynamicznymi, które utrudniają lub zapobiegają zbliżaniu się cząstek, obiektów lub warstw płynu do siebie w układach dynamicznych.

Związana jest bezpośrednio z lepkością płynu, generującą siły oporu.

## 10. Omów przewodnictwo cieplne.

Zjawisko polegające na przkazywaniu energii cieplnej bez wymiany samych cząsteczek. Zachodzi przez drgania atomów, zdeżenia atomów i cząsteczek lub przepływ elektronów.

Opisywane jest przez prawo Fouriera:

`q = -k(dT/dx)`

Gdzie:

- q - strumień cieplny
- k - współczynnik przewodnictwa cieplnego materiału [W/(m*k)]
- dT/dx - gradient temperatury

## 11. Konwekcja

Proces przekazywania ciepła związany z ruchem materii w gazie lub cieczy.

Z konwekcją związany jest prąd konwekcyjny, spowodowany różnicą gęstości pomiędzy obszarami o niższej i wyższej temperaturze.

## 12. Radiacja

Inaczej promieniowanie - proces emisji energii w postaci fal elektromagnetycznych lub cząsteczek.

Promieniowanie cieplne jest emitowane przez każde ciało o temperaturze > 0K - powodowane jest przez chaotyczny ruch atomów i spowodowaną przez ten ruch osycylacje ładunków elektrycznych.

Długość fali emitowanych przez ciało opisywane jest przez krzywą Plancka:

`LambdaMax = b/T`

Gdzie:

- LambdaMax - długość fali odpowiadająca maksymalnej emisji [m]
- b - stała Wiena [m*K]
- T - temperatura [K];

## 13. Rola topnika w procesie lutowania
- Usuwanie tlenków i zapobieganie utlenianiu;
- Oczyszczanie powierzchni;
- Poprawa adhezji lutu;

## 14. Lutowanie – podział i materiały

### Podział - Temperatura:
- Lutowanie miękkie - < 450°C - lutowanie elementów elektronicznych;
- Lutowanie twarde - > 450°C - Nyaaa :3;

### Podział - Sposób:
- selektywne
- na fali
- rozpływowe

### Materiały:
- Spoiwa lutownicze:
	- Jako podstawa - Cyna
	- Jako dodatek - Ołów, Srebro, Miedź;
- Topniki - o małej, średniej i dużej aktywności.

## 15. Problemy w lutowaniu:
- Zimne złącze (gdy spoiwo nie uległo pełnemu roztopieniu)
- Utlenienie i korozja
- Zła ilość spoiwa w połączeniu (za dużo, za mało)

### Konsekwencje:
Zmniejszenie odporności mechanicznej, zwiększenie rezystancji

## 16. Lutowanie na fali vs rozpływowe:

**Na Fali** - Głównie do lutowania elementów przewlekanych.
1. Płytka jest podgrzewana, by uniknąć szoku termicznego.
2. Płytka jest przepuszczana nad falą stopionego spoiwa. Spoiwo pokrywa wszystkie styki.
3. Płytka jest chłodzona.

**Rozpływowe** - Głównie do lutowanie elementów powierzchniowych.
1. Na pady nakładana jest pasta lutownicza.
2. Elementy umieszczane są na padach.
3. Płytka jest podgrzewana (w piekarniku najczęściej) do temperatury powyżej punktu topnienia lutu.
4. Płytka jest schładzana

## 17. Stop eutektyczny

Jest to stop dwóch lub więcej metali, którego temperatura topnienia jest niższa, niż temperatura topnienia jego składników. (chyba.)

## 18. Jest to rezystancja stykowa

Jest to rezystancja występująca w miejscu kontaktu dwóch przewodników.

### Składają się na nią:
- Efekt zagęszczenia prądu przy mikro-nierównościach stykających się powierzchni.
- Efekt związany z obecnością tlenków, warstw nalotowych i zabrudzeń na powierzchni zestyku.

### Jej wartość zależy od:
- Powierzchni styku
- Siły docisku
- Materiałów, z jakich wykonane są styki.

## 19. Efekt pełzania

Polega na trwałym odkształceniu / uszkodzeniu materiałów pod wpływem długotrwałego działania naprężeń mechanicznych lub temperatury, lub innych procesów (wilgoć, zanieczyszczenia, itp.)

## 20. Metoda flip-chip

Nie ma co opowiadać w sumie... chip montowany jest "do dołu". Połączenia chipu z płytką drukowaną zrobione są za pomocą wypusktek ze stopów lutowniczych. Chip umieszczany jest na podłożu, tak, by wypustki nakładały się na pady na podłożu, a następnie jest wyrównywany. Potem się go spieka i zalewa się jakimś plastkiem pozostałą przestrzeń.

## 21. Techniki montażu

W sensie THT i SMD??? Co to omawiać XD

## 22. Klej anizotropowy

Klej nakładany jest na podłoże i poddany naciskowi (razem z komponentem). Pod wpływem nacisku, cząsteczki przewodnika przemieszczają się, tworząc ścieżki elektryczne tylko w kierunku pionowym. Reszta kleju (najczęściej jakiegoś rodzaju żywica) jest izolatorem, co powoduje brak przewodnictwa w osi X i Y.