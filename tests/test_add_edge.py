import pytest
from graph.bus_graph import BusNetworkGraph

def test_add_edge():
    graph = BusNetworkGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B", 10)
    assert "B" in graph.graph["A"]
    assert graph.graph["A"]["B"] == 10
