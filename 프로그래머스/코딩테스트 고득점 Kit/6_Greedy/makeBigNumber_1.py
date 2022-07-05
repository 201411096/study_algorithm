"""
프로그래머스 -> 코딩테스트 연습 -> 그리디 -> 큰 수 만들기


문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한사항
number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.

입출력 예
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"

"""
# 풀리기는 하나 6952.48ms 시간이 걸리는 케이스 존재
def solution(number, k):
    # answer = ""
    answer = number
    deleteCnt = 0
    currentIdx = 0

    while True:
        if deleteCnt == k:
            break
        # 끝까지 다봤는데도 지울게 없다면 뒤에서 자름(전부 같은 수인 경우)
        if currentIdx == len(answer)-1:
            answer = answer[:-(k-deleteCnt)]
            break
        currentNum = int(answer[currentIdx])
        nextNum = int(answer[currentIdx+1])

        if currentNum < nextNum:
            deleteCnt += 1
            answer = answer[:currentIdx] + answer[currentIdx+1:]
            if currentIdx > 0:
                currentIdx -= 1
        else:
            currentIdx += 1

    return answer

# ====================================================================================================
number = "1924"
k = 2
print(solution(number, k)) # 94
# ====================================================================================================
number = "1231234"
k = 3
print(solution(number, k)) # 3234
# ====================================================================================================
number = "4177252841"
k = 4
print(solution(number, k)) # 775841
# ====================================================================================================
number = "4321999"
k = 3
print(solution(number, k)) # 4999