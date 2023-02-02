"""
최대공약수와 최소공배수
 
시간 제한   메모리 제한   제출   정답   맞힌 사람   정답 비율
1 초   128 MB   84467   48757   39580   58.232%
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

예제 입력 1 
24 18
예제 출력 1 
6
72
"""

import sys

stdInput = sys.stdin.readline

# 최대공약수
def gcd(a, b):
    result = None

    if b > a:
        a, b = b, a
    
    # 나누어떨어질때까지 반복
    while True:
        if a % b == 0:
            result = b
            break

        # 유클리드 호제법 ( a > b )
        # a 와 b의 최대공약수는 b와 a를 b로 나눈 나머지 r(a%b)의 최대공약수의 같다.
        # gcd(a, b) = gcd(b, a%b)
        a = a % b
        a, b = b, a

    return result


# 최소공배수
def lcm(a, b):
    return int( a * b / gcd(a, b) ) 

def main():
    a, b = map(int, stdInput().split())

    print(gcd(a, b))
    print(lcm(a, b))

main()