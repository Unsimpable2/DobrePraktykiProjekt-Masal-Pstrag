import json

def load_from_json(graph, file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        nodes = data.get("nodes")
        if isinstance(nodes, list):
            for node in nodes:
                if isinstance(node, dict) and "name" in node:
                    graph.add_node(node["name"])
                elif isinstance(node, str):
                    graph.add_node(node)

        edges = data.get("edges")
        if isinstance(edges, list):
            for edge in edges:
                from_node = edge.get("from")
                to_node = edge.get("to")
                weight = edge.get("weight", 1)
                if from_node and to_node:
                    graph.add_edge(from_node, to_node, weight)

        additional_properties = data.get("properties", {})
        if additional_properties:
            print("Wykryto dodatkowe właściwości grafu:", additional_properties)

        print("Dane zostały pomyślnie wczytane z pliku JSON.")
    except FileNotFoundError:
        print(f"Plik '{file_path}' nie został znaleziony.")
    except json.JSONDecodeError:
        print("Błąd podczas odczytu pliku JSON. Upewnij się, że format jest poprawny.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
