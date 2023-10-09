import sys
dp = [1,3]
for _ in range(998):
    dp.append(dp[-1]+2*dp[-2])
N = int(sys.stdin.readline())
print(dp[N-1]%10007)