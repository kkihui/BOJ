def solution(n, lost, reserve):
    student = [1]*(n+1)
    answer = 0
    
    for i in lost:
        student[i] = 0
    for i in reserve:
        student[i] += 1
    for i in range(1,n+1):
        if student[i] == 0:
            if i-1 >0 and student[i-1] == 2:
                student[i] += 1
                student[i-1] -= 1
            elif i < n and student[i+1] == 2:
                student[i] += 1
                student[i+1] -= 1
    for i in range(1,n+1):
        if student[i] > 0:
            answer+=1
    
    return answer