myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

# 정점 집합과 연결되어 있는 간선들 중 최소 비용 간선을 찾아내는 알고리즘

from collections import defaultdict
import heapq

def prim(start_node, edges):
    mst = list()
    adjacent_edgeList = defaultdict(list)

    # dictionary 구성
    # node : (weight, start, end)
    for weight, n1, n2 in edges:
        adjacent_edgeList[n1].append((weight, n1, n2))
        adjacent_edgeList[n2].append((weight, n2, n1))

    connected_nodeList = set(start_node)
    waiting_edgeList = adjacent_edgeList[start_node]
    heapq.heapify(waiting_edgeList)

    while waiting_edgeList:
        weight, n1, n2 = heapq.heappop(waiting_edgeList)

        # end_node not in connected_nodeList
        if n2 not in connected_nodeList:
            connected_nodeList.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edgeList[n2]:
                # end_node not in connected_nodeList
                # push to waiting_edgeList
                if edge[2] not in connected_nodeList:
                    heapq.heappush(waiting_edgeList, edge)

    return mst

print(prim ('A', myedges))