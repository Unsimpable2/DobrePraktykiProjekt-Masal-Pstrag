from feature_flags import FeatureFlags

class BusNetworkGraph:
    """
    Klasa reprezentująca sieć autobusową jako graf.
    Zarządza węzłami (przystankami) oraz krawędziami (trasami między przystankami).
    Obsługuje dynamiczne włączanie i wyłączanie funkcji za pomocą Feature Flags.
    """

    def __init__(self):
        """
        Inicjalizuje pusty graf oraz mechanizm Feature Flags.
        """
        self.graph = {}
        self.feature_flags = FeatureFlags()

    def add_node(self, node):
        """
        Dodaje nowy węzeł (przystanek) do grafu.

        Args:
            node (str): Nazwa węzła do dodania.

        Returns:
            None

        Wyświetla komunikat, jeśli dodawanie węzłów jest wyłączone lub węzeł już istnieje.
        """
        if not self.feature_flags.is_enabled("enable_add_node"):
            print("Funkcja dodawania węzłów jest wyłączona.")
            return

        if node not in self.graph:
            self.graph[node] = {}
            print(f"Węzeł '{node}' został dodany.")
        else:
            print(f"Węzeł '{node}' już istnieje.")

    def remove_node(self, node):
        """
        Usuwa węzeł (przystanek) z grafu.

        Args:
            node (str): Nazwa węzła do usunięcia.

        Returns:
            None

        Wyświetla komunikat, jeśli usuwanie węzłów jest wyłączone lub węzeł nie istnieje.
        """
        if not self.feature_flags.is_enabled("enable_remove_node"):
            print("Funkcja usuwania węzłów jest wyłączona.")
            return

        if node in self.graph:
            del self.graph[node]
            for edges in self.graph.values():
                edges.pop(node, None)
            print(f"Węzeł '{node}' został usunięty.")
        else:
            print(f"Węzeł '{node}' nie istnieje.")

    def add_edge(self, from_node, to_node, weight):
        """
        Dodaje nową krawędź (trasę) między węzłami do grafu.

        Args:
            from_node (str): Węzeł początkowy.
            to_node (str): Węzeł końcowy.
            weight (float): Waga krawędzi (np. odległość lub czas przejazdu).

        Returns:
            None

        Wyświetla komunikat, jeśli dodawanie krawędzi jest wyłączone, węzły nie istnieją
        lub węzeł początkowy i końcowy są takie same.
        """
        if not self.feature_flags.is_enabled("enable_add_edge"):
            print("Funkcja dodawania krawędzi jest wyłączona.")
            return

        if from_node == to_node:
            print("Początkowy i końcowy przystanek nie mogą być takie same.")
            return

        if from_node not in self.graph:
            print(f"Węzeł początkowy '{from_node}' nie istnieje. Najpierw go dodaj.")
            return
        if to_node not in self.graph:
            print(f"Węzeł końcowy '{to_node}' nie istnieje. Najpierw go dodaj.")
            return

        self.graph[from_node][to_node] = weight
        print(f"Krawędź z '{from_node}' do '{to_node}' o wadze {weight} została dodana.")

    def remove_edge(self, from_node, to_node):
        """
        Usuwa krawędź (trasę) między węzłami z grafu.

        Args:
            from_node (str): Węzeł początkowy.
            to_node (str): Węzeł końcowy.

        Returns:
            None

        Wyświetla komunikat, jeśli usuwanie krawędzi jest wyłączone lub krawędź nie istnieje.
        """
        if not self.feature_flags.is_enabled("enable_remove_edge"):
            print("Funkcja usuwania krawędzi jest wyłączona.")
            return

        if from_node in self.graph and to_node in self.graph[from_node]:
            del self.graph[from_node][to_node]
            print(f"Krawędź z '{from_node}' do '{to_node}' została usunięta.")
        else:
            print(f"Krawędź z '{from_node}' do '{to_node}' nie istnieje.")

    def display_graph(self):
        """
        Wyświetla aktualny stan grafu (węzły i krawędzie).

        Returns:
            None

        Wyświetla komunikat, jeśli wyświetlanie grafu jest wyłączone.
        """
        if not self.feature_flags.is_enabled("enable_display_graph"):
            print("Funkcja wyświetlania grafu jest wyłączona.")
            return

        print("\nAktualny stan grafu:")
        print("Przystanki:", list(self.graph.keys()))
        print("Połączenia:")
        for from_node, edges in self.graph.items():
            for to_node, weight in edges.items():
                print(f"  {from_node} -> {to_node} (waga: {weight})")
