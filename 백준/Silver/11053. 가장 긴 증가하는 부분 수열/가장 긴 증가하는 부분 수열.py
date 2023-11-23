import sys

def main():
    n = int(sys.stdin.readline())
    numli = list(map(int,sys.stdin.readline().split()))
    dp = [0]*1001
    cnt = 0

    for i in range(n):
        temp = numli[i]
        maxi = 0
        for j in range(temp):
            if dp[j] > maxi:
                maxi = dp[j]
        dp[temp] = maxi+1
                
    for i in range(1,1001):
        if dp[i] > cnt:
            cnt = dp[i]
            
    print(cnt)

if __name__ == '__main__':
    main()