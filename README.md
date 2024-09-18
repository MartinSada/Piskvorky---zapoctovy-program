# Piskvorky---zapoctovy-program
Zadání:
Jednoduchá, funkční hra piškvorky. Není nutné si nadměrně vyhrávat s grafikou.



Technický popis:
Hra používá pro vykreslování primitivní grafiky v konzoli pip balíček curses a skládá se ze třech hlavních částí.

První částí je třída Board, definovaná v souboru board.py. Tato třída udržuje informace o stavu hrací desky - kde jaký hráč nakreslil svoje symboly. Dále obsahuje dvě důležité funkce. Funkce get_symbol vrátí číslo hráče, jehož symbol je na dané souřadnici, nebo None pokud na souřadnici žádný symbol položen není. Funkce add_symbol se pokusí na danou souřadnici nakreslit symbol daného hráče a vrátí -1, pokud je souřadnice neplatná (nějaký symbol se zde už nachází), 0 pokud symbol byl položen ale hráč nevyhrál, nebo 1, pokud položením symbolu hráč vyhrál.

Druhou částí je třída BoardUi, definována v souboru board_ui.py. Tato třída se stará o vykreslování a uživatelské interakce s hrací deskou. Vnitřně si udržuje pozici "kamery", která je 0,0 v prostřed obrazovky a referenci na objekt Board. V konstrukoru jsou třídě předány informace o počtu řádků a sloupců, a také počáteční souřadnici, od které se má v konzoli vykreslovat. Funkce draw vykreslí prostor hrací desky okolo kamery na příslušné místo do konzole. Funkce pick_board_coordinates je funkce, která po zavolání začne v nekonečné smyčce vykreslovat hrací desku s blikajícím kurzorem na pozici kamery, a poté číst klávesy, které uživatel stiskl. Navrátí hodnotu v momentě, kdy uživatel vybere na hrací desce souřadnici. Uživatel může pomocí šipek posouvat pozici kamery, která je indikována blikajícím kurzorem, a pomocí klávesy enter potvrdit svůj výběr.

Třetí částí, která předchozí dvě spojuje do hratelné hry je hlavní soubor main.py. Ten po spuštění načte konfigurační soubor config.json ve formátu JSON, který obsahuje informace o hráčích (jméno, symbol k vykreslování) a nastavení hry (počet symbolů za sebou nutných k výhře). Poté inicializuje knihovnu curses pro grafické vykreslování do terminálu a vykreslí uživatelské rozhraní. Závěrem v nekonečné smyčce začne procházet seznam hráčů, každého nechá zahrát jeho tah a zkontroluje jestli tímto tahem hráč vyhrál, dokud někdo nevyhraje. V případě člověka bude při jeho tahu v nekonečné smyčce volána funkce pick_board_coordinates třídy BoardUi, dokud nebudou vráceny platné souřadnice, na které lze nakreslit symbol.



Instalace a spuštění:
Pro spuštěníé hry je nutno mít nainstalovaný Python 3 a pip balíček curses. Ten je možno na platformě Windows získat pomocí příkazu pip install windows-curses. Na ostatních platformách je curses součástí instalace Pythonu.

Po nainstalování Pythonu a curses je možno hru spustit příkazem "python main.py" zadaným do konzole, spuštěné ve složce obsahující soubor main.py.



Hra:
Po spuštění hry se v konzoli objeví hrací deska s blikajícím kurzorem a nahoře nad hrací deskou místo s informačními texty. Tyto texty hráčům sdělují, kdo je zrovna v průběhu hry na řadě.

Hra se ovládá pomocí ŠIPEK a klávesy ENTER.

Hráč, který začíná, nemá jinou možnost než umístit svůj symbol doprostřed plochy, první tah tedy pouze potvrdí stisknutím klávesy enter. Během každého následujícího tahu pak hráči volí místo, kam umístí svůj symbol, pomocí šipek a následně potvrzují výběr daného místa pomocí klávesy enter. Díky blikajícímu kurzoru má každý hráč při výběru místa pro svůj symbol neustále přehled o tom, kde na hrací desce se zrovna nachází.

Hráči se cyklicky střídají v tazích až do chvíle, kdy jeden z nich vyhraje. Jakmile jeden z hráčů dosáhne dané vítězně kombinace, hra se zastaví, kurzor přestane blikat a na místě s informačními texty nad hrací deskou se objeví nápis oznamující, že daný hráč právě vyhrál.

Následně po stisku další libovolné klávesy se hrací deska zavře a objeví se opět klasická konzole. Hru je následně možné spustit znovu opětovným zadáním příkazu „python main.py“ do konzole.

