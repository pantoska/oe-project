# Readme ustawień
## Podział plików
W folderze gui znajduja się pliki związane z okienkiem ustawień:
* `Settings.py` - Kontroler - z niego nalezy korzystać
* `SettingsConst.py` - Stałe używane przy listach rozwijanych
* `SettingsGui.py` - Rysowanie okienka

## Metody kontrolera

#### Konstruktor
Inicjalizuje zmienne

#### showWindow
Tworzy okienko i je wyświetla

#### Wszystkie gettery
Zwracają wartość zapisaną w tablicy w kontrolerze. 
Naciśnięcie przycisku OK w okienku aktualizuje wartosci.

#### Gettery do list rozwijanych
Zwracają one indeks elementu na liście.
Aby wiedzieć, co zostało zaznaczone należy porównywać do stałych

Lista tcyh getterów:
* `getTypeSelection`  
  * `VAL_SELECTIONCHOICE_WHEEL`
  * `VAL_SELECTIONCHOICE_TURNAMENT_SELECTION`
* `getTypeOutBread`
  * `VAL_OUTBREAD_ONE_POINT`
  * `VAL_OUTBREAD_TWO_POINT`
  * `VAL_OUTBREAD_TRIPLE_POINT`
* `getTypeMarginMutation`
  * `VAl_MARGIN_MUTATION_ONE_POINT`
  * `VAl_MARGIN_MUTATION_TWO_POINT`
* `getElityStartegy`
  * `VAL_ELITY_STRATEGY_PERCENT`
  * `VAL_ELITY_STRATEGY_AMOUNT`