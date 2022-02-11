from edge import Edge


def test_edge():
    e = Edge(1, 2)

    assert str(e) == "1 -> 2"
    assert str(e.reversed()) == "2 -> 1"
