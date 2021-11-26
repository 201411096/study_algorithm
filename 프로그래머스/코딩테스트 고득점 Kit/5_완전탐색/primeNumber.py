"""
[완전탐색 > 소수 찾기]

문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
numbers	return
"17"	3
"011"	2

입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
* 11과 011은 같은 숫자로 취급합니다. 

"""

import itertools

def solution(numbers):
    answer = 0
    numberList = []                 # numbers를 쪼개놓은 결과
    combinatedNumberArrayList = []  # combination한 결과
    combinatedNumberList = []       # combination한 list들을 join해둔 숫자 목록
    
    for i in range(len(numbers)):
        numberList.append(numbers[i])
    # print(numberList)
    
    for i in range(1, len(numbers)+1):
        combinatedNumberArrayList.extend(itertools.permutations(numberList, r=i))
    # print('combinatedNumberArrayList : ', combinatedNumberArrayList)
    
    for i in range(len(combinatedNumberArrayList)):
        combinatedNumberList.append( int("".join(combinatedNumberArrayList[i])) )
    # print('combinatedNumberList : ', combinatedNumberList)
    combinatedNumberList = list( set(combinatedNumberList) )  
    for combinatedNumber in combinatedNumberList:
        # print('combinatedNumber : ', combinatedNumber)
        primeCnt =  0
        for i in range(1, int(combinatedNumber/2 +1) ): # 100이라면 50까지만 확인
            if combinatedNumber % i == 0:
                # print('{} % {} = {}'.format(combinatedNumber, i, combinatedNumber % i))
                primeCnt += 1
            if primeCnt >= 2:
                break
        # print('primeCnt : ', primeCnt)
        
        if primeCnt == 1:                               # 자기 자신으로 나뉘는지는 확인하지 않음(-> cnt가 1이면 소수로 본다.)
            answer += 1
            
    return answer

numbers = "17"
print('case 1 : ', solution(numbers))   # 3

numbers = "011"
print('case 2 : ', solution(numbers))   # 2
