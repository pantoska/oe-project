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

* getChromosomePrecision
* getPopulation
* getEpoch
* getDivisionSelection
* getPropabilityOutBread
* getPropabilityMutation
* getPropabilityInversion
* getElityPercent
* getElityAmount
* getSaveFilePath
* getXdivisionStart
* getXdivisionEnd
* getYdivisionStart
* getYdivisionEnd
* getZdivisionStart
* getZdivisionEnd

#### Gettery do list rozwijanych
Zwracają one indeks elementu na liście.
Aby wiedzieć, co zostało zaznaczone należy porównywać do stałych

Lista tych getterów:
* `getTypeSelection`  
  * `VAL_SELECTIONCHOICE_WHEEL`
  * `VAL_SELECTIONCHOICE_TURNAMENT_SELECTION`
  * `VAL_SELECTIONCHOICE_THEBEST`
* `getTypeOutBread`
  * `VAL_OUTBREAD_ONE_POINT`
  * `VAL_OUTBREAD_TWO_POINT`
  * `VAL_OUTBREAD_TRIPLE_POINT`
  * `VAL_OUTBREAD_HOMOGENEOUS`
* `getTypeMutation`
  * `VAl_MUTATION_ONE_POINT`
  * `VAl_MUTATION_TWO_POINT`
  * `VAL_MUTATION_MARGIN`
* `getElityStartegy`
  * `VAL_ELITY_STRATEGY_PERCENT`
  * `VAL_ELITY_STRATEGY_AMOUNT`
* `getTypeOfFunction`
  * `VAL_MINIMALIZATION`
  * `VAL_MAXIMALIZATION`
  
# Funkcjonowanie

W pliku main jest tylko uruchamianie aplikacji, działanie jest zapisane w App.py.

Dostęp do ustawionych wartości z pliku App.py:

`self.frame.panel.settingswindow`

Akcja wywoływana po naciśnięciu Ok w ustawieniach to:

`SetData` w App