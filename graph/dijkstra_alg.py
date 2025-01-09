import heapq
from collections import defaultdict
from feature_flags import FeatureFlags

def dijkstra_alg(graph, start, end):
    """
    Znajduje najkrótszą trasę w grafie między dwoma węzłami za pomocą algorytmu Dijkstry.

    Args:
        graph (dict): Graf reprezentowany jako słownik sąsiedztwa.
        start (str): Nazwa węzła początkowego.
        end (str): Nazwa węzła końcowego.

    Returns:
        tuple: Najkrótsza ścieżka jako lista węzłów oraz jej koszt.
    """
    feature_flags = FeatureFlags()

    if feature_flags.is_enabled("traffic_optimization"):
        print("Włączono optymalizację ruchu drogowego.")
        graph = optimize_graph_based_on_traffic(graph)
    else:
        print("Optymalizacja ruchu drogowego jest wyłączona.")

    if start not in graph or end not in graph:
        print("Węzeł początkowy lub końcowy nie istnieje w grafie.")
        return None, float('inf')

    distances = defaultdict(lambda: float('inf'))
    previous_nodes = {}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path, current = [], end
    while current in previous_nodes:
        path.insert(0, current)
        current = previous_nodes[current]
    if distances[end] < float('inf'):
        path.insert(0, start)

    return path, distances[end]

def optimize_graph_based_on_traffic(graph):
    """
    Optymalizuje wagi krawędzi w grafie na podstawie współczynnika ruchu drogowego.

    Args:
        graph (dict): Graf reprezentowany jako słownik sąsiedztwa.

    Returns:
        dict: Zoptymalizowany graf z uwzględnieniem ruchu drogowego.
    """
    optimized_graph = {}
    for from_node, edges in graph.items():
        optimized_graph[from_node] = {}
        for to_node, weight in edges.items():
            traffic_factor = 1.5
            optimized_weight = weight * traffic_factor
            optimized_graph[from_node][to_node] = round(optimized_weight, 2)
    return optimized_graph
