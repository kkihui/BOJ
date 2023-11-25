def solution(nums):
    ea = len(nums)//2
    setnums = set(nums)
    if len(setnums) >= ea:
        answer = ea
    else:
        answer = len(setnums)
    
    return answer