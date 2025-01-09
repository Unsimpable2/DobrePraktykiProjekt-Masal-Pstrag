import pytest
from graph.bus_graph import BusNetworkGraph

def test_remove_node():
    graph = BusNetworkGraph()
    graph.add_node("A")
    graph.remove_node("A")
    assert "A" not in graph.graph
    assert len(graph.graph) == 0
