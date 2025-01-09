import pytest
from graph.bus_graph import BusNetworkGraph

def test_remove_edge():
    graph = BusNetworkGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B", 10)
    graph.remove_edge("A", "B")
    assert "B" not in graph.graph["A"]
