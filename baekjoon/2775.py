"""
부녀회장이 될테야
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	83126	46614	39782	56.541%
문제
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

이 아파트에 거주를 하려면 조건이 있는데, 
“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

입력
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

제한
1 ≤ k, n ≤ 14
예제 입력 1 
2
1
3
2
3
예제 출력 1 
6
10

"""

"""
풀이

0층     0   1   2   3   4   5
1층     0   1   3   6   10  15
2층     0   1   4   10  20  25
"""
import sys

stdInput = sys.stdin.readline

def solution(k, n):
    result = None

    # 계산 편의상 열도 하나씩 추가해둠
    arr = [[0 for c in range(n+1)] for r in range(k+1)]

    for i in range(k+1):
        for j in range(n+1):
            if j==0:
                arr[i][j] = 0
            elif i == 0:
                arr[i][j] = j
            else:
                # 아래(a-1)층의 1호부터 b호에 사는 사람 수는 ...
                # 바로 아래층, 같은 호에 사는 사람수(a-1층의 b호)과 같은층, 옆에 호 사는 사람(a층의 b-1호)수를 더한 것과 같음
                # ㄴ a층의 b-1호 사는 사람의 수가 a-1층의 1호부터 b-1호 까지 사는 사람 수의 합이기 때문
                arr[i][j] = arr[i-1][j] + arr[i][j-1]

    result = arr[k][n]


    return result

def main():
    inputTestCaseCnt = int(stdInput())
    answerList = []

    for i in range(inputTestCaseCnt):
        k = int(stdInput())
        n = int(stdInput())

        answerList.append(solution(k, n))

    for answer in answerList:
        print(answer)

main()