"""
수 정렬하기 3
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
5 초 (하단 참고)	8 MB (하단 참고)	211219	49091	37120	23.516%
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 
10
5
2
3
1
4
2
3
5
1
7
예제 출력 1 
1
1
2
2
3
3
4
5
5
7

- 답안을 확인해본 문제
- list.sort() 사용시 메모리 초과 발생
- 계수정렬 활용
"""

import sys

stdInput = sys.stdin.readline

def main():
    countArray = [0] * 100001

    cnt = int(stdInput())

    for _ in range(cnt):
        countArray[int(stdInput())] += 1

    for num in range(len(countArray)):
        for _ in range(countArray[num]):
            print(num)

main()