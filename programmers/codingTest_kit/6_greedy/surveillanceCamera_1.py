"""
프로그래머스 -> 코딩테스트 연습 -> 그리디 -> 단속카메라


문제 설명
고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.
고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

제한사항
차량의 대수는 1대 이상 10,000대 이하입니다.
routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

입출력 예
routes	return
[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	2

입출력 예 설명
-5 지점에 카메라를 설치하면 두 번째, 네 번째 차량이 카메라를 만납니다.
-15 지점에 카메라를 설치하면 첫 번째, 세 번째 차량이 카메라를 만납니다.

"""

# 답안을 확인해본 문제
# 아이디어 확인 O | 코드 확인 X
# 1. 차의 진입시점을 기준으로 정렬하는 것이 아님 -> 진출시점을 기준으로 정렬해야 함
# 2. 카메라는 먼저 진출한 지점 순서대로 설치해야함

from collections import deque

def solution(routes):
    answer = 0

    routes = deque(sorted(routes, key=lambda x : x[1]))

    print('routes : ', routes)

    while routes:
        answer += 1
        left, right = routes.popleft()

        print('left : ', left)
        print('right : ', right)
        print('answer : ', answer)

        while len(routes)>0:
            # 현재 차의 진입시점이 비교중인 차의 진출시점보다 오른쪽에 있다면 -> 주행구간이 겹치지 않는다면
            if routes[0][0] > right:
                break
            else:
                routes.popleft()


        

    return answer

# ====================================================================================================
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes)) # 2
# ====================================================================================================
routes = [[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]
print(solution(routes)) # 4
# ====================================================================================================
routes = [[0,12],[1,12],[2,12],[3,12],[5,6],[6,12],[10,12]]
print(solution(routes)) # 2
