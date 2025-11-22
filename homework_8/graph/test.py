def tests(get_graph_components):
    graph_empty = {'a': [], 'b': [], 'c': []}
    res = get_graph_components(graph_empty)
    assert len(res) == 3 and all(set([vertex]) in res for vertex in graph_empty), f"with get_graph_components(dict('a': [], 'b': [], 'c': [])) got {res}"

    graph_one_components = {
        'a':['b', 'c'],
        'b': ['a', 'c'],
        'c': ['a', 'b']
        }
    res = get_graph_components(graph_one_components)
    assert len(res) == 1 and set(['a', 'b', 'c']) in res, f"with get_graph_components(dict('a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a', 'b'])) got {res}"

    graph_petlya = {
        'a':['a'],
        'b': ['b'],
        'c': ['c']
        }
    res = get_graph_components(graph_petlya)
    assert len(res) == 3 and all(set([vertex]) in res for vertex in graph_empty), f"with get_graph_components(dict('a': ['a'], 'b': ['b'], 'c': ['c'])) got {res}"

    two_components = {
        'a':['a', 'b'],
        'b': ['b', 'a'],
        'c': ['c', 'd'],
        'd': ['c']
        }
    res = get_graph_components(two_components)
    assert len(res) == 2 and set(['a', 'b']) in res and set(['c', 'd']) in res, f"with get_graph_components(dict('a': ['a', 'b'], 'b': ['b', 'a'], 'c': ['c', 'd'], 'd': ['c'])) got {res}"
