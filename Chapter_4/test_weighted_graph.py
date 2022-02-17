from weighted_graph import WeightedGraph
from min_spanning_tree import mst
from weighted_edge import WeightedEdge


city_graph2 = WeightedGraph(
    [
        "Seattle",
        "San Francisco",
        "Los Angeles",
        "Riverside",
        "Phoenix",
        "Chicago",
        "Boston",
        "New York",
        "Atlanta",
        "Miami",
        "Dallas",
        "Houston",
        "Detroit",
        "Philadelphia",
        "Washington",
    ]
)
city_graph2.add_edge_by_vertices("Seattle", "Chicago", 1737)
city_graph2.add_edge_by_vertices("Seattle", "San Francisco", 678)
city_graph2.add_edge_by_vertices("San Francisco", "Riverside", 386)
city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
city_graph2.add_edge_by_vertices("Los Angeles", "Riverside", 50)
city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
city_graph2.add_edge_by_vertices("Riverside", "Phoenix", 307)
city_graph2.add_edge_by_vertices("Riverside", "Chicago", 1704)
city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887)
city_graph2.add_edge_by_vertices("Phoenix", "Houston", 1015)
city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805)
city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721)
city_graph2.add_edge_by_vertices("Dallas", "Houston", 225)
city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702)
city_graph2.add_edge_by_vertices("Houston", "Miami", 968)
city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588)
city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543)
city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604)
city_graph2.add_edge_by_vertices("Miami", "Washington", 923)
city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238)
city_graph2.add_edge_by_vertices("Detroit", "Boston", 613)
city_graph2.add_edge_by_vertices("Detroit", "Washington", 396)
city_graph2.add_edge_by_vertices("Detroit", "New York", 482)
city_graph2.add_edge_by_vertices("Boston", "New York", 190)
city_graph2.add_edge_by_vertices("New York", "Philadelphia", 81)
city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)

# print(city_graph2)

neighborhood_graph = WeightedGraph(["home", "Irish Pub", "Blind Tiger", "Siam Thai"])
neighborhood_graph.add_edge_by_vertices("home", "Irish Pub", 3)
neighborhood_graph.add_edge_by_vertices("home", "Blind Tiger", 4)
neighborhood_graph.add_edge_by_vertices("Irish Pub", "Blind Tiger", 1)
neighborhood_graph.add_edge_by_vertices("home", "Siam Thai", 7)
neighborhood_graph.add_edge_by_vertices("home", "Irish Pub", 3)


def test_mst_start_gt_vertex_none():
    wg = city_graph2
    result = mst(wg, 15)
    assert result is None


def test_mst_simple():
    wg = neighborhood_graph
    result = mst(wg, 0)
    assert result == [
        WeightedEdge(u=0, v=1, weight=3),
        WeightedEdge(u=1, v=2, weight=1),
        WeightedEdge(u=0, v=3, weight=7),
    ]
