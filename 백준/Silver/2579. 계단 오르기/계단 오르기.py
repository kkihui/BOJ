import sys

n = int(sys.stdin.readline())
stairli = []
dp = [[0,0] for _ in range(n-1)]
for _ in range(n):
    stairli.append(int(sys.stdin.readline()))

if n <= 2:
    print(sum(stairli))
    exit()
elif n == 3:
    if stairli[0] <= stairli[1]:
        print(sum(stairli)-stairli[0])
    else:
        print(sum(stairli)-stairli[1])
    exit()
    
dp.append([stairli[n-1],0])
dp[n-2] = [0,dp[n-1][0]+stairli[n-2]]
dp[n-3] = [dp[n-1][0]+stairli[n-3],0]

    
for _ in range(n-4,-1,-1):
    dp[_][0] = max(dp[_+2]) + stairli[_] #non conti 최댓값
    dp[_][1] = dp[_+1][0] + stairli[_] #conti 최댓값


print(max(max(dp[0]),max(dp[1])))