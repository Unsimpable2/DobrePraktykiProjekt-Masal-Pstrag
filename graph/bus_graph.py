class BusNetworkGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}
            print(f"Węzeł '{node}' został dodany.")
        else:
            print(f"Węzeł '{node}' już istnieje.")

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for edges in self.graph.values():
                edges.pop(node, None)
            print(f"Węzeł '{node}' został usunięty.")
        else:
            print(f"Węzeł '{node}' nie istnieje.")

    def add_edge(self, from_node, to_node, weight):
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
        if from_node in self.graph and to_node in self.graph[from_node]:
            del self.graph[from_node][to_node]
            print(f"Krawędź z '{from_node}' do '{to_node}' została usunięta.")
        else:
            print(f"Krawędź z '{from_node}' do '{to_node}' nie istnieje.")

    def display_graph(self):
        print("\nAktualny stan grafu:")
        print("Przystanki:", list(self.graph.keys()))
        print("Połączenia:")
        for from_node, edges in self.graph.items():
            for to_node, weight in edges.items():
                print(f"  {from_node} -> {to_node} (waga: {weight})")
