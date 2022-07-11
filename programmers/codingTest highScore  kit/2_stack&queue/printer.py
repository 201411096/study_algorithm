def solution(priorities, location):
    answer = 0
    pairList = []
    pairList2 = [] # 출력된 순서대로 저장할 리스트
    
    pairList = zip(range(len(priorities)), priorities) # idx, properties
    pairList = list(pairList)
    
    # print('pairList : ', pairList)
    
    while len(pairList) > 0:
        changeFlag = True
        for i in range(len(pairList)-1):
            if pairList[i][1] > pairList[0][1]:
                pair = pairList.pop(0)
                pairList.append(pair)
                changeFlag = False
        if changeFlag == True:
            pair = pairList.pop(0)
            pairList2.append(pair)
            
    print('pairList2 : ', pairList2)
    
    for idx, pair in enumerate(pairList2):
        # print('pair[1] : ', pair[1])
        # print('location : ', location)
        if pair[0] == location :
            answer = idx+1
    
    return answer

priorities = [2, 1, 3, 2]
location = 2
print('case 1 : ', solution(priorities, location)) # case 1 : 1

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print('case 2 : ', solution(priorities, location)) # case 2 : 5