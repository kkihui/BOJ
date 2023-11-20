import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    inf = 10**6
    dp = [inf]*(k+1)
    change = []
    for _ in range(n):
        change.append(int(sys.stdin.readline()))
    dp[0] = 0
    length = len(change)
    for i in range(1,k+1):
        for j in range(length):
            if i - change[j] >= 0:
                if dp[i-change[j]] != inf:
                    dp[i] = min(dp[i],dp[i-change[j]]+1)
    if dp[k] == inf:
        print(-1)
    else:
        print(dp[k])
    

if __name__ == '__main__':
    main()