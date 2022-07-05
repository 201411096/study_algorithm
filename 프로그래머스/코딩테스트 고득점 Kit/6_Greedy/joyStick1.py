"""
프로그래머스 -> 코딩테스트 연습 -> 그리디 -> 조이스틱


문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)

예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.

입출력 예
name	return
"JEROEN"	56
"JAN"	23

"""

# 빠른 경로 찾는 부분부터 이해를 하지 못함
def solution(name):
	# 조이스틱 조작 횟수
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    # 해당 알파벳 변경 최솟값 추가
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 이동할 이유가 없는 케이스
    if(len(name)==1 or answer == 0):
        return answer

    # 현재 바라보고 있는 알파벳의 Index
    currentIdx = 0
    
    # 왼쪽으로 먼저 이동 ==================================================
    tempName = 'A' + name[1:-1]+'A'
    left_min_move = 1
    currentIdx = len(name)-1
    
    while True:
        if tempName == 'A'*len(name):
            break
            
        distance = len(name)    # 현재 변경할 인덱스와의 거리(편의상 max로 설정)
        needChangeIdx = None
        
        for i, char in enumerate(tempName):
            if char != 'A':
                tempDistance = min(abs(currentIdx-i), len(name)-abs(currentIdx-i))
                if distance > tempDistance:
                    needChangeIdx = i   # 이동 거리가 가장 짧은 위치로 변경할 인덱스를 설정
                    distance = tempDistance

        tempName = tempName[:needChangeIdx] + 'A' + tempName[needChangeIdx+1:]
        currentIdx = needChangeIdx # 현재 인덱스를 최근에 변경한 알파벳 위치로 설정
        left_min_move+=distance
    # ======================================================================    
    # 오른쪽으로 먼저 이동 ==================================================
    tempName = 'AA'+name[2:]
    right_min_move = 1
    currentIdx = 1
    
    while True:
        if tempName == 'A'*len(name):
            break
            
        distance = len(name)    # 현재 변경할 인덱스와의 거리(편의상 max로 설정)
        needChangeIdx = None
        
        for i, char in enumerate(tempName):
            if char != 'A':
                tempDistance = min(abs(currentIdx-i), len(name)-abs(currentIdx-i))
                if distance > tempDistance:
                    needChangeIdx = i   # 이동 거리가 가장 짧은 위치로 변경할 인덱스를 설정
                    distance = tempDistance

        tempName = tempName[:needChangeIdx] + 'A' + tempName[needChangeIdx+1:]
        currentIdx = needChangeIdx # 현재 인덱스를 최근에 변경한 알파벳 위치로 설정
        right_min_move+=distance
    # ======================================================================
    
    min_move = min(left_min_move, right_min_move)

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer

name = "JEROEN"
print(solution(name)) # 56
name = "JAN"
print(solution(name)) # 23
name = "AAA"
print(solution(name)) # 0