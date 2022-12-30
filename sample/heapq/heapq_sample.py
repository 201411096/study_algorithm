import heapq

def pushToHeap(heap, sampleData):
    for item in sampleData:
        heapq.heappush(heap, item)

def popAndShow(heap):
    for i in range(len(heap)):
        node, price = heapq.heappop(heap)
        print(node, price)


heap = []

sampleData1 = [
    [5, 100],
    [4, 100],
    [1, 99],
    [1, 101],
    [1, 100],
    [1, 98],
    [1, 102],
    [2, 100],
]

pushToHeap(heap, sampleData1)
popAndShow(heap)
print('='*30)

sampleData2 = [
    [-5, 100],
    [-4, 100],
    [-1, 99],
    [-1, 101],
    [-1, 100],
    [-1, 98],
    [-1, 102],
    [-2, 100],
]

pushToHeap(heap, sampleData2)
popAndShow(heap)
print('='*30)

sampleData3 = [
    (5, 100),
    (4, 100),
    (1, 99),
    (1, 101),
    (1, 100),
    (1, 98),
    (1, 102),
    (2, 100)
]

pushToHeap(heap, sampleData3)
popAndShow(heap)