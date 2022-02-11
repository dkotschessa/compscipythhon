from typing import TypeVar, Generic, List, Optional
from edge import Edge
import sys

sys.path.insert(0, "..")
from Chapter_2.generic_search import bfs, Node, node_to_path


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [[] for _ in vertices]

    @property
    def vertex_count(self):
        return len(self._vertices)

    # add a vertex to the graph and return its index
    def add_vertex(self, vertex):
        self._vertices.append(vertex)
        self._edges.append([])  # empty list containiing edges
        return self.vertex_count - 1

    # undirected graph so edges go both ways
    def add_edge(self, edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # Add an edge using vertex indices
    def add_edge_by_indices(self, u, v):
        edge = Edge(u, v)
        self.add_edge(edge)

    # add edge ege by looking up vertex inidices
    def add_edge_by_vertices(self, first, second):
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # find vertex at a specific index
    def vertex_at(self, index):
        return self._vertices[index]

    def index_of(self, vertex):
        return self._vertices.index(vertex)

    # find the vertices that a vertex at some index is connected to
    def neighbors_for_index(self, index):
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # look up a vertice's index and find it's neigbors
    def neighbors_for_vertex(self, vertex):
        return self.neighbors_for_index(self.index_of(vertex))

    # return all edges associated with a vertex at some index
    def edges_for_index(self, index):
        return self._edges[index]

    # look up the nidex of a vertex and return its edges
    def edges_for_vertex(self, vertex):
        return self.edges_for_index(self.index_of(vertex))

    # make iit easy to pretty-print a graph
    def __str__(self):
        desc = "".join(
            f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
            for i in range(self.vertex_count)
        )
        return desc


def city_graph():
    city_graph = Graph(
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
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Boston", "New York")
    city_graph.add_edge_by_vertices("New York", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")
    return city_graph
