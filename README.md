Implementacja algorytmu Prima do wyznaczania minimalnego drzewa rozpinającego				

Projekt: Optymalizacja sieci autobusowej przy użyciu teorii grafów 
Cel projektu: 
    Twoim zadaniem będzie zaprojektowanie i zaimplementowanie systemu, który optymalizuje sieć autobusową, korzystając z teorii grafów. Sieć autobusowa będzie reprezentowana jako graf, gdzie węzły to przystanki autobusowe i zajezdnie, a krawędzie to trasy między nimi. System powinien być w stanie znaleźć najkrótszą trasę między dowolnymi punktami oraz ocenić efektywność algorytmów na podstawie benchmarków.

Projekt będzie rozwijany etapowo, a każdy tydzień wprowadzi nowe zagadnienia, które musisz zaimplementować w projekcie, m.in. testowanie, zarządzanie ryzykiem, kontrola wersji, a także dobra dokumentacja kodu.

Wymagania projektu: 
_____________________________________________________________________________________________________________________________________________
1. Reprezentacja sieci autobusowej (grafów) 

W pierwszym kroku zaimplementuj reprezentację sieci autobusowej w formie grafu. Graf powinien zawierać:

Węzły reprezentujące przystanki i zajezdnie autobusowe.
Krawędzie łączące węzły, które reprezentują możliwe trasy autobusów z przypisanymi wagami (np. czas przejazdu, odległość).
Zaimplementuj podstawowe operacje na grafach, takie jak dodawanie i usuwanie węzłów oraz krawędzi.

Kryteria oceny: 
Czy system posiada interfejs użytkownika do obsługi programu? +
Czy graf jest poprawnie zdefiniowany i łatwy w obsłudze? +
Czy system umożliwia łatwe dodawanie i usuwanie elementów sieci? +
_____________________________________________________________________________________________________________________________________________
2. Znalezienie najkrótszej ścieżki + Benchmarki 
Implementacja algorytmu optymalizacji trasy w sieci autobusowej. Zaimplementuj algorytm Dijkstry, który znajduje najkrótszą trasę między dwoma przystankami w grafie.

Wymagania: 
System powinien znaleźć najkrótszą trasę między dwoma dowolnymi węzłami (przystankami lub zajezdniami).
Uwzględnij wagi krawędzi (np. czas przejazdu lub dystans).
Zmierz wydajność algorytmu: przeprowadź benchmarki dla różnych rozmiarów sieci (np. 10, 100, 1000 węzłów) i zbadaj czas działania oraz zużycie pamięci.

Kryteria oceny: 
Poprawność algorytmu: czy znajduje faktycznie najkrótszą trasę. +
Efektywność: czas działania algorytmu dla różnych wielkości sieci. +
Benchmarki: czy raporty z testów wydajności są poprawnie zrealizowane i przedstawione. +
_____________________________________________________________________________________________________________________________________________
3. Wczytywanie sieci z pliku JSON 
Zaimplementuj możliwość wczytywania sieci autobusowej z pliku JSON. Sieć powinna być reprezentowana w strukturze JSON, która zawiera przystanki, zajezdnie i połączenia między nimi.

Struktura przykładowego pliku JSON: 
{
  "nodes": [
    {"id": "A", "type": "bus_stop", "name": "Przystanek Główna"},
    {"id": "B", "type": "bus_stop", "name": "Przystanek Młynarska"},
    {"id": "C", "type": "bus_stop", "name": "Przystanek Parkowa"},
    {"id": "D", "type": "depot", "name": "Zajezdnia Północ"},
    {"id": "E", "type": "depot", "name": "Zajezdnia Południe"}
  ],
  "edges": [
    {"from": "A", "to": "B", "distance": 3, "time": 6},
    {"from": "B", "to": "C", "distance": 2, "time": 4},
    {"from": "C", "to": "D", "distance": 5, "time": 10},
    {"from": "D", "to": "A", "distance": 8, "time": 16},
    {"from": "B", "to": "E", "distance": 6, "time": 12},
    {"from": "E", "to": "C", "distance": 4, "time": 8}
  ]
}

