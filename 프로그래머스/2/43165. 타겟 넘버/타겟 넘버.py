answer = 0
def solution(numbers, target):
    def recursion(present,result,sign):
        global answer
        if sign == '-':
            result -= numbers[present]
        else:
            result += numbers[present]
                
        if present == len(numbers)-1:
            if result == target:
                answer += 1
            return 0
        else:
            recursion(present+1,result,'+')
            recursion(present+1,result,'-')
        return 0
    
    recursion(0,0,'+')
    recursion(0,0,'-')
    
    return answer

''' 
# 1번 풀이 시간 초과
import itertools
import copy

def solution(numbers, target):
    answer = 0
    for i in itertools.product([-1,1], repeat=len(numbers)):
        num = copy.deepcopy(numbers)
        for j in range(len(numbers)):
            num[j] = i[j] * numbers[j]
        if sum(num) == target:
            answer += 1
    return answer
'''