import time 

# 백준 1009번 문제 풀다가 고속 거듭제곱 알고리즘이라고 해서 가져왔는데, 내장함수가 더 빠름(고속 거듭제곱이라는 다른 함수들 2~3개 적용해봐도 내장함수보다 시간이 더 느림)

def fast_power(a, b):
    result = 1
    while b > 0:
        if(b%2 == 1):
            result = result * a
            b = b-1

        a = a * a
        b = b/2
            
    return result


def power(a, b):
    return a**b

start = time.time()
fast_power(999, 1000000)
# print(fast_power(2, 1000000))
end = time.time()
print('time : ', (end-start))

start = time.time()
power(999, 1000000)
# print(power(2, 1000000))
end = time.time()
print('time : ', (end-start))