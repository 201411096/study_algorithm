# union-find    : 합집합 찾기
# disjoint-set  : 서로소 집합

# union 순서에 따라 tree가 linked list와 같은 형태가 되는 것을 방지하기 위함
# union by rank     : o
# path compression  : o

def makeSet(nodeList):
    parentDict = {}
    rankDict = {}

    for node in nodeList:
        parentDict[node] = node
        rankDict[node] = 0
    
    return parentDict, rankDict
    
def findRoot(parentDict, node):
    # print('node : ', node)
    # print('parentDict[node] : ', parentDict[node])
    if parentDict[node] != node :
        parentDict[node] = findRoot(parentDict, parentDict[node])   # path compression

    return parentDict[node]

def unionRoot(parentDict, rankDict, a, b):
    rootA = findRoot(parentDict, a)
    rootB = findRoot(parentDict, b)

    if rankDict[rootA] > rankDict[rootB]:                           # union by rank
        parentDict[rootB] = rootA
    elif rankDict[rootA] == rankDict[rootB]:
        parentDict[rootB] = rootA
        rankDict[rootA] += 1
    else:
        parentDict[rootA] = rootB

def compareRoot(parentDict, a, b):
    rootA = findRoot(parentDict, a)
    rootB = findRoot(parentDict, b)

    if rootA == rootB:
        return True
    else:
        return False

if __name__ == "__main__":
    nodeList = [1,2,3,4,5,6,7,8]

    parentDict, rankDict = makeSet(nodeList)

    unionRoot(parentDict, rankDict, 1, 2)           # [ [1, 2] ]
    print('parentDict : ', parentDict)              # parentDict :  {1: 1, 2: 1, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
    unionRoot(parentDict, rankDict, 2, 3)           # [ [1, 2, 3] ]
    print('parentDict : ', parentDict)              # parentDict :  {1: 1, 2: 1, 3: 1, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
    unionRoot(parentDict, rankDict, 4, 3)           # [ [1, 2, 3, 4] ]
    print('parentDict : ', parentDict)              # parentDict :  {1: 1, 2: 1, 3: 1, 4: 1, 5: 5, 6: 6, 7: 7, 8: 8}
    unionRoot(parentDict, rankDict, 5, 6)           # [ [1, 2, 3, 4], [5, 6] ]
    print('parentDict : ', parentDict)              # parentDict :  {1: 1, 2: 1, 3: 1, 4: 1, 5: 5, 6: 5, 7: 7, 8: 8}
    unionRoot(parentDict, rankDict, 7, 8)           # [ [1, 2, 3, 4], [5, 6], [7, 8] ]
    print('parentDict : ', parentDict)              # parentDict :  {1: 1, 2: 1, 3: 1, 4: 1, 5: 5, 6: 5, 7: 7, 8: 7}

    print('='*25)
    print('4,1 => same set? :', compareRoot(parentDict, 4, 1))    # True
    print('4,5 => same set? :', compareRoot(parentDict, 4, 5))    # False
    print('5,6 => same set? :', compareRoot(parentDict, 5, 6))    # True
    print('5,7 => same set? :', compareRoot(parentDict, 5, 7))    # False
    print('4,7 => same set? :', compareRoot(parentDict, 4, 7))    # False
    print('7,8 => same set? :', compareRoot(parentDict, 7, 8))    # True

    print('parentDict : ', parentDict)              # parentDict :  {1: 1, 2: 1, 3: 1, 4: 1, 5: 5, 6: 5, 7: 7, 8: 7}
    print('rankDict : ', rankDict)                  # rankDict :  {1: 1, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0}

    unionRoot(parentDict, rankDict, 5, 4)
    print('parentDict : ', parentDict)              # parentDict :  {1: 5, 2: 1, 3: 1, 4: 1, 5: 5, 6: 5, 7: 7, 8: 7}
    print('rankDict : ', rankDict)                  # rankDict :  {1: 1, 2: 0, 3: 0, 4: 0, 5: 2, 6: 0, 7: 1, 8: 0}
    unionRoot(parentDict, rankDict, 6, 7)
    print('parentDict : ', parentDict)              # parentDict :  {1: 5, 2: 1, 3: 1, 4: 1, 5: 5, 6: 5, 7: 5, 8: 7}
    print('rankDict : ', rankDict)                  # rankDict :  {1: 1, 2: 0, 3: 0, 4: 0, 5: 2, 6: 0, 7: 1, 8: 0}
    print('='*25)

    print('4,5 => same set? :', compareRoot(parentDict, 4, 5))    # True
    print('5,7 => same set? :', compareRoot(parentDict, 5, 7))    # True
    print('4,7 => same set? :', compareRoot(parentDict, 4, 7))    # True
    print('5,6 => same set? :', compareRoot(parentDict, 5, 6))    # True
    print('6,7 => same set? :', compareRoot(parentDict, 6, 7))    # True
    print('7,8 => same set? :', compareRoot(parentDict, 7, 8))    # True
    print('='*25)

    # path compression을 이해할 수 있는 부분 -> 한번 검색을 했던 부분은 압축
    print('parentDict : ', parentDict)              # parentDict :  {1: 5, 2: 1, 3: 1, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5}

    print('1,3 => same set? :', compareRoot(parentDict, 1, 3))    # True
    print('parentDict : ', parentDict)              # parentDict :  {1: 5, 2: 1, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5}

    print('1,2 => same set? :', compareRoot(parentDict, 1, 2))    # True
    print('parentDict : ', parentDict)              # parentDict :  {1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5}
    print('='*25)