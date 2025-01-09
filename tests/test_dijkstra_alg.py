import pytest
from graph.bus_graph import BusNetworkGraph
from graph.dijkstra_alg import dijkstra_alg

def test_dijkstra_alg():
    """
    Testuje algorytm Dijkstry na prostym grafie.

    Scenariusz:
    - Tworzenie grafu z trzema węzłami: "A", "B", "C".
    - Dodanie krawędzi z wagami:
        - "A" -> "B" (waga: 1)
        - "B" -> "C" (waga: 2)
    - Znalezienie najkrótszej ścieżki z "A" do "C".
    - Sprawdzenie poprawności ścieżki i jej całkowitego kosztu.

    Asserts:
        - Najkrótsza ścieżka to ["A", "B", "C"].
        - Całkowity koszt ścieżki wynosi 3.
    """
    graph = BusNetworkGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", 2)
    path, cost = dijkstra_alg(graph.graph, "A", "C")
    assert path == ["A", "B", "C"]
    assert cost == 3