Kryteria oceny: 
Poprawność wczytywania JSON: Czy system poprawnie parsuje plik JSON i tworzy na jego podstawie graf. +
Elastyczność: Czy system działa z różnymi plikami JSON o różnej strukturze (np. większa liczba węzłów, inne właściwości krawędzi). +
_____________________________________________________________________________________________________________________________________________
4. Kontrola wersji i CI/CD 
Wprowadź system kontroli wersji do projektu (np. Git). Każda nowa funkcjonalność powinna być oddzielnym commitem z odpowiednim opisem.

Skonfiguruj pipeline CI/CD, który będzie automatycznie testował i wdrażał projekt przy każdej nowej zmianie w kodzie.

Wymagania: 
Używaj Git do zarządzania kodem, commitując regularnie i opisując zmiany. 
Skonfiguruj pipeline CI/CD (np. GitHub Actions, GitLab CI), który będzie uruchamiał testy i automatycznie wdrażał aplikację.

Kryteria oceny: 
Czy kontrola wersji jest używana poprawnie (częste commity, opisy zmian)? +
Czy pipeline CI/CD działa poprawnie, uruchamiając testy i wdrażając aplikację? 
_____________________________________________________________________________________________________________________________________________
5. Testowanie kodu (TDD i testy jednostkowe) 
Wprowadź testowanie oparte na podejściu TDD (Test Driven Development). Każdy fragment funkcjonalności, który dodajesz do systemu, powinien być najpierw opisany przez test jednostkowy, a dopiero potem zaimplementowany.
Wymagania: 
Stwórz testy jednostkowe dla podstawowych operacji na grafach (dodawanie węzłów, krawędzi, znajdowanie najkrótszej ścieżki).
Wykorzystaj narzędzia do automatycznego uruchamiania testów (np. JUnit, PyTest).

Kryteria oceny: 
Czy wszystkie funkcjonalności są pokryte testami jednostkowymi? +
Czy kod jest pisany zgodnie z zasadami TDD? +
_____________________________________________________________________________________________________________________________________________
6. Feature Flagi (Zarządzanie ryzykiem) 
Wprowadź mechanizm Feature Flag, który umożliwia dynamiczne włączanie i wyłączanie niektórych funkcji w systemie bez konieczności zmiany kodu.

Wymagania: 
Zaimplementuj możliwość dodawania nowych funkcji (np. optymalizacja pod kątem ruchu drogowego) z możliwością ich wyłączenia bez modyfikacji głównej logiki.
Upewnij się, że system jest w stanie działać nawet bez tych dodatkowych funkcji.

Kryteria oceny: 
Czy mechanizm Feature Flagów działa poprawnie?
Czy możesz łatwo włączać i wyłączać funkcje w systemie?
_____________________________________________________________________________________________________________________________________________
7. Dokumentacja 
Dodaj do systemu dokumentacje, co i jak robi projekt oraz ważne informacje projektowe.

Wymagania i kryteria oceny: 
Dokumentacja w formie docStringów w kodzie
Wygenerowana dokumentacja w postaci github pages i MkDocs (w postaci pipelinu)
Dokładne i dopieszczone README.md projektu
_____________________________________________________________________________________________________________________________________________
8. Code Review i umiejętności miękkie 
Pracując w zespole, przeprowadź code review. Każdy członek zespołu powinien przeanalizować kod innego członka, sugerując poprawki, optymalizacje i lepsze rozwiązania.

Wymagania: 
Każdy musi przeprowadzić przynajmniej jedno code review na kodzie kolegi/koleżanki.
Dyskutujcie o rozwiązaniach w sposób konstruktywny, uzasadniając swoje komentarze.

Kryteria oceny: 
Jakość code review (czy poprawki są wartościowe, czy są konstruktywne).
Umiejętność dyskusji technicznej (czy wyrażacie się jasno i bez zbędnych emocji).
Links to this page