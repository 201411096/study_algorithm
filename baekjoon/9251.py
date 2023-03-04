"""
LCS
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.1 초 (하단 참고)	256 MB	64628	26265	19307	40.256%

문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

예제 입력 1 
ACAYKP
CAPCAK

예제 출력 1 
4
"""

import sys

stdInput = sys.stdin.readline

def main():
    str1 = stdInput().strip() # strip을 사용하지 않으면 \n 까지 비교함
    str2 = stdInput().strip()

    dpArr = [ [0 for j in range(len(str2)+1)] for i in range(len(str1)+1) ]

    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i==0 or j==0:
                dpArr[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dpArr[i][j] = dpArr[i-1][j-1] + 1
            else:
                dpArr[i][j] = max(dpArr[i-1][j], dpArr[i][j-1])
    
    print(dpArr[len(str1)][len(str2)])


main()