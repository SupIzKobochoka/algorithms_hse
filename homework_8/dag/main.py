from utils import Queue

def DFS(graph: dict[str, list[str]], current_vertex: str, global_visited_vertexes: set = None, local_visited_vertexes: set = None) -> tuple[list[str], bool, bool]:
    '''
    Спускаемся по детям current_vertex добавляяя значения в local_visited_vertexes, при подъёме вверх добавляем значения в global_visited_vertexes
    Проверяем в каждой вершине отсутствует ли она в global_visited_vertexes, если да, то:
        Проверяем видели ли её в local_visited_vertexes, если да:
            Поднимаемся вверх по графу пока не найдём эту же вершину, запоминая путь
        Иначе:
            Добавляем вершину в local_visited_vertexes
            Спускаемся вниз по детям текущей вершины и т.д.
    '''

    if global_visited_vertexes is None:
        global_visited_vertexes = set()

    if local_visited_vertexes is None:
        local_visited_vertexes = set([current_vertex])

    for vertex in graph[current_vertex]:
        if vertex not in global_visited_vertexes:
            if vertex in local_visited_vertexes:
                # vertexes, is_cycled, did_find_all_cycle_vertexes
                return [vertex], True, False
            
            local_visited_vertexes.add(vertex)
            vertexes, is_cycled, did_find_all_cycle_vertexes = DFS(graph=graph, 
                                                               current_vertex=vertex,
                                                                global_visited_vertexes=global_visited_vertexes,
                                                                local_visited_vertexes=local_visited_vertexes)
            if is_cycled:
                if did_find_all_cycle_vertexes or vertex == vertexes[0]:
                    return vertexes, is_cycled, True
                
                vertexes.append(vertex)
                return vertexes, is_cycled, did_find_all_cycle_vertexes
            
    global_visited_vertexes.add(current_vertex)
    return [], False, False


def check_cycles(graph) -> list|None:
    global_visited = set()
    for vertex in graph:
        if vertex not in global_visited:
            cycle, has_cycle, _ = DFS(graph, current_vertex=vertex, global_visited_vertexes=global_visited)
            if has_cycle:
                return cycle[::-1]


def kahn_sort(graph: dict[str, list[str]]) -> tuple[list[str], str]:
    cycles = check_cycles(graph)
    if cycles is not None:
        return cycles, 'have cycles'
    
    indegrees = dict.fromkeys(graph, 0)
    for parent in graph:
        for child in graph[parent]:
            indegrees[child] += 1

    queue = Queue()
    
    for vertex in indegrees:
        if indegrees[vertex] == 0:
            queue.push(vertex)
    
    sorted_list = []
    while not queue.is_empty():
        vertex = queue.pop()
        sorted_list.append(vertex)
        for child in graph[vertex]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                queue.push(child)
    return sorted_list, 'doesnt have cycles'


if __name__ == '__main__': 
    from test import tests

    tests(kahn_sort)