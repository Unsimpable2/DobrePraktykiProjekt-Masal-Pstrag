import pytest
from graph.bus_graph import BusNetworkGraph

def test_remove_node():
    """
    Testuje usuwanie węzła z grafu.

    Scenariusz:
    - Dodanie jednego węzła "A" do grafu.
    - Usunięcie węzła "A".
    - Sprawdzenie, czy węzeł "A" został poprawnie usunięty.
    - Sprawdzenie, czy graf jest pusty po usunięciu jedynego węzła.

    Asserts:
        - Węzeł "A" nie znajduje się w grafie.
        - Liczba węzłów w grafie wynosi 0.
    """
    graph = BusNetworkGraph()
    graph.add_node("A")
    graph.remove_node("A")
    assert "A" not in graph.graph
    assert len(graph.graph) == 0
