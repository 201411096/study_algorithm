"""
회문인 수
 
시간 제한   메모리 제한   제출   정답   맞힌 사람   정답 비율
1 초   256 MB   3050   1566   1330   55.976%
문제
어떤 수를 왼쪽부터 읽어도, 오른쪽부터 읽어도 같을 때 이 수를 회문인 수라고 한다. 
예를 들어, 747은 회문인 수이다. 255도 회문인 수인데, 16진수로 표현하면 FF이기 때문이다. 
양의 정수를 입력받았을 때, 이 수가 어떤 B진법 (2 ≤ B ≤ 64)으로 표현하면 회문이 되는 경우가 있는지 알려주는 프로그램을 작성하시오. B진법이란, 한 자리에서 수를 표현할 때 쓸 수 있는 수의 가짓수가 B라는 뜻이다. 예를 들어, 십진법에서 B는 10이다. 

입력
입력 데이터는 표준입력을 사용한다. 
입력은 T개의 테스트 데이터로 구성된다. 
입력의 첫 번째 줄에는 테스트 데이터의 수를 나타내는 정수 T가 주어진다. 
각 테스트 데이터는 64 이상 1,000,000 이하인 하나의 정수로 주어진다.

출력
출력은 표준출력을 사용한다. 
하나의 테스트 데이터에 대한 답을 하나의 줄에 출력한다. 
각 테스트 데이터에 대해, 주어진 수가 어떤 B진법 (2 ≤ B ≤ 64)으로 표현하여 회문이 될 수 있다면 1을, 그렇지 않다면 0을 출력한다.

예제 입력 1 
3
747
255
946734

예제 출력 1 
1
1
0
"""

import sys
from collections import deque

stdInput = sys.stdin.readline

# 1 -> 회문인 수 o
# 0 -> 회문인 수 x
def checkNumber(num):
    result = 0
    
    # 2-64
    # i : i진법
    for i in range(2, 65):
        currentNum = num
        divNum = i      # 나눌 값(i진법 * numValue)
        tempList = deque()

        while currentNum != 0:
            tempList.appendleft(currentNum % divNum)
            currentNum = currentNum // divNum
        
        # 해당 진법에서 회문인 수(Palindromic number)인지
        isPalindromic = True
        for idx in range(len(tempList)//2):
            if tempList[idx] != tempList[len(tempList)-idx-1]:
                isPalindromic = False
                break
        if isPalindromic == True:
            result = 1
            break
            
    return result

def main():
    inputCnt = int(stdInput())
    inputList = []

    for i in range(inputCnt):
        inputList.append(int(stdInput()))

    for inputNum in inputList:
        print(checkNumber(inputNum))
        
main()