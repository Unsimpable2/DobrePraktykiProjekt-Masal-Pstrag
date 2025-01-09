import pytest
from graph.bus_graph import BusNetworkGraph

def test_add_edge():
    """
    Testuje dodawanie krawędzi między węzłami w grafie.

    Scenariusz:
    - Dodanie dwóch węzłów ("A" i "B").
    - Dodanie krawędzi o wadze 10 między węzłami "A" i "B".
    - Sprawdzenie, czy węzeł "B" został poprawnie dodany jako sąsiad "A".
    - Sprawdzenie, czy waga krawędzi jest poprawnie ustawiona.

    Asserts:
        - "B" znajduje się w grafie jako sąsiad węzła "A".
        - Waga krawędzi między "A" i "B" wynosi 10.
    """
    graph = BusNetworkGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B", 10)
    assert "B" in graph.graph["A"]
    assert graph.graph["A"]["B"] == 10
