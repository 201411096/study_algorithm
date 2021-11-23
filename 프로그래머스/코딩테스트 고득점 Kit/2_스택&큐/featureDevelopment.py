def solution(progresses, speeds):
    answer = []
    completeDayList = []    # 각 작업들이 완료까지 몇일이 걸렸는지 저장하는 리스트
    dayCnt = 0
    
    for i in range(len(progresses)):
        completeDayList.append(0)
    
    while True:
        exitFlag = True
        dayCnt = dayCnt + 1
        for idx, progress in enumerate(progresses):
            progresses[idx] = progresses[idx] + speeds[idx]
        for idx, progress in enumerate(progresses):
            if(progresses[idx] >= 100 and completeDayList[idx] == 0): # 값이 초기화되어있는지 확인
                completeDayList[idx] = dayCnt
            elif (progresses[idx] < 100):
                exitFlag = False
                
        if exitFlag == True:
            break;
    
    currentVal = completeDayList[0]
    currentIdx = 0
    answer.append(1)

    for i in (range(len(completeDayList) -1 )):
        if completeDayList[i+1] <= currentVal:  # 다음 progress가 이미 끝나있다면
            answer[currentIdx] = answer[currentIdx] + 1
        else:                                   # 다음 progress가 끝나있지 않다면
            currentIdx = currentIdx + 1
            currentVal = completeDayList[i+1]  
            answer.append(1)
    
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print('case 1 : ', solution(progresses, speeds)) # print [2, 1]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print('case 2 : ', solution(progresses, speeds)) # print [1, 3, 2]

progresses = [20, 99, 93, 30, 55, 10]
speeds = [5, 10, 1, 1, 30, 5]
print('case 3 : ', solution(progresses, speeds)) # print [3, 3]