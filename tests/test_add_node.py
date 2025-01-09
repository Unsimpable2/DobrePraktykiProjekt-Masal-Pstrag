import pytest
from graph.bus_graph import BusNetworkGraph

def test_add_node():
    """
    Testuje dodawanie węzła do grafu.

    Scenariusz:
    - Dodanie jednego węzła "A" do pustego grafu.
    - Sprawdzenie, czy węzeł "A" został poprawnie dodany.
    - Sprawdzenie, czy liczba węzłów w grafie wynosi 1.

    Asserts:
        - "A" znajduje się w grafie.
        - Liczba węzłów w grafie wynosi 1.
    """
    graph = BusNetworkGraph()
    graph.add_node("A")
    assert "A" in graph.graph
    assert len(graph.graph) == 1
