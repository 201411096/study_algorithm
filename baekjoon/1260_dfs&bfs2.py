# n : 노드의 개수
# m : 간선의 개수

from collections import deque, defaultdict

n, m, start_node = map(int, input().split())

edges = []
graph = defaultdict(list)

for i in range(m):
    edges.append(list(map(int, input().split())))

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

def dfs(graph, start_node):
    visited = []
    need_visted = deque()

    need_visted.append(start_node)
    
    while need_visted:
        node = need_visted.pop()

        if node not in visited:
            visited.append(node)
            # need_visted.extend(sorted(graph[node]))
            need_visted.extend(sorted(graph[node], reverse=True))

    return visited

def bfs(graph, start_node):
    visited = []
    need_visted = deque()

    need_visted.append(start_node)

    while need_visted:
        node = need_visted.popleft()

        if node not in visited:
            visited.append(node)
            need_visted.extend(sorted(graph[node]))

    return visited

def printArray(array):
    for el in array:
        print(el, end=' ')

printArray(dfs(graph, start_node))
print()
printArray(bfs(graph, start_node))
