import sys

n = int(sys.stdin.readline())

if n==1:
    print('1')
elif n==2:
    print('2')
else:
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2
    for _ in range(2,n):
        dp[_] = dp[_-1] + dp[_-2]
    print(dp[-1]%10007)        