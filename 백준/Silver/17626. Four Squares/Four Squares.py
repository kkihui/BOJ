# 그것보다 작은 최대 소수 찾으면 안 됨.
# DP로 찾기 

import sys
import math

n = int(sys.stdin.readline())
primenum = []
dp = [0,1]
cnt = 0

for _ in range(1,224): # 루트 5만은 223.~~
    primenum.append(_**2)

for _ in range(2,50001): # 2~50000까지
    minimum = dp[_-1] +1
    for i in range(int(math.sqrt(_))): # 자기보다 작은 제곱수 뺀 가짓수 +1들 비교해서 최솟값 구함
        current = dp[_-primenum[i]]+1
        if current < minimum:
            minimum = current
    dp.append(minimum)

print(dp[n])