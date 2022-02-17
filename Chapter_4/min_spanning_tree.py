from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from Chapter_2.generic_search import PriorityQueue


def total_weight(wp):
    return sum(e.weight for e in wp)


def mst(wg, start):
    if start > (wg.vertex_count - 1) or start < 0:
        return None

    result = []
    pq = PriorityQueue()
    visited = [False] * wg.vertex_count

    def visit(index):
        visited[index] = True
        for edge in wg.edges_for_index(index):
            # add all edge scoming from here to pq
            if not visited[edge.v]:
                pq.push(edge)

    visit(start)  # the first vertex is where everything begins

    while not pq.empty:  # keep goingi while there are edges to process
        edge = pq.pop()
        if visited[edge.v]:
            continue  # don't ever revisit
        # this is the current smallest, so add it to solution
        result.append(edge)
        visit(edge.v)

    return result


def print_weighted_path(wg, wp):
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} {edge.weight} > {wg.vertex_at(edge.v)}")
    print(f"Total Weight: {total_weight(wp)}")
