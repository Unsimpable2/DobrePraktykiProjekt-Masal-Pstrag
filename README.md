# Dokumentacja Projektu: Optymalizacja Sieci Autobusowej

## Opis Projektu
Projekt ma na celu modelowanie i optymalizację sieci autobusowej za pomocą teorii grafów. Główne funkcjonalności obejmują:
- Reprezentację sieci autobusowej jako grafu (węzły to przystanki, a krawędzie to trasy między nimi).
- Obsługę operacji na grafie, takich jak dodawanie i usuwanie węzłów oraz krawędzi.
- Obliczanie najkrótszej trasy za pomocą algorytmu Dijkstry.
- Możliwość dynamicznego zarządzania funkcjami systemu dzięki mechanizmowi Feature Flags.
- Benchmarki wydajności dla różnych wielkości grafów.

---

## Funkcjonalności
### 1. Zarządzanie Grafem
- Dodawanie przystanków (węzłów).
- Usuwanie przystanków.
- Dodawanie tras (krawędzi) z określoną wagą (np. odległością lub czasem przejazdu).
- Usuwanie tras.
- Wyświetlanie aktualnego stanu grafu.

### 2. Algorytm Dijkstry
- Znajdowanie najkrótszej trasy między wybranymi przystankami.
- Obsługa optymalizacji wag tras na podstawie ruchu drogowego (Feature Flag).

### 3. Wczytywanie Grafu z Pliku JSON
- Obsługa plików JSON o strukturze zawierającej węzły, krawędzie i dodatkowe właściwości grafu.

### 4. Benchmarki Wydajności
- Testy wydajności dla grafów o różnych rozmiarach (np. 10, 100, 1000 węzłów).
- Generowanie raportów z czasów wykonania operacji.

### 5. Feature Flags
- Mechanizm dynamicznego włączania/wyłączania funkcji.
- Flagi obsługiwane w pliku `feature_flags.json`.

---

## Struktura Projektu
```
project/
├── main.py                    # Główna aplikacja
├── graph/
│   ├── __init__.py            # Inicjalizacja modułu grafu
│   ├── graph.py               # Klasa BusNetworkGraph
│   ├── dijkstra_alg.py        # Implementacja algorytmu Dijkstry
│   ├── json_import.py         # Obsługa wczytywania grafu z JSON
├── tests/
│   ├── __init__.py            # Inicjalizacja modułu testów
│   ├── test_add_node.py       # Test dodawania węzłów
│   ├── test_remove_node.py    # Test usuwania węzłów
│   ├── test_add_edge.py       # Test dodawania krawędzi
│   ├── test_remove_edge.py    # Test usuwania krawędzi
│   ├── test_dijkstra_alg.py   # Test algorytmu Dijkstry
│   ├── test_load_from_json.py # Test wczytywania grafu z JSON
├── .gitignore                 # Gitignore z ignorowaniem niepotrzebnych plików
├── 10.json                    # Plik JSON z 10 przystankami i łaczeniami
├── 100.json                   # Plik JSON z 100 przystankami i łaczeniami
├── 100.json                   # Plik JSON z 1000 przystankami i łaczeniami
├── benchmarks.py              # Benchmarki wydajności
├── feature_flags.py           # Mechanizm Feature Flags
├── feature_flags.json         # Konfiguracja Feature Flags
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Konfiguracja CI/CD (GitHub Actions)
```

---

## Plik feature_flags.json
```json
{
    "traffic_optimization": false,
    "benchmarking": true,
    "enable_add_node": true,
    "enable_remove_node": true,
    "enable_add_edge": true,
    "enable_remove_edge": true,
    "enable_display_graph": true,
    "enable_load_nodes": true,
    "enable_load_edges": true,
    "enable_load_properties": true
}
```

- **traffic_optimization:** Optymalizacja wag tras na podstawie ruchu drogowego.
- **benchmarking:** Włączanie/wyłączanie benchmarków.
- **enable_add_node:** Włączenie/wyłączenie dodawania węzłów.
- **enable_remove_node:** Włączenie/wyłączenie usuwania węzłów.
- **enable_add_edge:** Włączenie/wyłączenie dodawania krawędzi.
- **enable_remove_edge:** Włączenie/wyłączenie usuwania krawędzi.
- **enable_display_graph:** Włączenie/wyłączenie wyświetlania grafu.
- **enable_load_nodes:** Włączenie/wyłączenie wczytywania węzłów z JSON.
- **enable_load_edges:** Włączenie/wyłączenie wczytywania krawędzi z JSON.
- **enable_load_properties:** Włączenie/wyłączenie wczytywania dodatkowych właściwości.

---

## Uruchamianie
### 1. Uruchamianie aplikacji
```bash
python main.py
```

### 2. Uruchamianie testów
```bash
pytest tests/
```

### 3. Lokalna symulacja CI/CD
Jeśli używasz narzędzia [Act](https://github.com/nektos/act):
```bash
act push -j test
```

---

## Konfiguracja CI/CD
- **Plik `.github/workflows/ci-cd.yml`** definiuje pipeline CI/CD z:
  - Testami jednostkowymi.
  - Symulacją wdrożenia.
- Pipeline uruchamia się automatycznie przy zmianach w głównej gałęzi (`main`).

---

## Benchmarki
- Obsługuje testy wydajności dla grafów o różnych rozmiarach.
- Wyniki są prezentowane w konsoli.

Przykładowy wynik dla grafu 1000 węzłów:
```
Dodawanie węzłów: 0.1234 s
Dodawanie krawędzi: 0.5678 s
Najkrótsza ścieżka: 1.2345 s
```

---

## Przykładowy plik JSON
```json
{
    "nodes": ["Stop_1", "Stop_2", "Stop_3"],
    "edges": [
        {"from": "Stop_1", "to": "Stop_2", "weight": 5},
        {"from": "Stop_2", "to": "Stop_3", "weight": 10}
    ],
    "properties": {
        "description": "Przykładowy graf autobusowy"
    }
}
```

---

## Rozszerzenia
- Wdrożenie algorytmu A* dla lepszej wydajności w dużych grafach.
- Wizualizacja grafu za pomocą bibliotek takich jak `matplotlib` lub `networkx`.
- Dynamiczne wczytywanie danych o ruchu drogowym w czasie rzeczywistym.
