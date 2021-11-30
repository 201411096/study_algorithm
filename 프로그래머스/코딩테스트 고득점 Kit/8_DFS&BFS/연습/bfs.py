graph = {
    'A' : ['B'],
    'B' : ['A', 'C', 'H'],
    'C' : ['B', 'D'],
    'D' : ['C', 'E', 'G'],
    'E' : ['D', 'F'],
    'F' : ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def bfs(graph, start_node):
    visited = list()
    need_visited = list()
    
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            
    return visited

print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'H', 'D', 'I', 'J', 'M', 'E', 'G', 'K', 'F', 'L']
