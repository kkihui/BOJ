# n = 100만이므로 for 문이 20회 내로 연산하면 1초만에 연산 가능
def solution(number, k):
    num = list(number)
    answer = ''
    length = len(num) - k
    idxs = []
    end = 0
    
    if num.count('9') >= length:
        answer = '9'*length
        print(answer)
        return answer
    
    # 앞 자리 가능한 것 중 가장 커야함. 
    while not end:
        if len(idxs) == 0:
            idx = -1
        else:
            idx = idxs[-1]
        big = -1
        for i in range(idx+1,len(num)-length+1):
            if i >= len(num):
                end = 1
                break
            if int(num[i]) > big:
                big = int(num[i])
                idx_temp = i
            if big == 9:
                break
        if not end:
            idxs.append(idx_temp)
        length -= 1
    
    for idx in idxs:
        answer += num[idx]
    return answer