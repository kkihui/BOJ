# 주어진 범위가 1000개 이하이므로 O(n^2)으로 풀어도 가능

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt = 0
        for j in range(1,i+1):
            if i % j == 0:
                cnt += 1
        if cnt %2 == 0:
            answer += i
        else:
            answer -= i
    return answer