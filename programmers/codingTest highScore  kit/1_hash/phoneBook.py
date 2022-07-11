# 답안을 확인해본 문제

def solution(phone_book):
    hashMap = {}
    for phone_number in phone_book:
        hashMap[phone_number] = 1
    
    for phone_number in phone_book:
        tempNumber = ""
        
        for num in phone_number:
            tempNumber += num
            if tempNumber in hashMap and tempNumber !=phone_number:
                return False
    
    return True


list1 = ["119", "97674223", "1195524421"]
list2 = ["123","456","789"]
list3 = ["12","123","1235","567","88"]

print(solution(list1)) # false
print(solution(list2)) # true
print(solution(list3)) # false
