import pytest
from graph.bus_graph import BusNetworkGraph

def test_remove_edge():
    """
    Testuje usuwanie krawędzi z grafu.

    Scenariusz:
    - Tworzenie grafu z dwoma węzłami: "A" i "B".
    - Dodanie krawędzi między węzłami "A" i "B" z wagą 10.
    - Usunięcie krawędzi między "A" i "B".
    - Sprawdzenie, czy węzeł "B" nie jest już sąsiadem węzła "A".

    Asserts:
        - Węzeł "B" nie znajduje się w liście sąsiadów węzła "A".
    """
    graph = BusNetworkGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B", 10)
    graph.remove_edge("A", "B")
    assert "B" not in graph.graph["A"]
