import networkx as nx

# Понимаю, что не проверяю условие неоднозначности сортировки, извините
def nx_toposort(graph: dict[str, list[str]]) -> list[str]:
    g = nx.DiGraph()
    g.add_nodes_from(graph.keys())
    g.add_edges_from(
        (parent, child)
        for parent, children in graph.items()
        for child in children
    )
    return list(nx.topological_sort(g))


def tests(kahn_sort):
    # no cycle
    graph1 = {
        'A': ['B'],
        'B': ['C'],
        'C': []
    }
    nx1 = nx_toposort(graph1)
    res = kahn_sort(graph1)
    assert res[1] == 'doesnt have cycles', f"with kahn_sort({graph1}) got {res}"
    assert res[0] == nx1, f"order differs from nx_toposort: {res[0]} vs {nx1}"

    graph2 = {
        'A': [],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    nx2 = nx_toposort(graph2)
    res = kahn_sort(graph2)
    assert res[1] == 'doesnt have cycles', f"with kahn_sort({graph2}) got {res}"
    assert res[0] == nx2, f"order differs from nx_toposort: {res[0]} vs {nx2}"

    graph3 = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['C', 'D', 'E'],
        'C': ['D', 'E'],
        'D': ['E'],
        'E': []
    }
    nx3 = nx_toposort(graph3)
    res = kahn_sort(graph3)
    assert res[1] == 'doesnt have cycles', f"with kahn_sort({graph3}) got {res}"
    assert res[0] == nx3, f"order differs from nx_toposort: {res[0]} vs {nx3}"

    # with cycle
    graph4 = {
        'A': ['B'],
        'B': ['A']
    }
    res = kahn_sort(graph4)
    assert res[1] == 'have cycles', f"with kahn_sort({graph4}) got {res}"

    graph5 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    res = kahn_sort(graph5)
    assert res[1] == 'have cycles', f"with kahn_sort({graph5}) got {res}"

    graph6 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['B'],
        'D': ['A'],
        'E': []
    }
    res = kahn_sort(graph6)
    assert res[1] == 'have cycles', f"with kahn_sort({graph6}) got {res}"
