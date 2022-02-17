from dijkstra import (
    DijkstraNode,
    dijkstra,
    distance_array_to_vertex_dict,
    path_dict_to_path,
)
from test_weighted_graph import neighborhood_graph
from weighted_edge import WeightedEdge


def test_dijkstranode():
    dn = DijkstraNode(1, 3)
    dn2 = DijkstraNode(1, 4)
    assert dn < dn2


def test_dijkstra():
    wg = neighborhood_graph
    expected = (
        [3, 0, 1, 10],
        {
            0: WeightedEdge(u=1, v=0, weight=3),
            2: WeightedEdge(u=1, v=2, weight=1),
            3: WeightedEdge(u=0, v=3, weight=7),
        },
    )
    result = dijkstra(wg, "Irish Pub")
    assert result == expected


def test_distance_array_to_vertex_dict():
    wg = neighborhood_graph

    expected = {"home": 3, "Irish Pub": 4, "Blind Tiger": 1}
    result = distance_array_to_vertex_dict(wg, [3, 4, 1])
    assert result == expected


def test_path_dict_to_path():
    path_dict = {
        0: WeightedEdge(u=1, v=0, weight=3),
        2: WeightedEdge(u=1, v=2, weight=1),
        3: WeightedEdge(u=0, v=3, weight=7),
    }
    start = 0
    end = 3
    result = path_dict_to_path(start, end, path_dict)
    assert result == [WeightedEdge(u=0, v=3, weight=7)]
