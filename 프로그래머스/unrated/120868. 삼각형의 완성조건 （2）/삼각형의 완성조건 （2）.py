def solution(sides):
    answer = 0
    
    if sides[1] > sides[0]:
        maxsi = sides[1]
        othersi = sides[0]
    else:
        maxsi = sides[0]
        othersi = sides[1]
    
    for i in range(1,maxsi+1): # 가장긴게 주어진거
        if othersi + i > maxsi:
            answer += 1
    
    othermax = maxsi + othersi
    
    for i in range(maxsi+1,othermax): # 가장긴게 나머지
        if maxsi + othersi > i:
            answer += 1
    
    return answer