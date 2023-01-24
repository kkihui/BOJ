import sys

dp = [1]*1000001
for _ in range(2,1000001):
    dp[_] = dp[_-1] + (_*(_+1)//2)
    
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(dp[n])