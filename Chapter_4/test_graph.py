from graph import Graph, city_graph
from edge import Edge
import sys

sys.path.insert(0, "..")
from Chapter_2.generic_search import bfs, Node, node_to_path


def test_vertex_count():
    graph = city_graph()
    assert graph.vertex_count == 15


def test_add_vertex():
    graph = city_graph()
    vertex_to_add = "Tampa"
    index = graph.add_vertex(vertex_to_add)
    assert graph.vertex_at(index) == vertex_to_add


def test_add_edge():
    graph = city_graph()
    vertex_to_add = "Tampa"
    index = graph.add_vertex(vertex_to_add)
    edge = Edge(index, 1)
    graph.add_edge(edge)
    assert graph._edges[-1][0] == edge


def test_add_edge_by_indices():
    graph = city_graph()
    index = graph.add_vertex("Tampa")
    graph.add_edge_by_indices(1, index)
    edge = Edge(index, 1)
    assert graph._edges[-1][0] == edge


def test_add_edge_by_vertices():
    graph = city_graph()
    u = graph.add_vertex("New Jersey")
    v = graph.add_vertex("Wilmington")
    edge = Edge(u, v)
    graph.add_edge_by_vertices("New Jersey", "Wilmington")
    assert graph._edges[-2][0] == Edge(u, v)
    assert graph._edges[-1][0] == Edge(v, u)


def test_vertex_at():
    graph = city_graph()
    expected = graph._vertices[0]
    actual = graph.vertex_at(0)
    assert expected == actual


def test_index_of():
    graph = city_graph()
    assert graph.index_of("Seattle") == 0


def test_neighbors_for_index():
    graph = city_graph()
    result = graph.neighbors_for_index(0)
    assert result == ["Chicago", "San Francisco"]


def test_neighbors_for_vertex():
    graph = city_graph()
    result = graph.neighbors_for_vertex("Seattle")
    assert result == ["Chicago", "San Francisco"]


def test_edges_for_index():
    graph = city_graph()
    result = graph.edges_for_index(0)
    assert result == [Edge(u=0, v=5), Edge(u=0, v=1)]


def test_edges_for_vertex():
    graph = city_graph()
    result = graph.edges_for_vertex("Seattle")
    assert result == [Edge(u=0, v=5), Edge(u=0, v=1)]


def test_str(capsys):
    expected = "Seattle -> ['Chicago', 'San Francisco']"
    graph = city_graph()
    print(graph)
    captured = capsys.readouterr()
    result = captured.out
    assert expected in result


def test_bfs_solution(capsys):
    c_graph = city_graph()
    bfs_result = bfs("Boston", lambda x: x == "Miami", c_graph.neighbors_for_vertex)

    path = node_to_path(bfs_result)
    print("Path from Boston to Miami:")
    print(path)
    captured = capsys.readouterr()
    result = captured.out
    expected = "['Boston', 'Detroit', 'Washington', 'Miami']"
    assert expected in result
