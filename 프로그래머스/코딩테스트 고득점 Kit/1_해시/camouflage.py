def solution(clothes):
    answer = 1
    dic = {}
    
    for item in clothes:
        if item[1] in dic:
            dic[item[1]].append(item[0])
        else:
            dic[item[1]] = []
            dic[item[1]].append(item[0])
    
    # print('dic : ', dic)
        
    for item in dic:
        # print('answer :/ ', answer)
        # print('item : ', dic[item])
        # print('len : ', len(dic[item]))
        answer = answer * (len(dic[item])+1)
    
    answer = answer -1
    return answer


print('====================================================================================================')
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print('case 1 : ', solution(clothes))

clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print('case 2 : ', solution(clothes))
print('====================================================================================================')