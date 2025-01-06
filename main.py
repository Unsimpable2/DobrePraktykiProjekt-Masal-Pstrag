from graph import BusNetworkGraph

if __name__ == "__main__":
    graph = BusNetworkGraph()

    while True:
        print("\nZarządzanie siecią autobusową")
        print("1. Dodaj przystanek")
        print("2. Usuń przystanek")
        print("3. Dodaj trasę między przystankami")
        print("4. Usuń trasę między przystankami")
        print("5. Wyświetl stan grafu")
        print("6. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            node = input("Podaj nazwę przystanku: ")
            graph.add_node(node)

        elif choice == "2":
            node = input("Podaj nazwę przystanku do usunięcia: ")
            graph.remove_node(node)

        elif choice == "3":
            print("Dostępne przystanki:")
            nodes = graph.display_nodes()
            from_index = int(input("Wybierz numer przystanku początkowego: ")) - 1
            to_index = int(input("Wybierz numer przystanku końcowego: ")) - 1

            if from_index == to_index:
                print("Początkowy i końcowy przystanek nie mogą być takie same.")
            elif 0 <= from_index < len(nodes) and 0 <= to_index < len(nodes):
                from_node = nodes[from_index]
                to_node = nodes[to_index]
                weight = float(input("Podaj wagę trasy (np. czas lub odległość): "))
                graph.add_edge(from_node, to_node, weight)
            else:
                print("Nieprawidłowy wybór przystanków.")

        elif choice == "4":
            print("Dostępne przystanki:")
            nodes = graph.display_nodes()
            from_index = int(input("Wybierz numer przystanku początkowego: ")) - 1
            to_index = int(input("Wybierz numer przystanku końcowego: ")) - 1

            if from_index == to_index:
                print("Początkowy i końcowy przystanek nie mogą być takie same.")
            elif 0 <= from_index < len(nodes) and 0 <= to_index < len(nodes):
                from_node = nodes[from_index]
                to_node = nodes[to_index]
                graph.remove_edge(from_node, to_node)
            else:
                print("Nieprawidłowy wybór przystanków.")

        elif choice == "5":
            graph.display_graph()

        elif choice == "6":
            print("Zakończono program.")
            break

        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
