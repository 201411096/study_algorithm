# 이해가 잘 되지 않는 문제
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
# ============================================================
# 문제 설명
# 
# h번 이상 인용된 논문 h편 이상                                 
# h번 이하 인용된 논문 h편 이하
# ============================================================
# 기본 설명
# 
# len(citations)-i = citation 이상의 논문 개수 = h
# 
# citations[i]가 h이상일 때, H-index의 모든 조건 충족
# -> 1. h이상 인용된 논문이 h편 이상
# -> 2. 나머지는 h편 이하 인용
# 
# [0, 1, 3, 5, 6]
# ============================================================
# 참고사항
# 
# 1. 논문 개수(인용 수x)를 기준으로 h를 잡는게 문제를 이해하는데 도움이 됨.
# 2. 마지막 return 값이 다른 이유
# 2-1. 오름차순 정렬 후 문제풀이
# h값이 논문 배열의 길이부터 시작해서 줄어드는 방식(len(citation) to 0)
# len(citation), len(citation)-1, len(citation)-2, ..., 1, ?
# 마지막 값으로 0 반환 후 종료
# 2-2. 내림차순 정렬 후 문제풀이
# h값이 인덱스0부터 시작해서 하나씩 늘어나는 방식(0 to len(citation))
# 0, 1, ,2, ..., len(citation)-1, ?
# 마지막 값으로 len(citation) 반환 후 종료
# ============================================================

# 오름차순으로 정렬 후 문제풀이
def solution1(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        # citation              : 탐색 중인 논문의 인용 수
        # len(citations) - idx  : "citation"이상의 논문 개수(현재 탐색중인 문서를 포함) = h
        
        # citation이 h 이상일 때 => H-index의 모든 조건 충족
        # 1. h이상 인용된 논문이 h편 이상
        # 2. 나머지는 h편 이하로 인용
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0

# 내림차순으로 졍렬 후 문제풀이
def solution2(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        # citation  : 탐색 중인 논문의 인용 수
        # idx       : "citation"이하의 논문 개수(현재 탐색중인 문서를 포함) = h

        # citation이 h 이하일 때 : H-index의 모든 조건 충족
        # 1. h이하 인용된 논문이 h편 이하
        # 2. 나머지는 h편 이상으로 인용
        if idx >= citation:
            return idx
    return len(citations)

solution = solution1

citations = [3, 0, 6, 1, 5]
print(solution(citations)) # 3
citations = [3, 0, 6, 1, 5, 20, 15, 19, 18, 17]
print(solution(citations)) # 6
citations = [3, 0, 6, 1, 5, 20, 15, 19, 18, 17, 15, 8, 7]
print(solution(citations)) # 7
citations = [10000, 10000, 10000, 10]
print(solution(citations)) # 4
citations = [0, 1, 0, 0]
print(solution(citations)) # 1
citations = [0, 0, 0, 0]
print(solution(citations)) # 0