def solution(participant, completion):
    answer = ''
    tempDict = {}
    
    for person in participant:
        if person in tempDict:
            tempDict[person] += 1
        else:
            tempDict[person] = 1
            
    for person in completion:
        if tempDict[person] == 1:
            del tempDict[person]
        else:
            tempDict[person] -= 1
    
    return list(tempDict.keys())[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print('case 1 : ', solution(participant, completion)) # "leo"

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print('case 2 : ', solution(participant, completion)) # "vinko"

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print('case 3 : ', solution(participant, completion)) # "mislav"