import pytest
from graph.bus_graph import BusNetworkGraph

def test_add_node():
    graph = BusNetworkGraph()
    graph.add_node("A")
    assert "A" in graph.graph
    assert len(graph.graph) == 1
