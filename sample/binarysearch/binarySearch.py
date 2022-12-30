def binarySearch(array, target, start, end):
    if(start>end):
        return None
    mid = (start + end) // 2 # // -> 소수점 이하 삭제
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearch(array, target, start, mid-1)
    elif array[mid] < target:
        return binarySearch(array, target, mid+1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binarySearch(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)

"""
case_01
10 7
1 3 5 7 9 11 13 15 17 19

case_02
10 7
1 3 5 6 8 11 13 15 17 19
"""