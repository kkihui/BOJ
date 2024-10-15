# N = 20만이므로 O(200*N) 이어야 2초 안에 연산 가능
# 9C2 = 36이므로 가능한 2개의 조합으로 Stack에서 탐색하기

import sys
import itertools

n = int(sys.stdin.readline())
stack = list(map(int,sys.stdin.readline().split()))
kind = len(set(stack))
length_max = 0

# 이미 2종류 이하면 탐색할 필요 X
if kind <= 2:
    print(len(stack))
else:
    combi = list(itertools.combinations(set(stack),2))
    # 최대 9C2의 조합을 모두 계산
    for i,j in combi:
        length = 0
        for idx in range(len(stack)-1,-1,-1):
            # Stack을 pop하면서 최대 몇개까지 연속으로 나오는지 확인
            if stack[idx] == i or stack[idx] == j:
                length += 1
                length_max = max(length_max,length)
            else:
                length = 0
                
    print(length_max)