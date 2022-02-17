from weighted_edge import WeightedEdge


def test_weighted_edge():
    edge = WeightedEdge(4, 1, 22)
    reverse_edge = WeightedEdge(1, 4, 22)
    assert edge.reversed() == reverse_edge
    other_edge = WeightedEdge(4, 1, 100)
    assert edge < other_edge
