from graph import Graph
from weighted_edge import WeightedEdge


class WeightedGraph(Graph):
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [[] for _ in vertices]

    def add_edge_by_indices(self, u: int, v: int, weight):
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge)  # call superclass version

    def add_edge_by_vertices(self, first, second, weight):
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index: int):
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    def __str__(self):  # sourcery skip: use-join
        desc = ""
        for i in range(self.vertex_count):
            desc += (
                f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
            )
        return desc
