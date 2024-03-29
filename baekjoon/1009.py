"""
분산처리

문제
재용이는 최신 컴퓨터 10대를 가지고 있다. 어느 날 재용이는 많은 데이터를 처리해야 될 일이 생겨서 각 컴퓨터에 1번부터 10번까지의 번호를 부여하고, 10대의 컴퓨터가 다음과 같은 방법으로 데이터들을 처리하기로 하였다.

1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터, 3번 데이터는 3번 컴퓨터, ... ,

10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터, 12번 데이터는 2번 컴퓨터, ...

총 데이터의 개수는 항상 ab개의 형태로 주어진다. 재용이는 문득 마지막 데이터가 처리될 컴퓨터의 번호가 궁금해졌다. 이를 수행해주는 프로그램을 작성하라.

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 정수 a와 b가 주어진다. (1 ≤ a < 100, 1 ≤ b < 1,000,000)

출력
각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터의 번호를 출력한다.

예제 입력 1 
5
1 6
3 7
6 2
7 100
9 635
예제 출력 1 
1
7
6
1
9

풀이
- 거듭제곱은 시간초과가 발생
- 마지막 수만 계산하는 식으로 풀어나감
- 끝자리만 곱해보면서 반복을 찾아서 푸는 식

1   | 1
2   | 2 4 6 8
3   | 3 9 7 1
4   | 4 6
5   | 5
6   | 6
7   | 7 9 3 1
8   | 8 4 2 6
9   | 9 1
10  | 0
"""

import sys

n = int(input())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    answer = None
    
    num = a % 10

    if num == 0:
        print(10)
    elif num in [1, 5, 6]:
        print(num)
    elif num in [4, 9]:
        b = b % 2
        if b == 1:
            print(num)
        else:
            print(num * num  % 10)
    else:                           # case 2, 3, 7, 8
        b = b % 4
        if b == 0:
            print(num**4 % 10)
        else:
            print(num**b % 10)