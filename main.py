from benchmark import run_benchmarks
from feature_flags import FeatureFlags
from graph import BusNetworkGraph, dijkstra_alg, load_from_json

if __name__ == "__main__":
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
            node = input("Podaj nazwę przystanku: ")
            graph.add_node(node)

        elif choice == "2":
            node = input("Podaj nazwę przystanku do usunięcia: ")
            graph.remove_node(node)

        elif choice == "3":
            from_node = input("Podaj nazwę przystanku początkowego: ")
            to_node = input("Podaj nazwę przystanku końcowego: ")
            weight = float(input("Podaj wagę trasy: "))
            graph.add_edge(from_node, to_node, weight)

        elif choice == "4":
            from_node = input("Podaj nazwę przystanku początkowego: ")
            to_node = input("Podaj nazwę przystanku końcowego: ")
            graph.remove_edge(from_node, to_node)

        elif choice == "5":
            graph.display_graph()

        elif choice == "6":
            start = input("Podaj nazwę przystanku początkowego: ")
            end = input("Podaj nazwę przystanku końcowego: ")
            path, cost = dijkstra_alg(graph.graph, start, end)
            if path:
                print(f"Najkrótsza trasa: {' -> '.join(path)} (koszt: {cost})")
            else:
                print("Brak trasy między wybranymi przystankami.")

        elif choice == "7":
            file_path = input("Podaj ścieżkę do pliku JSON: ")
            load_from_json(graph, file_path)

        elif choice == "8":
            if feature_flags.is_enabled("benchmarking"):
                if not graph.graph:
                    print("Graf jest pusty. Wczytaj dane lub dodaj przystanki i połączenia przed wykonaniem benchmarków.")
                else:
                    print("Uruchamianie benchmarków wydajności...")
                    run_benchmarks()
            else:
                print("Funkcja benchmarków jest wyłączona.")

        elif choice == "9":
            if feature_flags.is_enabled("traffic_optimization"):
                print("Optymalizacja ruchu drogowego jest WŁĄCZONA. Wyłączam...")
                feature_flags.disable("traffic_optimization")
            else:
                print("Optymalizacja ruchu drogowego jest WYŁĄCZONA. Włączam...")
                feature_flags.enable("traffic_optimization")

        elif choice == "10":
            print("Zakończono program.")
            break

        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
