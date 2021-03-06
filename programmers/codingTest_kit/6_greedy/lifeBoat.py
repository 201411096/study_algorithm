"""
프로그래머스 -> 코딩테스트 연습 -> 그리디 -> 구명보트


문제 설명
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

입출력 예
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3

"""
# 효율성 테스트에서 전부 시간초과 나던 문제
# 1. 문제 이유 : list의 pop()은 O(1)이지만, pop(0)는 O(n)임
# 2. 해결 방법 : list의 pop(0) -> deque의 popleft()
from collections import deque
def solution(people, limit):
    # people.sort(reverse=True)
    people = deque(sorted(people, reverse=True))

    boatList = [] # [ (weight, cnt), ... ]
    boatList.append((people.popleft(), 1))

    while len(people) != 0:
        # 1. 마지막 보트가 꽉 차있음
        # 2. 더 탈 수 있는 상황이 아님
        if (boatList[-1][1] == 2) or (boatList[-1][0] + people[-1] > limit):
            boatList.append((people.popleft(), 1))
        else:
            boatList[-1] = (boatList[-1][0] + people.pop(), 2)

    return len(boatList)


# ====================================================================================================
people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit)) # 3
# ====================================================================================================
people = [70, 80, 50]
limit = 100
print(solution(people, limit)) # 3