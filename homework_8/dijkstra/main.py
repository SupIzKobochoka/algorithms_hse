from utils import makeheap

def dijkstra(target: str, starting_vertex: str, graph: dict[str, list[tuple[int|float, str]]]) -> tuple[float|int, list[str]]:
    if target == starting_vertex:
        return 0, [target]

    visited = set([starting_vertex])
    # connections = {child: (path_cost, parent)} 
    connections = {connected_vertex: (value, starting_vertex) for value, connected_vertex in graph[starting_vertex]}
    available_paths = makeheap(graph[starting_vertex])
    while not available_paths.is_empty():
        cheapest_path_cost, cheapest_vertex = available_paths.extract_min(return_with_key=True)
        if cheapest_vertex != target:
            if cheapest_vertex not in visited:
                visited.add(cheapest_vertex)
                for path_cost, connected_vertex in graph[cheapest_vertex]:
                    if connected_vertex not in visited:
                        # Для случая, когда 2 пути к непосещённой вершине
                        old_candidat = connections.get(connected_vertex, (float('inf'), None))
                        new_candidat = path_cost + cheapest_path_cost, cheapest_vertex
                        if new_candidat[0] < old_candidat[0]:
                            connections[connected_vertex] = new_candidat
                            available_paths.insert(path_cost + cheapest_path_cost, connected_vertex)
        else:
            full_path = [cheapest_vertex]
            child = cheapest_vertex 
            while child in connections:
                child = connections[child][1]
                full_path.append(child)
            return cheapest_path_cost, full_path[::-1]
    raise KeyError('Путь не найден')


if __name__ == '__main__': 
    from test import tests

    tests(dijkstra)