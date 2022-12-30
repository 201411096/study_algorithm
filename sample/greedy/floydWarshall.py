INF = float("inf")

# 기본 점화식
# D_ab = min(D_ab, (D_ak + D_kb))

# 편의를 위해 (노드개수+1)*(노드개수+1)로 표시해둠
# input_graph = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 4, 0, 6],
#     [0, 3, 0, 7, 0],
#     [0, 5, 0, 0, 4],
#     [0, 0, 0, 2, 0]
# ]

n = 4 # node 갯수
m = 7 # edge 갯수

edges = [
    [1, 2, 4],
    [1, 4, 6],
    [2, 1, 3],
    [2, 3, 7],
    [3, 1, 5],
    [3, 4, 4],
    [4, 3, 2]
]


# 2차원 리스트 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for a, b, c in edges:
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINITY', end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

"""
-------------
answer
-------------
0   4   8   6
3   0   7   9
5   9   0   4
7   11  2   0
-------------
"""