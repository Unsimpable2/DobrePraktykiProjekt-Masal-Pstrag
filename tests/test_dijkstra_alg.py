import pytest
from graph.bus_graph import BusNetworkGraph
from graph.dijkstra_alg import dijkstra_alg

def test_dijkstra_alg():
    graph = BusNetworkGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", 2)
    path, cost = dijkstra_alg(graph.graph, "A", "C")
    assert path == ["A", "B", "C"]
    assert cost == 3
