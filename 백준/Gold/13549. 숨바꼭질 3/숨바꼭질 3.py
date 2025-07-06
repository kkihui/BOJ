'''
시간제한이 2초이므로 4천만 번의 연산안에 끝나야 함.
20만번의 연산을 200번 안에 끝내야 한다.
dp로 빠르게 판단
'''
import sys

def main():
    N,K = map(int,sys.stdin.readline().split())
    dp = [100000] * 200000
    dp[N] = 0
    num = N
    while num < len(dp):
        if num == 0 or num == 1:
            break
        dp[num] = 0
        num *= 2
    
    # 앞으로 갈 경우
    for i in range(N,100000):
        dp[i+1] = min(dp[i]+1,dp[i+1])
        num = i+1
        while num < len(dp):
            dp[num] = min(dp[num],dp[i+1])
            num *= 2
    # 뒤로 갈 경우
    for i in range(N,0,-1):
        dp[i-1] = min(dp[i]+1,dp[i-1])
        num = i-1
        while num < len(dp):
            if num == 0:
                break
            dp[num] = min(dp[num],dp[i-1])
            num *= 2
    # 다시 처음부터 여러 번 확인
    for _ in range(10):
        for i in range(100001):
            if i == 0:
                dp[i] = min(dp[i],dp[i+1]+1)
            elif i == 100000:
                dp[i] = min(dp[i-1]+1,dp[i])    
            else:
                dp[i] = min(dp[i-1]+1,dp[i],dp[i+1]+1)
            num = i
            while num < len(dp):
                if num == 0:
                    break
                dp[num] = min(dp[num],dp[i])
                num *= 2
    
    print(dp[K])
    
if __name__ == "__main__":
    main()