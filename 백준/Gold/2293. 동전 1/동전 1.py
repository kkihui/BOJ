import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    dp = [0]*(k+1)
    change = []
    for _ in range(n):
        change.append(int(sys.stdin.readline()))
    length = len(change)
    
    for i in range(length):
        if change[i] <= k:
            dp[change[i]] +=1
        for j in range(1,k+1):
            if j - change[i] >= 0:
                dp[j] += dp[j-change[i]]
    
    print(dp[k])

if __name__ == '__main__':
    main()