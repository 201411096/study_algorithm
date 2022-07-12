# union-find    : 합집합 찾기
# disjoint-set  : 서로소 집합

# union by rank     : x
# path compression  : x

def makeSet(n):
    return [i for i in range(n+1)]

def findRoot(parents, n):
    if parents[n] == n:
        return n
    else:
        return findRoot(parents, parents[n])

def unionSet(parents, a, b):
    rootA = findRoot(parents, a)
    rootB = findRoot(parents, b)

    if rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB

def compareRoot(parents, a, b):
    rootA = findRoot(parents, a)
    rootB = findRoot(parents, b)

    if rootA == rootB:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 8

    parents = makeSet(n)

    unionSet(parents, 1, 2)        # [ [1, 2] ]
    print('parents : ', parents)    # parents :  [0, 1, 1, 3, 4, 5, 6, 7, 8]
    unionSet(parents, 2, 3)        # [ [1, 2, 3] ]
    print('parents : ', parents)    # parents :  [0, 1, 1, 1, 4, 5, 6, 7, 8]
    unionSet(parents, 4, 3)        # [ [1, 2, 3, 4] ]
    print('parents : ', parents)    # parents :  [0, 1, 1, 1, 1, 5, 6, 7, 8]
    unionSet(parents, 5, 6)        # [ [1, 2, 3, 4], [5, 6] ]
    print('parents : ', parents)    # parents :  [0, 1, 1, 1, 1, 5, 5, 7, 8]
    unionSet(parents, 7, 8)        # [ [1, 2, 3, 4], [5, 6], [7, 8] ]
    print('parents : ', parents)    # parents :  [0, 1, 1, 1, 1, 5, 5, 7, 7]

    print('='*25)
    print('4,1 => same set? :', compareRoot(parents, 4, 1))    # True
    print('4,5 => same set? :', compareRoot(parents, 4, 5))    # False
    print('5,6 => same set? :', compareRoot(parents, 5, 6))    # True
    print('5,7 => same set? :', compareRoot(parents, 5, 7))    # False
    print('4,7 => same set? :', compareRoot(parents, 4, 7))    # False
    print('7,8 => same set? :', compareRoot(parents, 7, 8))    # True

    unionSet(parents, 5, 4)
    print('parents : ', parents)    # parents :  [0, 1, 1, 1, 1, 1, 5, 7, 7]
    unionSet(parents, 6, 7)
    print('parents : ', parents)    # parents :  [0, 1, 1, 1, 1, 1, 5, 1, 7]
    print('='*25)

    print('4,5 => same set? :', compareRoot(parents, 4, 5))    # True
    print('5,7 => same set? :', compareRoot(parents, 5, 7))    # True
    print('4,7 => same set? :', compareRoot(parents, 4, 7))    # True
    print('5,6 => same set? :', compareRoot(parents, 5, 6))    # True
    print('6,7 => same set? :', compareRoot(parents, 6, 7))    # True
    print('7,8 => same set? :', compareRoot(parents, 7, 8))    # True
    print('='*25)
