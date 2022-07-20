"""

크루스칼 알고리즘(Kruskal's algorithm)

목적 : 그래프 내의 모든 정점들을 가장 적은 비용으로 연결하기 위해 사용

내용
1. 모든 정점을 독립적인 집합으로 만든다.
2. 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
3. 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.(사이클이 생기지 않도록)
    - unionFind 알고리즘 사용



"""

def makeSet(nodeList):
    parentDict = {}
    rankDict = {}

    for node in nodeList:
        parentDict[node] = node
        rankDict[node] = 0

    return parentDict, rankDict

def findRoot(parentDict, node):
    if parentDict[node] != node:
        # path compression
        parentDict[node] = findRoot(parentDict, parentDict[node])

    return parentDict[node]

def unionSet(parentDict, rankDict, nodeA, nodeB):
    rootA = findRoot(parentDict, nodeA)
    rootB = findRoot(parentDict, nodeB)

    # union by rank
    if rankDict[rootA] > rankDict[rootB]:
        parentDict[rootB] = rootA
    elif rankDict[rootA] == rankDict[rootB]:
        parentDict[rootB] = rootA
        rankDict[rootA] += 1
    else:
        parentDict[rootA] = rootB

def compareRoot(parentDict, nodeA, nodeB):
    rootA = findRoot(parentDict, nodeA)
    rootB = findRoot(parentDict, nodeB)

    if rootA == rootB:
        return True
    else:
        return False

# return MST's edges
def kruskal(graph):
    mstEdgeList = []

    nodeList = graph['vertices']
    edgeList = graph['edges']

    parentDict, rankDict = makeSet(nodeList)

    edgeList = sorted(edgeList, key=lambda x : x[0])

    for edge in edgeList:
        # cycle check
        if compareRoot(parentDict, edge[1], edge[2]) == False:
            mstEdgeList.append(edge)
            unionSet(parentDict, rankDict, edge[1], edge[2])
    
    return mstEdgeList

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

if __name__ == "__main__":
    mstEdgeList = kruskal(graph)
    mstEdgeListCnt = len(mstEdgeList)
    print('mstEdgeList : ', mstEdgeList)
    print('mstEdgeListCnt : ', mstEdgeListCnt)