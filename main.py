from benchmark import run_benchmarks
from feature_flags import FeatureFlags
from graph import BusNetworkGraph, dijkstra_alg, load_from_json

if __name__ == "__main__":
    """
    Główna aplikacja do zarządzania siecią autobusową.

    Funkcjonalności:
    - Dodawanie i usuwanie przystanków.
    - Dodawanie i usuwanie tras między przystankami.
    - Wyświetlanie stanu grafu.
    - Obliczanie najkrótszej trasy za pomocą algorytmu Dijkstry.
    - Wczytywanie grafu z pliku JSON.
    - Uruchamianie benchmarków wydajności.
    - Włączanie i wyłączanie optymalizacji ruchu drogowego.

    Sterowanie odbywa się za pomocą menu tekstowego.
    """
    graph = BusNetworkGraph()
    feature_flags = FeatureFlags()

    while True:
        print("\nZarządzanie siecią autobusową")
        print("1. Dodaj przystanek")
        print("2. Usuń przystanek")
        print("3. Dodaj trasę między przystankami")
        print("4. Usuń trasę między przystankami")
        print("5. Wyświetl stan grafu")
        print("6. Znajdź najkrótszą trasę (Dijkstra)")
        print("7. Wczytaj sieć z pliku JSON")
        print("8. Wykonaj benchmark wydajności")
        print("9. Włącz/wyłącz optymalizację ruchu drogowego")
        print("10. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            """
            Dodaje nowy przystanek do grafu.

            Użytkownik wprowadza nazwę przystanku.
            """
            node = input("Podaj nazwę przystanku: ")
            graph.add_node(node)

        elif choice == "2":
            """
            Usuwa istniejący przystanek z grafu.

            Użytkownik wprowadza nazwę przystanku do usunięcia.
            """
            node = input("Podaj nazwę przystanku do usunięcia: ")
            graph.remove_node(node)

        elif choice == "3":
            """
            Dodaje trasę (krawędź) między dwoma przystankami.

            Użytkownik wprowadza nazwę przystanku początkowego, końcowego i wagę trasy.
            """
            from_node = input("Podaj nazwę przystanku początkowego: ")
            to_node = input("Podaj nazwę przystanku końcowego: ")
            weight = float(input("Podaj wagę trasy: "))
            graph.add_edge(from_node, to_node, weight)

        elif choice == "4":
            """
            Usuwa trasę (krawędź) między dwoma przystankami.

            Użytkownik wprowadza nazwę przystanku początkowego i końcowego.
            """
            from_node = input("Podaj nazwę przystanku początkowego: ")
            to_node = input("Podaj nazwę przystanku końcowego: ")
            graph.remove_edge(from_node, to_node)

        elif choice == "5":
            """
            Wyświetla aktualny stan grafu.

            Pokazuje listę przystanków oraz ich połączenia.
            """
            graph.display_graph()

        elif choice == "6":
            """
            Znajduje najkrótszą trasę między dwoma przystankami za pomocą algorytmu Dijkstry.

            Użytkownik wprowadza nazwę przystanku początkowego i końcowego.
            """
            start = input("Podaj nazwę przystanku początkowego: ")
            end = input("Podaj nazwę przystanku końcowego: ")
            path, cost = dijkstra_alg(graph.graph, start, end)
            if path:
                print(f"Najkrótsza trasa: {' -> '.join(path)} (koszt: {cost})")
            else:
                print("Brak trasy między wybranymi przystankami.")

        elif choice == "7":
            """
            Wczytuje graf z pliku JSON.

            Użytkownik wprowadza ścieżkę do pliku JSON.
            """
            file_path = input("Podaj ścieżkę do pliku JSON: ")
            load_from_json(graph, file_path)

        elif choice == "8":
            """
            Uruchamia benchmark wydajności dla różnych rozmiarów grafów.

            Funkcja jest dostępna tylko wtedy, gdy benchmarking jest włączony w Feature Flags.
            """
            if feature_flags.is_enabled("benchmarking"):
                if not graph.graph:
                    print("Graf jest pusty. Wczytaj dane lub dodaj przystanki i połączenia przed wykonaniem benchmarków.")
                else:
                    print("Uruchamianie benchmarków wydajności...")
                    run_benchmarks()
            else:
                print("Funkcja benchmarków jest wyłączona.")

        elif choice == "9":
            """
            Włącza lub wyłącza optymalizację ruchu drogowego.

            Zmienia stan flagi "traffic_optimization" w Feature Flags.
            """
            if feature_flags.is_enabled("traffic_optimization"):
                print("Optymalizacja ruchu drogowego jest WŁĄCZONA. Wyłączam...")
                feature_flags.disable("traffic_optimization")
            else:
                print("Optymalizacja ruchu drogowego jest WYŁĄCZONA. Włączam...")
                feature_flags.enable("traffic_optimization")

        elif choice == "10":
            """
            Kończy działanie programu.
            """
            print("Zakończono program.")
            break

        else:
            """
            Wyświetla komunikat o nieprawidłowej opcji w menu.
            """
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
