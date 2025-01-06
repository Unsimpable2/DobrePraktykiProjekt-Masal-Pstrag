import time
import random
from graph import BusNetworkGraph, dijkstra_alg, load_from_json

def generate_test_graph(num_nodes, num_edges):
    graph = BusNetworkGraph()
    nodes = [f"Stop_{i}" for i in range(1, num_nodes + 1)]
    for node in nodes:
        graph.add_node(node)

    for _ in range(num_edges):
        from_node = random.choice(nodes)
        to_node = random.choice(nodes)
        if from_node != to_node:
            weight = random.uniform(1, 20)
            graph.add_edge(from_node, to_node, round(weight, 2))
    
    return graph, nodes


def benchmark_operation(name, func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time


def run_benchmarks():
    test_cases = [
        {"num_nodes": 10, "num_edges": 20, "label": "Mały graf"},
        {"num_nodes": 100, "num_edges": 200, "label": "Średni graf"},
        {"num_nodes": 1000, "num_edges": 5000, "label": "Duży graf"}
    ]

    results = []

    for case in test_cases:
        print(f"\n=== Benchmark dla {case['label']} ===")

        graph, nodes = generate_test_graph(case["num_nodes"], case["num_edges"])

        if case["num_nodes"] > 0 and case["num_edges"] > 0:
            _, add_time = benchmark_operation("Dodawanie węzłów", generate_test_graph, case["num_nodes"], 0)

            _, edge_time = benchmark_operation("Dodawanie krawędzi", generate_test_graph, case["num_nodes"], case["num_edges"])

            start_node = random.choice(nodes)
            end_node = random.choice(nodes)
            _, path_time = benchmark_operation("Najkrótsza ścieżka (Dijkstra)", dijkstra_alg, graph.graph, start_node, end_node)

            results.append({
                "label": case["label"],
                "add_time": add_time,
                "edge_time": edge_time,
                "path_time": path_time
            })

            print(f"Dodawanie węzłów: {add_time:.4f} s")
            print(f"Dodawanie krawędzi: {edge_time:.4f} s")
            print(f"Najkrótsza ścieżka: {path_time:.4f} s")
        else:
            print(f"Nie można przeprowadzić benchmarku dla {case['label']}, ponieważ graf jest pusty.")

    print("\n=== Raport Benchmarków ===")
    for result in results:
        print(f"\n{result['label']}:")
        print(f"  Dodawanie węzłów: {result['add_time']:.4f} s")
        print(f"  Dodawanie krawędzi: {result['edge_time']:.4f} s")
        print(f"  Najkrótsza ścieżka: {result['path_time']:.4f} s")
