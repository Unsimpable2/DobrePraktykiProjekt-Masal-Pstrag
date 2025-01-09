import pytest
from graph.bus_graph import BusNetworkGraph
from graph.json_import import load_from_json

def test_load_from_json(tmp_path):
    """
    Testuje wczytywanie grafu z pliku JSON.

    Scenariusz:
    - Tworzenie pliku JSON zawierającego węzły "A" i "B" oraz krawędź między nimi z wagą 1.
    - Wczytanie danych z pliku JSON do grafu.
    - Sprawdzenie, czy węzeł "A" został poprawnie dodany.
    - Sprawdzenie, czy węzeł "B" jest sąsiadem "A".
    - Sprawdzenie, czy waga krawędzi między "A" a "B" wynosi 1.

    Asserts:
        - Węzeł "A" znajduje się w grafie.
        - Węzeł "B" jest sąsiadem "A".
        - Waga krawędzi między "A" a "B" wynosi 1.
    """
    graph = BusNetworkGraph()
    json_file = tmp_path / "test_graph.json"
    json_data = {
        "nodes": ["A", "B"],
        "edges": [{"from": "A", "to": "B", "weight": 1}]
    }
    json_file.write_text(str(json_data).replace("'", '"'))
    load_from_json(graph, json_file)
    assert "A" in graph.graph
    assert "B" in graph.graph["A"]
    assert graph.graph["A"]["B"] == 1
