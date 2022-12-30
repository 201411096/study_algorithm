import heapq

def dijkstra(graph, start_node):
    distanceDict = {node : float('inf') for node in graph}
    distanceDict[start_node] = 0

    heap = []
    heapq.heappush(heap, [distanceDict[start_node], start_node])

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if distanceDict[current_node] < current_distance:
            continue

        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distanceDict[adjacent_node]:
                distanceDict[adjacent_node] = distance
                heapq.heappush(heap, [distance, adjacent_node])

    return distanceDict

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

result = dijkstra(mygraph, 'A')

print(result)   # {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}