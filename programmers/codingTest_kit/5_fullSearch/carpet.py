def solution(brown, yellow):
    answer = [0, 0]
    
    width = yellow
    height = 1
    
    for i in reversed(range(1, ( int(yellow/2))+1 ) ):
        if (yellow % i == 0 and int(yellow/i) >= i) and (i*2 + int(yellow/i)*2 + 4 == brown):
            height = i
            width = int(yellow / height)
            break
    
    answer[0] = width + 2
    answer[1] = height + 2
    
    return answer

print('case 1 : ', solution(10, 2))     # [4, 3]
print('case 2 : ', solution(8, 1))      # [3, 3]
print('case 3 : ', solution(24, 24))    # [8, 6]