"""
프로그래머스 -> 코딩테스트 연습 -> 정렬 -> H-Index


문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

입출력 예
citations	return
[3, 0, 6, 1, 5]	3

"""

# h번 이상 인용된 논문 h편 이상
# h번 이하 인용된 논문 h편 이하

def solution(citations):
    answer = 0
    length = len(citations)

    citations.sort(reverse=True)

    for (i, citation) in enumerate(citations):
        # 탐색한 문서 수 : i+1
        # 남은 문서 수 : length-i-1
        # 현재 인덱스의 인용 횟수 : citation
        searched = i+1
        remained = length-i-1

        # print('-'*20)
        # print('searched : ', searched)
        # print('remained : ', remained)

        for hIndex in range(citation, searched-1, -1):
            # print('hIndex : ', hIndex)
            if searched >= hIndex and hIndex >=remained:
                answer = hIndex
                break


    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations)) # 3
citations = [3, 0, 6, 1, 5, 20, 15, 19, 18, 17]
print(solution(citations)) # 6
citations = [3, 0, 6, 1, 5, 20, 15, 19, 18, 17, 15, 8, 7]
print(solution(citations)) # 7
citations = [10000, 10000, 10000, 10]
print(solution(citations)) # 4