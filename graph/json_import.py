import json
from feature_flags import FeatureFlags

def load_from_json(graph, file_path):
    """
    Wczytuje dane grafu z pliku JSON i dodaje je do istniejącego grafu.

    Funkcja obsługuje Feature Flags, które pozwalają dynamicznie włączać lub wyłączać
    wczytywanie węzłów, krawędzi oraz dodatkowych właściwości grafu.

    Args:
        graph (BusNetworkGraph): Obiekt grafu, do którego mają być wczytane dane.
        file_path (str): Ścieżka do pliku JSON zawierającego dane grafu.

    Returns:
        None

    Wyświetla komunikaty o stanie operacji oraz ostrzeżenia w przypadku wyłączenia
    poszczególnych funkcjonalności przez Feature Flags.
    """
    feature_flags = FeatureFlags()

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        if feature_flags.is_enabled("enable_load_nodes"):
            nodes = data.get("nodes")
            if isinstance(nodes, list):
                for node in nodes:
                    if isinstance(node, dict) and "name" in node:
                        graph.add_node(node["name"])
                    elif isinstance(node, str):
                        graph.add_node(node)
            print("Węzły zostały wczytane.")
        else:
            print("Wczytywanie węzłów jest wyłączone.")

        if feature_flags.is_enabled("enable_load_edges"):
            edges = data.get("edges")
            if isinstance(edges, list):
                for edge in edges:
                    from_node = edge.get("from")
                    to_node = edge.get("to")
                    weight = edge.get("weight", 1)
                    if from_node and to_node:
                        graph.add_edge(from_node, to_node, weight)
            print("Krawędzie zostały wczytane.")
        else:
            print("Wczytywanie krawędzi jest wyłączone.")

        if feature_flags.is_enabled("enable_load_properties"):
            additional_properties = data.get("properties", {})
            if additional_properties:
                print("Wykryto dodatkowe właściwości grafu:", additional_properties)
        else:
            print("Wczytywanie dodatkowych właściwości jest wyłączone.")

        print("Dane zostały pomyślnie wczytane z pliku JSON.")
    except FileNotFoundError:
        print(f"Plik '{file_path}' nie został znaleziony.")
    except json.JSONDecodeError:
        print("Błąd podczas odczytu pliku JSON. Upewnij się, że format jest poprawny.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")