def tests(dijkstra):
    
    graph_cycle = {
        'A': [(2, 'B')],
        'B': [(2, 'A')]
    }
    res = dijkstra('A', 'A', graph_cycle)
    assert res == (0, ['A']), f"with dijkstra(target='A', starting_vertex='A', graph={graph_cycle}) got {res}"

    graph_eazy = {
        'A': [(3, 'B')],
        'B': [(3, 'A')]
    }
    res = dijkstra('B', 'A', graph_eazy)
    assert res[0] == 3 and res[1] == ['A', 'B'], f"with dijkstra(target='B', starting_vertex='A', graph={graph_eazy}) got {res}"

    graph_eazy2 = {
        'A': [(1, 'B')],
        'B': [(1, 'A'), (2, 'C')],
        'C': [(2, 'B')]
    }
    res = dijkstra('C', 'A', graph_eazy2)
    assert res[0] == 3 and res[1] == ['A', 'B', 'C'], f"with dijkstra(target='C', starting_vertex='A', graph={graph_eazy2}) got {res}"

    graph_imposible = {
        'A': [(1, 'B')],
        'B': [(1, 'A')],
        'C': [(1, 'D')],
        'D': [(1, 'C')]
    }
    try:
        dijkstra('D', 'A', graph_imposible)
        assert False, f"with dijkstra(target='D', starting_vertex='A', graph={graph_imposible}) expected KeyError, got no exception"
    except KeyError:
        ...
