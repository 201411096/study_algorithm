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

graph2 = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'G', 'H', 'I'],
    'D' : ['B', 'E', 'F'],
    'E' : ['D'],
    'F' : ['D'],
    'G' : ['C'],
    'H' : ['C'],
    'I' : ['C', 'J'],
    'J' : ['I']
}

def dfs(graph, start_node):
    visited = list()
    need_visited = list()
    
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    
    return visited

def dfs_recursive(graph, start_node, visited=[]):
    visited.append(start_node)
    
    for node in graph[start_node]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    
    return visited

print(dfs(graph, 'A'))                      # ['A', 'B', 'H', 'M', 'J', 'K', 'L', 'I', 'C', 'D', 'G', 'E', 'F']
print(dfs(graph2, 'A'))                     # ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']
print(dfs_recursive(graph, 'A', []))        # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
print(dfs_recursive(graph2, 'A', []))       # ['A', 'B', 'D', 'E', 'F', 'C', 'G', 'H', 'I', 'J']