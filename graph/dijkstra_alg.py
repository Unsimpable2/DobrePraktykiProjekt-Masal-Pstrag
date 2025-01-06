import heapq
from collections import defaultdict

def dijkstra_alg(graph, start, end):
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
