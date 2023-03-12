"""
공통 부분 문자열
 
시간 제한   메모리 제한   제출   정답   맞힌 사람   정답 비율
2 초   256 MB   14746   5948   4669   42.265%
문제
두 문자열이 주어졌을 때, 두 문자열에 모두 포함된 가장 긴 공통 부분 문자열을 찾는 프로그램을 작성하시오.

어떤 문자열 s의 부분 문자열 t란, s에 t가 연속으로 나타나는 것을 말한다. 예를 들어, 문자열 ABRACADABRA의 부분 문자열은 ABRA, RAC, D, ACADABRA, ABRACADABRA, 빈 문자열 등이다. 하지만, ABRC, RAA, BA, K는 부분 문자열이 아니다.

두 문자열 ABRACADABRA와 ECADADABRBCRDARA의 공통 부분 문자열은 CA, CADA, ADABR, 빈 문자열 등이 있다. 이 중에서 가장 긴 공통 부분 문자열은 ADABR이며, 길이는 5이다. 또, 두 문자열이 UPWJCIRUCAXIIRGL와 SBQNYBSBZDFNEV인 경우에는 가장 긴 공통 부분 문자열은 빈 문자열이다.

입력
첫째 줄과 둘째 줄에 문자열이 주어진다. 문자열은 대문자로 구성되어 있으며, 길이는 1 이상 4000 이하이다.

출력
첫째 줄에 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이를 출력한다.

예제 입력 1 
ABRACADABRA
ECADADABRBCRDARA
예제 출력 1 
5
예제 입력 2 
UPWJCIRUCAXIIRGL
SBQNYBSBZDFNEV
예제 출력 2 
0
"""
import sys

stdInput = sys.stdin.readline

def solution_old():
    str1 = stdInput().strip()
    str2 = stdInput().strip()

    dpArr = [ [0 for j in range(len(str2)+1) ] for i in range(len(str1)+1)]

    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i==0 or j==0:
                dpArr[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dpArr[i][j] = dpArr[i-1][j-1] + 1
            else:
                dpArr[i][j] = 0

    print(max(map(max, dpArr)))

# 메모리 초과 문제로 다른 사람 코드를 참고한 풀이
# 메모리 초과가 왜 나는지도 찾지못함
# C++랑 시간차이가 40배이상 나는데 왜 그런지 알 수 없음
def solution():
    answer = 0
    str1 = stdInput().strip()
    str2 = stdInput().strip()

    dpArr1 = [0 for i in range(len(str2)+1)]

    for i in range(len(str1)+1):
        dpArr2 = [0 for i in range(len(str2)+1)]
        for j in range(len(str2)+1):
            if i==0 or j==0:
                dpArr2[j] = 0
            elif str1[i-1] == str2[j-1]:
                dpArr2[j] = dpArr1[j-1] + 1
            else:
                dpArr2[j] = 0
        
        dpArr1 = dpArr2

        if max(dpArr2) > answer:
            answer = max(dpArr2)

    print(answer)

def main():
    solution()

main()