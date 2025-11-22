def DFS(graph: dict[str, list[str]], current_vertex: str, visited_vertexes: set = None) -> set[str]:
    if visited_vertexes is None:
        visited_vertexes = set()
    visited_vertexes.add(current_vertex)
    for vertex in graph[current_vertex]:
        if vertex not in visited_vertexes:
            DFS(graph, vertex, visited_vertexes)
    return visited_vertexes

def get_graph_components(graph: dict[str, list[str]]) -> list[set[str]]:
    visited = set()
    components = []
    for vertex in graph:
        if vertex not in visited:
            component = DFS(graph, vertex)
            visited.update(component)
            components.append(component)
    return components

if __name__ == '__main__':
    from test import tests

    tests(get_graph_components)



