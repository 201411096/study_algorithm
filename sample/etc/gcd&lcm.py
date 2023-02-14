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